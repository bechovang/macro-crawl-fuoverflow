import pyautogui
import time
import os
import google.generativeai as genai
from tqdm import tqdm
from google.cloud import vision
from google.oauth2 import service_account

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

def extract_text_from_image_ocr(image_path, credentials_path):
    """
    Sử dụng Google Cloud Vision API để trích xuất văn bản từ một file ảnh.
    """
    try:
        # Khởi tạo client với credentials được cung cấp
        credentials = service_account.Credentials.from_service_account_file(credentials_path)
        client = vision.ImageAnnotatorClient(credentials=credentials)
        
        with open(image_path, "rb") as image_file:
            content = image_file.read()
        
        image = vision.Image(content=content)
        # Sử dụng document_text_detection để có kết quả tốt nhất cho văn bản có bố cục
        response = client.document_text_detection(image=image)
        
        if response.error.message:
            raise Exception(f"Lỗi từ Vision API: {response.error.message}")
            
        return response.full_text_annotation.text
    except FileNotFoundError:
        tqdm.write(f"\n[Lỗi] OCR: Không tìm thấy file ảnh tại: {image_path}")
        return ""
    except Exception as e:
        tqdm.write(f"\n[Lỗi] OCR thất bại: {e}")
        return ""

def format_question_with_gemini(raw_text, question_number):
    """
    Sử dụng Gemini với prompt chuyên dụng để định dạng câu hỏi trắc nghiệm.
    """
    # --- PROMPT CHUYÊN DỤNG CHO HỌC TẬP VÀ TRẮC NGHIỆM ---
    prompt = f"""
    Bạn là một trợ lý học tập thông minh. Nhiệm vụ của bạn là đọc một đoạn văn bản lộn xộn được trích xuất từ ảnh chụp màn hình của một câu hỏi trắc nghiệm và định dạng nó lại một cách rõ ràng, sạch sẽ theo định dạng Markdown.

    Văn bản thô từ OCR:
    ---
    {raw_text}
    ---

    Yêu cầu:
    1.  **Xác định câu hỏi chính:** Đặt câu hỏi bắt đầu bằng "Câu {question_number}:".
    2.  **Liệt kê các đáp án:** Trình bày các phương án A, B, C, D một cách rõ ràng, mỗi đáp án trên một dòng.
    3.  **Phát hiện đáp án đúng:** Nếu có một đáp án được làm nổi bật (ví dụ: bôi đậm, có màu khác), hãy xác định đó là đáp án đúng và đánh dấu nó bằng cách thêm `(**ĐÁP ÁN ĐÚNG**)` vào cuối dòng đó. Nếu không phát hiện được, bỏ qua bước này.
    4.  **Loại bỏ các chi tiết thừa:** Xóa bỏ các số trang, tiêu đề slide, hoặc các ký tự rác không liên quan đến câu hỏi.
    5.  **Trả lời chỉ bằng nội dung đã định dạng, không thêm bất kỳ lời giải thích nào khác.**

    Ví dụ kết quả mong muốn:
    Câu 1: Thủ đô của Việt Nam là gì?
    A. TP. Hồ Chí Minh
    B. Đà Nẵng
    C. Hà Nội (**ĐÁP ÁN ĐÚNG**)
    D. Hải Phòng
    """
    
    try:
        model = genai.GenerativeModel('gemini-1.5-pro-latest')
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        tqdm.write(f"\n[Lỗi] Gemini: Không thể định dạng văn bản cho câu {question_number}. Lỗi: {e}")
        # Trả về văn bản thô nếu Gemini lỗi
        return f"--- LỖI XỬ LÝ CÂU {question_number} ---\n{raw_text}\n--- KẾT THÚC LỖI ---"

def capture_and_process(num_slides, output_dir, delay, creds_path, gemini_key):
    """
    Hàm chính để chụp ảnh, OCR, định dạng và lưu kết quả.
    """
    print("\n==============================================")
    print("           BẮT ĐẦU THU THẬP DỮ LIỆU         ")
    print("==============================================")
    
    # --- Gộp kết quả vào một file duy nhất ---
    final_output_file = os.path.join(output_dir, "tong_hop_cau_hoi.md")
    all_formatted_text = []

    screen_width, screen_height = pyautogui.size()
    left_start = int(screen_width * 0.20)
    top_start = int(screen_height * 0.20)
    capture_width = screen_width - left_start
    capture_height = screen_height - top_start
    capture_region = (left_start, top_start, capture_width, capture_height)
    
    print(f"-> Vùng chụp đã được xác định: bắt đầu tại ({left_start}, {top_start}) với kích thước {capture_width}x{capture_height}")
    
    for i in tqdm(range(1, num_slides + 1), desc="Đang xử lý các câu hỏi"):
        # Đường dẫn lưu ảnh tạm thời
        temp_image_path = os.path.join(output_dir, f"temp_slide_{i}.png")
        
        # Bước 1: Chụp ảnh
        pyautogui.screenshot(temp_image_path, region=capture_region)
        
        # Bước 2: OCR - Chuyển ảnh thành văn bản thô
        raw_text = extract_text_from_image_ocr(temp_image_path, creds_path)
        
        # Bước 3: Gemini - Định dạng văn bản
        if raw_text:
            formatted_text = format_question_with_gemini(raw_text, i)
            all_formatted_text.append(formatted_text)
            tqdm.write(f"-> Đã xử lý xong câu {i}.")
        else:
            tqdm.write(f"-> Bỏ qua câu {i} do không nhận dạng được văn bản.")

        # Xóa file ảnh tạm để tiết kiệm dung lượng
        os.remove(temp_image_path)
        
        # Bước 4: Chuyển sang slide tiếp theo
        if i < num_slides:
            pyautogui.press('down')
            time.sleep(delay)
    
    # Ghi toàn bộ kết quả đã thu thập vào file tổng hợp
    print(f"\n-> Đang ghi kết quả vào file: {final_output_file}")
    with open(final_output_file, 'w', encoding='utf-8') as f:
        f.write("# TỔNG HỢP CÁC CÂU HỎI TRẮC NGHIỆM\n\n")
        f.write("\n\n---\n\n".join(all_formatted_text))


def main():
    """Hàm điều phối toàn bộ quy trình."""
    print("==============================================")
    print("      TRỢ LÝ HỌC TẬP TRẮC NGHIỆM (AI)      ")
    print("==============================================")
    
    print("\n*** VUI LÒNG THỰC HIỆN CÁC BƯỚC SAU: ***")
    print("1. Mở trình duyệt và bài trắc nghiệm của bạn.")
    print("2. Nhấn F11 để vào chế độ TOÀN MÀN HÌNH.")
    print("3. Di chuyển đến CÂU HỎI ĐẦU TIÊN.")
    print("4. Quay lại cửa sổ này để nhập thông tin.")
    print("-" * 30)

    # Nhận thông tin từ người dùng
    try:
        total_slides = int(input("(*) Vui lòng nhập TỔNG SỐ CÂU HỎI cần lấy: "))
        delay = float(input("(*) Nhập độ trễ giữa các câu (giây, vd: 2): "))
        gemini_api_key = input("(*) Vui lòng nhập Khóa API Gemini của bạn: ").strip()
        credentials_path = "credentials.json"
    except ValueError:
        print("\n[Lỗi] Vui lòng nhập một con số hợp lệ.")
        return

    if not os.path.isfile(credentials_path):
        print(f"\n[Lỗi] Không tìm thấy file 'credentials.json'. Vui lòng đặt file trong cùng thư mục.")
        return

    print("\n-> Đang xác thực Khóa API Gemini...")
    if not validate_gemini_api_key(gemini_api_key):
        return
    print("-> Khóa API Gemini hợp lệ!")

    output_dir = "ket_qua_hoc_tap"
    os.makedirs(output_dir, exist_ok=True)
    print(f"\n-> Kết quả sẽ được lưu trong thư mục: '{output_dir}'")

    print("\n!!! CHUẨN BỊ! HÃY CLICK LẠI VÀO CỬA SỔ TRÌNH DUYỆT NGAY BÂY GIỜ !!!")
    for i in range(5, 0, -1):
        print(f"Bắt đầu sau {i} giây... ", end='\r')
        time.sleep(1)
    
    capture_and_process(total_slides, output_dir, delay, credentials_path, gemini_api_key)

    print("\n==============================================")
    print("                 HOÀN TẤT!                  ")
    print(f"Toàn bộ kết quả đã được tổng hợp trong file 'tong_hop_cau_hoi.md' trong thư mục '{output_dir}'.")
    print("==============================================")

if __name__ == "__main__":
    main()