import pyautogui
import time
import os
import sys # Thêm sys để kiểm tra hệ điều hành
import google.generativeai as genai
from tqdm import tqdm
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# --- OCR.SPACE IMPORTS ---
import requests
import base64

# --- PHẦN ÂM THANH MỚI: SỬ DỤNG PYGAME ---
import pygame

def play_sound(sound_type):
    """
    **ĐÃ SỬA:** Hàm tiện ích để phát các loại âm thanh khác nhau bằng pygame.
    """
    try:
        # Khởi tạo pygame mixer nếu chưa được khởi tạo
        if not pygame.mixer.get_init():
            pygame.mixer.init()
        
        # sound_type: 1-Bắt đầu, 2-Xong 1 slide, 3-Hoàn tất, 4-Lỗi
        if sound_type == 1: # Bắt đầu, đếm ngược
            # Không phát âm thanh cho bắt đầu
            pass
        elif sound_type == 2: # Xong 1 slide - phát purchase-success.mp3
            if os.path.exists("purchase-success.mp3"):
                pygame.mixer.music.load("purchase-success.mp3")
                pygame.mixer.music.play()
        elif sound_type == 3: # Hoàn tất - phát victory.mp3 3 lần
            if os.path.exists("victory.mp3"):
                for _ in range(3):
                    pygame.mixer.music.load("victory.mp3")
                    pygame.mixer.music.play()
                    # Chờ âm thanh kết thúc trước khi phát lần tiếp theo
                    while pygame.mixer.music.get_busy():
                        pygame.time.wait(100)
        elif sound_type == 4: # Lỗi
            # Không phát âm thanh cho lỗi
            pass
    except Exception as e:
        # Bỏ qua nếu không phát được âm thanh
        print(f"[Debug] Không thể phát âm thanh: {e}")
        pass

# --- OCR.SPACE INITIALIZATION ---
def validate_ocrspace_api_key(api_key):
    """Kiểm tra xem API key của OCR.space có hợp lệ hay không."""
    try:
        # Tạo một ảnh test đơn giản
        from PIL import Image, ImageDraw, ImageFont
        
        # Tạo ảnh test
        img = Image.new('RGB', (200, 50), color='white')
        draw = ImageDraw.Draw(img)
        draw.text((10, 10), "Test OCR", fill='black')
        
        # Lưu ảnh test
        test_img_path = "test_ocr.png"
        img.save(test_img_path)
        
        # Test API
        result = extract_text_from_image_ocr(test_img_path, api_key)
        
        # Xóa file test
        os.remove(test_img_path)
        
        if result and "Test" in result:
            print("-> OCR.space API key hợp lệ!")
            return True
        else:
            print("-> OCR.space API key không hoạt động đúng.")
            return False
            
    except Exception as e:
        print(f"\n[Lỗi] Không thể xác thực OCR.space API key: {e}")
        return False

# --- CÁC HÀM XỬ LÝ CỐT LÕI ---

def validate_gemini_api_key(api_key):
    """Kiểm tra xem API key của Gemini có hợp lệ hay không."""
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash-latest')
        model.generate_content("Hello", generation_config=genai.types.GenerationConfig(max_output_tokens=5))
        return True
    except Exception as e:
        print(f"\n[Lỗi] Có vẻ Khóa API Gemini không hợp lệ hoặc có vấn đề kết nối: {e}")
        return False

def show_image_preview(image_path, title="Xem trước ảnh"):
    """
    **Hàm mới:** Sử dụng Matplotlib để hiển thị ảnh xem trước một cách đáng tin cậy.
    Chương trình sẽ dừng lại cho đến khi bạn đóng cửa sổ xem ảnh.
    """
    try:
        img = mpimg.imread(image_path)
        plt.figure(figsize=(10, 8)) # Tạo cửa sổ xem ảnh với kích thước hợp lý
        plt.imshow(img)
        plt.title(title, fontsize=16)
        plt.axis('off') # Ẩn các trục tọa độ
        print("-> Đang hiển thị cửa sổ xem trước. Hãy đóng cửa sổ này để tiếp tục...")
        plt.show()
    except Exception as e:
        print(f"\n[Lỗi] Không thể hiển thị ảnh xem trước: {e}")

def show_split_image_preview(q_path, a_path):
    """**Hàm mới:** Hiển thị cả ảnh Đề và Đáp án trong cùng một cửa sổ."""
    try:
        q_img = mpimg.imread(q_path)
        a_img = mpimg.imread(a_path)
        
        # Tạo một figure với 2 subplot xếp dọc
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
        fig.suptitle("Xem trước đường cắt (Đóng cửa sổ này để tiếp tục)", fontsize=16)
        
        ax1.imshow(q_img)
        ax1.set_title("Phần ĐỀ (phía trên)")
        ax1.axis('off')
        
        ax2.imshow(a_img)
        ax2.set_title("Phần ĐÁP ÁN (phía dưới)")
        ax2.axis('off')
        
        plt.tight_layout(rect=[0, 0.03, 1, 0.95])
        print("-> Đang hiển thị cửa sổ xem trước. Hãy đóng cửa sổ này để tiếp tục...")
        plt.show()
    except Exception as e:
        print(f"\n[Lỗi] Không thể hiển thị ảnh xem trước: {e}")

def extract_text_from_image_ocr(image_path, ocrspace_api_key):
    """Sử dụng OCR.space API để trích xuất văn bản từ ảnh."""
    try:
        # Đọc ảnh và encode base64
        with open(image_path, 'rb') as image_file:
            image_data = image_file.read()
            image_base64 = base64.b64encode(image_data).decode('utf-8')
        
        # Gửi yêu cầu đến OCR.space API
        url = "https://api.ocr.space/parse/image"
        payload = {
            'apikey': ocrspace_api_key,
            'base64Image': f'data:image/png;base64,{image_base64}',
            'language': 'eng',  # Có thể thay đổi thành 'vie' cho tiếng Việt
            'isOverlayRequired': False,
            'filetype': 'png',
            'detectOrientation': True,
            'scale': True,
            'OCREngine': 2  # Engine 2 cho độ chính xác cao hơn
        }
        
        response = requests.post(url, data=payload, timeout=30)
        result = response.json()
        
        # Debug: In ra cấu trúc response để kiểm tra
        if 'IsErroredOnProcessing' in result and result['IsErroredOnProcessing']:
            error_msg = result.get('ErrorMessage', 'Unknown error')
            tqdm.write(f"\n[Lỗi] OCR.space API: {error_msg}")
            return ""
        
        # Kiểm tra cấu trúc response
        if 'ParsedResults' not in result:
            tqdm.write(f"\n[Lỗi] OCR.space API: Response không có ParsedResults")
            tqdm.write(f"Response: {result}")
            return ""
        
        if not result['ParsedResults']:
            tqdm.write(f"\n[Lỗi] OCR.space API: ParsedResults rỗng")
            return ""
        
        # Trích xuất text từ kết quả
        first_result = result['ParsedResults'][0]
        if 'ParsedText' not in first_result:
            tqdm.write(f"\n[Lỗi] OCR.space API: Không có ParsedText trong kết quả")
            tqdm.write(f"First result: {first_result}")
            return ""
        
        parsed_text = first_result['ParsedText']
        
        return parsed_text.strip()
        
    except KeyError as e:
        tqdm.write(f"\n[Lỗi] OCR.space API - KeyError: {e}")
        tqdm.write(f"Response structure: {result}")
        return ""
    except Exception as e:
        tqdm.write(f"\n[Lỗi] OCR.space API thất bại: {e}")
        return ""

def format_question_and_explanation(question_text, answer_text, question_number, use_gemini=True):
    """Định dạng câu hỏi và giải thích."""
    if not use_gemini:
        # Chỉ OCR, không dùng Gemini
        if answer_text:
            return f"""Câu {question_number}:
{question_text}

**Ghi chú:**
{answer_text}

---"""
        else:
            # Trường hợp OCR nguyên 1 slide, không có phần đáp án riêng
            return f"""Câu {question_number}:
{question_text}

---
"""
    
    # Sử dụng Gemini để định dạng
    if answer_text:
        # Trường hợp có phần đáp án riêng
        prompt = f"""
        Bạn là một gia sư AI chuyên nghiệp. Nhiệm vụ của bạn là đọc văn bản của một câu hỏi trắc nghiệm và phần ghi chú đáp án, sau đó định dạng lại một cách rõ ràng để học tập và cung cấp lời giải thích ngắn gọn.

        Văn bản câu hỏi (đề bài):
        ---
        {question_text}
        ---
        Văn bản ghi chú (chứa đáp án và/hoặc lời giải):
        ---
        {answer_text}
        ---

        Yêu cầu:
        1.  **Định dạng câu hỏi:** Bắt đầu bằng "Câu {question_number}:", liệt kê các phương án A, B, C, D rõ ràng. **KHÔNG** được đánh dấu hay làm nổi bật đáp án đúng trong phần này.
        2.  **Cung cấp lời giải thích:** Dưới phần các đáp án, thêm một mục `**Giải thích:**`. Trong phần giải thích này, hãy:
            -   Bắt đầu bằng việc nêu rõ đáp án đúng là gì (ví dụ: "Đáp án đúng là D.").
            -   Sau đó, giải thích ngắn gọn, súc tích tại sao đáp án đó lại đúng, dựa trên thông tin trong phần ghi chú.
        3.  **Loại bỏ các chi tiết thừa** trong cả câu hỏi và phần giải thích.
        4.  **Trả lời chỉ bằng nội dung đã định dạng theo Markdown.**
        """
    else:
        # Trường hợp OCR nguyên 1 slide, không có phần đáp án riêng
        prompt = f"""
        Bạn là một gia sư AI chuyên nghiệp. Nhiệm vụ của bạn là đọc văn bản của một slide trắc nghiệm và định dạng lại một cách rõ ràng để học tập.

        Văn bản slide (bao gồm cả câu hỏi và đáp án):
        ---
        {question_text}
        ---

        Yêu cầu:
        1.  **Định dạng câu hỏi:** Bắt đầu bằng "Câu {question_number}:", liệt kê các phương án A, B, C, D rõ ràng nếu có.
        2.  **Tách biệt câu hỏi và đáp án:** Nếu trong văn bản có cả câu hỏi và đáp án, hãy tách chúng ra thành 2 phần riêng biệt.
        3.  **Cung cấp lời giải thích:** Nếu có thông tin về đáp án đúng, hãy thêm phần `**Giải thích:**` để giải thích ngắn gọn.
        4.  **Loại bỏ các chi tiết thừa** và định dạng lại cho dễ đọc.
        5.  **Trả lời chỉ bằng nội dung đã định dạng theo Markdown.**
        """
    try:
        model = genai.GenerativeModel('gemini-1.5-flash-latest')
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        tqdm.write(f"\n[Lỗi] Gemini: Không thể định dạng câu {question_number}. Lỗi: {e}")
        return f"--- LỖI XỬ LÝ CÂU {question_number} ---\nĐề: {question_text}\nĐáp án: {answer_text}\n--- KẾT THÚC LỖI ---"

def calibrate_main_region(output_dir):
    """Hàm tương tác để người dùng căn chỉnh vùng chụp chính."""
    screen_width, screen_height = pyautogui.size()
    print("\n--- BƯỚC 1: CĂN CHỈNH VÙNG CHỤP CHÍNH ---")
    
    # Hỏi người dùng muốn dùng phương pháp nào
    print("Chọn phương pháp canh chỉnh:")
    print("1. Nhập phần trăm thủ công")
    print("2. Chọn vùng bằng chuột (khuyến nghị)")
    
    choice = input("Nhập lựa chọn (1/2): ").strip()
    
    if choice == "2":
        # Sử dụng công cụ canh chỉnh bằng chuột
        try:
            from mouse_calibration import calibrate_with_mouse
            print("\n-> Chuẩn bị mở công cụ canh chỉnh...")
            print("-> Hãy đảm bảo cửa sổ trình duyệt đang ở chế độ toàn màn hình")
            print("-> Nhấn Enter để bắt đầu...")
            input()
            
            region = calibrate_with_mouse()
            
            if region:
                x, y, width, height = region
                print(f"\n✅ Vùng chụp đã chọn: ({x}, {y}, {width}, {height})")
                
                # Chụp ảnh thử nghiệm để xác nhận
                print("  Đang chụp ảnh thử nghiệm...")
                preview_path = os.path.join(output_dir, "preview_main.png")
                pyautogui.screenshot(preview_path, region=region)
                
                show_image_preview(preview_path, "XEM TRƯỚC VÙNG CHỤP CHÍNH")
                
                confirm = input("  Vùng chụp này đã OK chưa? (ok/thử lại): ").lower()
                if confirm == 'ok':
                    os.remove(preview_path)
                    return region
                else:
                    print("-> Chuyển sang phương pháp thủ công.")
                    choice = "1"
            else:
                print("\n❌ Không có vùng nào được chọn, chuyển sang phương pháp thủ công.")
                choice = "1"
        except ImportError:
            print("\n❌ Không thể import công cụ canh chỉnh bằng chuột.")
            print("Chuyển sang phương pháp thủ công.")
            choice = "1"
        except Exception as e:
            print(f"\n❌ Lỗi khi sử dụng công cụ canh chỉnh: {e}")
            print("Chuyển sang phương pháp thủ công.")
            choice = "1"
    
    if choice == "1":
        # Phương pháp thủ công
        while True:
            try:
                left_margin_percent = int(input("  -> Nhập % thụt vào từ LỀ TRÁI (vd: 10): "))
                top_margin_percent = int(input("  -> Nhập % thụt vào từ LỀ TRÊN (vd: 15): "))
                
                left = int(screen_width * (left_margin_percent / 100))
                top = int(screen_height * (top_margin_percent / 100))
                capture_width = screen_width - left
                capture_height = screen_height - top
                
                region = (left, top, capture_width, capture_height)
                
                print("  Đang chụp ảnh thử nghiệm...")
                preview_path = os.path.join(output_dir, "preview_main.png")
                pyautogui.screenshot(preview_path, region=region)
                
                show_image_preview(preview_path, "XEM TRƯỚC VÙNG CHỤP CHÍNH")
                
                confirm = input("  Vùng chụp này đã OK chưa? (ok/thử lại): ").lower()
                if confirm == 'ok':
                    os.remove(preview_path)
                    return region
            except ValueError:
                print("  Vui lòng nhập một con số!")
            except Exception as e:
                print(f"  Có lỗi xảy ra: {e}")
    
    return None

def calibrate_split_line(main_region, output_dir):
    """Hàm tương tác để người dùng căn chỉnh đường cắt ngang."""
    print("\n--- BƯỚC 2: CĂN CHỈNH ĐƯỜNG CẮT NGANG (ĐỀ / ĐÁP ÁN) ---")
    
    # Hỏi người dùng muốn chia slide hay không
    print("Chọn phương pháp xử lý slide:")
    print("1. Chia slide thành 2 phần (Đề + Đáp án) - Mặc định")
    print("2. OCR nguyên 1 slide (không chia)")
    
    split_choice = input("Nhập lựa chọn (1/2): ").strip()
    
    if split_choice == "2":
        # Không chia slide, sử dụng toàn bộ vùng chính
        print("-> Chọn OCR nguyên 1 slide")
        return main_region, None  # Trả về main_region cho cả 2, None cho answer_region
    
    # Phương pháp chia slide (mặc định)
    print("-> Chọn chia slide thành 2 phần")
    
    while True:
        try:
            split_percent = int(input("  -> Nhập % cắt từ DƯỚI LÊN cho phần đáp án (vd: 20): "))
            
            main_left, main_top, main_width, main_height = main_region
            
            answer_height = int(main_height * (split_percent / 100))
            question_height = main_height - answer_height
            question_region = (main_left, main_top, main_width, question_height)
            
            answer_top = main_top + question_height
            answer_region = (main_left, answer_top, main_width, answer_height)

            print("  Đang chụp 2 ảnh thử nghiệm...")
            question_preview_path = os.path.join(output_dir, "preview_question.png")
            answer_preview_path = os.path.join(output_dir, "preview_answer.png")

            pyautogui.screenshot(question_preview_path, region=question_region)
            pyautogui.screenshot(answer_preview_path, region=answer_region)

            show_split_image_preview(question_preview_path, answer_preview_path)

            confirm = input("  Đường cắt này đã OK chưa? (ok/thử lại): ").lower()
            if confirm == 'ok':
                os.remove(question_preview_path)
                os.remove(answer_preview_path)
                return question_region, answer_region
        except ValueError:
            print("  Vui lòng nhập một con số!")
        except Exception as e:
            print(f"  Có lỗi xảy ra: {e}")

def capture_and_process(num_slides, output_dir, delay, ocrspace_api_key, gemini_key, question_region, answer_region, use_gemini=True):
    """Thu thập và xử lý dữ liệu sử dụng OCR.space API."""
    print("\n==============================================")
    print("           BẮT ĐẦU THU THẬP DỮ LIỆU         ")
    print("==============================================")
    
    all_formatted_text = []
    current_file_text = []
    file_counter = 1
    
    # Khởi tạo file tổng hợp
    final_output_file = os.path.join(output_dir, "tong_hop_cau_hoi_va_giai_thich.md")
    with open(final_output_file, 'w', encoding='utf-8') as f:
        f.write("# TỔNG HỢP CÁC CÂU HỎI VÀ GIẢI THÍCH\n\n")
    
    # Kiểm tra xem có chia slide hay không
    is_split_mode = answer_region is not None
    
    for i in tqdm(range(1, num_slides + 1), desc="Đang xử lý các câu hỏi"):
        if is_split_mode:
            # Chế độ chia slide (mặc định)
            question_img_path = os.path.join(output_dir, f"temp_question_{i}.png")
            answer_img_path = os.path.join(output_dir, f"temp_answer_{i}.png")
            
            pyautogui.screenshot(question_img_path, region=question_region)
            pyautogui.screenshot(answer_img_path, region=answer_region)
            
            question_text = extract_text_from_image_ocr(question_img_path, ocrspace_api_key)
            answer_text = extract_text_from_image_ocr(answer_img_path, ocrspace_api_key)
            
            os.remove(question_img_path)
            os.remove(answer_img_path)
        else:
            # Chế độ OCR nguyên 1 slide
            slide_img_path = os.path.join(output_dir, f"temp_slide_{i}.png")
            
            pyautogui.screenshot(slide_img_path, region=question_region)  # question_region chính là main_region
            
            full_text = extract_text_from_image_ocr(slide_img_path, ocrspace_api_key)
            
            os.remove(slide_img_path)
            
            # Tách text thành question và answer (nếu có thể)
            question_text = full_text
            answer_text = ""  # Không có phần đáp án riêng
        
        if question_text:
            formatted_text = format_question_and_explanation(question_text, answer_text, i, use_gemini)
            current_file_text.append(formatted_text)
            all_formatted_text.append(formatted_text)
            
            # Cập nhật file tổng hợp ngay lập tức
            with open(final_output_file, 'a', encoding='utf-8') as f:
                f.write(formatted_text + "\n\n---\n\n")
            
            play_sound(2)
        else:
            tqdm.write(f"-> Bỏ qua câu {i} do không nhận dạng được văn bản.")
        
        # Ghi file khi đủ 100 câu hoặc khi kết thúc
        if len(current_file_text) >= 100 or i == num_slides:
            file_name = f"cau_hoi_{file_counter:03d}.md"
            file_path = os.path.join(output_dir, file_name)
            
            print(f"\n-> Đang ghi file: {file_name}")
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(f"# CÂU HỎI {file_counter:03d}\n\n")
                f.write("\n\n---\n\n".join(current_file_text))
            
            current_file_text = []
            file_counter += 1
        
        if i < num_slides:
            pyautogui.press('down')
            time.sleep(delay)
    
    print(f"\n-> Hoàn thành! File tổng hợp đã được cập nhật liên tục: {final_output_file}")

def main():
    print("==============================================")
    print("      TRỢ LÝ HỌC TẬP TRẮC NGHIỆM (AI)      ")
    print("==============================================")
    
    print("\n*** VUI LÒNG CHUẨN BỊ TRƯỚC KHI BẮT ĐẦU: ***")
    print("1. Mở trình duyệt và bài trắc nghiệm của bạn.")
    print("2. Nhấn F11 để vào chế độ TOÀN MÀN HÌNH.")
    print("3. Di chuyển đến CÂU HỎI ĐẦU TIÊN để căn chỉnh.")
    
    output_dir = "ket_qua_hoc_tap"
    os.makedirs(output_dir, exist_ok=True)
    
    input("\nNhấn Enter khi bạn đã sẵn sàng để bắt đầu căn chỉnh...")
    main_region = calibrate_main_region(output_dir)
    question_region, answer_region = calibrate_split_line(main_region, output_dir)
    print("\n--- CĂN CHỈNH HOÀN TẤT! ---")

    print("\n*** NHẬP THÔNG TIN CUỐI CÙNG: ***")
    try:
        total_slides = int(input("(*) Vui lòng nhập TỔNG SỐ CÂU HỎI cần lấy: "))
        delay = float(input("(*) Nhập độ trễ giữa các câu (giây, vd: 2): "))
        
        # Hỏi có sử dụng Gemini hay không
        use_gemini_input = input("(*) Có sử dụng Gemini để định dạng câu hỏi không? (y/n): ").strip().lower()
        use_gemini = use_gemini_input in ['y', 'yes', 'có', 'co']
        
        # Luôn cần OCR.space API key
        ocrspace_api_key = input("(*) Vui lòng nhập OCR.space API key của bạn: ").strip()
        
        if use_gemini:
            gemini_api_key = input("(*) Vui lòng nhập Khóa API Gemini của bạn: ").strip()
            
            print("\n-> Đang xác thực Khóa API Gemini...")
            if not validate_gemini_api_key(gemini_api_key):
                return
            print("-> Khóa API Gemini hợp lệ!")
        else:
            gemini_api_key = ""  # Không cần API key nếu không dùng Gemini
            print("-> Chế độ chỉ OCR (không sử dụng Gemini)")
            
    except ValueError:
        print("\n[Lỗi] Vui lòng nhập một con số hợp lệ.")
        return

    print("\n-> Đang xác thực OCR.space API key...")
    if not validate_ocrspace_api_key(ocrspace_api_key):
        print("[Lỗi] Không thể xác thực OCR.space API key. Vui lòng kiểm tra API key.")
        return

    print("\n!!! CHUẨN BỊ! HÃY CLICK LẠI VÀO CỬA SỔ TRÌNH DUYỆT NGAY BÂY GIỜ !!!")
    for i in range(5, 0, -1):
        print(f"Bắt đầu sau {i} giây... ", end='\r')
        time.sleep(1)
    
    capture_and_process(total_slides, output_dir, delay, ocrspace_api_key, gemini_api_key, question_region, answer_region, use_gemini)

    print("\n==============================================")
    print("                 HOÀN TẤT!                  ")
    print(f"Toàn bộ kết quả đã được tổng hợp trong file '{os.path.basename(output_dir)}{os.sep}tong_hop_cau_hoi_va_giai_thich.md'.")
    print("==============================================")
    play_sound(3)

if __name__ == "__main__":
    main()