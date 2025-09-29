# Hướng dẫn Canh chỉnh bằng Chuột

## 🖱️ Công cụ Canh chỉnh Vùng chụp (DPI-safe)

Công cụ canh chỉnh bằng chuột giúp bạn chọn vùng chụp chính xác hơn so với phương pháp nhập phần trăm thủ công.

### 📋 Cách sử dụng:

1. **Chuẩn bị:**
   - Đảm bảo cửa sổ trình duyệt đang ở chế độ toàn màn hình (F11)
   - Di chuyển đến câu hỏi đầu tiên

2. **Chọn phương pháp:**
   - Khi chương trình hỏi, chọn option `2` (Chọn vùng bằng chuột)
   - Nhấn Enter để bắt đầu

3. **Chọn vùng:**
   - Một cửa sổ mờ sẽ xuất hiện phủ toàn màn hình (ở **màn hình chính/primary monitor**)
   - Kéo chuột để chọn vùng. Tọa độ chuột đã được chuẩn hoá DPI để trùng khớp với PyAutoGUI trên Windows (kể cả 125%, 150%).
   - Khung đỏ sẽ hiển thị vùng được chọn
   - Kích thước vùng sẽ hiển thị ở góc trên bên trái

4. **Xác nhận:**
   - Nhấn **Enter** để xác nhận vùng đã chọn
   - Nhấn **Escape** để chọn lại

### 💡 Mẹo sử dụng:

- **Chọn vùng vừa phải:** Không chọn quá rộng để tránh bắt thêm các yếu tố không cần thiết
- **Bao gồm đầy đủ:** Đảm bảo vùng chọn bao gồm cả câu hỏi và các đáp án
- **Tránh thanh công cụ:** Không chọn các thanh công cụ trình duyệt
- **Có thể chọn lại:** Nếu không ưng ý, nhấn Escape và chọn lại

### 🔧 Tính năng:

- **Hiển thị kích thước:** Kích thước vùng được chọn hiển thị real-time
- **DPI-safe:** Toạ độ đã được quy đổi chuẩn giữa Tkinter và PyAutoGUI
- **Xem trước:** Sau khi chọn, vẫn có thể xem trước để xác nhận

### ⚠️ Lưu ý:

- Dùng **màn hình chính (primary monitor)** để chọn vùng. Không di chuyển cửa sổ trình duyệt sau khi căn chỉnh.
- Với `tao_pdf_trac_nghiem.py`, bạn sẽ chọn 3 lần bằng chuột: Vùng chính → Vùng Câu hỏi → Vùng Đáp án. Preview sẽ hiển thị đúng 2 ảnh như bạn đã chọn.
- Tọa độ đã DPI-safe. Nếu vẫn lệch, kiểm tra lại tỉ lệ thu phóng Windows và thử chọn lại.

### 🎯 Ưu điểm:

- **Chính xác hơn:** Chọn vùng trực quan thay vì ước lượng phần trăm
- **Nhanh hơn:** Không cần thử nhiều lần với các giá trị khác nhau
- **Dễ sử dụng:** Giao diện trực quan, dễ hiểu
- **Linh hoạt:** Có thể chọn lại nhiều lần nếu cần 