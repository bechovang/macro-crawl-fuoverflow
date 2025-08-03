import pyautogui
import time
import os
import google.generativeai as genai
from tqdm import tqdm
from google.cloud import vision
from google.oauth2 import service_account
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

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


def extract_text_from_image_ocr(image_path, credentials_path):
    #... (Giữ nguyên không đổi)
    try:
        credentials = service_account.Credentials.from_service_account_file(credentials_path)
        client = vision.ImageAnnotatorClient(credentials=credentials)
        with open(image_path, "rb") as image_file:
            content = image_file.read()
        image = vision.Image(content=content)
        response = client.document_text_detection(image=image)
        if response.error.message:
            raise Exception(f"Lỗi từ Vision API: {response.error.message}")
        return response.full_text_annotation.text
    except Exception as e:
        tqdm.write(f"\n[Lỗi] OCR thất bại: {e}")
        return ""

def format_question_and_explanation(question_text, answer_text, question_number):
    #... (Giữ nguyên không đổi)
    prompt = f"""
    Bạn là một gia sư AI chuyên nghiệp. Nhiệm vụ của bạn là đọc văn bản của một câu hỏi trắc nghiệm và phần ghi chú đáp án, sau đó định dạng lại một cách rõ ràng và cung cấp lời giải thích ngắn gọn.

    Văn bản câu hỏi (đề bài):
    ---
    {question_text}
    ---
    Văn bản ghi chú (chứa đáp án):
    ---
    {answer_text}
    ---

    Yêu cầu:
    1.  **Định dạng câu hỏi:** Bắt đầu bằng "Câu {question_number}:", liệt kê các đáp án A, B, C, D rõ ràng.
    2.  **Xác định và đánh dấu đáp án đúng:** Dựa vào phần ghi chú, tìm ra đáp án đúng và đánh dấu nó bằng `(**ĐÁP ÁN ĐÚNG**)`.
    3.  **Cung cấp lời giải thích:** Dưới phần đáp án, thêm một mục `**Giải thích:**` và giải thích ngắn gọn, súc tích tại sao đáp án đó lại đúng, dựa trên thông tin trong phần ghi chú.
    4.  **Loại bỏ các chi tiết thừa** trong cả câu hỏi và phần giải thích.
    5.  **Trả lời chỉ bằng nội dung đã định dạng theo Markdown.**
    """
    try:
        model = genai.GenerativeModel('gemini-1.5-pro-latest')
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        tqdm.write(f"\n[Lỗi] Gemini: Không thể định dạng câu {question_number}. Lỗi: {e}")
        return f"--- LỖI XỬ LÝ CÂU {question_number} ---\nĐề: {question_text}\nĐáp án: {answer_text}\n--- KẾT THÚC LỖI ---"


def calibrate_main_region(output_dir):
    """**Đã sửa:** Hàm tương tác để người dùng căn chỉnh vùng chụp chính."""
    screen_width, screen_height = pyautogui.size()
    print("\n--- BƯỚC 1: CĂN CHỈNH VÙNG CHỤP CHÍNH ---")
    
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
            
            # Sử dụng hàm xem trước mới, đáng tin cậy
            show_image_preview(preview_path, "XEM TRƯỚC VÙNG CHỤP CHÍNH")
            
            confirm = input("  Vùng chụp này đã OK chưa? (ok/thử lại): ").lower()
            if confirm == 'ok':
                os.remove(preview_path)
                return region
        except ValueError:
            print("  Vui lòng nhập một con số!")
        except Exception as e:
            print(f"  Có lỗi xảy ra: {e}")


def calibrate_split_line(main_region, output_dir):
    """**Đã sửa:** Hàm tương tác để người dùng căn chỉnh đường cắt ngang."""
    print("\n--- BƯỚC 2: CĂN CHỈNH ĐƯỜNG CẮT NGANG (ĐỀ / ĐÁP ÁN) ---")
    
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

            # Sử dụng hàm xem trước mới, hiển thị cả 2 ảnh cùng lúc
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

def capture_and_process(num_slides, output_dir, delay, creds_path, gemini_key, question_region, answer_region):
    #... (Giữ nguyên không đổi)
    print("\n==============================================")
    print("           BẮT ĐẦU THU THẬP DỮ LIỆU         ")
    print("==============================================")
    
    final_output_file = os.path.join(output_dir, "tong_hop_cau_hoi_va_giai_thich.md")
    all_formatted_text = []
    
    for i in tqdm(range(1, num_slides + 1), desc="Đang xử lý các câu hỏi"):
        question_img_path = os.path.join(output_dir, f"temp_question_{i}.png")
        answer_img_path = os.path.join(output_dir, f"temp_answer_{i}.png")
        
        pyautogui.screenshot(question_img_path, region=question_region)
        pyautogui.screenshot(answer_img_path, region=answer_region)
        
        question_text = extract_text_from_image_ocr(question_img_path, creds_path)
        answer_text = extract_text_from_image_ocr(answer_img_path, creds_path)
        
        if question_text:
            formatted_text = format_question_and_explanation(question_text, answer_text, i)
            all_formatted_text.append(formatted_text)
        else:
            tqdm.write(f"-> Bỏ qua câu {i} do không nhận dạng được văn bản câu hỏi.")

        os.remove(question_img_path)
        os.remove(answer_img_path)
        
        if i < num_slides:
            pyautogui.press('down')
            time.sleep(delay)
    
    print(f"\n-> Đang ghi kết quả vào file: {final_output_file}")
    with open(final_output_file, 'w', encoding='utf-8') as f:
        f.write("# TỔNG HỢP CÁC CÂU HỎI VÀ GIẢI THÍCH\n\n")
        f.write("\n\n---\n\n".join(all_formatted_text))


def main():
    #... (Giữ nguyên không đổi)
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
        gemini_api_key = input("(*) Vui lòng nhập Khóa API Gemini của bạn: ").strip()
        credentials_path = "credentials.json"
    except ValueError:
        print("\n[Lỗi] Vui lòng nhập một con số hợp lệ.")
        return

    if not os.path.isfile(credentials_path):
        print(f"\n[Lỗi] Không tìm thấy file 'credentials.json'.")
        return

    print("\n-> Đang xác thực Khóa API Gemini...")
    if not validate_gemini_api_key(gemini_api_key):
        return
    print("-> Khóa API Gemini hợp lệ!")

    print("\n!!! CHUẨN BỊ! HÃY CLICK LẠI VÀO CỬA SỔ TRÌNH DUYỆT NGAY BÂY GIỜ !!!")
    for i in range(5, 0, -1):
        print(f"Bắt đầu sau {i} giây... ", end='\r')
        time.sleep(1)
    
    capture_and_process(total_slides, output_dir, delay, credentials_path, gemini_api_key, question_region, answer_region)

    print("\n==============================================")
    print("                 HOÀN TẤT!                  ")
    print(f"Toàn bộ kết quả đã được tổng hợp trong file '{os.path.basename(output_dir)}{os.sep}tong_hop_cau_hoi_va_giai_thich.md'.")
    print("==============================================")

if __name__ == "__main__":
    main()