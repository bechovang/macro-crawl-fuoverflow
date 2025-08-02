"""
Configuration file for Google Slides Crawler
Contains all configurable settings for the application
"""

import os
from typing import Optional

# Browser Configuration
HEADLESS_MODE = os.getenv('CHROME_HEADLESS', 'true').lower() == 'true'
WINDOW_SIZE = os.getenv('WINDOW_SIZE', '1920,1080')
CHROME_OPTIONS = [
    '--disable-gpu',
    '--no-sandbox',
    '--disable-dev-shm-usage',
    '--disable-blink-features=AutomationControlled',
    '--disable-extensions',
    '--disable-plugins',
    '--disable-images',  # Optional: disable images for faster loading
]

# Timing Configuration
SLIDE_DELAY = int(os.getenv('SLIDE_DELAY', '2'))  # seconds between slides
LOAD_TIMEOUT = int(os.getenv('LOAD_TIMEOUT', '10'))  # seconds to wait for page load
OCR_TIMEOUT = int(os.getenv('OCR_TIMEOUT', '30'))  # seconds for OCR processing

# API Configuration
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY', 'AIzaSyBYEKKI0v-5WvixUA4BY9EPLeOul92FYcQ')
GOOGLE_APPLICATION_CREDENTIALS = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')

# Gemini Configuration
GEMINI_MODEL = os.getenv('GEMINI_MODEL', 'gemini-1.5-flash')
GEMINI_MAX_TOKENS = int(os.getenv('GEMINI_MAX_TOKENS', '1000'))
GEMINI_TEMPERATURE = float(os.getenv('GEMINI_TEMPERATURE', '0.7'))

# Output Configuration
OUTPUT_DIR = os.getenv('OUTPUT_DIR', './output')
SCREENSHOT_FORMAT = os.getenv('SCREENSHOT_FORMAT', 'png')
TEXT_ENCODING = os.getenv('TEXT_ENCODING', 'utf-8')

# Processing Configuration
MAX_RETRIES = int(os.getenv('MAX_RETRIES', '3'))
BATCH_SIZE = int(os.getenv('BATCH_SIZE', '5'))  # slides per batch
ENABLE_AI_FORMATTING = os.getenv('ENABLE_AI_FORMATTING', 'true').lower() == 'true'

# Logging Configuration
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
LOG_FILE = os.getenv('LOG_FILE', 'crawler.log')

# Google Slides URL Patterns
SLIDE_URL_PATTERNS = {
    'edit': '/edit',
    'present': '/present',
    'preview': '/preview',
    'embed': '/embed',
}

# CSS Selectors (may need updates if Google changes their UI)
CSS_SELECTORS = {
    'slide_container': '.punch-present-slide-container, .punch-viewer-content',
    'notes_container': '.punch-present-notes-container, .speaker-notes-container',
    'slide_content': '.punch-viewer-content',
    'presenter_view': '.punch-presenter-view',
}

# AI Prompt Templates
AI_PROMPTS = {
    'format_slide': """
    Đây là nội dung OCR từ một slide thuyết trình:
    
    NỘI DUNG SLIDE:
    {slide_text}
    
    GHI CHÚ/NOTES:
    {notes_text}
    
    Hãy sắp xếp lại thành định dạng rõ ràng, bao gồm:
    1. Tiêu đề chính
    2. Nội dung chính của slide
    3. Ghi chú bổ sung (nếu có)
    
    Giữ nguyên ý nghĩa và thông tin quan trọng.
    """,
    
    'format_slide_en': """
    Here is OCR content from a presentation slide:
    
    SLIDE CONTENT:
    {slide_text}
    
    SPEAKER NOTES:
    {notes_text}
    
    Please organize this into a clear format including:
    1. Main title
    2. Key slide content
    3. Additional notes (if any)
    
    Preserve the original meaning and important information.
    """
}

# Error Messages
ERROR_MESSAGES = {
    'driver_init': 'Failed to initialize Chrome driver',
    'slide_not_found': 'Slide element not found on page',
    'notes_not_found': 'Speaker notes not found',
    'ocr_failed': 'OCR processing failed',
    'ai_format_failed': 'AI formatting failed',
    'api_error': 'API request failed',
}

# File Naming Patterns
FILE_PATTERNS = {
    'screenshot_full': 'slide_{number}_with_notes.{format}',
    'screenshot_slide': 'slide_{number}_content.{format}',
    'screenshot_notes': 'slide_{number}_notes.{format}',
    'formatted_text': 'slide_{number}_formatted.txt',
    'raw_text': 'slide_{number}_raw.txt',
}

# Performance Settings
MEMORY_LIMIT = int(os.getenv('MEMORY_LIMIT', '512'))  # MB
CLEANUP_INTERVAL = int(os.getenv('CLEANUP_INTERVAL', '10'))  # slides

# Security Settings
ENABLE_SSL_VERIFY = os.getenv('ENABLE_SSL_VERIFY', 'true').lower() == 'true'
REQUEST_TIMEOUT = int(os.getenv('REQUEST_TIMEOUT', '30'))

# Development Settings
DEBUG_MODE = os.getenv('DEBUG_MODE', 'false').lower() == 'true'
SAVE_DEBUG_IMAGES = os.getenv('SAVE_DEBUG_IMAGES', 'false').lower() == 'true'

def validate_config() -> bool:
    """
    Validate that all required configuration is present
    Returns True if valid, False otherwise
    """
    required_vars = [
        'GOOGLE_APPLICATION_CREDENTIALS',
    ]
    
    missing_vars = []
    for var in required_vars:
        if not globals().get(var):
            missing_vars.append(var)
    
    if missing_vars:
        print(f"Missing required environment variables: {missing_vars}")
        return False
    
    return True

def get_output_path(filename: str) -> str:
    """
    Get full path for output file
    """
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    return os.path.join(OUTPUT_DIR, filename)

def get_chrome_options() -> list:
    """
    Get Chrome options as list
    """
    options = CHROME_OPTIONS.copy()
    options.append(f'--window-size={WINDOW_SIZE}')
    
    if HEADLESS_MODE:
        options.append('--headless')
    
    return options 