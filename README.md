# Google Slides Crawler - Sử dụng Gemini 1.5 Pro

Công cụ tự động hóa việc trích xuất và định dạng nội dung từ các bài thuyết trình trên Google Slides bằng sức mạnh của AI. Biến những slide tĩnh thành tài liệu văn bản có cấu trúc, dễ đọc và dễ dàng lưu trữ.

## Tổng quan

Dự án này giải quyết vấn đề chuyển đổi thủ công nội dung từ Google Slides sang văn bản. Thay vì phải copy-paste từng slide, công cụ này sẽ tự động:

1.  **Chụp ảnh** từng slide trong bài thuyết trình.
2.  **Sử dụng OCR** (Nhận dạng ký tự quang học) để "đọc" và trích xuất văn bản từ các ảnh đó.
3.  **Tận dụng Gemini 1.5 Pro** để làm sạch, định dạng và cấu trúc lại văn bản một cách thông minh.

## Luồng hoạt động

```
URL Google Slides
      |
      v
[Selenium] -> Chụp ảnh màn hình từng slide (.png)
      |
      v
[Google Cloud Vision] -> Trích xuất văn bản thô từ ảnh
      |
      v
[Gemini 1.5 Pro] -> Định dạng, làm sạch, cấu trúc lại văn bản
      |
      v
[File Kết quả] -> Lưu ảnh và văn bản đã định dạng (.txt)
```

## Tính năng chính

-   **Tự động hóa hoàn toàn**: Chỉ cần cung cấp URL và tổng số slide.
-   **Trích xuất chính xác**: Sử dụng Google Cloud Vision, một trong những công nghệ OCR hàng đầu.
-   **Định dạng thông minh**: Tích hợp Gemini 1.5 Pro để hiểu và tái cấu trúc nội dung một cách tự nhiên.
-   **Xử lý hàng loạt**: Có khả năng xử lý toàn bộ bài thuyết trình một cách tuần tự.
-   **Kết quả có tổ chức**: Lưu trữ riêng biệt ảnh và văn bản cho từng slide trong một thư mục duy nhất.

## Yêu cầu hệ thống

Trước khi bắt đầu, bạn cần chuẩn bị:

1.  **Python 3.8+**
2.  **Trình duyệt Google Chrome** được cài đặt trên máy.
3.  **Tài khoản Google Cloud Platform**:
    - Đã kích hoạt **Vision API**.
    - Đã tạo một **Service Account** và tải về file **credentials JSON**.
4.  **Khóa API của Google Gemini**: Lấy từ [Google AI Studio](https://aistudio.google.com/app/apikey).

## Hướng dẫn Cài đặt & Sử dụng

### Bước 1: Chuẩn bị Dự án

1.  **Clone repository này về máy:**
    ```bash
    git clone <URL-repository-cua-ban>
    cd <ten-thu-muc-repository>
    ```

2.  **Tạo và kích hoạt môi trường ảo (khuyến khích):**
    ```bash
    # Windows
    python -m venv venv
    .\venv\Scripts\activate

    # macOS / Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Cài đặt các thư viện cần thiết:**
    ```bash
    pip install -r requirements.txt
    ```

### Bước 2: Cấu hình API

1.  **Google Cloud Vision API:**
    - Đặt biến môi trường hệ thống để trỏ đến file JSON của bạn. Đây là cách an toàn nhất.
    - **Windows (Command Prompt):**
      ```cmd
      set GOOGLE_APPLICATION_CREDENTIALS="C:\duong\dan\den\file-credentials.json"
      ```
    - **macOS / Linux:**
      ```bash
      export GOOGLE_APPLICATION_CREDENTIALS="/duong/dan/den/file-credentials.json"
      ```
    - **Lưu ý:** Bạn cần chạy lệnh này trong mỗi phiên terminal mới, hoặc thêm nó vào file cấu hình shell của bạn (`.bashrc`, `.zshrc`, ...).

2.  **Google Gemini API:**
    - Bạn sẽ nhập khóa API trực tiếp khi chạy chương trình.

### Bước 3: Chạy chương trình

1.  Mở terminal trong thư mục gốc của dự án.
2.  Chạy lệnh sau:
    ```bash
    python main.py
    ```
3.  Chương trình sẽ yêu cầu bạn nhập các thông tin sau:
    - **URL của Google Slides**.
    - **Khóa API Gemini** (sẽ được ẩn khi bạn gõ).
    - **Tổng số slide** của bài thuyết trình.

### Bước 4: Xem kết quả

-   Sau khi chương trình chạy xong, một thư mục có tên `slides_output` sẽ được tạo ra.
-   Bên trong thư mục này, bạn sẽ thấy các file kết quả được đặt tên theo quy tắc:
    - `slide_1.png`: Ảnh chụp màn hình của slide 1.
    - `slide_1_formatted.txt`: Nội dung văn bản của slide 1 đã được Gemini định dạng.
    - `slide_2.png`
    - `slide_2_formatted.txt`
    - ...

## License

Dự án này được cấp phép theo Giấy phép MIT. Xem file `LICENSE` để biết thêm chi tiết.




------


Hướng dẫn sử dụng (Rất quan trọng)
Hãy làm theo đúng 2 bước sau:
Bước 1: Chạy lần đầu để Đăng nhập
Đảm bảo biến DEBUG_MODE ở đầu file được đặt là True.
Generated python
DEBUG_MODE = True
Use code with caution.
Python
Chạy chương trình: python main.py.
Một cửa sổ trình duyệt Chrome mới và trống trơn sẽ hiện ra. Chương trình sẽ điều hướng đến URL slide và bạn sẽ thấy trang yêu cầu đăng nhập của Google.
Hãy đăng nhập vào tài khoản Google của bạn ngay trên cửa sổ Chrome này.
Sau khi đăng nhập thành công và thấy được nội dung slide, bạn có thể để chương trình chạy hết hoặc dừng nó lại bằng cách nhấn Ctrl + C trong cửa sổ terminal.
Lúc này, một thư mục mới tên là chrome_profile_for_bot đã được tạo ra, chứa thông tin đăng nhập của bạn.
Bước 2: Chạy các lần sau một cách bình thường
Bây giờ, bạn có thể sửa lại biến DEBUG_MODE thành False để chương trình chạy ẩn, không hiện cửa sổ trình duyệt nữa.
Generated python
DEBUG_MODE = False
Use code with caution.
Python
Chạy lại chương trình python main.py.
Lần này, chương trình sẽ tự động sử dụng profile đã đăng nhập ở Bước 1 và sẽ chạy một cách mượt mà mà không gặp lỗi SessionNotCreatedException nữa.