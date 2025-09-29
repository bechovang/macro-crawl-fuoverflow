import pyautogui
import time
import os
import sys
from fpdf import FPDF
from PIL import Image
from tqdm import tqdm
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pygame
import tkinter as tk  # --- THÊM MỚI: Thư viện cho giao diện đồ họa (GUI)
from tkinter import messagebox

# Cấu hình: nếu muốn tự động tránh chồng lấn, bật thành True
ENFORCE_NON_OVERLAP = False

# ==============================================================================
# LỚP CÔNG CỤ CANH CHỈNH BẰNG CHUỘT (TÍCH HỢP TRỰC TIẾP)
# ==============================================================================
class MouseCalibrationTool:
    """Một lớp GUI để người dùng kéo thả chuột chọn một vùng trên màn hình."""
    def __init__(self, instructions_text):
        self.root = tk.Tk()
        self.root.title("Công cụ Canh chỉnh Vùng chụp")
        self.root.attributes('-fullscreen', True)
        self.root.attributes('-alpha', 0.2)  # Màn hình mờ để thấy phía sau
        self.root.configure(bg='black')

        self.start_x = None
        self.start_y = None
        self.rect = None
        self.selected_region = None

        # Tính hệ số scale giữa toạ độ Tkinter (logical) và PyAutoGUI (pixel thật)
        # Điều này giúp khắc phục sai lệch khi Windows dùng DPI scaling
        try:
            screen_w, screen_h = pyautogui.size()
            tk_w = self.root.winfo_screenwidth()
            tk_h = self.root.winfo_screenheight()
            self.scale_x = (screen_w / tk_w) if tk_w else 1.0
            self.scale_y = (screen_h / tk_h) if tk_h else 1.0
        except Exception:
            self.scale_x = 1.0
            self.scale_y = 1.0

        self.canvas = tk.Canvas(self.root, cursor="cross", bg="black")
        self.canvas.pack(fill="both", expand=True)

        self.canvas.bind("<ButtonPress-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.on_mouse_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)
        self.root.bind("<Escape>", self.cancel_selection)
        
        # Hiển thị hướng dẫn
        self.instructions = tk.Label(
            self.root, text=instructions_text, font=("Arial", 16, "bold"),
            fg="white", bg="black", relief="raised", borderwidth=3
        )
        self.instructions.place(relx=0.5, rely=0.5, anchor="center")
        
    def on_button_press(self, event):
        self.instructions.place_forget() # Ẩn hướng dẫn khi bắt đầu kéo
        self.start_x = self.canvas.canvasx(event.x)
        self.start_y = self.canvas.canvasy(event.y)
        if self.rect:
            self.canvas.delete(self.rect)
        self.rect = self.canvas.create_rectangle(
            self.start_x, self.start_y, self.start_x, self.start_y,
            outline='red', width=3
        )

    def on_mouse_drag(self, event):
        cur_x = self.canvas.canvasx(event.x)
        cur_y = self.canvas.canvasy(event.y)
        self.canvas.coords(self.rect, self.start_x, self.start_y, cur_x, cur_y)

    def on_button_release(self, event):
        end_x = self.canvas.canvasx(event.x)
        end_y = self.canvas.canvasy(event.y)
        
        x1 = min(self.start_x, end_x)
        y1 = min(self.start_y, end_y)
        x2 = max(self.start_x, end_x)
        y2 = max(self.start_y, end_y)

        # Quy đổi sang toạ độ pixel thật theo PyAutoGUI và lưu vùng đã chọn
        px_left = int(x1 * self.scale_x)
        px_top = int(y1 * self.scale_y)
        px_right = int(x2 * self.scale_x)
        px_bottom = int(y2 * self.scale_y)
        px_width = max(1, px_right - px_left)
        px_height = max(1, px_bottom - px_top)
        self.selected_region = (px_left, px_top, px_width, px_height)
        self.root.quit()

    def cancel_selection(self, event=None):
        self.selected_region = None
        self.root.quit()

    def run(self):
        self.root.mainloop()
        self.root.destroy()
        return self.selected_region

def calibrate_with_mouse(instructions):
    """Hàm helper để chạy công cụ canh chỉnh và trả về kết quả."""
    tool = MouseCalibrationTool(instructions)
    region = tool.run()
    if region and (region[2] == 0 or region[3] == 0): # Nếu chỉ click mà không kéo
        print("\n❌ Lỗi: Vùng chọn không hợp lệ (chiều rộng hoặc cao bằng 0).")
        return None
    return region

# ==============================================================================
# PHẦN CODE CHÍNH CỦA CHƯƠNG TRÌNH
# ==============================================================================

def play_sound(sound_type):
    """Hàm tiện ích để phát các loại âm thanh khác nhau."""
    try:
        if not pygame.mixer.get_init():
            pygame.mixer.init()
        if sound_type == 2:
            if os.path.exists("purchase-success.mp3"):
                pygame.mixer.music.load("purchase-success.mp3")
                pygame.mixer.music.play()
        elif sound_type == 3:
            if os.path.exists("victory.mp3"):
                pygame.mixer.music.load("victory.mp3")
                pygame.mixer.music.play()
    except Exception as e:
        print(f"[Debug] Không thể phát âm thanh: {e}")
        pass

def show_image_preview(image_path, title="Xem trước ảnh"):
    """Sử dụng Matplotlib để hiển thị ảnh xem trước."""
    try:
        img = mpimg.imread(image_path)
        plt.figure(figsize=(10, 8))
        plt.imshow(img)
        plt.title(title, fontsize=16)
        plt.axis('off')
        print("-> Đang hiển thị cửa sổ xem trước. Hãy đóng cửa sổ này để tiếp tục...")
        plt.show()
    except Exception as e:
        print(f"\n[Lỗi] Không thể hiển thị ảnh xem trước: {e}")

def show_split_image_preview(q_path, a_path):
    """Hiển thị cả ảnh Đề và Đáp án trong cùng một cửa sổ."""
    try:
        q_img = mpimg.imread(q_path)
        a_img = mpimg.imread(a_path)
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
        fig.suptitle("Xem trước đường cắt (Đóng cửa sổ này để tiếp tục)", fontsize=16)
        ax1.imshow(q_img)
        ax1.set_title("VÙNG CÂU HỎI (phía trên)")
        ax1.axis('off')
        ax2.imshow(a_img)
        ax2.set_title("VÙNG ĐÁP ÁN (phía dưới)")
        ax2.axis('off')
        plt.tight_layout(rect=[0, 0.03, 1, 0.95])
        print("-> Đang hiển thị cửa sổ xem trước. Hãy đóng cửa sổ này để tiếp tục...")
        plt.show()
    except Exception as e:
        print(f"\n[Lỗi] Không thể hiển thị ảnh xem trước: {e}")

def _clamp_region_to_bounds(region, bounds):
    """Giới hạn một region (left, top, w, h) vào trong bounds (left, top, w, h)."""
    if not region or not bounds:
        return region
    r_left, r_top, r_w, r_h = region
    b_left, b_top, b_w, b_h = bounds
    r_right = r_left + r_w
    r_bottom = r_top + r_h
    b_right = b_left + b_w
    b_bottom = b_top + b_h

    cl_left = max(r_left, b_left)
    cl_top = max(r_top, b_top)
    cl_right = min(r_right, b_right)
    cl_bottom = min(r_bottom, b_bottom)

    cl_w = max(1, cl_right - cl_left)
    cl_h = max(1, cl_bottom - cl_top)
    return (cl_left, cl_top, cl_w, cl_h)

def create_pdf_from_images(image_paths, output_pdf_path):
    """Gom các cặp ảnh câu hỏi và đáp án vào một file PDF."""
    print(f"\n-> Bắt đầu tạo file PDF: {os.path.basename(output_pdf_path)}")
    pdf = FPDF('P', 'mm', 'A4')
    pdf.set_font('Arial', 'B', 16)

    for i, (q_path, a_path) in enumerate(tqdm(image_paths, desc="Đang tạo PDF")):
        pdf.add_page()
        pdf.cell(0, 10, f'Cau hoi {i + 1}', 0, 1, 'C')
        pdf.ln(5)
        try:
            with Image.open(q_path) as img:
                aspect_ratio = img.height / img.width
                pdf_img_width = pdf.w - 20
                pdf_img_height = pdf_img_width * aspect_ratio
                pdf.image(q_path, x=10, w=pdf_img_width, h=pdf_img_height)
        except Exception as e:
            print(f"\n[Lỗi] Không thể thêm ảnh câu hỏi {i+1} vào PDF: {e}")
        pdf.ln(5)
        try:
            with Image.open(a_path) as img:
                aspect_ratio = img.height / img.width
                pdf_img_width = pdf.w - 20
                pdf_img_height = pdf_img_width * aspect_ratio
                pdf.image(a_path, x=10, w=pdf_img_width, h=pdf_img_height)
        except Exception as e:
            print(f"\n[Lỗi] Không thể thêm ảnh đáp án {i+1} vào PDF: {e}")

    pdf.output(output_pdf_path)
    print(f"✅ Đã tạo PDF thành công!")

def capture_images(num_slides, output_dir, delay, question_region, answer_region):
    """Chụp ảnh màn hình và lưu lại đường dẫn để tạo PDF."""
    print("\n==============================================")
    print("           BẮT ĐẦU CHỤP ẢNH CÂU HỎI         ")
    print("==============================================")
    captured_image_paths = []
    for i in tqdm(range(1, num_slides + 1), desc="Đang chụp các câu hỏi"):
        question_img_path = os.path.join(output_dir, f"cau_{i:03d}_de.png")
        answer_img_path = os.path.join(output_dir, f"cau_{i:03d}_dap_an.png")
        pyautogui.screenshot(question_img_path, region=question_region)
        pyautogui.screenshot(answer_img_path, region=answer_region)
        captured_image_paths.append((question_img_path, answer_img_path))
        play_sound(2)
        if i < num_slides:
            pyautogui.press('right')
            time.sleep(delay)
    print("\n-> Đã chụp xong toàn bộ ảnh!")
    return captured_image_paths

# DÁN CODE NÀY ĐỂ THAY THẾ TOÀN BỘ HÀM main() CŨ

def main():
    """Hàm chính điều khiển toàn bộ chương trình."""
    print("==============================================")
    print("      CÔNG CỤ TẠO PDF TRẮC NGHIỆM TỰ ĐỘNG     ")
    print("==============================================")
    print("\n*** VUI LÒNG CHUẨN BỊ TRƯỚC KHI BẮT ĐẦU: ***")
    print("1. Mở trình duyệt và bài trắc nghiệm của bạn.")
    print("2. Nhấn F11 để vào chế độ TOÀN MÀN HÌNH.")
    print("3. Di chuyển đến CÂU HỎI ĐẦU TIÊN để căn chỉnh.")
    
    output_dir = "ket_qua_hoc_tap"
    images_dir = os.path.join(output_dir, "images")
    os.makedirs(images_dir, exist_ok=True)
    
    input("\nNhấn Enter để bắt đầu căn chỉnh...")

    # --- BƯỚC 1: CANH CHỈNH VÙNG CHÍNH BẰNG CHUỘT ---
    main_region = None
    while not main_region:
        print("\n--- BƯỚC 1: CHỌN VÙNG CHÍNH ---")
        instructions1 = (
            "KÉO CHUỘT để chọn vùng chứa CẢ CÂU HỎI VÀ ĐÁP ÁN\n"
            "(Dùng màn hình chính/primary monitor; Nhấn ESC để hủy)"
        )
        main_region = calibrate_with_mouse(instructions1)
        if not main_region:
            if input("Bạn có muốn thử lại không? (y/n): ").lower() != 'y':
                print("Đã hủy chương trình.")
                return
        else:
            print(f"✅ Vùng chính đã chọn: {main_region}")
            preview_path = os.path.join(images_dir, "preview_main.png")
            pyautogui.screenshot(preview_path, region=main_region)
            show_image_preview(preview_path, "XEM TRƯỚC VÙNG CHÍNH")
            if input("  Vùng chụp này đã OK chưa? (ok/thử lại): ").lower() != 'ok':
                main_region = None
            os.remove(preview_path)


    # --- BƯỚC 2: CHỌN RÕ 2 VÙNG: CÂU HỎI và ĐÁP ÁN ---
    question_region = None
    answer_region = None
    while not (question_region and answer_region):
        print("\n--- BƯỚC 2: CHỌN VÙNG CÂU HỎI ---")
        instructions2 = (
            "Bây giờ, KÉO CHUỘT để chọn vùng CHỈ CÓ CÂU HỎI (phần đề bài)\n"
            "(Dùng màn hình chính/primary monitor; Nhấn ESC để hủy)"
        )
        temp_q = calibrate_with_mouse(instructions2)
        if not temp_q:
            if input("Bạn có muốn thử lại không? (y/n): ").lower() != 'y':
                print("Đã hủy chương trình.")
                return
            continue

        print("\n--- BƯỚC 3: CHỌN VÙNG ĐÁP ÁN ---")
        instructions3 = (
            "KÉO CHUỘT để chọn vùng CHỈ CÓ ĐÁP ÁN (phần bên dưới)\n"
            "(Dùng màn hình chính/primary monitor; Nhấn ESC để hủy)"
        )
        temp_a = calibrate_with_mouse(instructions3)
        if not temp_a:
            if input("Bạn có muốn thử lại không? (y/n): ").lower() != 'y':
                print("Đã hủy chương trình.")
                return
            continue

        # Giới hạn mỗi vùng vào trong vùng chính (giữ nguyên vị trí/lề người dùng đã chọn)
        main_x, main_y, main_w, main_h = main_region
        temp_q = _clamp_region_to_bounds(temp_q, main_region)
        temp_a = _clamp_region_to_bounds(temp_a, main_region)

        q_left, q_top, q_w, q_h = temp_q
        a_left, a_top, a_w, a_h = temp_a

        question_region = (q_left, q_top, q_w, q_h)
        answer_region = (a_left, a_top, a_w, a_h)

        # Tuỳ chọn: Nếu bật ENFORCE_NON_OVERLAP, tách 2 vùng để không chồng lấn
        if ENFORCE_NON_OVERLAP:
            q_bottom = question_region[1] + question_region[3]
            if answer_region[1] < q_bottom:
                a_top_new = q_bottom
                a_h_new = max(1, (answer_region[1] + answer_region[3]) - a_top_new)
                answer_region = (answer_region[0], a_top_new, answer_region[2], a_h_new)

        print(f"✅ Vùng câu hỏi: {question_region}")
        print(f"✅ Vùng đáp án: {answer_region}")

        q_preview = os.path.join(images_dir, "preview_q.png")
        a_preview = os.path.join(images_dir, "preview_a.png")
        pyautogui.screenshot(q_preview, region=question_region)
        pyautogui.screenshot(a_preview, region=answer_region)
        show_split_image_preview(q_preview, a_preview)
        ok = input("  Hai vùng này đã OK chưa? (ok/thử lại): ").lower()
        os.remove(q_preview)
        os.remove(a_preview)
        if ok != 'ok':
            question_region = None
            answer_region = None

    print("\n--- CĂN CHỈNH HOÀN TẤT! ---")

    try:
        total_slides = int(input("(*) Vui lòng nhập TỔNG SỐ CÂU HỎI cần lấy: "))
        delay = float(input("(*) Nhập độ trễ giữa các câu (giây, vd: 2): "))
    except ValueError:
        print("\n[Lỗi] Vui lòng nhập một con số hợp lệ.")
        return

    print("\n!!! CHUẨN BỊ! HÃY CLICK LẠI VÀO CỬA SỔ TRÌNH DUYỆT NGAY BÂY GIỜ !!!")
    for i in range(5, 0, -1):
        print(f"Bắt đầu sau {i} giây... ", end='\r')
        time.sleep(1)

    image_paths = capture_images(total_slides, images_dir, delay, question_region, answer_region)
    
    pdf_output_path = ""
    if image_paths:
        pdf_output_path = os.path.join(output_dir, "tong_hop_cau_hoi.pdf")
        create_pdf_from_images(image_paths, pdf_output_path)
    else:
        print("\n[Lỗi] Không có ảnh nào được chụp, không thể tạo PDF.")

    print("\n==============================================")
    print("                 HOÀN TẤT!                  ")
    if pdf_output_path:
        print(f"Toàn bộ kết quả đã được tổng hợp trong file PDF tại: '{pdf_output_path}'")
    print(f"Các file ảnh được lưu tại thư mục: '{images_dir}'")
    print("==============================================")
    play_sound(3)

if __name__ == "__main__":
    main()