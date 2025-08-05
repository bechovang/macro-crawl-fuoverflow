#!/usr/bin/env python3
"""
Công cụ canh chỉnh bằng chuột để chọn vùng chụp chính xác.
"""

import tkinter as tk
from tkinter import messagebox
import pyautogui
import time
from PIL import Image, ImageTk
import numpy as np

class MouseCalibrationTool:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Công cụ Canh chỉnh Vùng chụp")
        self.root.attributes('-fullscreen', True)
        self.root.attributes('-alpha', 0.3)  # Mờ để thấy màn hình phía sau
        self.root.configure(bg='black')
        
        # Biến để lưu vùng được chọn
        self.start_x = None
        self.start_y = None
        self.end_x = None
        self.end_y = None
        self.is_drawing = False
        
        # Canvas để vẽ
        self.canvas = tk.Canvas(self.root, bg='black', highlightthickness=0)
        self.canvas.pack(fill='both', expand=True)
        
        # Bind events
        self.canvas.bind('<Button-1>', self.on_mouse_down)
        self.canvas.bind('<B1-Motion>', self.on_mouse_drag)
        self.canvas.bind('<ButtonRelease-1>', self.on_mouse_up)
        self.root.bind('<Escape>', self.cancel_selection)
        self.root.bind('<Return>', self.confirm_selection)
        
        # Hướng dẫn
        self.show_instructions()
        
        # Biến kết quả
        self.selected_region = None
        
    def show_instructions(self):
        """Hiển thị hướng dẫn sử dụng."""
        instructions = """
        🖱️ CÔNG CỤ CANH CHỈNH VÙNG CHỤP
        
        📋 HƯỚNG DẪN:
        1. Kéo chuột để chọn vùng chụp
        2. Nhấn Enter để xác nhận
        3. Nhấn Escape để hủy
        
        💡 MẸO:
        - Chọn vùng chứa câu hỏi và đáp án
        - Tránh chọn quá rộng để tăng độ chính xác
        - Có thể chọn lại nhiều lần
        """
        
        # Tạo label hướng dẫn
        self.instruction_label = tk.Label(
            self.root,
            text=instructions,
            bg='black',
            fg='white',
            font=('Arial', 12),
            justify='left'
        )
        self.instruction_label.place(x=10, y=10)
        
        # Tự động ẩn sau 5 giây
        self.root.after(5000, self.instruction_label.destroy)
    
    def on_mouse_down(self, event):
        """Xử lý khi nhấn chuột."""
        self.start_x = event.x
        self.start_y = event.y
        self.is_drawing = True
        
        # Xóa hình chữ nhật cũ nếu có
        self.canvas.delete("selection_rect")
    
    def on_mouse_drag(self, event):
        """Xử lý khi kéo chuột."""
        if self.is_drawing:
            self.end_x = event.x
            self.end_y = event.y
            
            # Xóa hình chữ nhật cũ
            self.canvas.delete("selection_rect")
            
            # Vẽ hình chữ nhật mới
            x1 = min(self.start_x, self.end_x)
            y1 = min(self.start_y, self.end_y)
            x2 = max(self.start_x, self.end_x)
            y2 = max(self.start_y, self.end_y)
            
            # Vẽ khung chọn với màu đỏ
            self.canvas.create_rectangle(
                x1, y1, x2, y2,
                outline='red',
                width=3,
                tags="selection_rect"
            )
            
            # Hiển thị kích thước
            width = x2 - x1
            height = y2 - y1
            self.canvas.create_text(
                x1 + 10, y1 - 10,
                text=f"{width} x {height}",
                fill='red',
                font=('Arial', 12, 'bold'),
                tags="selection_rect"
            )
    
    def on_mouse_up(self, event):
        """Xử lý khi thả chuột."""
        if self.is_drawing:
            self.end_x = event.x
            self.end_y = event.y
            self.is_drawing = False
            
            # Tính toán vùng được chọn
            x1 = min(self.start_x, self.end_x)
            y1 = min(self.start_y, self.end_y)
            x2 = max(self.start_x, self.end_x)
            y2 = max(self.start_y, self.end_y)
            
            # Lưu vùng được chọn
            self.selected_region = (x1, y1, x2 - x1, y2 - y1)
            
            # Hiển thị thông tin
            self.show_region_info()
    
    def show_region_info(self):
        """Hiển thị thông tin vùng được chọn."""
        if self.selected_region:
            x, y, width, height = self.selected_region
            
            info_text = f"""
            ✅ VÙNG ĐÃ CHỌN:
            
            📍 Vị trí: ({x}, {y})
            📏 Kích thước: {width} x {height}
            
            💡 Nhấn Enter để xác nhận
            💡 Nhấn Escape để chọn lại
            """
            
            # Tạo cửa sổ thông tin
            info_window = tk.Toplevel(self.root)
            info_window.title("Thông tin Vùng chọn")
            info_window.geometry("300x200")
            info_window.configure(bg='lightblue')
            
            tk.Label(
                info_window,
                text=info_text,
                bg='lightblue',
                font=('Arial', 10),
                justify='left'
            ).pack(pady=20)
            
            # Tự động đóng sau 3 giây
            info_window.after(3000, info_window.destroy)
    
    def confirm_selection(self, event=None):
        """Xác nhận vùng được chọn."""
        if self.selected_region:
            self.root.quit()
        else:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn một vùng trước!")
    
    def cancel_selection(self, event=None):
        """Hủy lựa chọn."""
        self.selected_region = None
        self.root.quit()
    
    def get_selected_region(self):
        """Trả về vùng được chọn."""
        return self.selected_region
    
    def run(self):
        """Chạy công cụ canh chỉnh."""
        self.root.mainloop()
        self.root.destroy()
        return self.selected_region

def calibrate_with_mouse():
    """Canh chỉnh vùng chụp bằng chuột."""
    print("\n=== CANH CHỈNH BẰNG CHUỘT ===")
    print("-> Chuẩn bị mở công cụ canh chỉnh...")
    print("-> Hãy đảm bảo cửa sổ trình duyệt đang ở chế độ toàn màn hình")
    print("-> Nhấn Enter để bắt đầu...")
    input()
    
    # Tạo công cụ canh chỉnh
    tool = MouseCalibrationTool()
    selected_region = tool.run()
    
    if selected_region:
        x, y, width, height = selected_region
        print(f"\n✅ Vùng đã chọn: ({x}, {y}, {width}, {height})")
        
        # Tính toán phần trăm
        screen_width, screen_height = pyautogui.size()
        left_percent = (x / screen_width) * 100
        top_percent = (y / screen_height) * 100
        width_percent = (width / screen_width) * 100
        height_percent = (height / screen_height) * 100
        
        print(f"📊 Phần trăm:")
        print(f"   - Lề trái: {left_percent:.1f}%")
        print(f"   - Lề trên: {top_percent:.1f}%")
        print(f"   - Chiều rộng: {width_percent:.1f}%")
        print(f"   - Chiều cao: {height_percent:.1f}%")
        
        return selected_region
    else:
        print("\n❌ Không có vùng nào được chọn.")
        return None

if __name__ == "__main__":
    # Test công cụ canh chỉnh
    region = calibrate_with_mouse()
    if region:
        print(f"\n🎯 Kết quả: {region}")
    else:
        print("\n❌ Không có kết quả.") 