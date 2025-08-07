
2025-08-05 21:39

Status:

Tags: [[source]] [[CSI]]
Disable spell check :`teh`
# SOURCE CSI 0-100



# Ngân Hàng Câu Hỏi
## I. Thông tin chung & Tài liệu tham khảo

Phần này bao gồm các thông báo, liên kết và tài liệu học tập hữu ích.

*   **Nhóm Facebook:** Mọi người nên tham gia nhóm Facebook để cập nhật thông tin và truy cập các đề thi mới (đặc biệt là đề FE SU25 cho các bạn thi lại).
*   **Tài liệu học tập:**
    *   Nên ưu tiên ôn tập dựa trên **slide bài giảng**.
    *   **Tài liệu đọc hiểu bổ sung:** Có thể hữu ích cho việc tìm hiểu sâu hơn.
    *   **Tài liệu tham khảo (SRO, PT, EBS):** [Google Drive](https://drive.google.com/drive/folders/1XE-KS-im7DAAqbvCfLazKWd1m438iZI?usp=sharing)
    *   **Luyện tập Flashcard:** [Quizlet CSI106](https://quizlet.com/vn/966878782/csi-106-flash-card)
*   **Thông tin khóa học (Tham khảo):**
    *   Khóa học **PRO192 - Lập trình hướng đối tượng** có sẵn lộ trình chi tiết tại: [https://4user.net/home/courses](https://4user.net/home/courses)

---

## II. Kiến thức nền tảng

Đây là phần tổng hợp các khái niệm, công thức và bảng tham chiếu quan trọng.

### 1. Bảng chuyển đổi các hệ đếm

Bảng này so sánh các giá trị tương đương giữa hệ Nhị phân (Binary), Thập phân (Decimal) và Thập lục phân (Hexadecimal).

| BINARY | DECIMAL | HEXADECIMAL |
| :--- | :--- | :--- |
| 0001 | 1 | 1 |
| 0010 | 2 | 2 |
| 0011 | 3 | 3 |
| 0100 | 4 | 4 |
| 0101 | 5 | 5 |
| 0110 | 6 | 6 |
| 0111 | 7 | 7 |
| 1000 | 8 | 8 |
| 1001 | 9 | 9 |
| 1010 | 10 | A |
| 1011 | 11 | B |
| 1100 | 12 | C |
| 1101 | 13 | D |
| 1110 | 14 | E |
| 1111 | 15 | F |
| 10000| 16 | 10 |

### 2. Cách chuyển đổi Nhị phân sang Thập phân

Để chuyển một số từ hệ nhị phân sang hệ thập phân, ta nhân mỗi chữ số nhị phân với 2 lũy thừa vị trí của nó (tính từ phải sang trái, bắt đầu từ 0) rồi cộng tất cả lại.

**Ví dụ:** Chuyển số `11001`₂ sang hệ thập phân.
*   Vị trí các bit: `1` (4), `1` (3), `0` (2), `0` (1), `1` (0)
*   Giá trị = (1 × 2⁴) + (1 × 2³) + (0 × 2²) + (0 × 2¹) + (1 × 2⁰) = 16 + 8 + 0 + 0 + 1 = `25`.

### 3. So sánh mô hình TCP/IP và OSI

Mô hình TCP/IP là một phiên bản rút gọn và thực tế hơn của mô hình OSI lý thuyết.

| Lớp trong mô hình TCP/IP | Tương ứng trong mô hình OSI |
| :--- | :--- |
| **Application Layer** | Application, Presentation, Session Layer |
| **Transport Layer** | Transport Layer |
| **Internet Layer (Network)** | Network Layer |
| **Network Access Layer** | Data Link, Physical Layer |

### 4. So sánh địa chỉ IPv4 và IPv6

IPv6 được tạo ra để giải quyết vấn đề cạn kiệt địa chỉ của IPv4.

| Đặc điểm | IPv4 | IPv6 |
| :--- | :--- | :--- |
| **Độ dài** | 32-bit | 128-bit |
| **Số lượng địa chỉ** | ~4.3 tỷ | ~3.4 x 10³⁸ |
| **Ví dụ** | `192.168.1.1` | `2001:0db8:85a3::8a2e:0370:7334`|

### 5. Các đơn vị lưu trữ dữ liệu

Nắm vững các công thức này để giải bài tập chuyển đổi.

*   1 Kilobyte (KB) = 2¹⁰ Bytes = 1024 Bytes
*   1 Megabyte (MB) = 2¹⁰ KB = 1024 KB
*   1 Megabyte (MB) = 2²⁰ Bytes

---

## Câu 12:
For each entity set in the E-R diagram we create a relation (table) in which there are n columns related to the attributes defined for that set.
A. n-1
B. n
C. n+1
D. 1-n
> **Giải thích:**
> **Đáp án đúng là B.** Trong mô hình Thực thể-Kết hợp (E-R), mỗi tập thực thể (entity set) được ánh xạ thành một bảng (relation). Mỗi thuộc tính (attribute) của tập thực thể sẽ trở thành một cột (column) trong bảng đó. Do đó, nếu một tập thực thể có `n` thuộc tính, bảng tương ứng sẽ có `n` cột.

---

## Câu 13:
The base of the binary number system is \_\_\_\_\_\_.
A. 2
B. 8
C. 10
D. 16
> **Giải thích:**
> **Đáp án đúng là A.** Hệ nhị phân (binary) chỉ sử dụng hai ký tự là 0 và 1, do đó cơ số (base) của nó là 2.

---

## Câu 14:
The base of the octal number system is \_\_\_\_\_\_.
A. 2
B. 8
C. 10
D. 16
> **Giải thích:**
> **Đáp án đúng là B.** Hệ bát phân (octal) sử dụng tám ký tự từ 0 đến 7, do đó cơ số (base) của nó là 8.

---

## Câu 15:
The base of the hexadecimal number system is \_\_\_\_\_\_.
A. 2
B. 8
C. 10
D. 16
> **Giải thích:**
> **Đáp án đúng là D.** Hệ thập lục phân (hexadecimal) sử dụng 16 ký tự (0-9 và A-F), do đó cơ số (base) của nó là 16.

---

## Câu 16:
A byte consists of \_\_\_\_\_\_ bits.
A. 2
B. 4
C. 8
D. 16
> **Giải thích:**
> **Đáp án đúng là C.** Theo định nghĩa chuẩn trong khoa học máy tính, một byte bao gồm 8 bit.

---

## Câu 17:
A control unit with five wires can define up to \_\_\_\_\_\_ operations.
A. 5
B. 10
C. 16
D. 32
> **Giải thích:**
> **Đáp án đúng là D.** Với `n` dây (wires), số lượng trạng thái hoặc hoạt động khác nhau có thể biểu diễn là 2ⁿ. Trong trường hợp này, với 5 dây, ta có 2⁵ = 32 hoạt động khác nhau.

---

## Câu 18:
The maximum value of an octal integer with K=2 digits is Nmax = \_\_\_\_\_\_.
A. 63
B. 64
C. 65
D. 66
E. None of the others
> **Giải thích:**
> **Đáp án đúng là A.** Giá trị lớn nhất của một số trong hệ cơ số `b` với `K` chữ số được tính bằng công thức: N_max = bᴷ - 1. Trong trường hợp này, hệ cơ số là bát phân (b=8) và số chữ số là K=2. Vậy, N_max = 8² - 1 = 64 - 1 = 63.

---

## Câu 19:
The maximum value of a binary integer with K digits. For example, if K = 5, then the maximum value is —?
A. 30
B. 31
C. 32
D. 33
> **Giải thích:**
> **Đáp án đúng là B.** Áp dụng công thức N_max = bᴷ - 1. Với hệ nhị phân (b=2) và K=5 chữ số, ta có N_max = 2⁵ - 1 = 32 - 1 = 31.

---

## Câu 20:
EBCDIC can code up to how many different characters?
A. 8
B. 16
C. 32
D. 64
E. 256
> **Giải thích:**
> **Đáp án đúng là E.** EBCDIC (Extended Binary Coded Decimal Interchange Code) là một bảng mã 8-bit. Do đó, nó có thể biểu diễn 2⁸ = 256 ký tự khác nhau.

---

## Câu 21:
What is the number of bit patterns provided by a 7-bit code?
A. 256
B. 128
C. 64
D. 512
E. None of the others
> **Giải thích:**
> **Đáp án đúng là B.** Một mã 7-bit có thể tạo ra 2⁷ = 128 mẫu bit (bit patterns) khác nhau.

---

## Câu 22:
If the memory address space is 16 MB and the word size is 8 bits, then \_\_\_\_\_\_ bits are needed to access each byte.
A. 8
B. 16
C. 24
D. 32
> **Giải thích:**
> **Đáp án đúng là C.** Số bit cần thiết để định địa chỉ cho bộ nhớ được tính bằng logarit cơ số 2 của tổng số byte trong không gian địa chỉ.
> 1.  Chuyển đổi không gian địa chỉ sang byte: 16 MB = 16 × 2²⁰ bytes = 2⁴ × 2²⁰ = 2²⁴ bytes.
> 2.  Số bit cần thiết = log₂(2²⁴) = 24 bits.

---

## Câu 23:
In a positional number system with base b, we can always find the number of digits of an integer. So how many digits can we find in the decimal number 20 in hexadecimal system?
A. 1
B. 2
C. 3
D. 4
E. None of the others
> **Giải thích:**
> **Đáp án đúng là B.** Để tìm số chữ số cần thiết để biểu diễn số 20 (hệ 10) trong hệ 16, ta chỉ cần chuyển đổi nó: 20 chia cho 16 được 1 dư 4. Vậy số 20 trong hệ 16 là `14₁₆`. Nó cần 2 chữ số.

---

## Câu 24:
A group contains \_\_\_\_\_\_ bits in the binary system are represented as one digit in the octal system.
A. 1
B. 2
C. 3
D. 4
E. None of the others
> **Giải thích:**
> **Đáp án đúng là C.** Hệ bát phân có cơ số 8, và 8 = 2³. Do đó, mỗi chữ số trong hệ bát phân có thể được biểu diễn bằng một nhóm 3 bit trong hệ nhị phân.

---

## Câu 25:
A group includes \_\_\_\_\_\_ bits in the binary system are represented as one digit in the hexadecimal system.
A. 1
B. 2
C. 3
D. 4
E. None of the others
> **Giải thích:**
> **Đáp án đúng là D.** Hệ thập lục phân có cơ số 16, và 16 = 2⁴. Do đó, mỗi chữ số trong hệ thập lục phân có thể được biểu diễn bằng một nhóm 4 bit trong hệ nhị phân.

---

## Câu 26:
In a positional number system with base b, we can always find the number of digits of an integer. So how many digits can we find in the decimal number 20 in octal system?
A. 1
B. 2
C. 3
D. 4
E. None of the others
> **Giải thích:**
> **Đáp án đúng là B.** Để chuyển số 20 (hệ 10) sang hệ bát phân (octal):
> *   20 chia 8 được 2, dư 4.
> *   2 chia 8 được 0, dư 2.
> Đọc ngược số dư, ta được `24₈`. Số này cần 2 chữ số.

---

## Câu 27:
In a positional number system with base b, we can always find the number of digits of an integer. So how many digits can we find in the decimal number 20 in hexadecimal system?
A. 1
B. 2
C. 3
D. 4
E. None of the others
> **Giải thích:**
> **Đáp án đúng là B.** Câu này lặp lại câu 23. Chuyển số 20 (hệ 10) sang hệ thập lục phân (hexadecimal) ta được `14₁₆`, cần 2 chữ số.

---

## Câu 28:
A database management system (DBMS) is a combination of \_\_\_\_\_\_ components.
A. 2
B. 3
C. 4
D. 5
> **Giải thích:**
> **Đáp án đúng là D.** Một hệ quản trị cơ sở dữ liệu (DBMS) điển hình bao gồm 5 thành phần chính: Phần cứng (Hardware), Phần mềm (Software), Dữ liệu (Data), Thủ tục (Procedures), và Người dùng (Database Access Language/Users).

---

## Câu 29:
How many bits that we can find in the decimal number 20 in binary system?
A. 4
B. 5
C. 6
D. 7
> **Giải thích:**
> **Đáp án đúng là B.** Chuyển số 20 (hệ 10) sang hệ nhị phân:
> 20 = 16 + 4 = 2⁴ + 2².
> Vậy số 20 trong hệ nhị phân là `10100₂`. Số này cần 5 bit.

---

## Câu 30:
In two's complement representation with a 4-bit allocation, we get \_\_\_\_\_\_ when we add 5 to 5.
A. -5
B. -6
C. -7
D. 10
> **Giải thích:**
> **Đáp án đúng là B.**
> 1.  Biểu diễn số 5 trong hệ nhị phân 4-bit: `0101`.
> 2.  Thực hiện phép cộng: `0101 + 0101 = 1010`.
> 3.  Kết quả `1010` trong biểu diễn bù hai 4-bit là một số âm (vì bit đầu tiên là 1). Để tìm giá trị thập phân, ta lấy bù hai của nó:
>     *   Đảo bit: `0101`.
>     *   Cộng 1: `0101 + 1 = 0110`.
>     *   `0110` là 6. Vì vậy, `1010` biểu diễn cho -6.

---

## Câu 31:
In two's complement representation with a 4-bit allocation, what do we get when we subtract 7 from -6?
A. 6
B. -6
C. 7
D. -7
> **Giải thích:**
> **Đáp án đúng là D (dựa trên một số quy ước, dù phép tính gây tràn số).**
> Phép tính là `(-6) - 7`, tương đương với `(-6) + (-7)`.
> *   -6 trong bù hai 4-bit là `1010`.
> *   -7 trong bù hai 4-bit là `1001`.
> *   Cộng chúng lại: `1010 + 1001 = 10011`.
> Vì chỉ có 4 bit, bit thứ 5 (tràn ra) bị loại bỏ, kết quả là `0011`, tương đương với số `+3`. Tuy nhiên, phép cộng này đã gây ra tràn số (overflow) vì cộng hai số âm lại ra một số dương, điều này không hợp lệ. Dải biểu diễn của bù hai 4-bit là từ -8 đến +7. Giá trị `-13` nằm ngoài dải này. Nếu xét theo logic của đề, có thể có lỗi trong câu hỏi hoặc đáp án.

---

## Câu 32:
Assume a memory location that can only hold four bits. What is the result, if we have stored the integer 11 and then try to add 9 to the unsigned integer?
A. 4
B. 9
C. 11
D. 20
> **Giải thích:**
> **Đáp án đúng là A.**
> 1.  Số 11 (hệ 10) trong hệ nhị phân là `1011`.
> 2.  Số 9 (hệ 10) trong hệ nhị phân là `1001`.
> 3.  Thực hiện phép cộng: `1011 + 1001 = 10100`.
> 4.  Vì vị trí bộ nhớ chỉ có thể chứa 4 bit, bit thứ 5 (tràn ra) sẽ bị loại bỏ. Kết quả còn lại là `0100`.
> 5.  `0100` trong hệ nhị phân tương đương với 4 trong hệ thập phân.

---

## Câu 33:
If a new Excess system uses 11 bits to represent the exponent section. What is the bias value in this system?
A. 1023
B. 1024
C. 65535
D. 65536
> **Giải thích:**
> **Đáp án đúng là A (giả sử A là 1023).**
> Giá trị bias trong hệ thống Excess-K được tính bằng công thức: Bias = 2⁽ⁿ⁻¹⁾ - 1, trong đó n là số bit.
> Với n = 11, ta có: Bias = 2⁽¹¹⁻¹⁾ - 1 = 2¹⁰ - 1 = 1024 - 1 = 1023.
> *Lưu ý: Các lựa chọn trong câu hỏi gốc có thể không chính xác. 1023 là câu trả lời đúng.*

---

## Câu 34:
Which 32-bit microprocessor is used in IBM's PS/2 model-80 computer?
A. 8088
B. 80286
C. 80386
D. 80486
E. None of the others
> **Giải thích:**
> **Đáp án đúng là C.** Máy tính IBM Personal System/2 (PS/2) Model 80 được ra mắt vào năm 1987 và sử dụng bộ vi xử lý Intel 80386 32-bit.

---

## Câu 35:
In storing audio, how many samples per second is good enough to reproduce an audio signal for human hearing?
A. 10,000
B. 20,000
C. 30,000
D. 40,000
> **Giải thích:**
> **Đáp án đúng là D.** Theo định lý lấy mẫu Nyquist-Shannon, tần số lấy mẫu phải lớn hơn gấp đôi tần số cao nhất của tín hiệu. Tai người có thể nghe được âm thanh có tần số lên đến khoảng 20,000 Hz. Do đó, tần số lấy mẫu phải ít nhất là 2 × 20,000 = 40,000 mẫu/giây (samples/sec) để tái tạo lại tín hiệu âm thanh một cách trung thực.

---

## Câu 36:
Conversion of binary number 1010101000010111 to hexadecimal number is \_\_\_\_\_\_.
A. D8F9
B. A8B9
C. AA17
D. D9F8
E. None of the others
> **Giải thích:**
> **Đáp án đúng là C.**
> 1.  Nhóm chuỗi nhị phân thành các nhóm 4 bit từ phải sang trái: `1010 1010 0001 0111`.
> 2.  Chuyển đổi từng nhóm sang số thập lục phân tương ứng:
>     *   `1010` = A
>     *   `1010` = A
>     *   `0001` = 1
>     *   `0111` = 7
> 3.  Kết quả là `AA17`.

---

## Câu 37:
Which of the following is equivalent to 12 in decimal?
A. (1110)₂
B. (C)₁₆
C. (15)₈
D. None of the others
> **Giải thích:**
> **Đáp án đúng là B.**
> *   A. (1110)₂ = 8 + 4 + 2 = 14
> *   B. (C)₁₆ = 12
> *   C. (15)₈ = 1*8¹ + 5*8⁰ = 8 + 5 = 13

---

## Câu 38:
Which of the following representations is erroneous?
A. (111)₂
B. (346)₈
C. (EEG)₁₆
D. 221
> **Giải thích:**
> **Đáp án đúng là C.**
> *   Hệ nhị phân (cơ số 2) chỉ dùng 0, 1. (111)₂ hợp lệ.
> *   Hệ bát phân (cơ số 8) dùng 0-7. (346)₈ hợp lệ.
> *   Hệ thập lục phân (cơ số 16) dùng 0-9 và A-F. Ký tự 'G' không hợp lệ. (EEG)₁₆ là sai.
> *   221 (mặc định là hệ thập phân) hợp lệ.

---

## Câu 39:
Which of the following representations is erroneous?
A. (110)₂
B. (141)₈
C. (EF)₁₆
D. 22A
> **Giải thích:**
> **Đáp án đúng là D.** Một số không có chỉ số cơ số thường được ngầm định là hệ thập phân (cơ số 10). Hệ thập phân không sử dụng ký tự 'A'. Do đó, `22A` là một biểu diễn sai nếu không có chỉ định cơ số rõ ràng (như 16).

---

## Câu 40:
If we call the bit depth or number of bits per sample B, the number of samples per second S, so how to calculate BIT RATE (R)?
A. B x 2S
B. 2B x S
C. B x S
D. B² x S²
> **Giải thích:**
> **Đáp án đúng là C.** Tốc độ bit (Bit Rate) được tính bằng cách nhân số bit trên mỗi mẫu (bit depth - B) với số mẫu trên mỗi giây (sampling rate - S). Công thức là `R = B × S`.

---

## Câu 41:
The ASCII code for the character J is:
A. 1001 0001
B. 1001 1010
C. 0100 1010
D. 1010 0001
E. None of the others
> **Giải thích:**
> **Đáp án đúng là C.** Trong bảng mã ASCII, ký tự 'J' hoa có giá trị thập phân là 74. Chuyển 74 sang nhị phân 8-bit ta được:
> 74 = 64 + 8 + 2 = 2⁶ + 2³ + 2¹ = `01001010`.

---

## Câu 42:
Use an arithmetic right shift operation on the bit pattern 1001 1000.
A. 0100 1100
B. 1100 1100
C. 1101 1001
D. 1001 1000
> **Giải thích:**
> **Đáp án đúng là B.** Phép dịch phải số học (arithmetic right shift) dịch chuyển tất cả các bit sang phải một vị trí. Bit ngoài cùng bên trái (bit dấu) được sao chép và điền vào vị trí trống bên trái.
> *   Mẫu ban đầu: `1001 1000`
> *   Dịch phải: `_100 1100`
> *   Bit dấu là `1`, nên điền `1` vào vị trí trống: `1100 1100`.

---

## Câu 43:
Use a simple right shift operation on the bit pattern 1001 1000.
A. 1001 1001
B. 1001 1000
C. 0100 1101
D. 0100 1100
> **Giải thích:**
> **Đáp án đúng là D.** Phép dịch phải đơn giản (còn gọi là dịch phải logic) dịch chuyển tất cả các bit sang phải một vị trí và luôn điền số 0 vào vị trí trống bên trái.
> *   Mẫu ban đầu: `1001 1000`
> *   Dịch phải: `_100 1100`
> *   Điền `0` vào vị trí trống: `0100 1100`.

---

## Câu 44:
Use a simple left shift operation on the bit pattern 1001 1000.
A. 0001 1001
B. 0001 1010
C. 0011 0000
D. 0011 0001
> **Giải thích:**
> **Đáp án đúng là C.** Phép dịch trái đơn giản (dịch trái logic) dịch chuyển tất cả các bit sang trái một vị trí và luôn điền số 0 vào vị trí trống bên phải.
> *   Mẫu ban đầu: `1001 1000`
> *   Dịch trái: `0011 000_`
> *   Điền `0` vào vị trí trống: `0011 0000`.

---

## Câu 45:
Use a circular right shift operation on the bit pattern 1001 1000.
A. 0100 1100
B. 0011 0001
C. 0100 1100
D. 1001 1000
> **Giải thích:**
> **Đáp án đúng là A (giả sử câu A là 0100 1100).** Phép dịch phải vòng tròn (circular right shift) dịch chuyển các bit sang phải. Bit cuối cùng bên phải được chuyển lên vị trí đầu tiên bên trái.
> *   Mẫu ban đầu: `1001 100`**`0`**
> *   Dịch phải, bit `0` sẽ được chuyển lên đầu: **`0`**`100 1100`.

---

## Câu 46:
Use a circular left shift operation on the bit pattern 1001 1000.
A. 0001 1001
B. 0011 0001
C. 1001 1001
D. 1001 1000
> **Giải thích:**
> **Đáp án đúng là B.** Phép dịch trái vòng tròn (circular left shift) dịch chuyển các bit sang trái. Bit đầu tiên bên trái được chuyển xuống vị trí cuối cùng bên phải.
> *   Mẫu ban đầu: **`1`**`001 1000`
> *   Dịch trái, bit `1` sẽ được chuyển xuống cuối: `001 1000`**`1`**.

---

## Câu 47:
The binary equivalent of the Octal number 13.54 is \_\_\_\_\_\_.
A. 1011.1011
B. 1101.1110
C. 1001.1110
D. None of the others
> **Giải thích:**
> **Đáp án đúng là A.** Ta chuyển từng chữ số bát phân sang nhóm 3 bit nhị phân:
> *   1 = `001`
> *   3 = `011`
> *   5 = `101`
> *   4 = `100`
> Ghép lại ta có: `001 011 . 101 100`. Bỏ các số 0 không cần thiết ở đầu và cuối, ta được `1011.1011`.

---

## Câu 48:
What is the result of storing -25 in an 8-bit memory location using two's complement representation?
A. 00011001
B. 00110010
C. 11100111
D. 11110010
> **Giải thích:**
> **Đáp án đúng là C.**
> 1.  Biểu diễn số dương 25 trong 8-bit: `00011001`.
> 2.  Đảo tất cả các bit (bù một): `11100110`.
> 3.  Cộng thêm 1 để được bù hai: `11100110 + 1 = 11100111`.

---

## Câu 49:
An IPv4 address is a \_\_\_\_\_\_ address that uniquely and universally defines the connection of a host or a router to the Internet.
A. 32-bit
B. 64-bit
C. 128-bit
D. None of others
> **Giải thích:**
> **Đáp án đúng là A.** Địa chỉ IPv4 là một địa chỉ 32-bit. Địa chỉ 128-bit là của IPv6.

---

## Câu 51:
The major design goals of an operating system:
A. Efficient use of hardware and easy use of resources
B. Control subsystems and manage memory
C. Access I/O device and CPU
D. Provide UI
E. Operation on data
F. Text editor
> **Giải thích:**
> **Các đáp án đúng là A, B, C, D.** Các mục tiêu chính của hệ điều hành bao gồm:
> *   Sử dụng phần cứng hiệu quả và quản lý tài nguyên dễ dàng (A).
> *   Điều khiển các hệ thống con và quản lý bộ nhớ (B).
> *   Cung cấp quyền truy cập vào thiết bị I/O và CPU (C).
> *   Cung cấp giao diện người dùng (UI) (D).
> Các mục E và F là chức năng của ứng dụng chứ không phải mục tiêu cốt lõi của HĐH.

---

## Câu 53:
Defining the users, requirements, and methods is part of the \_\_\_\_\_\_ phase.
A. Analysis
B. Design
C. Implementation
D. Testing
> **Giải thích:**
> **Đáp án đúng là A.** Giai đoạn Phân tích (Analysis) trong quy trình phát triển hệ thống là giai đoạn thu thập thông tin, xác định người dùng, yêu cầu của họ và các phương pháp cần thiết để giải quyết vấn đề.

---

## Câu 54:
In the system development process, structure charts are tools used in the \_\_\_\_\_\_ phase.
A. Analysis
B. Design
C. Implementation
D. Testing
> **Giải thích:**
> **Đáp án đúng là B.** Sơ đồ cấu trúc (Structure charts) là công cụ được sử dụng trong giai đoạn Thiết kế (Design) để mô tả cấu trúc phân cấp của một hệ thống, bao gồm các module và mối quan hệ giữa chúng.

---

## Câu 55:
In the \_\_\_\_\_\_ the project team needs to choose a language or a set of languages.
A. Analysis phase
B. Design phase
C. Implementation phase
D. Testing phase
> **Giải thích:**
> **Đáp án đúng là C.** Giai đoạn Thực thi (Implementation) là giai đoạn mà mã nguồn thực tế được viết. Việc lựa chọn ngôn ngữ lập trình cụ thể là một phần quan trọng của giai đoạn này, dựa trên các quyết định đã đưa ra trong giai đoạn thiết kế.

---

## Câu 56:
\_\_\_\_\_\_ is an English-language-like representation of code.
A. A UML diagram
B. A program
C. Pseudocode
D. An algorithm
> **Giải thích:**
> **Đáp án đúng là C.** Mã giả (Pseudocode) là một cách mô tả thuật toán bằng ngôn ngữ tự nhiên, giống tiếng Anh, giúp lập trình viên dễ dàng hiểu và chuyển đổi thành mã nguồn thực tế.

---

## Câu 57:
A step-by-step solution to a problem is called \_\_\_\_\_\_.
A. Hardware
B. An operating system
C. A computer language
D. An algorithm
> **Giải thích:**
> **Đáp án đúng là D.** Thuật toán (Algorithm) được định nghĩa là một tập hợp hữu hạn các hướng dẫn hoặc quy tắc được xác định rõ ràng, từng bước một, để giải quyết một vấn đề hoặc thực hiện một nhiệm vụ.

---

## Câu 58:
\_\_\_\_\_\_ is a step-by-step method for solving a problem or doing a task.
A. A construct
B. A recursion
C. An iteration
D. An algorithm
> **Giải thích:**
> **Đáp án đúng là D.** Đây là một định nghĩa khác của Thuật toán (Algorithm).

---

## Câu 59:
The \_\_\_\_\_\_ scheduler creates a process from a job and changes a process back to a job.
A. Job
B. Process
C. Virtual
D. Queue
> **Giải thích:**
> **Đáp án đúng là A.** Bộ lập lịch công việc (Job scheduler), hay còn gọi là bộ lập lịch dài hạn, chịu trách nhiệm chọn các công việc từ hàng đợi và nạp chúng vào bộ nhớ để tạo thành các tiến trình (processes).

---

## Câu 60:
\_\_\_\_\_\_ is a program in execution. It is a program that has started but has not finished.
A. Program
B. Job
C. Process
D. Task
> **Giải thích:**
> **Đáp án đúng là C.** Một tiến trình (Process) được định nghĩa là một chương trình đang được thực thi.

---

## Câu 61:
A \_\_\_\_\_\_ analyzer reads the source code symbol by symbol and creates a list of tokens in the source language.
A. Lexical
B. Syntax
C. Semantic
D. Code generation
> **Giải thích:**
> **Đáp án đúng là A.** Bộ phân tích từ vựng (Lexical Analyzer) là giai đoạn đầu tiên của trình biên dịch, có nhiệm vụ đọc mã nguồn và nhóm các ký tự thành các đơn vị cú pháp gọi là tokens (ví dụ: từ khóa, định danh, toán tử).

---

## Câu 62:
\_\_\_\_\_\_ analyzer checks the sentences created by the syntax analyzer to be sure that they contain no ambiguity.
A. Lexical
B. Syntax
C. Semantic
D. Code generation
> **Giải thích:**
> **Đáp án đúng là C.** Bộ phân tích ngữ nghĩa (Semantic Analyzer) kiểm tra cây cú pháp để đảm bảo rằng các câu lệnh có ý nghĩa và không có sự mơ hồ, ví dụ như kiểm tra kiểu dữ liệu của biến, phạm vi của biến...

---

## Câu 63:
In the sequential file we process the records one by one. After the operating system processes the last record \_\_\_\_\_\_ is detected and the loop is exited.
A. Hashed file
B. Sequential file
C. EOF
D. None of others
> **Giải thích:**
> **Đáp án đúng là C.** EOF (End-of-File) là một ký hiệu hoặc tín hiệu mà hệ điều hành sử dụng để chỉ ra rằng đã đọc đến cuối cùng của một tệp.

---

## Câu 64:
A \_\_\_\_\_\_ contains data that is meaningful only if it is properly interpreted by a program.
A. Text file
B. Binary file
C. Sequential file
D. EOF
> **Giải thích:**
> **Đáp án đúng là B.** Tệp nhị phân (Binary file) chứa dữ liệu ở định dạng mà máy tính có thể đọc trực tiếp. Con người không thể đọc trực tiếp nội dung của nó mà cần một chương trình cụ thể để diễn giải và hiển thị dữ liệu một cách có ý nghĩa.

---

## Câu 65:
If personal information about each employee in a company is stored in a file we can use \_\_\_\_\_\_ access to retrieve each record at the end of the month to print the paychecks.
A. Hashed file
B. Sequential file
C. EOF
D. Index file
> **Giải thích:**
> **Đáp án đúng là B.** Truy cập tuần tự (Sequential access) là phương pháp phù hợp khi bạn cần xử lý tất cả các bản ghi trong một tệp theo thứ tự từ đầu đến cuối, chẳng hạn như việc in bảng lương cho tất cả nhân viên.

---

## Câu 66:
\_\_\_\_\_\_ is an attack that reduce the capability of a computer system to function correctly or bring the system down altogether by exhausting its resources.
A. DoS
B. Trojan horses
C. Worms
D. Viruses
> **Giải thích:**
> **Đáp án đúng là A.** Tấn công từ chối dịch vụ (Denial of Service - DoS) có mục tiêu làm cho một hệ thống máy tính không thể sử dụng được bằng cách làm cạn kiệt tài nguyên của nó, chẳng hạn như băng thông mạng hoặc sức mạnh xử lý của CPU.

---

## Câu 67:
\_\_\_\_\_\_ is an independent program which can copy itself and which travels through the network. It tries to find weaknesses in the system to inflict harm.
A. DoS
B. Trojan horses
C. Worms
D. Viruses
> **Giải thích:**
> **Đáp án đúng là C.** Sâu máy tính (Worm) là một chương trình độc hại độc lập, có khả năng tự nhân bản và lây lan qua mạng máy tính mà không cần sự can thiệp của người dùng.

---

## Câu 68:
\_\_\_\_\_\_ are unwanted programs that are hidden within other programs (host). When the user executes the host program, the unwanted program also runs.
A. DoS
B. Trojan horses
C. Worms
D. Viruses
> **Giải thích:**
> **Đáp án đúng là B (Trojan horses) hoặc D (Viruses) tùy vào định nghĩa.**
> *   **Virus:** Gắn chính nó vào một chương trình chủ và được kích hoạt khi chương trình chủ chạy.
> *   **Trojan Horse:** Ngụy trang thành một chương trình hợp pháp, nhưng thực hiện các hành động độc hại khi được chạy.
> Dựa trên mô tả "hidden within other programs", cả hai đều có thể phù hợp, nhưng **Virus** thường là câu trả lời chính xác hơn cho việc "ẩn mình" và chạy cùng chương trình chủ.

---

## Câu 69:
These are the "bad guys". They are the types of hackers who break into computer networks with purely negative motives such as monetary gain or reputation.
A. Black Hat Hacker
B. Grey Hat Hacker
C. Red Hat Hacker
D. Blue Hat Hacker
> **Giải thích:**
> **Đáp án đúng là A.** Hacker Mũ Đen (Black Hat Hacker) là những người xâm nhập hệ thống máy tính một cách bất hợp pháp với mục đích xấu như trộm cắp dữ liệu, phá hoại, hoặc kiếm lợi tài chính.

---

## Câu 70:
\_\_\_\_\_\_ who create algorithms to break existing internet networks so as to solve the loopholes in them.
A. Black Hat Hacker
B. Grey Hat Hacker
C. White Hat Hacker
D. Blue Hat Hacker
> **Giải thích:**
> **Đáp án đúng là C.** Hacker Mũ Trắng (White Hat Hacker), hay còn gọi là chuyên gia bảo mật, là những người được ủy quyền để cố gắng xâm nhập vào hệ thống nhằm tìm ra các lỗ hổng bảo mật và khắc phục chúng.

---

## Câu 71:
\_\_\_\_\_\_ is the amateur. Usually their techniques are deployed out of ill motives such as revenge attacks.
A. Black Hat Hacker
B. Grey Hat Hacker
C. Red Hat Hacker
D. Blue Hat Hacker
> **Giải thích:**
> **Đáp án đúng là D.** Hacker Mũ Xanh (Blue Hat Hacker), trong một số ngữ cảnh, dùng để chỉ những người mới vào nghề, thường hành động vì mục đích trả thù hoặc phá hoại mà không có kỹ năng cao. Thuật ngữ này cũng có thể chỉ các chuyên gia bảo mật bên ngoài được thuê để kiểm tra lỗi hệ thống trước khi ra mắt.

---

## Câu 72:
\_\_\_\_ who exploit the internet systems only to make public certain vast datasets of information that would be of benefit to everyone.
A. Black Hat Hacker
B. Grey Hat Hacker
C. Red Hat Hacker
D. Blue Hat Hacker
> **Giải thích:**
> **Đáp án đúng là B.** Hacker Mũ Xám (Grey Hat Hacker) hoạt động ở ranh giới giữa mũ trắng và mũ đen. Họ có thể xâm nhập hệ thống mà không được phép, nhưng mục đích của họ có thể là để thông báo cho quản trị viên về lỗ hổng hoặc công khai thông tin mà họ tin là có lợi cho cộng đồng.

---

## Câu 73:
In storing images, the samples are called \_\_\_\_\_\_ (which stands for picture elements).
A. Bit map
B. Pixels
C. Resolution
D. Color depth
E. None of others
> **Giải thích:**
> **Đáp án đúng là B.** Pixel, viết tắt của "picture element" (phần tử ảnh), là đơn vị cơ bản nhất tạo nên một hình ảnh kỹ thuật số.

---

## Câu 74:
The scanning rate in image processing is called \_\_\_\_\_\_. If it is sufficiently high, the human eye cannot recognize the discontinuity in reproduced images.
A. Bit map
B. Pixels
C. Resolution
D. Color depth
E. None of others
> **Giải thích:**
> **Đáp án đúng là C.** Độ phân giải (Resolution) của một hình ảnh đề cập đến số lượng pixel trên mỗi đơn vị diện tích (ví dụ: pixels per inch - PPI). Độ phân giải càng cao, hình ảnh càng chi tiết và mượt mà.

---

## Câu 75:
In physical layer, an \_\_\_\_\_\_ has infinitely many levels of intensity over a period of time.
A. Analog signal
B. Electromagnetic signal
C. Digital signal
D. Electronic signal
> **Giải thích:**
> **Đáp án đúng là A.** Tín hiệu tương tự (Analog signal) là một tín hiệu liên tục có thể nhận vô số giá trị cường độ trong một khoảng thời gian.

---

## Câu 76:
In physical layer, a \_\_\_\_\_\_, can have only a limited number of defined values. Although each value can be any number, it is often as simple as 1 and 0.
A. Analog signal
B. Electromagnetic signal
C. Digital signal
D. Electronic signal
> **Giải thích:**
> **Đáp án đúng là C.** Tín hiệu số (Digital signal) là một tín hiệu không liên tục, chỉ có một số lượng hữu hạn các giá trị xác định, thường là 0 và 1.

---

## Câu 77:
The \_\_\_\_\_\_ construct uses a set of actions one after another.
A. Sequence
B. Decision
C. Repetition
D. Flow
> **Giải thích:**
> **Đáp án đúng là A.** Cấu trúc Tuần tự (Sequence) là cấu trúc điều khiển cơ bản nhất, trong đó các lệnh được thực thi lần lượt, từ trên xuống dưới, không có sự rẽ nhánh hay lặp lại.

---

## Câu 78:
The \_\_\_\_\_\_ construct tests a condition.
A. Sequence
B. Decision
C. Repetition
D. Flow
> **Giải thích:**
> **Đáp án đúng là B.** Cấu trúc Quyết định (Decision) hay rẽ nhánh (ví dụ: if-else) cho phép chương trình kiểm tra một điều kiện và thực hiện các hành động khác nhau dựa trên kết quả của điều kiện đó.

---

## Câu 79:
The program in a high-level language is called the \_\_\_\_\_\_.
A. Programming language
B. Source program
C. Translation
D. Interpretation
> **Giải thích:**
> **Đáp án đúng là B.** Chương trình được viết bằng ngôn ngữ lập trình bậc cao được gọi là chương trình nguồn (Source program) hay mã nguồn (source code).

---

## Câu 80:
\_\_\_\_\_\_ refers to the process of translating each line of the source program into the corresponding line of the object program and executing the line.
A. Object program
B. Source program
C. Translation
D. Interpretation
> **Giải thích:**
> **Đáp án đúng là D.** Thông dịch (Interpretation) là quá trình dịch và thực thi chương trình theo từng dòng một. Trình thông dịch đọc một dòng mã nguồn, dịch nó sang mã máy và thực thi ngay lập tức trước khi chuyển sang dòng tiếp theo.

---

## Câu 81:
Prolog is an example of a(n) \_\_\_\_\_\_ language.
A. Procedural
B. Functional
C. Declarative
D. Object-oriented
> **Giải thích:**
> **Đáp án đúng là C.** Prolog là một ngôn ngữ lập trình logic, thuộc nhóm lập trình khai báo (Declarative). Thay vì chỉ ra *cách* giải quyết vấn đề, bạn mô tả các sự thật và quy tắc, và hệ thống sẽ suy luận để tìm ra câu trả lời.

---

## Câu 82:
Pascal is a(n) \_\_\_\_\_\_ language.
A. Procedural
B. Functional
C. Declarative
D. Object-oriented
> **Giải thích:**
> **Đáp án đúng là A.** Pascal là một ngôn ngữ lập trình mệnh lệnh và thủ tục (Procedural), nơi chương trình được cấu trúc xung quanh các thủ tục hoặc hàm.

---

## Câu 83:
In a three-level DBMS architecture, the layer that interacts directly with the hardware is the \_\_\_\_\_\_ level.
A. External
B. Conceptual
C. Internal
D. Physical
> **Giải thích:**
> **Đáp án đúng là C.** Mức Trong (Internal level), hay còn gọi là mức vật lý, mô tả cách dữ liệu thực sự được lưu trữ trên các thiết bị phần cứng. Nó tương tác trực tiếp với hệ điều hành và phần cứng.

---

## Câu 84:
In a three-level DBMS architecture, the \_\_\_\_\_\_ level interacts directly with the users.
A. External
B. Conceptual
C. Internal
D. Physical
> **Giải thích:**
> **Đáp án đúng là A.** Mức Ngoài (External level), hay còn gọi là mức khung nhìn (view level), định nghĩa cách người dùng cá nhân hoặc nhóm người dùng nhìn thấy dữ liệu. Đây là mức tương tác trực tiếp với người dùng cuối hoặc ứng dụng.

---

## Câu 85:
The \_\_\_\_\_\_ level of a three-level DBMS architecture defines the logical view of the data.
A. External
B. Conceptual
C. Internal
D. Physical
> **Giải thích:**
> **Đáp án đúng là B.** Mức Quan niệm (Conceptual level), hay còn gọi là mức logic, mô tả cấu trúc logic tổng thể của toàn bộ cơ sở dữ liệu, bao gồm các thực thể, thuộc tính và mối quan hệ giữa chúng, độc lập với cách lưu trữ vật lý.

---

## Câu 86:
Each row in a relation is called \_\_\_\_\_\_.
A. An attribute
B. A tuple
C. A union
D. An attitude
> **Giải thích:**
> **Đáp án đúng là B.** Trong mô hình dữ liệu quan hệ, một bảng được gọi là một quan hệ (relation), một cột được gọi là một thuộc tính (attribute), và một hàng được gọi là một bộ (tuple).

---

## Câu 87:
Each column in a relation is called \_\_\_\_\_\_.
A. An attribute
B. A tuple
C. A union
D. An attitude
> **Giải thích:**
> **Đáp án đúng là A.** Trong mô hình dữ liệu quan hệ, một cột của một bảng (relation) được gọi là một thuộc tính (attribute).

---

## Câu 88:
\_\_\_\_\_\_ between modules in a software system must be maximized.
A. Coupling
B. Cohesion
C. Neither coupling nor cohesion
D. Both coupling and cohesion
> **Giải thích:**
> **Đáp án đúng là B.** Tính gắn kết (Cohesion) đo lường mức độ liên quan và tập trung của các thành phần bên trong một module. Cohesion cao là một đặc điểm thiết kế tốt, có nghĩa là module đó thực hiện một nhiệm vụ duy nhất và rõ ràng.

---

## Câu 89:
\_\_\_\_\_\_ between modules in a software system must be minimized.
A. Coupling
B. Cohesion
C. Neither coupling nor cohesion
D. Both coupling and cohesion
> **Giải thích:**
> **Đáp án đúng là A.** Tính liên kết (Coupling) đo lường mức độ phụ thuộc giữa các module khác nhau. Coupling thấp là một đặc điểm thiết kế tốt, giúp hệ thống dễ bảo trì và sửa đổi hơn vì thay đổi ở một module ít ảnh hưởng đến các module khác.

---

## Câu 90:
\_\_\_\_\_\_ cryptography is often used for short messages, such as encrypting a session key.
A. Symmetric-key
B. Asymmetric-key
C. Secret-key
D. Open-key
> **Giải thích:**
> **Đáp án đúng là B.** Mật mã hóa bất đối xứng (Asymmetric-key), hay mật mã hóa khóa công khai, thường chậm hơn so với mật mã hóa đối xứng. Do đó, nó thường được sử dụng để mã hóa các thông điệp ngắn và quan trọng như khóa phiên (session key) hoặc chữ ký số, thay vì mã hóa toàn bộ dữ liệu lớn.

---

## Câu 91:
\_\_\_\_\_\_ ciphers are sometimes called public-key ciphers.
A. Symmetric-key
B. Asymmetric-key
C. Public-key
D. Private-key
> **Giải thích:**
> **Đáp án đúng là B.** Mật mã hóa khóa bất đối xứng (Asymmetric-key) là tên gọi kỹ thuật của hệ thống mật mã sử dụng một cặp khóa: một khóa công khai (public key) để mã hóa và một khóa riêng tư (private key) để giải mã. Do đó, nó còn được gọi phổ biến là mật mã hóa khóa công khai (public-key cryptography).

---

## Câu 92:
The ethical principle that dictates that an act is ethical when a majority of people in society agrees with it is referred to as \_\_\_\_\_\_.
A. Moral rules
B. Utilitarianism
C. Social contract
D. None of the others
> **Giải thích:**
> **Đáp án đúng là C.** Nguyên tắc Khế ước xã hội (Social contract) cho rằng các hành động đạo đức là những hành động tuân theo các quy tắc mà những người có lý trí trong xã hội sẽ đồng ý tuân theo vì lợi ích chung.

---

## Câu 93:
The ethical principle that dictates that a decision should be made according to the universally accepted principles of morality is referred to as \_\_\_\_\_\_.
A. Moral rules
B. Utilitarianism
C. Social contract
D. None of the others
> **Giải thích:**
> **Đáp án đúng là A.** Các quy tắc đạo đức (Moral rules) hoặc chủ nghĩa nghĩa vụ (Deontology) nhấn mạnh rằng một số hành động là đúng hoặc sai về bản chất, dựa trên các quy tắc hoặc nguyên tắc đạo đức phổ quát, bất kể hậu quả của chúng.

---

## Câu 94:
In the \_\_\_\_\_\_, we can think of a program as an active agent that manipulates passive objects.
A. Procedural paradigm
B. Functional paradigm
C. Declarative paradigm
D. Object-oriented paradigm
> **Giải thích:**
> **Đáp án đúng là A.** Trong mô hình lập trình thủ tục (Procedural paradigm), chương trình được xem như một tác nhân chủ động (một chuỗi các lệnh) thao tác trên các đối tượng dữ liệu bị động. Dữ liệu và các thủ tục xử lý nó thường được tách biệt.

---

## Câu 95:
\_\_\_\_\_\_ uses the principle of logical reasoning to answer queries. It is based on formal logic defined by Greek mathematicians and later developed into first-order predicate calculus.
A. Procedural paradigm
B. Functional paradigm
C. Declarative paradigm
D. Object-oriented paradigm
> **Giải thích:**
> **Đáp án đúng là C.** Mô hình lập trình khai báo (Declarative paradigm), đặc biệt là lập trình logic (logic programming) như Prolog, hoạt động dựa trên nguyên tắc suy luận logic. Lập trình viên định nghĩa các sự thật và quy tắc, và hệ thống sử dụng logic vị từ bậc nhất để suy ra câu trả lời cho các truy vấn.

---

## Câu 96:
A \_\_\_\_\_\_ is a unit of code consisting of zero or more statements. It is also known as a block. Example: `{ x = 1; y = 20; }`
A. Compound statement
B. Assignment statement
C. Control statement
D. None of others
> **Giải thích:**
> **Đáp án đúng là A.** Một câu lệnh phức hợp (Compound statement) hay khối lệnh (block) là một nhóm gồm không hoặc nhiều câu lệnh được bao bọc bởi một cặp dấu ngoặc (ví dụ `{}` trong C/Java) và được coi như một câu lệnh đơn.

---

## Câu 97:
In the \_\_\_\_\_\_ section, we use the symbols to store a value in a variable, which has already been created in the declaration.
A. Compound statement
B. Assignment statement
C. Control statement
D. None of above
> **Giải thích:**
> **Đáp án đúng là B.** Câu lệnh gán (Assignment statement) được sử dụng để gán một giá trị cho một biến đã được khai báo trước đó.

---

## Câu 98:
Which of the following attacks is threatening confidentiality?
A. Snooping
B. Repudiation
C. Denial of service
D. Modification
> **Giải thích:**
> **Đáp án đúng là A.** Tấn công nghe lén (Snooping) là hành vi truy cập trái phép vào dữ liệu khi nó đang được truyền đi. Điều này vi phạm trực tiếp tính bảo mật (Confidentiality) vì thông tin bị lộ cho các bên không được phép.

---

## Câu 99:
In the attacks that threaten confidentiality, \_\_\_\_\_\_ involves obtaining some other type of information by monitoring online traffic.
A. Snooping
B. Repudiation
C. Denial of service
D. Traffic analysis
> **Giải thích:**
> **Đáp án đúng là D.** Phân tích lưu lượng (Traffic analysis) là một hình thức tấn công bảo mật trong đó kẻ tấn công không cần đọc nội dung của tin nhắn, mà chỉ cần quan sát các mẫu lưu lượng (ai đang liên lạc với ai, khi nào, trong bao lâu) để suy ra thông tin nhạy cảm. Điều này đe dọa tính bảo mật.

---

## Câu 100:
In the attacks that threaten integrity, with \_\_\_\_\_\_ attack the attacker modifies the information to make it beneficial to them.
A. Snooping
B. Modification
C. Denial of service
D. Traffic analysis
> **Giải thích:**
> **Đáp án đúng là B.** Tấn công sửa đổi (Modification) là hành vi thay đổi, chèn, xóa hoặc sắp xếp lại dữ liệu một cách trái phép. Cuộc tấn công này đe dọa trực tiếp đến tính toàn vẹn (Integrity) của dữ liệu.


# References

