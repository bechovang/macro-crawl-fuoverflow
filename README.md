# Google Slides Crawler

A Python tool to automatically capture Google Slides presentations, extract text using OCR, and format content with AI assistance using Google's Gemini 1.5.

## English Version

### Overview

This project provides an automated solution to capture Google Slides presentations, extract text content using Google Cloud Vision API, and format the results using Google's Gemini 1.5 AI. It's particularly useful for creating documentation from presentations or analyzing slide content programmatically.

### Features

- **Automated Slide Capture**: Uses Selenium WebDriver to navigate and capture slides
- **OCR Text Extraction**: Integrates Google Cloud Vision API for accurate text recognition
- **AI-Powered Formatting**: Uses Google Gemini 1.5 to clean and structure extracted text
- **Speaker Notes Support**: Captures both slide content and presenter notes
- **Batch Processing**: Handles entire presentations with configurable delays
- **Multiple Output Formats**: Generates screenshots, OCR text, and formatted content

### Prerequisites

- Python 3.8+
- Google Chrome browser
- Google Cloud Vision API credentials
- Google Gemini API key (for text formatting)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd crawl-google-slide
   ```

2. **Create and activate virtual environment**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate
   
   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up Google Cloud Vision API**
   - Create a Google Cloud project
   - Enable the Vision API
   - Create a service account and download credentials JSON
   - Set environment variable:
     ```bash
     # Windows
     set GOOGLE_APPLICATION_CREDENTIALS=path\to\credentials.json
     
     # macOS/Linux
     export GOOGLE_APPLICATION_CREDENTIALS=path/to/credentials.json
     ```

5. **Configure Gemini API**
   - Get a Gemini API key from https://makersuite.google.com/app/apikey
   - The API key is already configured in the project: `AIzaSyBYEKKI0v-5WvixUA4BY9EPLeOul92FYcQ`

### Usage

1. **Basic Usage**
   ```python
   from main import GoogleSlidesCapture
   
   # Initialize capturer
   capturer = GoogleSlidesCapture(headless=False)
   
   # Process a single slide
   result = capturer.process_slide(
       "https://docs.google.com/presentation/d/YOUR_ID/edit",
       1
   )
   
   # Process entire presentation
   results = capturer.process_presentation(
       "https://docs.google.com/presentation/d/YOUR_ID/edit",
       total_slides=10
   )
   
   capturer.close()
   ```

2. **Command Line Usage**
   ```bash
   python main.py
   ```

### Configuration

- **Headless Mode**: Set `headless=True` for background processing
- **Delay Between Slides**: Adjust `SLIDE_DELAY` in config.py to avoid rate limiting
- **Output Directory**: Screenshots and text files are saved in the current directory
- **AI Formatting**: Customize the prompt in `config.py` AI_PROMPTS section

### Output Files

For each slide, the tool generates:
- `slide_{number}_with_notes.png`: Full screenshot
- `slide_{number}_content.png`: Slide content only
- `slide_{number}_notes.png`: Speaker notes only
- `slide_{number}_formatted.txt`: AI-formatted text content

### Error Handling

- Automatic retry for failed OCR operations
- Graceful handling of missing speaker notes
- Logging of processing errors
- Fallback to basic text extraction if AI formatting fails

### Security Notes

- Never commit API keys to version control
- Use environment variables for sensitive credentials
- Consider using OAuth for user-specific access
- Implement proper session management for production use

---

## Vietnamese Version

### Tổng quan

Dự án này cung cấp giải pháp tự động để chụp các bài thuyết trình Google Slides, trích xuất nội dung văn bản bằng Google Cloud Vision API và định dạng kết quả bằng Google Gemini 1.5 AI. Đặc biệt hữu ích cho việc tạo tài liệu từ bài thuyết trình hoặc phân tích nội dung slide một cách lập trình.

### Tính năng

- **Chụp Slide Tự động**: Sử dụng Selenium WebDriver để điều hướng và chụp slide
- **Trích xuất văn bản OCR**: Tích hợp Google Cloud Vision API để nhận dạng văn bản chính xác
- **Định dạng bằng AI**: Sử dụng Google Gemini 1.5 để làm sạch và cấu trúc văn bản trích xuất
- **Hỗ trợ Ghi chú**: Chụp cả nội dung slide và ghi chú của người thuyết trình
- **Xử lý hàng loạt**: Xử lý toàn bộ bài thuyết trình với độ trễ có thể cấu hình
- **Nhiều định dạng đầu ra**: Tạo ra ảnh chụp màn hình, văn bản OCR và nội dung đã định dạng

### Yêu cầu hệ thống

- Python 3.8+
- Trình duyệt Google Chrome
- Thông tin xác thực Google Cloud Vision API
- Khóa API Google Gemini (để định dạng văn bản)

### Cài đặt

1. **Clone repository**
   ```bash
   git clone <repository-url>
   cd crawl-google-slide
   ```

2. **Tạo và kích hoạt môi trường ảo**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate
   
   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Cài đặt dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Thiết lập Google Cloud Vision API**
   - Tạo dự án Google Cloud
   - Bật Vision API
   - Tạo service account và tải xuống file credentials JSON
   - Thiết lập biến môi trường:
     ```bash
     # Windows
     set GOOGLE_APPLICATION_CREDENTIALS=path\to\credentials.json
     
     # macOS/Linux
     export GOOGLE_APPLICATION_CREDENTIALS=path/to/credentials.json
     ```

5. **Cấu hình Gemini API**
   - Lấy khóa API Gemini từ https://makersuite.google.com/app/apikey
   - Khóa API đã được cấu hình sẵn trong dự án: `AIzaSyBYEKKI0v-5WvixUA4BY9EPLeOul92FYcQ`

### Cách sử dụng

1. **Sử dụng cơ bản**
   ```python
   from main import GoogleSlidesCapture
   
   # Khởi tạo capturer
   capturer = GoogleSlidesCapture(headless=False)
   
   # Xử lý một slide
   result = capturer.process_slide(
       "https://docs.google.com/presentation/d/YOUR_ID/edit",
       1
   )
   
   # Xử lý toàn bộ bài thuyết trình
   results = capturer.process_presentation(
       "https://docs.google.com/presentation/d/YOUR_ID/edit",
       total_slides=10
   )
   
   capturer.close()
   ```

2. **Sử dụng Command Line**
   ```bash
   python main.py
   ```

### Cấu hình

- **Chế độ Headless**: Đặt `headless=True` để xử lý nền
- **Độ trễ giữa các slide**: Điều chỉnh `SLIDE_DELAY` trong config.py để tránh bị giới hạn tốc độ
- **Thư mục đầu ra**: Ảnh chụp màn hình và file văn bản được lưu trong thư mục hiện tại
- **Định dạng AI**: Tùy chỉnh prompt trong phần AI_PROMPTS của config.py

### File đầu ra

Cho mỗi slide, công cụ tạo ra:
- `slide_{number}_with_notes.png`: Ảnh chụp màn hình đầy đủ
- `slide_{number}_content.png`: Chỉ nội dung slide
- `slide_{number}_notes.png`: Chỉ ghi chú
- `slide_{number}_formatted.txt`: Nội dung văn bản đã định dạng bằng AI

### Xử lý lỗi

- Tự động thử lại cho các thao tác OCR thất bại
- Xử lý nhẹ nhàng khi thiếu ghi chú
- Ghi log các lỗi xử lý
- Fallback về trích xuất văn bản cơ bản nếu định dạng AI thất bại

### Lưu ý bảo mật

- Không bao giờ commit khóa API vào version control
- Sử dụng biến môi trường cho các thông tin xác thực nhạy cảm
- Cân nhắc sử dụng OAuth cho quyền truy cập người dùng cụ thể
- Triển khai quản lý phiên phù hợp cho sử dụng production

## License

MIT License - see LICENSE file for details. 