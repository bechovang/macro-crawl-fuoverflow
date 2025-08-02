from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import os
from google.cloud import vision
import google.generativeai as genai
import config

class GoogleSlidesCapture:
    def __init__(self, headless=True):
        self.setup_driver(headless)
        self.vision_client = vision.ImageAnnotatorClient()
        self.setup_gemini()
        
    def setup_gemini(self):
        """Thiết lập Gemini API"""
        try:
            genai.configure(api_key=config.GEMINI_API_KEY)
            self.gemini_model = genai.GenerativeModel(config.GEMINI_MODEL)
            print("✅ Gemini API configured successfully")
        except Exception as e:
            print(f"⚠️  Failed to configure Gemini API: {e}")
            self.gemini_model = None
        
    def setup_driver(self, headless=True):
        """Thiết lập Chrome driver"""
        chrome_options = Options()
        if headless:
            chrome_options.add_argument('--headless')
        chrome_options.add_argument('--window-size=1920,1080')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        
        self.driver = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.driver, 10)
        
    def login_google(self, email, password):
        """Đăng nhập Google (hoặc load cookies đã save)"""
        # Thực hiện login hoặc load cookies
        pass
    
    def get_slide_with_notes(self, slide_url, slide_number):
        """Chụp slide kèm notes như trong ảnh của bạn"""
        try:
            # Navigate to slide URL
            self.driver.get(slide_url)
            
            # Đợi slide load
            time.sleep(3)
            
            # Tìm và click vào presenter view hoặc notes view
            # URL format để show notes: thêm '/present' hoặc modify URL
            notes_url = slide_url.replace('/edit', '/present')
            self.driver.get(notes_url)
            
            # Đợi load xong
            time.sleep(2)
            
            # Cách 1: Chụp toàn bộ màn hình presenter view
            screenshot_path = f"slide_{slide_number}_with_notes.png"
            self.driver.save_screenshot(screenshot_path)
            
            # Cách 2: Chụp riêng slide content + notes area
            # Tìm container chứa cả slide và notes
            try:
                # Selector có thể thay đổi tùy Google cập nhật
                slide_container = self.wait.until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, 
                        ".punch-present-slide-container, .punch-viewer-content"))
                )
                
                notes_container = self.driver.find_element(By.CSS_SELECTOR, 
                    ".punch-present-notes-container, .speaker-notes-container")
                
                # Screenshot riêng slide
                slide_path = f"slide_{slide_number}_content.png"
                slide_container.screenshot(slide_path)
                
                # Screenshot riêng notes
                notes_path = f"slide_{slide_number}_notes.png"
                notes_container.screenshot(notes_path)
                
                return {
                    'full_screenshot': screenshot_path,
                    'slide_only': slide_path,
                    'notes_only': notes_path
                }
                
            except Exception as e:
                print(f"Không tìm thấy notes container: {e}")
                # Fallback: chỉ chụp slide
                slide_container = self.driver.find_element(By.CSS_SELECTOR, 
                    ".punch-viewer-content")
                slide_path = f"slide_{slide_number}_content.png"
                slide_container.screenshot(slide_path)
                
                return {
                    'full_screenshot': screenshot_path,
                    'slide_only': slide_path,
                    'notes_only': None
                }
                
        except Exception as e:
            print(f"Lỗi khi chụp slide {slide_number}: {e}")
            return None
    
    def ocr_image(self, image_path):
        """OCR ảnh thành text"""
        try:
            with open(image_path, "rb") as f:
                content = f.read()
            
            image = vision.Image(content=content)
            response = self.vision_client.document_text_detection(image=image)
            
            if response.text_annotations:
                return response.text_annotations[0].description
            return ""
            
        except Exception as e:
            print(f"Lỗi OCR: {e}")
            return ""
    
    def format_text_with_ai(self, slide_text, notes_text=""):
        """Dùng Gemini để format lại text"""
        if not self.gemini_model:
            return f"SLIDE CONTENT:\n{slide_text}\n\nNOTES:\n{notes_text}"
        
        prompt = config.AI_PROMPTS['format_slide'].format(
            slide_text=slide_text,
            notes_text=notes_text
        )
        
        try:
            response = self.gemini_model.generate_content(prompt)
            
            if response.text:
                return response.text
            else:
                print("⚠️  Gemini returned empty response")
                return f"SLIDE CONTENT:\n{slide_text}\n\nNOTES:\n{notes_text}"
                
        except Exception as e:
            print(f"Lỗi Gemini formatting: {e}")
            return f"SLIDE CONTENT:\n{slide_text}\n\nNOTES:\n{notes_text}"
    
    def process_slide(self, slide_url, slide_number):
        """Xử lý một slide hoàn chỉnh"""
        print(f"Xử lý slide {slide_number}...")
        
        # 1. Chụp ảnh
        screenshots = self.get_slide_with_notes(slide_url, slide_number)
        if not screenshots:
            return None
        
        # 2. OCR
        slide_text = ""
        notes_text = ""
        
        if screenshots['slide_only']:
            slide_text = self.ocr_image(screenshots['slide_only'])
        
        if screenshots['notes_only']:
            notes_text = self.ocr_image(screenshots['notes_only'])
        
        # 3. Format với AI
        if config.ENABLE_AI_FORMATTING:
            formatted_text = self.format_text_with_ai(slide_text, notes_text)
        else:
            formatted_text = f"SLIDE CONTENT:\n{slide_text}\n\nNOTES:\n{notes_text}"
        
        # 4. Lưu kết quả
        output_file = f"slide_{slide_number}_formatted.txt"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(formatted_text)
        
        return {
            'slide_number': slide_number,
            'screenshots': screenshots,
            'formatted_text': formatted_text,
            'output_file': output_file
        }
    
    def process_presentation(self, base_url, total_slides):
        """Xử lý toàn bộ presentation"""
        results = []
        
        for i in range(1, total_slides + 1):
            # Tạo URL cho từng slide
            slide_url = f"{base_url}#slide=id.p{i}"
            
            result = self.process_slide(slide_url, i)
            if result:
                results.append(result)
            
            # Nghỉ giữa các slide để tránh bị block
            time.sleep(config.SLIDE_DELAY)
        
        return results
    
    def close(self):
        """Đóng driver"""
        self.driver.quit()

# Cách sử dụng
if __name__ == "__main__":
    # Khởi tạo
    capturer = GoogleSlidesCapture(headless=False)  # Set False để xem trình duyệt
    
    try:
        # Login (nếu cần)
        # capturer.login_google("email", "password")
        
        # URL presentation (thay bằng URL thực tế)
        presentation_url = "https://docs.google.com/presentation/d/YOUR_PRESENTATION_ID/edit"
        
        # Xử lý toàn bộ presentation
        results = capturer.process_presentation(presentation_url, total_slides=10)
        
        print(f"Đã xử lý {len(results)} slides")
        
        # In kết quả
        for result in results:
            print(f"\nSlide {result['slide_number']}:")
            print(f"- Screenshots: {result['screenshots']}")
            print(f"- Output file: {result['output_file']}")
        
    finally:
        capturer.close()