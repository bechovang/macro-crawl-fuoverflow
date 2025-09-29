Rõ rồi 👍. Mình sẽ chia thành **2 prompt riêng biệt**, theo đúng nhu cầu bạn nói:

---

# 🟢 Prompt 1: **Từ text OCR → đề trắc nghiệm (EN) + giải thích (VI)**

```
Bạn là một trợ lý chuyên xử lý kết quả OCR từ đề trắc nghiệm.

Tôi sẽ dán nguyên văn text OCR vào đây:
{{PASTE_OCR_TEXT_Ở_ĐÂY}}

Nhiệm vụ của bạn:

A. Phân tích nhanh
1. Xác định ngôn ngữ của câu hỏi (hầu hết sẽ là English).
2. Liệt kê 3 lỗi OCR đáng chú ý (ví dụ: ký tự bị thay, chữ/số lẫn lộn).

B. Làm sạch & trích xuất
1. Sửa lỗi OCR rõ rệt (không đổi nội dung chuyên môn). Nếu có sửa, hiện song song:
   - Raw (OCR gốc)
   - Cleaned (sửa)
2. Tách thành các câu hỏi theo thứ tự Câu 1, Câu 2, ...
3. Mỗi câu trình bày:
   - Question (giữ tiếng Anh gốc, đã cleaned)
   - Options (A, B, C, D — tiếng Anh, mỗi dòng một lựa chọn)
   - Answer:
     • Nếu OCR có ghi đáp án → "Answer (OCR): X"
     • Nếu không → "Answer (inferred): Y" + lý do ngắn
   - Explanation (tiếng Việt): giải thích tại sao chọn đáp án đúng (dùng từ chuyên ngành trong ngoặc tiếng Anh).
   - Confidence: Cao / Trung bình / Thấp + lý do.
   - Nếu có đoạn nghi ngờ, thêm "Ghi chú OCR: ..."

C. Xuất bản
1. **Form trắc nghiệm (Study)**: hiện đủ câu hỏi + đáp án đúng (đánh dấu ✅) + explanation tiếng Việt.
2. **Form trắc nghiệm (Blank)**: chỉ có câu hỏi + options, chưa hiện đáp án.
3. **Answer Key**: bảng ngắn C1 → B, C2 → C...
4. **CSV**: bảng với cột: id,question,optionA,optionB,optionC,optionD,answer,explanation_short,confidence.

D. Quy tắc
- Câu hỏi & đáp án giữ nguyên tiếng Anh.
- Giải thích bằng tiếng Việt, có thể thêm chú thích (English terms) trong ngoặc.
- Không đoán mù; nếu không chắc → "Không rõ, cần kiểm tra".
```

---

# 🟢 Prompt 2: **Từ trắc nghiệm → Flashcards (Front/Back)**

```
Bạn là một trợ lý tạo flashcard.

Input: Tôi sẽ dán vào đây danh sách trắc nghiệm dạng chuẩn (question + options + answer + explanation).

Nhiệm vụ của bạn:
1. Tạo flashcard cho từng câu theo định dạng:
   - Front: Question (tiếng Anh) + Options (A–D)
   - Back: Correct Answer (ghi rõ "Answer: X") + Explanation (tiếng Việt, có kèm thuật ngữ tiếng Anh trong ngoặc)
2. Mỗi flashcard đánh số theo câu gốc.
3. Output:
   - Danh sách flashcards dạng text (front/back).
   - CSV (cột: id,front,back) để import vào Anki/Quizlet.
   - Nếu có nhiều câu, trình bày cách nhau bằng dòng "---".

Quy tắc:
- Question và options giữ tiếng Anh.
- Explanation bằng tiếng Việt, có thuật ngữ (English) trong ngoặc.
- Ngắn gọn, dễ học.
```

---

👉 Với combo này:

* **Prompt 1**: từ OCR → đề trắc nghiệm chuẩn, có giải thích.
* **Prompt 2**: từ trắc nghiệm chuẩn (output của Prompt 1) → flashcard front/back để học.

---

Bạn có muốn mình **demo chạy thử Prompt 1** trên đoạn OCR bạn đã gửi hôm trước (5 câu hỏi về MULTICS, time-sharing, UNIVAC, fetch-decode-execute, CPU) để thấy kết quả trực quan không?
