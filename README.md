# Trợ lý Học tập Trắc nghiệm AI

Một công cụ mạnh mẽ sử dụng Trí tuệ Nhân tạo (AI) để tự động hóa việc thu thập, định dạng và giải thích các câu hỏi trắc nghiệm từ bất kỳ nguồn nào trên màn hình của bạn.

## Tổng quan

Bạn mệt mỏi với việc phải gõ lại hoặc chụp ảnh màn hình từng câu hỏi để ôn tập? Công cụ này sẽ giải quyết vấn đề đó. Nó hoạt động như một trợ lý ảo, "nhìn" vào màn hình của bạn, tự động chụp lại câu hỏi và đáp án, sau đó sử dụng AI để:

1.  **Nhận dạng văn bản** từ hình ảnh một cách chính xác bằng VietOCR (tối ưu cho tiếng Việt).
2.  **Định dạng lại** câu hỏi và các lựa chọn một cách sạch sẽ, rõ ràng.
3.  **Cung cấp lời giải thích** ngắn gọn cho đáp án đúng.
4.  **Tổng hợp tất cả** vào một file duy nhất, sẵn sàng cho việc ôn tập.

## Tính năng chính

-   **Canh chỉnh bằng chuột:** Công cụ canh chỉnh trực quan cho phép bạn kéo chuột để chọn vùng chụp chính xác.
-   **Căn chỉnh Tương tác:** Cho phép bạn tự định nghĩa vùng chụp và đường cắt một cách trực quan trước khi chạy.
-   **Độ chính xác cao:** Sử dụng OCR.space API, một dịch vụ OCR chuyên nghiệp với độ chính xác cao.
-   **Giải thích thông minh:** Tích hợp Gemini 1.5 Pro không chỉ để định dạng mà còn để giải thích đáp án, giúp bạn hiểu sâu hơn.
-   **Giấu đáp án:** Câu hỏi được trình bày không có đáp án đúng, giúp bạn tự kiểm tra kiến thức. Đáp án và giải thích được đặt ở phần riêng biệt.
-   **Phản hồi Âm thanh:** Phát âm thanh "purchase-success.mp3" khi hoàn thành một câu hỏi và "victory.mp3" 3 lần khi kết thúc toàn bộ chương trình.
-   **Tổng hợp tiện lợi:** Tất cả các câu hỏi được gộp vào một file Markdown duy nhất, dễ dàng đọc, tìm kiếm và sao chép.

## Yêu cầu hệ thống

Trước khi bắt đầu, bạn cần chuẩn bị:

1.  **Python 3.8+**
2.  **OCR.space API Key**: Bắt buộc để OCR. Lấy từ [OCR.space](https://ocr.space/ocrapi/freekey) (miễn phí, 25,000 ảnh/tháng).
3.  **Khóa API của Google Gemini** (tùy chọn): Chỉ cần nếu bạn muốn sử dụng Gemini để định dạng câu hỏi. Lấy từ [Google AI Studio](https://aistudio.google.com/app/apikey).

## Cài đặt & Thiết lập

### Bước 1: Chuẩn bị Thư mục và Code

1.  Tạo một thư mục mới cho dự án, ví dụ `ai_quiz_helper`.
2.  Sao chép file `main.py` và `requirements.txt` vào thư mục này.

### Bước 2: Tạo và Kích hoạt Môi trường ảo (Rất khuyến khích)

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
- OCR.space API cần kết nối internet để hoạt động.
- Gói miễn phí cho phép 25,000 ảnh/tháng, đủ cho hầu hết nhu cầu.
- Để có âm thanh thông báo, hãy đặt file `purchase-success.mp3` và `victory.mp3` trong cùng thư mục với `main.py`.

## Hướng dẫn sử dụng

### Bước 1: Chuẩn bị Giao diện

1.  Mở trình duyệt và truy cập vào bài trắc nghiệm của bạn.
2.  Nhấn phím **F11** để vào chế độ **TOÀN MÀN HÌNH**. Đây là bước cực kỳ quan trọng để đảm bảo ảnh chụp không bị lẫn các yếu tố thừa.
3.  Di chuyển đến câu hỏi trắc nghiệm đầu tiên.

### Bước 2: Chạy chương trình và Căn chỉnh

1.  Mở terminal trong thư mục dự án (đảm bảo môi trường ảo `venv` đã được kích hoạt).
2.  Chạy lệnh: `python main.py`
3.  Chương trình sẽ hướng dẫn bạn qua 2 bước căn chỉnh:
    -   **Căn chỉnh vùng chụp chính:** 
        - Chọn phương pháp: Nhập phần trăm thủ công hoặc chọn vùng bằng chuột (khuyến nghị)
        - Nếu chọn chuột: Kéo chuột để chọn vùng chụp, nhấn Enter để xác nhận
        - Nếu chọn thủ công: Nhập phần trăm thụt lề từ trên và trái
        - Một cửa sổ xem trước sẽ hiện ra. Hãy xem và đóng nó lại, sau đó nhập `ok` nếu đã vừa ý, hoặc `thử lại` để làm lại.
    -   **Căn chỉnh đường cắt:** Nhập phần trăm cắt từ dưới lên cho phần đáp án. Hai cửa sổ xem trước (Đề và Đáp án) sẽ hiện ra. Hãy xem và đóng chúng, sau đó xác nhận.

### Bước 3: Nhập thông tin và Bắt đầu

1.  Sau khi căn chỉnh xong, chương trình sẽ yêu cầu bạn nhập các thông tin cuối cùng:
    -   Tổng số câu hỏi cần lấy.
    -   Độ trễ giữa mỗi câu (để slide có thời gian tải).
    -   **OCR.space API Key:** Bắt buộc để OCR.
    -   **Tùy chọn sử dụng Gemini:** Chọn có (y) hoặc không (n) để sử dụng Gemini định dạng câu hỏi.
    -   **Khóa API Gemini:** Chỉ cần nhập nếu chọn sử dụng Gemini.
2.  Chương trình sẽ xác thực OCR.space API key.
3.  Chương trình sẽ bắt đầu đếm ngược 5 giây. **TRONG LÚC NÀY, HÃY NHANH CHÓNG CLICK LẠI VÀO CỬA SỔ TRÌNH DUYỆT ĐANG Ở CHẾ ĐỘ TOÀN MÀN HÌNH.**

### Bước 4: Xem kết quả

-   Chương trình sẽ tự động chạy, bạn sẽ nghe thấy âm thanh báo hiệu sau mỗi câu hỏi được xử lý.
-   Khi hoàn tất, một âm thanh báo hiệu thành công sẽ vang lên.
-   Kết quả được lưu trong thư mục `ket_qua_hoc_tap`:
    -   **File tổng hợp:** `tong_hop_cau_hoi_va_giai_thich.md` (tất cả câu hỏi)
    -   **File chia nhỏ:** `cau_hoi_001.md`, `cau_hoi_002.md`, ... (mỗi file 100 câu)

## Ưu điểm của OCR.space

- **Độ chính xác cao:** Sử dụng các model OCR tiên tiến được huấn luyện trên dữ liệu lớn.
- **Hỗ trợ đa ngôn ngữ:** Hỗ trợ nhiều ngôn ngữ bao gồm tiếng Anh và tiếng Việt.
- **Không cần cài đặt model nặng:** Tất cả xử lý được thực hiện trên server.
- **API đơn giản:** Dễ dàng tích hợp và sử dụng.
- **Gói miễn phí hào phóng:** 25,000 ảnh/tháng miễn phí.