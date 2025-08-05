#!/usr/bin/env python3
"""
Test script để kiểm tra OCR.space API.
"""

import requests
import base64
from PIL import Image, ImageDraw
import os

def test_ocrspace_api(api_key):
    """Test OCR.space API với ảnh đơn giản."""
    try:
        print("-> Đang tạo ảnh test...")
        
        # Tạo ảnh test
        img = Image.new('RGB', (300, 100), color='white')
        draw = ImageDraw.Draw(img)
        draw.text((10, 10), "Hello World Test", fill='black')
        draw.text((10, 40), "OCR.space API Test", fill='black')
        
        # Lưu ảnh test
        test_img_path = "test_ocrspace.png"
        img.save(test_img_path)
        
        print("-> Đang gửi yêu cầu đến OCR.space API...")
        
        # Đọc ảnh và encode base64
        with open(test_img_path, 'rb') as image_file:
            image_data = image_file.read()
            image_base64 = base64.b64encode(image_data).decode('utf-8')
        
        # Gửi yêu cầu đến OCR.space API
        url = "https://api.ocr.space/parse/image"
        payload = {
            'apikey': api_key,
            'base64Image': f'data:image/png;base64,{image_base64}',
            'language': 'eng',
            'isOverlayRequired': False,
            'filetype': 'png',
            'detectOrientation': True,
            'scale': True,
            'OCREngine': 2
        }
        
        response = requests.post(url, data=payload, timeout=30)
        result = response.json()
        
        # Xóa file test
        os.remove(test_img_path)
        
        if result['IsErroredOnProcessing']:
            print(f"❌ Lỗi: {result['ErrorMessage']}")
            return False
        
        # Trích xuất text từ kết quả
        parsed_text = result['ParsedResults'][0]['ParsedText']
        
        print(f"✅ Kết quả OCR: '{parsed_text}'")
        
        if "Hello" in parsed_text or "Test" in parsed_text:
            print("✅ OCR.space API hoạt động bình thường!")
            return True
        else:
            print("❌ OCR.space API không nhận dạng được text đơn giản.")
            return False
            
    except Exception as e:
        print(f"❌ Lỗi: {e}")
        return False

if __name__ == "__main__":
    print("=== TEST OCR.SPACE API ===")
    
    api_key = input("Nhập OCR.space API key của bạn: ").strip()
    
    if not api_key:
        print("❌ API key không được để trống!")
        exit(1)
    
    success = test_ocrspace_api(api_key)
    
    if success:
        print("\n✅ OCR.space API đã sẵn sàng để sử dụng!")
        print("Bạn có thể chạy main.py để bắt đầu sử dụng.")
    else:
        print("\n❌ Có vấn đề với OCR.space API.")
        print("Hãy kiểm tra:")
        print("- API key có đúng không")
        print("- Kết nối internet")
        print("- API key có còn hiệu lực không") 