# Hướng dẫn Bảo trì (Maintenance Guide) - Công cụ tạo PDF trắc nghiệm

Tài liệu này mô tả cấu trúc dự án thực tế của repo hiện tại, các thành phần cốt lõi trong `tao_pdf_trac_nghiem.py`, cùng hướng dẫn bảo trì và khắc phục sự cố.

## 1. Cấu trúc Dự án

```
macro-crawl-fuoverflow/
├── tao_pdf_trac_nghiem.py      # Script chính: chọn vùng, chụp ảnh, ghép PDF
├── requirements.txt            # Thư viện phụ thuộc
├── ket_qua_hoc_tap/            # Thư mục kết quả (tự tạo nếu chưa có)
│   └── images/                 # Ảnh chụp từng câu (được sinh ra khi chạy)
├── purchase-success.mp3        # Âm báo khi xong một câu (tuỳ chọn)
├── victory.mp3                 # Âm báo khi hoàn tất (tuỳ chọn)
├── prompt_ai_after_run.md      # Prompt gợi ý xử lý bằng AI sau khi chạy
└── ...
```

## 2. Thành phần Cốt lõi (`tao_pdf_trac_nghiem.py`)

 -  `play_sound(sound_type)`: Phát âm thanh bằng `pygame`. Không có âm thanh vẫn chạy bình thường.

 -  `show_image_preview(...)` và `show_split_image_preview(...)`: Dùng `matplotlib` hiển thị ảnh xem trước, tạm dừng luồng cho đến khi đóng.

 -  `MouseCalibrationTool` và `calibrate_with_mouse(...)`: Lớp/tiện ích Tkinter toàn màn hình cho phép kéo chuột chọn vùng. Có tính toán tỉ lệ DPI giữa Tkinter và PyAutoGUI để khớp toạ độ.

 -  `_clamp_region_to_bounds(...)`: Kẹp vùng con vào trong vùng chính, tránh tràn mép.

 -  `capture_images(...)`: Vòng lặp chụp ảnh 2 vùng (câu hỏi/đáp án) cho mỗi câu, tự nhấn phím `Right` để sang câu kế tiếp, lưu đường dẫn ảnh.

 -  `create_pdf_from_images(...)`: Ghép ảnh câu hỏi và đáp án vào một PDF, giữ tỉ lệ, chèn tiêu đề trang.

 -  `main()`: Quy trình điều phối: hướng dẫn, căn chỉnh 3 bước, nhập tổng số câu và độ trễ, đếm ngược, chụp hàng loạt, ghép PDF, thông báo hoàn tất.

### 2.1. Tùy chọn cấu hình

-  `ENFORCE_NON_OVERLAP = False`: Nếu bật, sẽ tự điều chỉnh để vùng đáp án bắt đầu ngay dưới đáy vùng câu hỏi, tránh chồng lấn.
-  Phím chuyển trang mặc định là `Right` (có thể điều chỉnh trực tiếp trong code nếu trang của bạn dùng phím khác).

## 3. Nhiệm vụ Bảo trì

1.  Cập nhật dependencies:
    -   Chạy `pip list --outdated` trong venv và cân nhắc nâng cấp có kiểm soát.

2.  Kiểm tra tương thích hệ điều hành/Màn hình:
    -   Test lại khi thay đổi DPI scaling trên Windows (125%, 150%, ...).
    -   Nếu chuyển sang đa màn hình, đảm bảo canh chỉnh trên màn hình chính (primary).

3.  Quản lý tài nguyên:
    -   Dọn thư mục `ket_qua_hoc_tap/images` định kỳ để tránh chiếm dụng dung lượng.
    -   Đảm bảo file âm thanh tồn tại; nếu không cần, có thể xoá để giảm footprint.

## 4. Hướng dẫn Khắc phục Sự cố

| Vấn đề | Nguyên nhân có thể | Giải pháp |
| --- | --- | --- |
| Cửa sổ xem trước không hiển thị | Backend `matplotlib` lỗi, thiếu GUI backend | Cài đặt/upgrade `matplotlib`; thử chạy lại trong môi trường có GUI |
| Ảnh chụp bị lệch | Di chuyển cửa sổ/zoom sau khi căn chỉnh; DPI thay đổi | Căn chỉnh lại; giữ nguyên zoom/position trong quá trình chạy |
| Không phát âm thanh | `pygame` chưa init hoặc thiếu file mp3 | Bỏ qua hoặc kiểm tra file mp3, driver âm thanh |

## 5. Ghi chú khác

-   Không có khoá API hoặc dịch vụ đám mây trong phiên bản này; chỉ cần các thư viện Python theo `requirements.txt`.
-   Khuyến nghị thêm `venv/` và `ket_qua_hoc_tap/` vào `.gitignore` nếu public repo.