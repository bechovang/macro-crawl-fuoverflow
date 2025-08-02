# Hướng dẫn Bảo trì (Maintenance Guide) - Google Slides Crawler

Tài liệu này cung cấp thông tin kỹ thuật về cấu trúc dự án, các thành phần cốt lõi và hướng dẫn bảo trì, khắc phục sự cố cho lập trình viên.

## 1. Cấu trúc Dự án

```
.
├── main.py              # File thực thi chính, điều phối toàn bộ luồng hoạt động
├── requirements.txt      # Danh sách các thư viện Python phụ thuộc
├── README.md            # Hướng dẫn cho người dùng cuối
└── MAINTAIN.md          # Tài liệu bảo trì này
```

## 2. Phân tích các Thành phần Cốt lõi (`main.py`)

-   **`validate_gemini_api_key(api_key)`**: Kiểm tra tính hợp lệ của khóa API Gemini bằng cách thực hiện một cuộc gọi thử nghiệm nhỏ. Đây là bước quan trọng để cung cấp phản hồi sớm cho người dùng.
-   **`setup_driver()`**: Cấu hình và khởi tạo Selenium WebDriver. Sử dụng `webdriver-manager` để tự động hóa việc quản lý driver và các tùy chọn `headless` để chạy ngầm.
-   **`capture_slide_screenshot(...)`**: **(Cần triển khai)** Logic cốt lõi để điều khiển trình duyệt, điều hướng đến từng slide và chụp ảnh màn hình của phần tử chứa nội dung chính (`.punch-viewer-content`).
-   **`extract_text_from_image_ocr(...)`**: **(Cần triển khai)** Logic để gọi Google Cloud Vision API. Nó nhận đường dẫn ảnh và trả về một chuỗi văn bản thô.
-   **`format_text_with_gemini(...)`**: Gửi văn bản thô từ OCR cùng với một "prompt" (câu lệnh) được thiết kế cẩn thận đến Gemini 1.5 Pro API để nhận lại văn bản đã được định dạng.
-   **`main()`**: Hàm điều phối chính. Chịu trách nhiệm nhận đầu vào từ người dùng, gọi tuần tự các hàm xử lý trong một vòng lặp và quản lý việc lưu file kết quả.

## 3. Nhiệm vụ Bảo trì

### Hàng tuần / Hàng tháng

1.  **Cập nhật Dependencies:**
    - Thường xuyên kiểm tra các phiên bản mới của thư viện để nhận các bản vá bảo mật và tính năng mới.
    - Chạy `pip list --outdated` để xem danh sách.
    - Chạy `pip install -U -r requirements.txt` để cập nhật.

2.  **Kiểm tra Selector của Selenium:**
    - Google có thể thay đổi cấu trúc HTML/CSS của Slides. Selector `.punch-viewer-content` có thể không còn hợp lệ.
    - Nếu chức năng chụp ảnh bị lỗi, hãy mở Google Slides trong trình duyệt, sử dụng Developer Tools (F12) để kiểm tra và cập nhật lại CSS Selector trong hàm `capture_slide_screenshot`.

### Khi có sự cố

1.  **Giám sát Chi phí API:**
    - Cả Google Cloud Vision và Gemini API đều tính phí dựa trên lượng sử dụng. Thường xuyên kiểm tra bảng điều khiển thanh toán trên Google Cloud để tránh phát sinh chi phí bất ngờ.

2.  **Xem lại Prompt của Gemini:**
    - Hiệu quả của AI phụ thuộc rất lớn vào prompt. Nếu chất lượng đầu ra bị giảm, hãy xem xét việc tinh chỉnh lại prompt trong hàm `format_text_with_gemini` để rõ ràng và cụ thể hơn.

## 4. Hướng dẫn Khắc phục Sự cố (Troubleshooting)

| Vấn đề                                           | Nguyên nhân có thể xảy ra                                                                                             | Giải pháp                                                                                                                                                             |
| ------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Lỗi `webdriver` hoặc trình duyệt không khởi động** | - ChromeDriver không tương thích với phiên bản Chrome hiện tại.<br>- Chrome chưa được cài đặt.                       | - `webdriver-manager` thường tự xử lý việc này. Thử xóa cache của nó.<br>- Chạy `pip install --upgrade webdriver-manager`. <br>- Đảm bảo Google Chrome đã được cài đặt. |
| **Chụp ảnh màn hình thất bại hoặc ra ảnh trắng**     | - Selector CSS đã thay đổi.<br>- Mạng chậm, slide chưa tải xong khi chụp.<br>- Cần đăng nhập để xem slide.             | - Kiểm tra và cập nhật CSS Selector.<br>- Tăng thời gian chờ trong `WebDriverWait`. <br>- (Nâng cao) Thêm cơ chế nạp cookie để xác thực phiên đăng nhập.         |
| **Lỗi OCR (trả về văn bản trống hoặc sai)**        | - Ảnh chụp có độ phân giải thấp, bị mờ.<br>- Vision API chưa được bật hoặc credentials không hợp lệ. <br>- Hết quota API. | - Đảm bảo `window-size` đủ lớn.<br>- Kiểm tra lại cấu hình `GOOGLE_APPLICATION_CREDENTIALS`.<br>- Kiểm tra bảng điều khiển Google Cloud.                                 |
| **Lỗi từ Gemini API (xác thực, quota)**          | - Khóa API không chính xác.<br>- Hết hạn mức miễn phí hoặc quota.                                                      | - Lấy lại khóa API mới từ Google AI Studio.<br>- Kiểm tra trang quản lý API của bạn.                                                                                   |
| **Bị Google chặn vì truy cập quá nhanh**          | - Gửi quá nhiều yêu cầu trong một thời gian ngắn.                                                                     | - Tăng thời gian `time.sleep()` giữa các lần xử lý slide trong vòng lặp chính.                                                                                         |

## 5. Thực hành Bảo mật Tốt nhất

-   **Không bao giờ commit khóa API hoặc file credentials lên Git.** Thêm file `credentials.json` và các file cấu hình nhạy cảm khác vào `.gitignore`.
-   **Luôn sử dụng biến môi trường** cho `GOOGLE_APPLICATION_CREDENTIALS` thay vì hardcode đường dẫn trong code.
-   Khi tạo Service Account trên Google Cloud, hãy cấp cho nó quyền tối thiểu cần thiết (ví dụ: chỉ quyền sử dụng Vision API), không cấp quyền quản trị toàn bộ dự án.