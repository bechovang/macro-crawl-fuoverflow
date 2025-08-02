# Google Slides Crawler - Maintenance Guide

## English Version

### Project Structure

```
crawl-google-slide/
├── main.py              # Main application file
├── requirements.txt      # Python dependencies
├── README.md           # Project documentation
├── MAINTAIN.md         # This maintenance guide
├── planning.md         # Original planning document
└── venv/              # Virtual environment (not in repo)
```

### Core Components

#### 1. GoogleSlidesCapture Class
- **Purpose**: Main orchestrator for slide capture and processing
- **Key Methods**:
  - `setup_driver()`: Configures Chrome WebDriver
  - `get_slide_with_notes()`: Captures slides and speaker notes
  - `ocr_image()`: Performs text extraction using Google Vision API
  - `format_text_with_ai()`: Formats text using OpenAI GPT
  - `process_slide()`: Complete slide processing pipeline
  - `process_presentation()`: Batch processing for entire presentations

#### 2. Dependencies
- **Selenium**: Web automation and screenshot capture
- **Google Cloud Vision**: OCR text extraction
- **OpenAI**: AI-powered text formatting
- **Chrome WebDriver**: Browser automation

### Maintenance Tasks

#### Daily Operations
1. **Monitor API Usage**
   - Check Google Cloud Vision API quotas
   - Monitor OpenAI API usage and costs
   - Review error logs for failed OCR operations

2. **Performance Monitoring**
   - Track processing time per slide
   - Monitor memory usage during batch operations
   - Check for memory leaks in long-running sessions

#### Weekly Tasks
1. **Dependency Updates**
   ```bash
   pip list --outdated
   pip install --upgrade selenium google-cloud-vision openai
   ```

2. **Code Review**
   - Review error handling in `get_slide_with_notes()`
   - Check for deprecated Selenium selectors
   - Update Google Slides URL patterns if needed

3. **Backup and Logs**
   - Archive processed slide images
   - Clean up old screenshot files
   - Review and rotate log files

#### Monthly Tasks
1. **Security Review**
   - Rotate API keys
   - Review access permissions
   - Update credentials if needed

2. **Performance Optimization**
   - Profile memory usage
   - Optimize screenshot capture settings
   - Review and update Chrome options

3. **Documentation Updates**
   - Update README with new features
   - Review and update error messages
   - Check API documentation for changes

### Troubleshooting Guide

#### Common Issues

1. **Chrome Driver Issues**
   ```bash
   # Update ChromeDriver
   pip install --upgrade webdriver-manager
   ```

2. **OCR Failures**
   - Check image quality and resolution
   - Verify Google Cloud Vision API credentials
   - Review API quotas and billing

3. **Rate Limiting**
   - Increase delays between requests
   - Implement exponential backoff
   - Check Google Slides access permissions

4. **Memory Issues**
   - Close browser sessions properly
   - Implement garbage collection
   - Monitor for memory leaks

#### Debug Mode
```python
# Enable debug logging
import logging
logging.basicConfig(level=logging.DEBUG)

# Run with visible browser
capturer = GoogleSlidesCapture(headless=False)
```

### Configuration Management

#### Environment Variables
```bash
# Required
GOOGLE_APPLICATION_CREDENTIALS=path/to/credentials.json

# Optional
OPENAI_API_KEY=your_openai_key
CHROME_HEADLESS=false
SLIDE_DELAY=2
```

#### Configuration File (config.py)
```python
# Create config.py for centralized settings
SLIDE_DELAY = 2
HEADLESS_MODE = True
OUTPUT_DIR = "./output"
MAX_RETRIES = 3
```

### Testing Strategy

#### Unit Tests
```python
# test_main.py
import unittest
from main import GoogleSlidesCapture

class TestGoogleSlidesCapture(unittest.TestCase):
    def test_setup_driver(self):
        capturer = GoogleSlidesCapture()
        self.assertIsNotNone(capturer.driver)
        capturer.close()
```

#### Integration Tests
- Test with sample Google Slides presentations
- Verify OCR accuracy with known text
- Test AI formatting with various content types

### Deployment Considerations

#### Production Setup
1. **Environment Isolation**
   ```bash
   python -m venv production_env
   source production_env/bin/activate
   pip install -r requirements.txt
   ```

2. **Process Management**
   ```bash
   # Use supervisor or systemd
   sudo systemctl enable google-slides-crawler
   ```

3. **Monitoring**
   - Set up logging to file
   - Implement health checks
   - Monitor API usage and costs

### Security Best Practices

1. **API Key Management**
   - Use environment variables
   - Rotate keys regularly
   - Implement key rotation automation

2. **Access Control**
   - Limit Google Slides access to necessary presentations
   - Use service accounts with minimal permissions
   - Implement IP whitelisting if possible

3. **Data Protection**
   - Encrypt sensitive data at rest
   - Implement secure deletion of temporary files
   - Audit access logs regularly

---

## Vietnamese Version

### Cấu trúc Dự án

```
crawl-google-slide/
├── main.py              # File ứng dụng chính
├── requirements.txt      # Dependencies Python
├── README.md           # Tài liệu dự án
├── MAINTAIN.md         # Hướng dẫn bảo trì này
├── planning.md         # Tài liệu kế hoạch gốc
└── venv/              # Môi trường ảo (không có trong repo)
```

### Thành phần Cốt lõi

#### 1. Lớp GoogleSlidesCapture
- **Mục đích**: Điều phối chính cho việc chụp và xử lý slide
- **Các phương thức chính**:
  - `setup_driver()`: Cấu hình Chrome WebDriver
  - `get_slide_with_notes()`: Chụp slide và ghi chú
  - `ocr_image()`: Trích xuất văn bản bằng Google Vision API
  - `format_text_with_ai()`: Định dạng văn bản bằng OpenAI GPT
  - `process_slide()`: Pipeline xử lý slide hoàn chỉnh
  - `process_presentation()`: Xử lý hàng loạt cho toàn bộ bài thuyết trình

#### 2. Dependencies
- **Selenium**: Tự động hóa web và chụp màn hình
- **Google Cloud Vision**: Trích xuất văn bản OCR
- **OpenAI**: Định dạng văn bản bằng AI
- **Chrome WebDriver**: Tự động hóa trình duyệt

### Nhiệm vụ Bảo trì

#### Hoạt động Hàng ngày
1. **Giám sát Sử dụng API**
   - Kiểm tra quota Google Cloud Vision API
   - Giám sát sử dụng và chi phí OpenAI API
   - Xem xét log lỗi cho các thao tác OCR thất bại

2. **Giám sát Hiệu suất**
   - Theo dõi thời gian xử lý mỗi slide
   - Giám sát sử dụng bộ nhớ trong quá trình xử lý hàng loạt
   - Kiểm tra rò rỉ bộ nhớ trong các phiên chạy dài

#### Nhiệm vụ Hàng tuần
1. **Cập nhật Dependencies**
   ```bash
   pip list --outdated
   pip install --upgrade selenium google-cloud-vision openai
   ```

2. **Xem xét Code**
   - Xem xét xử lý lỗi trong `get_slide_with_notes()`
   - Kiểm tra các selector Selenium đã deprecated
   - Cập nhật pattern URL Google Slides nếu cần

3. **Sao lưu và Logs**
   - Lưu trữ ảnh slide đã xử lý
   - Dọn dẹp file screenshot cũ
   - Xem xét và luân chuyển file log

#### Nhiệm vụ Hàng tháng
1. **Xem xét Bảo mật**
   - Luân chuyển khóa API
   - Xem xét quyền truy cập
   - Cập nhật credentials nếu cần

2. **Tối ưu hóa Hiệu suất**
   - Profile sử dụng bộ nhớ
   - Tối ưu cài đặt chụp màn hình
   - Xem xét và cập nhật Chrome options

3. **Cập nhật Tài liệu**
   - Cập nhật README với tính năng mới
   - Xem xét và cập nhật thông báo lỗi
   - Kiểm tra tài liệu API cho các thay đổi

### Hướng dẫn Khắc phục Sự cố

#### Các vấn đề Thường gặp

1. **Vấn đề Chrome Driver**
   ```bash
   # Cập nhật ChromeDriver
   pip install --upgrade webdriver-manager
   ```

2. **Lỗi OCR**
   - Kiểm tra chất lượng và độ phân giải ảnh
   - Xác minh credentials Google Cloud Vision API
   - Xem xét quota và billing API

3. **Rate Limiting**
   - Tăng độ trễ giữa các request
   - Triển khai exponential backoff
   - Kiểm tra quyền truy cập Google Slides

4. **Vấn đề Bộ nhớ**
   - Đóng session trình duyệt đúng cách
   - Triển khai garbage collection
   - Giám sát rò rỉ bộ nhớ

#### Chế độ Debug
```python
# Bật debug logging
import logging
logging.basicConfig(level=logging.DEBUG)

# Chạy với trình duyệt hiển thị
capturer = GoogleSlidesCapture(headless=False)
```

### Quản lý Cấu hình

#### Biến Môi trường
```bash
# Bắt buộc
GOOGLE_APPLICATION_CREDENTIALS=path/to/credentials.json

# Tùy chọn
OPENAI_API_KEY=your_openai_key
CHROME_HEADLESS=false
SLIDE_DELAY=2
```

#### File Cấu hình (config.py)
```python
# Tạo config.py cho cài đặt tập trung
SLIDE_DELAY = 2
HEADLESS_MODE = True
OUTPUT_DIR = "./output"
MAX_RETRIES = 3
```

### Chiến lược Testing

#### Unit Tests
```python
# test_main.py
import unittest
from main import GoogleSlidesCapture

class TestGoogleSlidesCapture(unittest.TestCase):
    def test_setup_driver(self):
        capturer = GoogleSlidesCapture()
        self.assertIsNotNone(capturer.driver)
        capturer.close()
```

#### Integration Tests
- Test với bài thuyết trình Google Slides mẫu
- Xác minh độ chính xác OCR với văn bản đã biết
- Test định dạng AI với các loại nội dung khác nhau

### Cân nhắc Triển khai

#### Thiết lập Production
1. **Cô lập Môi trường**
   ```bash
   python -m venv production_env
   source production_env/bin/activate
   pip install -r requirements.txt
   ```

2. **Quản lý Process**
   ```bash
   # Sử dụng supervisor hoặc systemd
   sudo systemctl enable google-slides-crawler
   ```

3. **Giám sát**
   - Thiết lập logging ra file
   - Triển khai health checks
   - Giám sát sử dụng và chi phí API

### Thực hành Bảo mật Tốt nhất

1. **Quản lý Khóa API**
   - Sử dụng biến môi trường
   - Luân chuyển khóa thường xuyên
   - Triển khai tự động hóa luân chuyển khóa

2. **Kiểm soát Truy cập**
   - Giới hạn quyền truy cập Google Slides cho các bài thuyết trình cần thiết
   - Sử dụng service account với quyền tối thiểu
   - Triển khai IP whitelisting nếu có thể

3. **Bảo vệ Dữ liệu**
   - Mã hóa dữ liệu nhạy cảm khi lưu trữ
   - Triển khai xóa an toàn file tạm thời
   - Kiểm tra log truy cập thường xuyên

### Lịch Bảo trì

#### Hàng ngày
- [ ] Kiểm tra log lỗi
- [ ] Giám sát sử dụng API
- [ ] Xác minh hoạt động bình thường

#### Hàng tuần
- [ ] Cập nhật dependencies
- [ ] Sao lưu dữ liệu
- [ ] Xem xét hiệu suất

#### Hàng tháng
- [ ] Luân chuyển khóa API
- [ ] Cập nhật tài liệu
- [ ] Kiểm tra bảo mật

#### Hàng quý
- [ ] Đánh giá hiệu suất tổng thể
- [ ] Cập nhật chiến lược bảo mật
- [ ] Xem xét cải tiến tính năng 