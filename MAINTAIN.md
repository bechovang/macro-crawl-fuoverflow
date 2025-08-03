# Hướng dẫn Bảo trì (Maintenance Guide) - Trợ lý Học tập Trắc nghiệm AI

Tài liệu này cung cấp thông tin kỹ thuật về cấu trúc dự án, các thành phần cốt lõi và hướng dẫn bảo trì, khắc phục sự cố cho lập trình viên.

## 1. Cấu trúc Dự án

```
ai_quiz_helper/
├── main.py              # File thực thi chính, chứa toàn bộ logic
├── requirements.txt      # Danh sách các thư viện Python phụ thuộc
├── credentials.json      # File xác thực của Google Cloud (KHÔNG được đưa lên Git)
├── ket_qua_hoc_tap/      # Thư mục chứa kết quả đầu ra
│   └── tong_hop_cau_hoi_va_giai_thich.md
└── venv/                  # Thư mục môi trường ảo Python
```

## 2. Phân tích các Thành phần Cốt lõi (`main.py`)

-   **`play_sound(sound_type)`**: Sử dụng thư viện `winsound` (chỉ trên Windows) để cung cấp phản hồi âm thanh. Được thiết kế để không làm crash chương trình nếu không phải Windows hoặc không phát được âm thanh.

-   **`validate_gemini_api_key(api_key)`**: Gửi một yêu cầu thử nghiệm nhỏ đến Gemini để xác thực khóa API trước khi thực hiện các tác vụ chính, giúp phát hiện lỗi sớm.

-   **`show_image_preview(...)` & `show_split_image_preview(...)`**: Sử dụng `matplotlib` để hiển thị ảnh xem trước một cách đáng tin cậy, khắc phục vấn đề của các trình xem ảnh mặc định. Các hàm này sẽ tạm dừng chương trình cho đến khi cửa sổ xem trước được đóng lại.

-   **`extract_text_from_image_ocr(...)`**: Cầu nối với Google Cloud. Chịu trách nhiệm gửi ảnh đến Vision API và trả về văn bản thô. Yêu cầu file `credentials.json` hợp lệ.

-   **`format_question_and_explanation(...)`**: **Trái tim của ứng dụng**.
    -   Chứa "prompt" được thiết kế đặc biệt cho việc học tập trắc nghiệm.
    -   Nhận đầu vào là văn bản câu hỏi và văn bản đáp án.
    -   Yêu cầu Gemini định dạng câu hỏi (không có đáp án) và viết phần giải thích (có nêu đáp án đúng).
    -   Đây là nơi quan trọng nhất để tinh chỉnh nếu muốn thay đổi định dạng đầu ra.

-   **`calibrate_main_region(...)` & `calibrate_split_line(...)`**: Cung cấp quy trình tương tác cho người dùng để xác định chính xác các vùng cần chụp ảnh thông qua các vòng lặp `while`, cho phép thử lại đến khi hài lòng.

-   **`capture_and_process(...)`**: Vòng lặp chính xử lý hàng loạt. Với mỗi câu hỏi, nó thực hiện chuỗi hành động: chụp 2 ảnh -> OCR 2 ảnh -> gửi 2 văn bản cho Gemini -> lưu kết quả -> nhấn phím di chuyển.

-   **`main()`**: Hàm điều phối cấp cao nhất, điều khiển luồng chạy của toàn bộ chương trình từ lúc bắt đầu, qua các bước căn chỉnh, đến khi xử lý hàng loạt và kết thúc.

## 3. Nhiệm vụ Bảo trì

1.  **Cập nhật Dependencies:**
    -   Thường xuyên chạy `pip list --outdated` trong môi trường ảo để kiểm tra các phiên bản mới. Cân nhắc cập nhật để có các bản vá lỗi và bảo mật.

2.  **Giám sát Chi phí API:**
    -   **Rất quan trọng!** Thường xuyên truy cập bảng điều khiển Google Cloud để theo dõi chi phí sử dụng của **Cloud Vision API**.
    -   Theo dõi mức sử dụng của **Gemini API** tại [Google AI Studio](https://aistudio.google.com/app/apikey).

3.  **Tinh chỉnh Prompt:**
    -   Nếu chất lượng định dạng hoặc giải thích của Gemini giảm sút hoặc không như ý, nơi đầu tiên cần xem xét và chỉnh sửa là chuỗi `prompt` bên trong hàm `format_question_and_explanation`.

## 4. Hướng dẫn Khắc phục Sự cố

| Vấn đề                                           | Nguyên nhân có thể xảy ra                                                                                                                              | Giải pháp                                                                                                                                                                 |
| ------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Lỗi OCR thất bại / `credentials.json` không hợp lệ** | - File `credentials.json` không tồn tại hoặc sai vị trí.<br>- File JSON không phải của **Service Account**.<br>- API Cloud Vision chưa được bật.<br>- Tài khoản Service Account không có quyền. | - Đảm bảo file `credentials.json` nằm cùng cấp với `main.py`.<br>- Tạo lại và tải về đúng file **Service Account Key** từ Google Cloud Console.<br>- Vào Console để bật API.   |
| **Lỗi Gemini API**                               | - Khóa API không chính xác.<br>- Hết hạn mức sử dụng (nếu có).                                                                                            | - Kiểm tra lại khóa API bạn đã nhập.<br>- Truy cập Google AI Studio để kiểm tra trạng thái và hạn mức của khóa.                                                                 |
| **Cửa sổ xem trước không hiển thị**               | - Lỗi cài đặt `matplotlib` hoặc backend đồ họa của nó.                                                                                                    | - Thử chạy lại `pip install --upgrade matplotlib`.<br>- Đảm bảo các thư viện trong `requirements.txt` đã được cài đặt thành công.                                                |
| **Ảnh chụp bị lệch hoặc sai nội dung**           | - Người dùng di chuyển cửa sổ trình duyệt sau khi căn chỉnh.<br>- Độ phân giải màn hình thay đổi.                                                         | - Chạy lại chương trình để thực hiện lại quy trình căn chỉnh. Đảm bảo cửa sổ trình duyệt giữ nguyên vị trí trong suốt quá trình chạy.                                    |
| **Không có âm thanh (trên Windows)**              | - Lỗi driver âm thanh của hệ điều hành.                                                                                                                | - Kiểm tra xem các âm thanh hệ thống khác có hoạt động không. Code đã được thiết kế để bỏ qua lỗi này và tiếp tục chạy mà không có âm thanh.                                |

## 5. Thực hành Bảo mật Tốt nhất

-   **KHÔNG BAO GIỜ** đưa file `credentials.json` hoặc ghi trực tiếp Khóa API Gemini vào trong code rồi đẩy lên các kho lưu trữ công khai như GitHub.
-   Tạo một file `.gitignore` và thêm `credentials.json`, `venv/`, `ket_qua_hoc_tap/` vào đó để loại trừ chúng khỏi việc commit.