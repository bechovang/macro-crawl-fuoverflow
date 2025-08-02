import pyautogui
import time
import os

def capture_slides(num_slides, output_dir, delay_between_slides):
    """
    Hàm chính để chụp ảnh màn hình trong một vùng cụ thể và chuyển slide.
    """
    print("\n==============================================")
    print("           BẮT ĐẦU CHỤP SLIDES             ")
    print("==============================================")
    
    # Lấy kích thước màn hình MỘT LẦN DUY NHẤT
    screen_width, screen_height = pyautogui.size()
    print(f"-> Màn hình có kích thước: {screen_width}x{screen_height} pixels")

    # --- THAY ĐỔI QUAN TRỌNG: TÍNH TOÁN VÙNG CHỤP THEO YÊU CẦU ---
    # Tính toán điểm bắt đầu (thụt vào 20% từ trên và trái)
    left_start = int(screen_width * 0.12)
    top_start = int(screen_height * 0.20)
    
    # Tính toán chiều rộng và chiều cao của vùng chụp (phần còn lại, tức 80%)
    capture_width = screen_width - left_start
    capture_height = screen_height - top_start
    
    # Tạo ra vùng chụp theo định dạng (left, top, width, height)
    capture_region = (left_start, top_start, capture_width, capture_height)
    
    print(f"-> Vùng chụp đã được xác định: bắt đầu tại ({left_start}, {top_start}) với kích thước {capture_width}x{capture_height}")
    
    for i in range(1, num_slides + 1):
        # Tạo tên file cho ảnh chụp màn hình
        filename = os.path.join(output_dir, f"slide_{i}.png")
        
        # Chụp vùng màn hình đã xác định
        screenshot = pyautogui.screenshot(region=capture_region)
        screenshot.save(filename)
        
        print(f"-> Đã chụp và lưu slide {i} tại: {filename}")
        
        # Nếu đây chưa phải slide cuối, nhấn phím mũi tên xuống để chuyển slide
        if i < num_slides:
            print(f"   Chuyển sang slide tiếp theo...")
            pyautogui.press('down')
            # Chờ một chút để slide mới tải xong và các hiệu ứng hoàn tất
            time.sleep(delay_between_slides)

def main():
    """Hàm điều phối toàn bộ quy trình."""
    print("==============================================")
    print("  CHƯƠNG TRÌNH CHỤP SLIDE - GIẢ LẬP BÀN PHÍM  ")
    print("==============================================")
    
    # --- HƯỚNG DẪN SỬ DỤNG ---
    print("\n*** VUI LÒNG THỰC HIỆN CÁC BƯỚC SAU: ***")
    print("1. Mở trình duyệt Chrome của bạn.")
    print("2. Truy cập vào đúng bài Google Slides cần chụp.")
    print("3. Nhấn phím F11 để vào chế độ TOÀN MÀN HÌNH (quan trọng!).")
    print("4. Click chuột vào slide ĐẦU TIÊN của bài thuyết trình.")
    print("5. Quay lại cửa sổ này để nhập thông tin bên dưới.")
    print("-" * 30)

    # Nhận thông tin từ người dùng
    try:
        total_slides = int(input("(*) Vui lòng nhập TỔNG SỐ SLIDE cần chụp: "))
        delay = float(input("(*) Nhập độ trễ giữa các slide (giây, vd: 2): "))
    except ValueError:
        print("\n[Lỗi] Vui lòng nhập một con số hợp lệ.")
        return

    # Tạo thư mục lưu trữ nếu chưa có
    output_dir = "screenshots_output"
    os.makedirs(output_dir, exist_ok=True)
    print(f"\n-> Ảnh sẽ được lưu trong thư mục: '{output_dir}'")

    # Đếm ngược 5 giây để người dùng có thời gian chuyển về cửa sổ Chrome
    print("\n!!! CHUẨN BỊ! HÃY CLICK LẠI VÀO CỬA SỔ CHROME NGAY BÂY GIỜ !!!")
    for i in range(5, 0, -1):
        # In đè lên cùng một dòng
        print(f"Bắt đầu sau {i} giây... ", end='\r')
        time.sleep(1)
    
    # Bắt đầu công việc
    capture_slides(total_slides, output_dir, delay)

    print("\n==============================================")
    print("                 HOÀN TẤT!                  ")
    print(f"Toàn bộ {total_slides} ảnh đã được lưu trong thư mục '{output_dir}'.")
    print("==============================================")

if __name__ == "__main__":
    main()