# Trợ lý Tạo PDF Trắc nghiệm từ Màn hình

Một công cụ nhỏ gọn giúp bạn chọn vùng màn hình bằng chuột, tự động chụp lần lượt câu hỏi và đáp án trên trang trắc nghiệm, rồi ghép lại thành một file PDF gọn gàng để in/ôn tập. Công cụ sử dụng `PyAutoGUI` để chụp màn hình, `Tkinter` để chọn vùng trực quan, `matplotlib` để xem trước, và `fpdf2` để xuất PDF. Có hỗ trợ phát âm thanh báo hiệu tiến trình bằng `pygame`.

## Tổng quan

Bạn mệt mỏi với việc phải chụp và sắp xếp thủ công từng câu hỏi? Công cụ này cho phép bạn xác định chính xác vùng câu hỏi và vùng đáp án trên giao diện trắc nghiệm, sau đó tự động chụp từng câu, chuyển trang, và cuối cùng ghép thành một file PDF duy nhất để tiện xem lại.

## Tính năng chính

-   Canh chỉnh vùng bằng chuột (DPI-safe) trên màn hình chính.
-   Xem trước ảnh chụp để xác nhận trước khi chạy hàng loạt.
-   Chụp 2 vùng riêng: Câu hỏi và Đáp án, tự nhấn phím chuyển trang giữa các lần chụp.
-   Ghép tất cả ảnh thành một file PDF duy nhất theo thứ tự.
-   Phát âm thanh báo hiệu khi hoàn thành mỗi câu và khi hoàn tất.

## Yêu cầu hệ thống

-   Python 3.8+
-   Windows/macOS/Linux (đã thử nghiệm tốt trên Windows)
-   Màn hình chính chạy chế độ toàn màn hình cho trình duyệt (F11)

## Cài đặt & Thiết lập

### Bước 1: Chuẩn bị Thư mục và Code

1.  Clone repo này về máy.
2.  Đảm bảo các file âm thanh `purchase-success.mp3` và `victory.mp3` nằm cùng thư mục với script.

### Bước 2: Tạo và Kích hoạt Môi trường ảo (Khuyến nghị)

Sử dụng môi trường ảo giúp các thư viện của dự án này không ảnh hưởng đến các dự án Python khác trên máy của bạn.

1.  Mở Command Prompt hoặc Terminal trong thư mục dự án (`ai_quiz_helper`).
2.  Chạy lệnh sau để tạo môi trường ảo (tên là `venv`):
    ```bash
    python -m venv venv
    ```
3.  Kích hoạt môi trường ảo:
    -   **Trên Windows:**
        ```bash
        .\venv\Scripts\activate
        ```
        *(Sau khi chạy, bạn sẽ thấy `(venv)` ở đầu dòng lệnh của mình)*

    -   **Trên macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```

### Bước 3: Cài đặt các Thư viện cần thiết

Khi môi trường ảo đã được kích hoạt, hãy chạy lệnh sau. Lệnh này sẽ tự động đọc file `requirements.txt` và cài đặt tất cả các thư viện cần thiết.

```bash
pip install -r requirements.txt
```

**Lưu ý:**
- Để có âm thanh thông báo, hãy đặt file `purchase-success.mp3` và `victory.mp3` trong thư mục gốc dự án.
- Nếu không có âm thanh, chương trình vẫn chạy bình thường.

## Hướng dẫn sử dụng

### Bước 1: Chuẩn bị Giao diện

1.  Mở trình duyệt và truy cập vào bài trắc nghiệm của bạn.
2.  Nhấn phím **F11** để vào chế độ **TOÀN MÀN HÌNH**. Đây là bước cực kỳ quan trọng để đảm bảo ảnh chụp không bị lẫn các yếu tố thừa.
3.  Di chuyển đến câu hỏi trắc nghiệm đầu tiên.

### Bước 2: Chạy chương trình và Căn chỉnh

1.  Mở terminal trong thư mục dự án (đảm bảo môi trường ảo `venv` đã được kích hoạt).
2.  Chạy lệnh: `python tao_pdf_trac_nghiem.py`
3.  Chương trình sẽ hướng dẫn bạn qua 3 lần chọn bằng chuột (DPI-safe):
    -   Chọn Vùng chính (Main Region):
        - Kéo chuột khoanh toàn bộ khu vực chứa cả đề và đáp án.
        - Preview sẽ hiển thị; nhập `ok` để xác nhận hoặc chọn lại.
    -   Chọn Vùng Câu hỏi (Question Region):
        - Kéo chuột khoanh đúng phần đề bài ở BÊN TRONG vùng chính.
    -   Chọn Vùng Đáp án (Answer Region):
        - Kéo chuột khoanh đúng phần đáp án tham khảo ở BÊN TRONG vùng chính.
    -   Hệ thống sẽ hiển thị preview 2 ảnh (đề/đáp án) đúng theo vùng bạn đã chọn.
    -   Lưu ý: Toạ độ đã được chuẩn hoá DPI giữa Tkinter và PyAutoGUI để tránh lệch trên Windows (125%, 150%, ...).

### Bước 3: Nhập thông tin và Bắt đầu

1.  Sau khi căn chỉnh xong, chương trình sẽ yêu cầu bạn nhập các thông tin cuối cùng:
    -   Tổng số câu hỏi cần lấy.
    -   Độ trễ giữa mỗi câu (để slide có thời gian tải).
    -   Tổng số câu cần chụp.
    -   Độ trễ giữa mỗi câu (để trang có thời gian tải).
2.  Chương trình sẽ bắt đầu đếm ngược 5 giây. Hãy nhấp lại vào cửa sổ trình duyệt ở màn hình chính (F11 toàn màn hình).

### Bước 4: Xem kết quả

-   Chương trình sẽ tự động chạy, bạn sẽ nghe thấy âm thanh báo hiệu sau mỗi câu hỏi được xử lý.
-   Khi hoàn tất, một âm thanh báo hiệu thành công sẽ vang lên.
-   Kết quả được lưu trong thư mục `ket_qua_hoc_tap`:
    -   PDF: `tong_hop_cau_hoi.pdf`
    -   Ảnh: lưu trong thư mục con `images/`

## Mẹo sử dụng

-   Đặt trình duyệt ở chế độ toàn màn hình để tránh các phần tử giao diện dư thừa.
-   Không di chuyển/zoom trang sau khi đã căn chỉnh vùng chụp.
-   Nếu dùng Windows có DPI scaling (125%, 150%, ...), công cụ đã bù trừ, nhưng vẫn nên giữ nguyên trong quá trình chạy.

## Gợi ý xử lý tài liệu bằng AI (Tùy chọn)

Nếu muốn tạo đề trắc nghiệm chuẩn hoặc flashcards từ ảnh đã chụp, tham khảo `prompt_ai_after_run.md` để có sẵn 2 prompt: chuyển từ OCR sang trắc nghiệm có giải thích (VI) và từ trắc nghiệm sang flashcards.