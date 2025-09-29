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
-   **Xử lý Slide Linh hoạt:** Chọn giữa chia slide thành 2 phần (Đề + Đáp án) hoặc OCR nguyên 1 slide.
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
4.  **Nhiều API Key** (khuyến nghị): Để xử lý nhiều slide, nên có nhiều OCR.space API key để tránh giới hạn 180 requests/giờ.

## Cài đặt & Thiết lập

### Bước 1: Chuẩn bị Thư mục và Code

1.  Tạo một thư mục mới cho dự án, ví dụ `ai_quiz_helper`.
2.  Sao chép file `main.py`, `requirements.txt`, và `test_ocrspace.py` vào thư mục này.

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
- Sử dụng `test_ocrspace.py` để quản lý và test nhiều API key hiệu quả.

## Hướng dẫn sử dụng

### Bước 1: Chuẩn bị Giao diện

1.  Mở trình duyệt và truy cập vào bài trắc nghiệm của bạn.
2.  Nhấn phím **F11** để vào chế độ **TOÀN MÀN HÌNH**. Đây là bước cực kỳ quan trọng để đảm bảo ảnh chụp không bị lẫn các yếu tố thừa.
3.  Di chuyển đến câu hỏi trắc nghiệm đầu tiên.

### Bước 2: Chạy chương trình và Căn chỉnh

1.  Mở terminal trong thư mục dự án (đảm bảo môi trường ảo `venv` đã được kích hoạt).
2.  Chạy lệnh: `python main.py`
3.  Với công cụ tạo PDF trắc nghiệm `tao_pdf_trac_nghiem.py`, chương trình sẽ hướng dẫn bạn qua 3 lần chọn bằng chuột (DPI-safe):
    -   **Chọn Vùng chính (Main Region):**
        - Kéo chuột khoanh toàn bộ khu vực chứa cả đề và đáp án.
        - Preview sẽ hiển thị; nhập `ok` để xác nhận hoặc chọn lại.
    -   **Chọn Vùng Câu hỏi (Question Region):**
        - Kéo chuột khoanh đúng phần đề bài ở BÊN TRONG vùng chính.
    -   **Chọn Vùng Đáp án (Answer Region):**
        - Kéo chuột khoanh đúng phần đáp án tham khảo ở BÊN TRONG vùng chính.
    -   Hệ thống sẽ hiển thị preview 2 ảnh (đề/đáp án) đúng theo vùng bạn đã chọn.
    -   Lưu ý: Toạ độ đã được chuẩn hoá DPI giữa Tkinter và PyAutoGUI để tránh lệch trên Windows (125%, 150%, ...).

### Bước 3: Nhập thông tin và Bắt đầu

1.  Sau khi căn chỉnh xong, chương trình sẽ yêu cầu bạn nhập các thông tin cuối cùng:
    -   Tổng số câu hỏi cần lấy.
    -   Độ trễ giữa mỗi câu (để slide có thời gian tải).
    -   **OCR.space API Key:** Bắt buộc để OCR.
    -   **Tùy chọn sử dụng Gemini:** Chọn có (y) hoặc không (n) để sử dụng Gemini định dạng câu hỏi.
    -   **Khóa API Gemini:** Chỉ cần nhập nếu chọn sử dụng Gemini.
2.  Chương trình sẽ xác thực OCR.space API key.
3.  Chương trình sẽ bắt đầu đếm ngược 5 giây. **TRONG LÚC NÀY, HÃY NHANH CHÓNG CLICK LẠI VÀO CỬA SỔ TRÌNH DUYỆT Ở MÀN HÌNH CHÍNH (PRIMARY) VÀ CHẾ ĐỘ TOÀN MÀN HÌNH.**

### Bước 4: Xem kết quả

-   Chương trình sẽ tự động chạy, bạn sẽ nghe thấy âm thanh báo hiệu sau mỗi câu hỏi được xử lý.
-   Khi hoàn tất, một âm thanh báo hiệu thành công sẽ vang lên.
-   Kết quả được lưu trong thư mục `ket_qua_hoc_tap`:
    -   **File tổng hợp:** `tong_hop_cau_hoi_va_giai_thich.md` (tất cả câu hỏi)
    -   **File chia nhỏ:** `cau_hoi_001.md`, `cau_hoi_002.md`, ... (mỗi file 100 câu)

## Lưu ý quan trọng về OCR.space API

OCR.space API có giới hạn sử dụng:
- **25,000 requests mỗi tháng** (miễn phí)
- **180 requests mỗi giờ**

Nếu bạn cần xử lý nhiều slide, hãy cân nhắc:
- Sử dụng nhiều tài khoản Google để có nhiều API key
- Chia nhỏ công việc thành nhiều lần chạy
- Sử dụng chế độ OCR-only để tiết kiệm API calls

### Quản lý API Key với test_ocrspace.py

Để quản lý nhiều API key hiệu quả, sử dụng script `test_ocrspace.py`:

```bash
python test_ocrspace.py
```

**Tính năng:**
- **Test nhiều key**: Nhập danh sách key theo format `Tên1;Key1|Tên2;Key2|...`
- **Xem trạng thái**: Kiểm tra key nào hoạt động, đang chờ, hoặc lỗi
- **Bảo vệ giới hạn**: Tự động ngăn test cùng key trong vòng 1 giờ
- **Lưu lịch sử**: Tất cả kết quả test được lưu vào `check_key.txt`

**Ví dụ sử dụng:**
```
Nhập danh sách key: Key1;abc123|Key2;def456|Key3;ghi789
```

**Kết quả:**
- Hiển thị key nào hoạt động ✅
- Key nào đang chờ ⏰ (chưa đủ 1 giờ từ lần test cuối)
- Key nào lỗi ❌
- Ước tính khả năng xử lý slide/giờ

## Ưu điểm của OCR.space

- **Độ chính xác cao:** Sử dụng các model OCR tiên tiến được huấn luyện trên dữ liệu lớn.
- **Hỗ trợ đa ngôn ngữ:** Hỗ trợ nhiều ngôn ngữ bao gồm tiếng Anh và tiếng Việt.
- **Không cần cài đặt model nặng:** Tất cả xử lý được thực hiện trên server.
- **API đơn giản:** Dễ dàng tích hợp và sử dụng.
- **Gói miễn phí hào phóng:** 25,000 ảnh/tháng miễn phí.

## Format tài liệu với AI (Tùy chọn)

Sau khi OCR xong, nếu bạn muốn format cho đẹp hơn, có thể sử dụng prompt sau với bất kỳ AI nào (ChatGPT, Claude, Gemini, etc.):

```
Bạn là một trợ lý AI chuyên gia, có nhiệm vụ chuyển đổi văn bản OCR thô từ các slide học liệu thành một tài liệu học tập có cấu trúc chuyên nghiệp bằng định dạng Markdown cho Obsidian.

Mục tiêu cuối cùng là tạo ra một tài liệu không chỉ đẹp về hình thức mà còn hiệu quả cho việc ôn tập. Hãy tuân thủ nghiêm ngặt các quy tắc sau:

**1. Phân tích và Cấu trúc tổng thể:**
*   **Tự động phân loại nội dung:** Khi nhận được văn bản, hãy xác định các phần khác nhau: thông báo, liên kết, kiến thức lý thuyết (bảng biểu, định nghĩa), và câu hỏi trắc nghiệm.
*   **Tổ chức lại tài liệu:** Sắp xếp các nội dung đã phân loại vào các mục logic như: `I. Thông tin chung & Tài liệu tham khảo`, `II. Kiến thức nền tảng`, và `III. Ngân hàng câu hỏi trắc nghiệm`. Sử dụng các tiêu đề (headings) để phân cấp rõ ràng.

**2. Quy tắc xử lý Câu hỏi trắc nghiệm:**
*   **Ngôn ngữ gốc:** Giữ nguyên văn bản tiếng Anh cho phần câu hỏi và các lựa chọn trả lời (A, B, C, D,...).
*   **Không tiết lộ đáp án:** Tuyệt đối không được làm nổi bật (in đậm, đánh dấu `*`) hoặc chỉ ra đáp án đúng trong phần đề bài và lựa chọn.
*   **Tạo phần Giải thích:** Dưới mỗi câu hỏi, thêm một mục `> **Giải thích:**`.

**3. Yêu cầu cho phần "Giải thích":**
*   **Ngôn ngữ:** Phần giải thích phải được viết hoàn toàn bằng **tiếng Việt**.
*   **Nêu rõ đáp án:** Bắt đầu phần giải thích bằng việc nêu rõ đáp án đúng. Ví dụ: `**Đáp án đúng là A.**`
*   **Diễn giải chi tiết:** Cung cấp lời giải thích rõ ràng, súc tích về lý do tại sao đáp án đó đúng và tại sao các đáp án khác sai.
*   **Thuật ngữ chuyên ngành:** Khi sử dụng một thuật ngữ kỹ thuật bằng tiếng Việt, **bắt buộc** phải kèm theo thuật ngữ tiếng Anh tương ứng trong dấu ngoặc đơn ngay sau đó.
    *   **Ví dụ:** `hệ điều hành (operating system)`, `tính gắn kết (Cohesion)`, `mã hóa bất đối xứng (Asymmetric-key cryptography)`.

**4. Định dạng và Tự chủ:**
*   Sử dụng các yếu tố Markdown (như `##`, `*`, `-`, bảng `|`, blockquotes `>`) một cách hợp lý để tài liệu trở nên trực quan và dễ đọc.
*   Bạn có quyền tự sửa các lỗi OCR nhỏ, diễn đạt lại các câu văn khó hiểu để tăng tính rõ ràng, miễn là **không làm thay đổi ý nghĩa kỹ thuật cốt lõi** của câu hỏi và khái niệm, cũng như là làm mất đi tính bẫy / đánh lừa của câu hỏi.
*   Phần nào có code thì để trong codeblock
```