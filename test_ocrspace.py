#!/usr/bin/env python3
"""
Test script để kiểm tra OCR.space API với nhiều key.
"""

import requests
import base64
from PIL import Image, ImageDraw
import os
import json
from datetime import datetime, timedelta

def load_check_history():
    """Load lịch sử check từ file check_key.txt"""
    if os.path.exists('check_key.txt'):
        try:
            with open('check_key.txt', 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return {}
    return {}

def save_check_history(history):
    """Lưu lịch sử check vào file check_key.txt"""
    with open('check_key.txt', 'w', encoding='utf-8') as f:
        json.dump(history, f, ensure_ascii=False, indent=2)

def can_test_key(key_name, history):
    """Kiểm tra xem có thể test key này không dựa trên lịch sử"""
    if key_name not in history:
        return True
    
    last_check = history[key_name]['last_check']
    last_check_time = datetime.fromisoformat(last_check)
    current_time = datetime.now()
    
    # Nếu chưa đủ 1 giờ kể từ lần check cuối
    if current_time - last_check_time < timedelta(hours=1):
        remaining_time = timedelta(hours=1) - (current_time - last_check_time)
        print(f"⏰ Key '{key_name}' đã được check gần đây. Chờ thêm {remaining_time}")
        return False
    
    return True

def test_ocrspace_api(api_key, key_name):
    """Test OCR.space API với ảnh đơn giản."""
    try:
        print(f"-> Đang test key: {key_name}")
        print("-> Đang tạo ảnh test...")
        
        # Tạo ảnh test
        img = Image.new('RGB', (300, 100), color='white')
        draw = ImageDraw.Draw(img)
        draw.text((10, 10), "Hello World Test", fill='black')
        draw.text((10, 40), "OCR.space API Test", fill='black')
        
        # Lưu ảnh test
        test_img_path = f"test_ocrspace_{key_name}.png"
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
            return False, result.get('ErrorMessage', 'Unknown error')
        
        # Trích xuất text từ kết quả
        parsed_text = result['ParsedResults'][0]['ParsedText']
        
        print(f"✅ Kết quả OCR: '{parsed_text}'")
        
        if "Hello" in parsed_text or "Test" in parsed_text:
            print("✅ OCR.space API hoạt động bình thường!")
            return True, "Success"
        else:
            print("❌ OCR.space API không nhận dạng được text đơn giản.")
            return False, "OCR failed to recognize simple text"
            
    except Exception as e:
        print(f"❌ Lỗi: {e}")
        return False, str(e)

def format_time_ago(timestamp_str):
    """Format thời gian cách đây"""
    try:
        check_time = datetime.fromisoformat(timestamp_str)
        now = datetime.now()
        diff = now - check_time
        
        if diff.days > 0:
            return f"{diff.days} ngày trước"
        elif diff.seconds > 3600:
            hours = diff.seconds // 3600
            return f"{hours} giờ trước"
        elif diff.seconds > 60:
            minutes = diff.seconds // 60
            return f"{minutes} phút trước"
        else:
            return "Vừa xong"
    except:
        return "Không xác định"

def can_use_key(key_name, history):
    """Kiểm tra xem key có thể sử dụng không"""
    if key_name not in history:
        return True, "Chưa test"
    
    last_check = history[key_name]['last_check']
    last_check_time = datetime.fromisoformat(last_check)
    current_time = datetime.now()
    
    # Nếu chưa đủ 1 giờ kể từ lần check cuối
    if current_time - last_check_time < timedelta(hours=1):
        remaining_time = timedelta(hours=1) - (current_time - last_check_time)
        return False, f"Chờ thêm {remaining_time}"
    
    return True, "Có thể test"

def show_key_status():
    """Hiển thị trạng thái các key"""
    print("=== TRẠNG THÁI CHECK KEY OCR.SPACE ===")
    
    history = load_check_history()
    
    if not history:
        print("📝 Chưa có lịch sử check key nào.")
        print("Chạy test để test key.")
        return
    
    print(f"📋 Tìm thấy {len(history)} key trong lịch sử:")
    print()
    
    working_keys = []
    failed_keys = []
    waiting_keys = []
    
    for key_name, data in history.items():
        status, message = can_use_key(key_name, history)
        last_check = format_time_ago(data['last_check'])
        
        if data['success']:
            # Nếu key hoạt động, luôn hiển thị là HOẠT ĐỘNG
            working_keys.append((key_name, last_check))
            if status:
                print(f"✅ {key_name}: HOẠT ĐỘNG (check {last_check})")
            else:
                print(f"✅ {key_name}: HOẠT ĐỘNG (check {last_check}) - {message}")
        else:
            failed_keys.append((key_name, last_check, data['message']))
            print(f"❌ {key_name}: LỖI - {data['message']} (check {last_check})")
    
    print(f"\n{'='*50}")
    print("📊 THỐNG KÊ:")
    print(f"✅ Hoạt động: {len(working_keys)}")
    print(f"❌ Lỗi: {len(failed_keys)}")
    
    if working_keys:
        print(f"\n💡 KHUYẾN NGHỊ:")
        print(f"- Sử dụng {len(working_keys)} key hoạt động:")
        for key_name, last_check in working_keys:
            print(f"  + {key_name} (check {last_check})")
        print(f"- Mỗi key có thể xử lý ~180 slide/giờ")
        print(f"- Tổng cộng có thể xử lý ~{len(working_keys) * 180} slide/giờ")
        print(f"- Lưu ý: Mỗi key chỉ có thể test lại sau 1 giờ")
    
    if failed_keys:
        print(f"\n❌ CÁC KEY LỖI:")
        for key_name, last_check, message in failed_keys:
            print(f"  - {key_name}: {message}")

def test_multiple_keys():
    """Test nhiều key"""
    print("=== TEST OCR.SPACE API - MULTIPLE KEYS ===")
    print("Nhập danh sách key theo format: Tên1;Key1|Tên2;Key2|...")
    print("Ví dụ: Key1;abc123|Key2;def456")
    
    input_keys = input("Nhập danh sách key: ").strip()
    
    if not input_keys:
        print("❌ Không có key nào được nhập!")
        return
    
    # Parse input
    keys = []
    for pair in input_keys.split('|'):
        if ';' in pair:
            name, key = pair.split(';', 1)
            keys.append((name.strip(), key.strip()))
    
    if not keys:
        print("❌ Format không đúng!")
        return
    
    print(f"\n📋 Tìm thấy {len(keys)} key để test:")
    for name, key in keys:
        print(f"  - {name}: {key[:10]}...")
    
    # Load lịch sử
    history = load_check_history()
    
    print("\n🔍 Kiểm tra lịch sử test...")
    
    # Test từng key
    results = []
    for key_name, api_key in keys:
        print(f"\n{'='*50}")
        print(f"Testing: {key_name}")
        
        # Kiểm tra xem có thể test không
        if not can_test_key(key_name, history):
            continue
        
        # Test key
        success, message = test_ocrspace_api(api_key, key_name)
        
        # Lưu kết quả
        current_time = datetime.now()
        history[key_name] = {
            'last_check': current_time.isoformat(),
            'success': success,
            'message': message,
            'requests_used': 1
        }
        
        results.append({
            'name': key_name,
            'success': success,
            'message': message,
            'time': current_time.isoformat()
        })
        
        if success:
            print(f"✅ {key_name}: HOẠT ĐỘNG")
        else:
            print(f"❌ {key_name}: LỖI - {message}")
    
    # Lưu lịch sử
    save_check_history(history)
    
    # Hiển thị tổng kết
    print(f"\n{'='*50}")
    print("📊 TỔNG KẾT:")
    
    working_keys = [r for r in results if r['success']]
    failed_keys = [r for r in results if not r['success']]
    
    print(f"✅ Hoạt động: {len(working_keys)}")
    for result in working_keys:
        print(f"  - {result['name']}")
    
    if failed_keys:
        print(f"❌ Lỗi: {len(failed_keys)}")
        for result in failed_keys:
            print(f"  - {result['name']}: {result['message']}")
    
    # Hiển thị thông tin về giới hạn
    print(f"\n📈 THÔNG TIN GIỚI HẠN:")
    print("- Mỗi key: 180 requests/giờ")
    print("- Mỗi key: 25,000 requests/tháng")
    
    if working_keys:
        print(f"\n💡 KHUYẾN NGHỊ:")
        print(f"- Sử dụng {len(working_keys)} key hoạt động")
        print(f"- Mỗi key có thể xử lý ~180 slide/giờ")
        print(f"- Tổng cộng có thể xử lý ~{len(working_keys) * 180} slide/giờ")

def main():
    print("=== OCR.SPACE API KEY MANAGER ===")
    print("1. Test nhiều key")
    print("2. Xem trạng thái key")
    print("3. Thoát")
    
    choice = input("\nChọn chức năng (1-3): ").strip()
    
    if choice == "1":
        test_multiple_keys()
    elif choice == "2":
        show_key_status()
    elif choice == "3":
        print("Tạm biệt!")
    else:
        print("❌ Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main() 