
2025-08-06 22:18

Status:

Tags: [[source]]  [[CEA]]
Disable spell check :`teh`
# SOURCE CEA



## I. Thông tin chung & Tài liệu tham khảo

Phần này bao gồm các thông báo và liên kết tài liệu được trích xuất từ các slide đầu.

*   **Nhóm Facebook:** Mọi người nên tham gia nhóm Facebook để cập nhật thông tin và truy cập các đề thi mới (đặc biệt là đề FE SU25 cho các bạn thi lại).
*   **Tài liệu học tập:**
    *   **SRO, PT, EBS:** [Google Drive](https://drive.google.com/drive/folders/1IFDhitt5i2nNgCFL60o_gol33mBLR4E0D?usp=sharing)
    *   **Facebook liên hệ:** [Vũ Hoàng](https://www.facebook.com/vu.hoang.79219/)
*   **Thông tin khóa học (Tham khảo):**
    *   Khóa học **PRO192 - Lập trình hướng đối tượng** có sẵn lộ trình chi tiết tại: [https://4user.net/home/courses](https://4user.net/home/courses)
*   **Lưu ý:** Có các dạng bài tập mới được cập nhật ở cuối tài liệu, các bạn nên xem qua.

---

## II. Kiến thức nền tảng

Đây là phần tổng hợp các khái niệm, công thức và bảng tham chiếu quan trọng.

### 1. Đơn vị lưu trữ dữ liệu

Nắm vững các công thức này để giải bài tập chuyển đổi.

*   1 Kilobyte (KB) = 2¹⁰ Bytes = 1024 Bytes
*   1 Megabyte (MB) = 2¹⁰ KB = 1024 KB
*   1 Megabyte (MB) = 2²⁰ Bytes

**Ví dụ chuyển đổi:**
*   256 MB = 256 × 2²⁰ = 2⁸ × 2²⁰ = 2²⁸ bytes.
*   512 KB = 512 × 2¹⁰ = 2⁹ × 2¹⁰ = 2¹⁹ bytes.

### 2. Logic Gates (Cổng Logic)

Bảng chân lý cho các cổng logic cơ bản.

| A | B | AND (A.B) | OR (A+B) | XOR (A⊕B) | NAND | NOR |
|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 1 | 1 |
| 0 | 1 | 0 | 1 | 1 | 1 | 0 |
| 1 | 0 | 0 | 1 | 1 | 1 | 0 |
| 1 | 1 | 1 | 1 | 0 | 0 | 0 |

---

## III. Ngân hàng câu hỏi trắc nghiệm

### Câu 10
How many bytes of data does each sector in the Winchester hard drive disk have?
A. 128 bytes
B. 256 bytes
C. 512 bytes
D. 1024 bytes
E. 4096 bytes
> **Giải thích:**
> **Đáp án đúng là C.** 512 bytes là kích thước tiêu chuẩn công nghiệp trong nhiều thập kỷ cho mỗi cung từ (sector) của một ổ đĩa cứng (hard drive disk), bao gồm cả kiến trúc Winchester. Các ổ đĩa hiện đại hơn có thể sử dụng các sector 4096 byte (4K), nhưng 512 vẫn là một tiêu chuẩn cơ bản.

### Câu 11
A byte addressable microprocessor has a 24-bit address bus. What is its maximum memory capacity?
A. 4 MegaByte
B. 8 MegaByte
C. 16 MegaByte
D. 32 MegaByte
> **Giải thích:**
> **Đáp án đúng là C.**
> 1.  Với bus địa chỉ 24-bit, số lượng địa chỉ duy nhất có thể đánh là 2²⁴.
> 2.  Vì hệ thống là định vị theo byte (byte addressable), mỗi địa chỉ tương ứng với một byte. Vậy dung lượng tối đa là 2²⁴ bytes.
> 3.  Chuyển đổi sang Megabyte (MB), với 1 MB = 2²⁰ bytes:
>     Dung lượng tối đa = 2²⁴ / 2²⁰ = 2⁽²⁴⁻²⁰⁾ = 2⁴ = 16 MB.

### Câu 12
What is the maximum addressable memory of a 32-bit microprocessor with a 24-bit address bus?
A. 16 GB
B. 16 MB
C. 16 Gbits
D. 16 Mbits
> **Giải thích:**
> **Đáp án đúng là B.** Khả năng định vị bộ nhớ tối đa của một bộ vi xử lý (microprocessor) phụ thuộc hoàn toàn vào độ rộng của bus địa chỉ (address bus), không phụ thuộc vào độ rộng của bus dữ liệu hay kiến trúc (ví dụ: 32-bit). Với bus địa chỉ 24-bit, dung lượng tối đa là 2²⁴ bytes, tương đương 16 MB.

### Câu 13
Consider a 5-drive, 200 GBytes-per-drive RAID array. What is the available data storage capacity for RAID level 5?
A. 200 GBytes
B. 400 GBytes
C. 600 GBytes
D. 800 GBytes
E. None of the mentioned
> **Giải thích:**
> **Đáp án đúng là D.** Trong RAID 5, dữ liệu chẵn lẻ (parity data) được phân bổ trên tất cả các ổ đĩa. Tổng dung lượng của phần dữ liệu chẵn lẻ này tương đương với dung lượng của một ổ đĩa.
> *   Công thức tính dung lượng khả dụng cho RAID 5: `(Số ổ đĩa - 1) × Dung lượng mỗi ổ đĩa`.
> *   Áp dụng: (5 - 1) × 200 GBytes = 4 × 200 GBytes = 800 GBytes.

### Câu 14
Consider a 5-drive, 100 GBytes-per-drive RAID array. What is the available data storage capacity for RAID level 5?
A. 400 GBytes
B. 200 GBytes
C. 300 GBytes
D. 500 GBytes
> **Giải thích:**
> **Đáp án đúng là A.** Áp dụng công thức tương tự câu trên:
> *   Dung lượng khả dụng = (5 - 1) × 100 GBytes = 4 × 100 GBytes = 400 GBytes.

### Câu 15
In the direct mapping method from a 256MB main memory with a 512KB cache, what is the number of bits for the TAG field in the address?
A. 6
B. 7
C. 8
D. 9
> **Giải thích:**
> **Đáp án đúng là D.**
> 1.  **Tổng số bit địa chỉ (Total address bits):** Bộ nhớ chính 256 MB = 2⁸ × 2²⁰ = 2²⁸ bytes. Vậy cần 28 bit để định địa chỉ.
> 2.  Trong ánh xạ trực tiếp (direct mapping), địa chỉ bộ nhớ được chia thành `Tag | Line (Index) | Offset`. Để tìm `Line` và `Offset`, ta cần biết số dòng cache và kích thước khối. Tuy nhiên, nếu theo một cách tiếp cận đơn giản hơn như trong ghi chú, ta có thể tính số bit dành cho việc định vị trong cache.
> 3.  **Số bit liên quan đến Cache (Cache-related bits):** Cache có kích thước 512 KB = 2¹⁹ bytes. Vậy cần 19 bit để định vị một byte trong cache.
> 4.  **Số bit Tag:** Số bit còn lại của địa chỉ bộ nhớ chính sẽ được dùng làm Tag.
>     `TAG bits = Tổng bit địa chỉ - Số bit liên quan đến Cache = 28 - 19 = 9 bits`.

### Câu 16
In error correcting code (single ECC), how many check bits are needed to correct one bit error in 8-bit data?
A. 4
B. 5
C. 6
D. 7
> **Giải thích:**
> **Đáp án đúng là A.** Để tìm số bit kiểm tra (check bits - r) cần thiết cho m bit dữ liệu, ta sử dụng công thức Hamming: `2ʳ ≥ m + r + 1`.
> *   Với `m = 8`, ta cần tìm `r` nhỏ nhất thỏa mãn `2ʳ ≥ 8 + r + 1`, tức là `2ʳ ≥ r + 9`.
> *   Thử các giá trị của `r`:
>     *   Nếu r = 3: 2³ = 8, r + 9 = 12. (8 < 12 -> không thỏa mãn).
>     *   Nếu r = 4: 2⁴ = 16, r + 9 = 13. (16 ≥ 13 -> thỏa mãn).
> *   Vậy cần tối thiểu 4 bit kiểm tra.

### Câu 17
Consider the expression: NOT (1111 1010). What is the result of this expression?
A. 0000 1010
B. 0000 0101
C. 1111 0101
D. 1111 1010
> **Giải thích:**
> **Đáp án đúng là B.** Phép toán NOT đảo ngược từng bit: `1` thành `0` và `0` thành `1`.
> NOT (1111 1010) = 0000 0101.

### Câu 18
Consider the expression: 1000 0000 OR 1111 1010. What is the result of this expression?
A. 1000 0000
B. 1111 1010
C. 1001 1010
D. 1001 0101
> **Giải thích:**
> **Đáp án đúng là B.** Phép toán OR cho kết quả `1` nếu có ít nhất một trong hai bit là `1`.
> ```
>   1000 0000
> OR 1111 1010
> -----------
>   1111 1010
> ```

### Câu 19
Consider the expression: 1000 0000 AND 1111 1010. What is the result of this expression?
A. 1000 0000
B. 1111 0000
C. 1001 1010
D. 1001 0101
> **Giải thích:**
> **Đáp án đúng là A.** Phép toán AND chỉ cho kết quả `1` khi cả hai bit đều là `1`.
> ```
>   1000 0000
> AND 1111 1010
> -----------
>   1000 0000
> ```

### Câu 20
What is the result of 10100101 XOR 11001001?
A. 11101101
B. 10000001
C. 01101100
D. 10101100
> **Giải thích:**
> **Đáp án đúng là C.** Phép toán XOR cho kết quả `1` chỉ khi hai bit khác nhau (`1` và `0`).
> ```
>   1010 0101
> XOR 1100 1001
> -----------
>   0110 1100
> ```

### Câu 21
(R1) = 01110110, (R2) = 11011111, the result of (R1) XOR (R2) is:
A. 11011011
B. 00010110
C. 10101001
D. 11001101
> **Giải thích:**
> **Đáp án đúng là C.**
> ```
>   0111 0110
> XOR 1101 1111
> -----------
>   1010 1001
> ```

### Câu 22
What is the result of a left rotate of 10110101 by 2 bits?
A. 01101011
B. 10101101
C. 01101101
D. 11010110
E. 11010100
> **Giải thích:**
> **Đáp án đúng là D.** Phép xoay trái (left rotate) 2 bit: 2 bit ngoài cùng bên trái (`10`) được dịch chuyển và đưa vào cuối bên phải.
> *   Ban đầu: `10110101`
> *   Dịch trái 2 bit các bit còn lại: `110101__`
> *   Đưa `10` vào cuối: `11010110`

### Câu 23
What is the result of a logical right shift of 10110000 by 2 bits?
A. 00101100
B. 01011000
C. 01001100
D. 00110000
> **Giải thích:**
> **Đáp án đúng là A.** Phép dịch phải logic (logical right shift) 2 bit: các bit dịch sang phải 2 vị trí, và 2 bit `0` được thêm vào đầu bên trái.
> *   Ban đầu: `10110000`
> *   Dịch phải 2 bit: `__101100`
> *   Thêm `00` vào đầu: `00101100`

### Câu 24
What is the output of the Left Shift Operator `<<` on (00011000 << 2)?
A. 01100000
B. 11000000
C. 00000110
D. 00000011
> **Giải thích:**
> **Đáp án đúng là A.** Phép dịch trái logic (logical left shift) 2 bit: các bit dịch sang trái 2 vị trí, và 2 bit `0` được thêm vào cuối bên phải.
> *   Ban đầu: `00011000`
> *   Dịch trái 2 bit: `011000__`
> *   Thêm `00` vào cuối: `01100000`

### Câu 25
Express the integer number +18 (using 8-bits length) in two's complement representation.
A. 00010010
B. 10010010
C. 00001101
D. 10011101
> **Giải thích:**
> **Đáp án đúng là A.** Đối với số dương, biểu diễn bù hai (two's complement) giống hệt với biểu diễn nhị phân thông thường.
> *   Chuyển 18 sang nhị phân: 18 = 16 + 2 = 2⁴ + 2¹ = `10010`.
> *   Biểu diễn trong 8 bit bằng cách thêm các số 0 vào đầu: `00010010`.

### Câu 26
If you have an integer number +18 in sign-magnitude representation, which is 00010010, what is the correct option for -18?
A. 00010010
B. 10010010
C. 11110010
D. 01110010
> **Giải thích:**
> **Đáp án đúng là B.** Trong biểu diễn dấu-lượng (sign-magnitude), bit ngoài cùng bên trái là bit dấu (`0` cho số dương, `1` cho số âm), các bit còn lại biểu diễn độ lớn.
> *   +18 là `0` `0010010`.
> *   Để có -18, ta chỉ cần đổi bit dấu thành `1`: `1` `0010010`.

### Câu 27
Convert 64 from decimal to its binary number equivalent.
A. 1000000
B. 100100
C. 111000
D. 101010
> **Giải thích:**
> **Đáp án đúng là A.**
> 64 = 2⁶. Trong hệ nhị phân, 2ⁿ được biểu diễn bằng số `1` theo sau bởi `n` số `0`.
> Vậy 2⁶ = `1000000`.

### Câu 28
Using Hamming Code with one-error correction to store a 12-bit word in memory, the stored word `111001001101` consists of 8 bits of data and 4 parity check bits. What are the parity bits?
A. 0110
B. 0111
C. 1110
D. 0101
> **Giải thích:**
> **Đáp án đúng là D.**
> Các bit chẵn lẻ (parity bits) nằm ở các vị trí là lũy thừa của 2: 1, 2, 4, 8.
> *   Bit Position: 12 11 10 9 **8** 7 6 5 **4** 3 **2** **1**
> *   Stored Word:  1  1  1  0 **0** 1 0 0 **1** 1 **0** **1**
> Ta chỉ cần đọc các giá trị tại các vị trí bit chẵn lẻ:
> *   P₁ (vị trí 1) = 1
> *   P₂ (vị trí 2) = 0
> *   P₄ (vị trí 4) = 1
> *   P₈ (vị trí 8) = 0
> Sắp xếp theo thứ tự P₈P₄P₂P₁, ta được `0101`.

### Câu 30
For the following Boolean expression: `AB + AB'` and the truth table, choose the correct option to replace `?`.
| A | B | B' | output |
|---|---|---|---|
| 1 | 1 | 0 | ? |
| 1 | 0 | 1 | ? |
| 0 | 1 | 0 | ? |
| 0 | 0 | 1 | ? |
A. 1, 1, 0, 0
B. 1, 1, 1, 1
C. 1, 0, 1, 0
D. 0, 1, 1, 0
> **Giải thích:**
> **Đáp án đúng là A.**
> Ta có thể rút gọn biểu thức: `AB + AB' = A(B + B')`. Vì `B + B'` luôn bằng `1`, nên biểu thức rút gọn thành `A`.
> Do đó, cột `output` sẽ giống hệt cột `A`.
> *   Khi A=1, B=1 -> output = 1
> *   Khi A=1, B=0 -> output = 1
> *   Khi A=0, B=1 -> output = 0
> *   Khi A=0, B=0 -> output = 0
> Thứ tự từ trên xuống dưới là `1, 1, 0, 0`.

### Câu 31
What is the output of a NOT gate when the input is 0?
A. 0
B. 1
C. Undefined
D. 2
> **Giải thích:**
> **Đáp án đúng là B.** Cổng NOT là cổng đảo, nó sẽ cho đầu ra là `1` khi đầu vào là `0`, và ngược lại.

### Câu 32
When both inputs are 0, what is the result of a NOR gate?
A. 0
B. 1
C. 2
D. Undefined
> **Giải thích:**
> **Đáp án đúng là B.** Cổng NOR là cổng OR theo sau bởi cổng NOT.
> *   Khi cả hai đầu vào là 0, cổng OR sẽ cho ra 0.
> *   Cổng NOT sẽ đảo 0 thành 1.
> *   Vậy, đầu ra của NOR là 1.

### Câu 33
When both inputs are 1, what is the result of a NAND gate?
A. 0
B. 1
C. 2
D. Undefined
> **Giải thích:**
> **Đáp án đúng là A.** Cổng NAND là cổng AND theo sau bởi cổng NOT.
> *   Khi cả hai đầu vào là 1, cổng AND sẽ cho ra 1.
> *   Cổng NOT sẽ đảo 1 thành 0.
> *   Vậy, đầu ra của NAND là 0.

### Câu 34
A set-associative cache consists of 64 lines, divided into four-line sets. Main memory contains 2¹⁹ words and 4K blocks of 128 words each. How many bits are there in the tag field of the cache?
A. 5
B. 6
C. 7
D. 8
E. 9
> **Giải thích:**
> **Đáp án đúng là D.**
> 1.  **Tổng bit địa chỉ (Total address bits):** Bộ nhớ chính có 2¹⁹ từ. Vậy cần 19 bit.
> 2.  **Số bit cho Offset (Offset bits):** Mỗi khối có 128 từ = 2⁷ từ. Vậy cần 7 bit cho Offset.
> 3.  **Số bit cho Index (Index bits):** Cache có 64 dòng, chia thành các set 4 dòng. Số set = 64 / 4 = 16 set = 2⁴ set. Vậy cần 4 bit cho Index.
> 4.  **Số bit cho Tag (Tag bits):** `Tag bits = Tổng bit địa chỉ - Index bits - Offset bits = 19 - 4 - 7 = 8 bits`.

### Câu 35
Consider a machine with a byte addressable main memory of 2¹⁶ bytes and block size of 8 bytes. Assume that a direct mapped cache consisting of 32 lines is used with this machine. How many bits are there in the line field of the cache?
A. 3
B. 4
C. 5
D. 6
E. 7
> **Giải thích:**
> **Đáp án đúng là C.** Trường dòng (line field) chính là trường chỉ số (Index field). Số bit của nó được tính bằng logarit cơ số 2 của tổng số dòng trong cache.
> *   `Index bits = log₂(Số dòng cache) = log₂(32) = 5 bits`.

### Câu 36
An instruction has five stages: fetch opcode (4 cycles), fetch operand address (3 cycles), fetch operand (3 cycles), add 1 to operand (3 cycles), and store operand (3 cycles). An interrupt request arrives at the beginning of the "fetch operand" stage. How many cycles pass from the start of the instruction until the processor enters the interrupt processing cycle?
A. 6
B. 7
C. 8
D. 9
E. 10
> **Giải thích:**
> **Đáp án đúng là E.** Câu hỏi này giả định một kiến trúc mà CPU sẽ hoàn thành giai đoạn đang diễn ra trước khi xử lý ngắt, thay vì hoàn thành cả chỉ thị.
> *   Các giai đoạn đã hoàn thành trước khi có yêu cầu ngắt:
>     1.  Fetch opcode: 4 chu kỳ
>     2.  Fetch operand address: 3 chu kỳ
> *   Yêu cầu ngắt đến khi bắt đầu giai đoạn "fetch operand". CPU sẽ hoàn thành nốt giai đoạn này.
>     3.  Fetch operand: 3 chu kỳ
> *   Tổng số chu kỳ đã trôi qua trước khi CPU bắt đầu xử lý ngắt là: `4 + 3 + 3 = 10` chu kỳ.

### Câu 37
In the concept of Register Windows, how many register groups are there?
A. 4
B. 3
C. 2
D. No distinction
> **Giải thích:**
> **Đáp án đúng là A.** Kiến trúc Cửa sổ thanh ghi (Register Windows), ví dụ như trong kiến trúc SPARC, thường chia các thanh ghi thành 4 nhóm chính:
> 1.  **Global Registers:** Thanh ghi toàn cục, được tất cả các hàm thấy.
> 2.  **Input Registers:** Thanh ghi đầu vào, nhận tham số từ hàm gọi.
> 3.  **Local Registers:** Thanh ghi cục bộ, chỉ dùng trong hàm hiện tại.
> 4.  **Output Registers:** Thanh ghi đầu ra, dùng để truyền tham số cho hàm được gọi.

### Câu 38
How many common classifications of parallel systems are there as proposed by Flynn?
A. 2
B. 3
C. 4
D. 5
> **Giải thích:**
> **Đáp án đúng là C.** Phân loại Flynn (Flynn's Taxonomy) đề xuất 4 loại kiến trúc máy tính song song chính:
> 1.  **SISD** (Single Instruction, Single Data)
> 2.  **SIMD** (Single Instruction, Multiple Data)
> 3.  **MISD** (Multiple Instruction, Single Data)
> 4.  **MIMD** (Multiple Instruction, Multiple Data)

### Câu 39
How many general-purpose registers are there in the Microprocessor Register Organizations of Intel 80386-Pentium 4?
A. 8
B. 16
C. 4
D. 12
> **Giải thích:**
> **Đáp án đúng là A.** Trong kiến trúc IA-32 (bắt đầu từ Intel 80386 đến Pentium 4), có 8 thanh ghi đa dụng (general-purpose registers) 32-bit: EAX, EBX, ECX, EDX, EBP, ESP, ESI, và EDI.

### Câu 40
If you have a boolean function with 3 variables, how many rows are there in the truth table?
A. 8 rows
B. 3 rows
C. 6 rows
D. 12 rows
> **Giải thích:**
> **Đáp án đúng là A.** Số hàng trong bảng chân lý (truth table) của một hàm Boole với `n` biến được tính bằng công thức: `Số hàng = 2ⁿ`.
> *   Với n = 3, số hàng = 2³ = 8.

### Câu 41
Follow Amdahl's law for multiprocessors, if 90% of the code is parallelizable (f = 0.9), running the program on a multicore system with 4 processors, the performance gain (speedup factor) would be approximately:
A. 3.07
B. 2.97
C. 3.17
D. 3.27
> **Giải thích:**
> **Đáp án đúng là A (gần đúng).**
> *   Phần song song (parallel portion), `f = 0.9`.
> *   Phần tuần tự (serial portion), `1 - f = 0.1`.
> *   Số bộ xử lý, `n = 4`.
> *   Công thức định luật Amdahl: `Speedup = 1 / [ (1 - f) + (f / n) ]`.
> *   Áp dụng: `Speedup = 1 / [ 0.1 + (0.9 / 4) ] = 1 / [ 0.1 + 0.225 ] = 1 / 0.325 ≈ 3.0769`.
> *   Giá trị này gần nhất với 3.07.

### Câu 42
A benchmark program is running on a 400 MHz processor. The executed program consists of 500 instruction executions, with the following instruction mix and clock cycle count:
| Instruction type | Instruction count | Cycles per Instruction |
|---|---|---|
| Arithmetic | 300 | 1 |
| Data transfer | 100 | 2 |
| Control transfer | 100 | 2 |
Calculate the MIPS rate for this case.
A. 285.7
B. 275.7
C. 265.7
D. 295.7
> **Giải thích:**
> **Đáp án đúng là A.**
> 1.  **Tính tổng số chu kỳ (Total Cycles):**
>     `(300 lệnh × 1 chu kỳ/lệnh) + (100 lệnh × 2 chu kỳ/lệnh) + (100 lệnh × 2 chu kỳ/lệnh) = 300 + 200 + 200 = 700 chu kỳ`.
> 2.  **Tính thời gian thực thi (Execution Time):**
>     `Thời gian = Tổng chu kỳ / Tần số = 700 / (400 × 10⁶ chu kỳ/giây)`.
> 3.  **Tính MIPS (Million Instructions Per Second):**
>     `MIPS = Tổng số lệnh / (Thời gian thực thi × 10⁶) = 500 / [ (700 / (400 × 10⁶)) × 10⁶ ] = 500 / (700 / 400) = 500 / 1.75 = 285.7`.

### Câu 43
In a cache system using the direct mapping technique, with the cache containing 10 lines, which memory block's data can be transferred to cache line 7?
A. 7, 17, 27, 37,...
B. 0, 1, 2, 3, 4, 5, 6, 7,...
C. 0, 7, 17, 27, 37,...
D. 0, 7, 77, 777,...
> **Giải thích:**
> **Đáp án đúng là A.** Trong ánh xạ trực tiếp (direct mapping), một khối bộ nhớ được ánh xạ vào một dòng cache theo công thức: `Dòng Cache = (Địa chỉ khối) mod (Số dòng cache)`.
> *   Ta cần tìm các địa chỉ khối `X` sao cho `X mod 10 = 7`.
> *   Kiểm tra đáp án A:
>     *   7 mod 10 = 7 (Đúng)
>     *   17 mod 10 = 7 (Đúng)
>     *   27 mod 10 = 7 (Đúng)
> *   Các đáp án khác không thỏa mãn quy luật này.

### Câu 45
Regarding the ALU (Arithmetic Logic Unit), besides basic arithmetic operations, what operations can it perform? (choose two correct answers)
A. It handles logical operations such as AND, OR, XOR, NOT.
B. It handles data transfer operations like MOVE, GO, JUMP.
C. It handles decoding operations after an instruction is fetched.
D. It handles bit shifting operations like multiply and divide operations by powers of two.
> **Giải thích:**
> **Đáp án đúng là A và D.**
> Đơn vị Số học và Logic (Arithmetic Logic Unit - ALU) chịu trách nhiệm thực hiện:
> *   Các phép toán số học (cộng, trừ, nhân, chia).
> *   Các phép toán logic (AND, OR, XOR, NOT). (A đúng)
> *   Các phép toán dịch bit (bit shifting), có thể được dùng để nhân/chia cho lũy thừa của 2. (D đúng)
> Các hoạt động chuyển dữ liệu (B) và giải mã lệnh (C) do Đơn vị Điều khiển (Control Unit) quản lý.

### Câu 46
Why is cache design used in high-performance computing (HPC)? (Choose three correct answers)
A. Because there is a significant speed gap between the processor and the internal memory in HPC.
B. Because applications in HPC often require a large bandwidth to support intensive data processing.
C. Because power consumption can be a significant operational cost in HPC environments.
D. Because multiple processors are often working in parallel, caches provide a way to efficiently manage data required by these processors.
> **Giải thích:**
> **Đáp án đúng là A, B, D.**
> *   **A:** Cache giúp bắc cầu qua khoảng cách tốc độ lớn giữa CPU siêu nhanh và bộ nhớ chính chậm hơn, đây là lý do cốt lõi.
> *   **B:** Cache cung cấp băng thông (bandwidth) cực cao cho CPU, đáp ứng nhu cầu xử lý dữ liệu lớn của các ứng dụng HPC.
> *   **D:** Trong hệ thống đa xử lý, cache (đặc biệt là các cơ chế đồng bộ cache) rất quan trọng để quản lý dữ liệu hiệu quả và tránh xung đột.
> *   (C) Mặc dù đúng là tiêu thụ điện năng là một vấn đề trong HPC, nhưng cache không phải lúc nào cũng là giải pháp tiết kiệm điện nhất (SRAM trong cache tốn điện hơn DRAM trong bộ nhớ chính khi ở chế độ chờ). Vai trò chính của nó là tăng hiệu năng.

### Câu 47
In the computer, what categories do external devices include? (choose 3 correct answers)
A. Human readable
B. Communication
C. Data Conversion
D. Machine readable
> **Giải thích:**
> **Đáp án đúng là A, B, D.**
> Các thiết bị ngoại vi (external devices) thường được phân thành ba loại chính:
> 1.  **Có thể đọc bởi người (Human readable):** Dành cho việc giao tiếp với người dùng. Ví dụ: màn hình, bàn phím, máy in.
> 2.  **Có thể đọc bởi máy (Machine readable):** Dành cho việc giao tiếp với các thiết bị điện tử khác. Ví dụ: ổ đĩa cứng, cảm biến.
> 3.  **Giao tiếp (Communication):** Dành cho việc giao tiếp với các thiết bị ở xa. Ví dụ: modem, card mạng.

### Câu 49
\_\_\_\_\_\_ is a set of physical disk drives viewed by the operating system as a single logical drive.
A. CLV
B. SSD
C. RAID
D. CAV
> **Giải thích:**
> **Đáp án đúng là C.** RAID (Redundant Array of Independent Disks) là một công nghệ kết hợp nhiều ổ đĩa vật lý thành một hoặc nhiều đơn vị logic để tăng hiệu suất, độ tin cậy hoặc cả hai.

### Câu 50
In a \_\_\_\_\_\_ processor, there are multiple functional units, each of which is implemented as a pipeline.
A. Scalar
B. Superpipelined
C. Superscalar
D. Vector
> **Giải thích:**
> **Đáp án đúng là C.** Bộ xử lý siêu vô hướng (Superscalar) có khả năng thực thi nhiều hơn một chỉ thị cùng một lúc bằng cách sử dụng nhiều đơn vị chức năng (functional units) song song (ví dụ: nhiều ALU, nhiều FPU).

### Câu 51
\_\_\_\_\_\_ refers to the operational units and their interconnections that realize the architectural specifications.
A. Computer architecture
B. Computer function
C. Computer organization
D. Instruction set architecture
> **Giải thích:**
> **Đáp án đúng là C.** Tổ chức máy tính (Computer organization) liên quan đến việc các thành phần phần cứng được triển khai và kết nối với nhau như thế nào để hiện thực hóa kiến trúc máy tính. Nó trả lời câu hỏi "Làm thế nào?". Trong khi đó, kiến trúc máy tính (computer architecture) trả lời câu hỏi "Cái gì?" (ví dụ: tập lệnh, chế độ địa chỉ).

### Câu 52
\_\_\_\_\_\_ interprets the instructions in memory and causes them to be executed.
A. Registers
B. CPU interconnection
C. Arithmetic and Logic Unit (ALU)
D. I/O Modules
E. Control Unit (CU)
> **Giải thích:**
> **Đáp án đúng là E.** Đơn vị điều khiển (Control Unit - CU) là thành phần của CPU chịu trách nhiệm nạp, giải mã và điều phối việc thực thi các chỉ thị.

### Câu 53
If the operation involves a reference to an operand in memory or available via I/O, then determine the address of the operand. This phase is called \_\_\_\_\_\_.
A. Operand fetch
B. Data operation
C. Operand store
D. Operand address calculation
> **Giải thích:**
> **Đáp án đúng là D.** Tính toán địa chỉ toán hạng (Operand address calculation) là một bước trong chu kỳ lệnh, nơi CPU xác định địa chỉ bộ nhớ hoặc thanh ghi của toán hạng sẽ được sử dụng trong phép toán.

### Câu 54
The \_\_\_\_\_\_ can exchange data directly with the processor. Just as the processor can initiate a read or write with memory, designating the address of a specific location, the processor can also read data from or write data to the \_\_\_\_\_\_.
A. I/O module / Memory
B. Interrupts / I/O module
C. I/O module / Interrupts
D. Interrupts / Interrupts
E. Memory / I/O module
> **Giải thích:**
> **Đáp án đúng là E.** Câu này mô tả hai luồng trao đổi dữ liệu chính của bộ xử lý (processor):
> 1.  Với bộ nhớ (Memory).
> 2.  Với module vào/ra (I/O module).
> Do đó, Memory và I/O module có thể điền vào hai chỗ trống.

### Câu 55
Determine the address of the next instruction to be executed. Usually, this involves adding a fixed number to the address of the previous instruction. This phase is called \_\_\_\_\_\_.
A. Instruction fetch
B. Instruction operation decoding
C. Instruction address calculation
D. Operand fetch
E. Operand address calculation
> **Giải thích:**
> **Đáp án đúng là C.** Tính toán địa chỉ lệnh (Instruction address calculation) là bước xác định địa chỉ của lệnh tiếp theo sẽ được nạp. Thông thường, nó chỉ đơn giản là tăng con trỏ lệnh (program counter).

### Câu 56
\_\_\_\_\_\_ is (are) determined by the number of instructions that can be fetched and executed at the same time and by the speed and sophistication of the mechanisms that the processor uses to find independent instructions.
A. Instruction-level parallelism
B. Machine parallelism
C. Both instruction-level parallelism and machine parallelism
D. None of the mentioned
> **Giải thích:**
> **Đáp án đúng là B.** Song song máy (Machine parallelism) là một thước đo khả năng của bộ xử lý trong việc tận dụng tính song song ở cấp độ lệnh (Instruction-Level Parallelism - ILP). Nó phụ thuộc vào các yếu tố phần cứng như số lượng đường ống (pipelines) và khả năng thực thi ngoài thứ tự.

### Câu 58
Consider the expression: `NOT(A + B) = ?`. Apply DeMorgan's Theorem to find the equivalent expression.
A. NOT A AND NOT B
B. NOT A OR NOT B
C. A OR NOT A AND B
D. A AND NOT B
> **Giải thích:**
> **Đáp án đúng là A.** Định luật De Morgan phát biểu rằng phủ định của một phép OR bằng phép AND của các phủ định.
> `NOT (A OR B)` tương đương với `(NOT A) AND (NOT B)`.

### Câu 59
Consider the expression: `NOT (A OR B)`. Choose the correct expression that is equal to the given expression.
A. A NOR B
B. A NAND B
C. NOT A NOR B
D. NOT A OR B
> **Giải thích:**
> **Đáp án đúng là A.** Cổng NOR (Not OR) được định nghĩa chính xác là phủ định của phép OR. Do đó, `NOT (A OR B)` chính là `A NOR B`.

### Câu 60
Assume that a truth table:
| X | Y | OUTPUT |
|---|---|---|
| 1 | 1 | 1 |
| 1 | 0 | 1 |
| 0 | 1 | 1 |
| 0 | 0 | 0 |
Which basic operator matches the table above?
A. AND
B. OR
C. NAND
D. NOR
> **Giải thích:**
> **Đáp án đúng là B.** Bảng chân lý này cho thấy đầu ra là `1` nếu có ít nhất một trong hai đầu vào là `1`, và chỉ là `0` khi cả hai đầu vào đều là `0`. Đây chính là định nghĩa của phép toán OR.

### Câu 61
The operation \_\_\_\_\_\_ yields true (binary value 1) if and only if both of its operands are true.
A. OR
B. AND
C. XOR
D. NAND
> **Giải thích:**
> **Đáp án đúng là B.** Đây là định nghĩa của phép toán AND logic.

### Câu 62
Which gate can be used to create an inverted output of an input signal in digital logic?
A. NOT gate
B. OR gate
C. AND gate
D. XOR gate
> **Giải thích:**
> **Đáp án đúng là A.** Cổng NOT (còn gọi là bộ đảo - inverter) được thiết kế đặc biệt để tạo ra đầu ra là phủ định (nghịch đảo) của đầu vào.

### Câu 63
The effective address of \_\_\_\_\_\_ is `EA = A + (R)` and then `(R) ← (R) + 1`.
A. relative addressing
B. autoindexing
C. postindexing
D. preindexing
> **Giải thích:**
> **Đáp án đúng là B.** Tự động lập chỉ số (Autoindexing) là một dạng của chế độ địa chỉ chỉ số (indexed addressing), trong đó giá trị của thanh ghi chỉ số được tự động tăng hoặc giảm sau mỗi lần nó được sử dụng để tính toán địa chỉ hiệu dụng (effective address - EA).

### Câu 64
The effective address of Register indirect addressing mode is \_\_\_\_\_\_.
A. EA = R
B. EA = (R)
C. EA = (R) + A
D. EA = (R) + (A)
> **Giải thích:**
> **Đáp án đúng là B.** Trong chế độ địa chỉ gián tiếp qua thanh ghi (Register indirect addressing), lệnh chứa tên một thanh ghi (R). Địa chỉ hiệu dụng (EA) của toán hạng là nội dung được lưu trữ trong thanh ghi đó, ký hiệu là (R).

### Câu 65
Which of the following PDP series computers is known for its use of 12-bit instructions and a single general-purpose register, the accumulator?
A. PDP-8
B. PDP-10
C. PDP-11
D. PDP-6
> **Giải thích:**
> **Đáp án đúng là A.** Máy tính PDP-8 của DEC là một máy tính mini 12-bit rất thành công và có ảnh hưởng, kiến trúc của nó chỉ sử dụng một thanh ghi đa dụng chính là thanh ghi tích lũy (accumulator).

### Câu 66
Which RAID level uses a striping technique with a minimum of 3 disks and provides fault tolerance through the use of a dedicated parity bit disk?
A. RAID 0
B. RAID 1
C. RAID 2
D. RAID 3
> **Giải thích:**
> **Đáp án đúng là D.** RAID 3 sử dụng kỹ thuật xé nhỏ dữ liệu ở mức byte (byte-level striping) trên nhiều ổ đĩa và dành riêng một ổ đĩa để lưu trữ thông tin chẵn lẻ (parity). Nó yêu cầu tối thiểu 3 ổ đĩa (2 cho dữ liệu, 1 cho parity).
> *Lưu ý: RAID 5 cũng yêu cầu tối thiểu 3 đĩa và dùng parity nhưng parity được phân bổ (distributed) thay vì tập trung (dedicated).*

### Câu 67
Which register is the memory address register?
A. MAR
B. MBR
C. IR
D. PC
> **Giải thích:**
> **Đáp án đúng là A.** MAR (Memory Address Register) là thanh ghi chứa địa chỉ của bộ nhớ mà CPU muốn đọc hoặc ghi dữ liệu vào.

### Câu 68
Which register can interact with the secondary storage?
A. MAR and MBR
B. PC
C. IR
D. R0
> **Giải thích:**
> **Đáp án đúng là A (diễn giải).** Mặc dù CPU không tương tác *trực tiếp* với bộ nhớ thứ cấp (secondary storage), quá trình trao đổi dữ liệu giữa bộ nhớ chính và bộ nhớ thứ cấp (thông qua DMA chẳng hạn) vẫn liên quan đến việc xác định địa chỉ bộ nhớ (liên quan đến MAR) và chứa dữ liệu được truyền (liên quan đến MBR - Memory Buffer Register). Trong số các lựa chọn, đây là cặp thanh ghi liên quan nhất.

### Câu 69
For reads from and writes to main memory, the \_\_\_\_\_\_ translates each virtual address into a physical address.
A. MAR
B. MMU
C. Overlays
D. TLB
E. Accumulator
> **Giải thích:**
> **Đáp án đúng là B.** MMU (Memory Management Unit) là một thành phần phần cứng của CPU chịu trách nhiệm dịch địa chỉ ảo (virtual address) do chương trình tạo ra thành địa chỉ vật lý (physical address) trong bộ nhớ chính.

### Câu 70
What are the basic registers that help the CPU establish a connection with an I/O device?
A. I/OAR, I/OBR
B. I/OAR, MAR
C. I/OBR, MBR
D. MAR, MBR
> **Giải thích:**
> **Đáp án đúng là A.** Để giao tiếp với một module I/O, CPU sử dụng một cặp thanh ghi tương tự như với bộ nhớ:
> *   **I/O Address Register (I/OAR):** Chứa địa chỉ của thiết bị I/O cụ thể.
> *   **I/O Buffer Register (I/OBR):** Dùng để trao đổi dữ liệu với thiết bị.

### Câu 71
Consider the expression: `A + (B.C)`. What expression is equal to the given expression?
A. (A + B) . (A + C)
B. (A + B) . C
C. A . (B + C)
D. NOT (A . (B + C))
> **Giải thích:**
> **Đáp án đúng là A.** Đây là luật phân phối (Distributive Law) trong đại số Boole: `X + (Y.Z) = (X + Y).(X + Z)`.
> Áp dụng vào biểu thức, ta có `A + (B.C) = (A + B).(A + C)`.

### Câu 72
In MASM32, which command is incorrect?
A. ADD EAX, a
B. ADD EAX, EBX
C. ADD a, EAX
D. ADD a, b
> **Giải thích:**
> **Đáp án đúng là D.** Trong hợp ngữ x86 (bao gồm MASM32), lệnh `ADD` không thể có cả hai toán hạng đều là địa chỉ bộ nhớ. Ít nhất một trong hai toán hạng phải là một thanh ghi (register). `a` và `b` ở đây được ngầm hiểu là các biến trong bộ nhớ.

### Câu 73
Consider some computer generations and the technologies used. Select the main technology applied in each computer generation (1st, 2nd, 3rd).
A: Vacuum Tubes, B: Transistors, C: Integrated Circuits (IC)
A. 1-A; 2-B; 3-C
B. 1-A; 2-C; 3-B
C. 1-C; 2-B; 3-A
D. 1-B; 2-A; 3-C
> **Giải thích:**
> **Đáp án đúng là A (diễn giải lại từ câu hỏi).**
> *   Thế hệ 1 (First generation): Sử dụng bóng đèn chân không (Vacuum Tubes).
> *   Thế hệ 2 (Second generation): Sử dụng bóng bán dẫn (Transistors).
> *   Thế hệ 3 (Third generation): Sử dụng mạch tích hợp (Integrated Circuits - IC).
> *   Do đó, cặp ghép đúng là: `1-A; 2-B; 3-C`.

### Câu 75
What is the initial state of a process when it is admitted by the high-level scheduler, but not yet ready to execute?
A. New
B. Ready
C. Running
D. Halted
> **Giải thích:**
> **Đáp án đúng là A.** Khi một tiến trình vừa được tạo ra, nó sẽ ở trạng thái Mới (New). Sau đó, bộ lập lịch sẽ quyết định chuyển nó sang trạng thái Sẵn sàng (Ready) khi có đủ tài nguyên.

### Câu 76
What is the most common mapping technique used in cache memory in modern computers?
A. Direct Mapping
B. Fully Associative
C. Set Associative
D. None of the mentioned
> **Giải thích:**
> **Đáp án đúng là C.** Ánh xạ tập hợp liên kết (Set-associative mapping) là kỹ thuật phổ biến nhất trong các máy tính hiện đại. Nó là sự dung hòa giữa sự đơn giản, chi phí thấp của ánh xạ trực tiếp (direct mapping) và sự linh hoạt, hiệu suất cao (nhưng chi phí cao) của ánh xạ liên kết hoàn toàn (fully associative).

### Câu 77
What is the cache memory level that is integrated into the processor chip and has the lowest latency?
A. L1 cache
B. L2 cache
C. L3 cache
D. L4 cache
> **Giải thích:**
> **Đáp án đúng là A.** Cache L1 (Level 1) là bộ nhớ đệm nằm gần nhất với lõi xử lý (core), thường được tích hợp ngay trên chip. Do đó, nó có dung lượng nhỏ nhất, tốc độ nhanh nhất và độ trễ (latency) thấp nhất.

### Câu 78
Which cache is not typically a shared cache?
A. L4 cache
B. L3 cache
C. L2 cache
D. L1 cache
> **Giải thích:**
> **Đáp án đúng là D.** Trong các CPU đa lõi hiện đại, cache L1 thường được dành riêng cho từng lõi xử lý (ví dụ, L1 instruction cache và L1 data cache cho mỗi core). Cache L2 có thể riêng hoặc chung, trong khi cache L3 và L4 (nếu có) hầu như luôn được chia sẻ (shared) cho tất cả các lõi.

### Câu 79
What electronic component is used to govern operations such as fetching, decoding, and executing performed by a processor?
A. A system clock
B. A quartz crystal
C. An analog to digital converter
D. A counter
> **Giải thích:**
> **Đáp án đúng là A.** Đồng hồ hệ thống (system clock) tạo ra các xung tín hiệu đều đặn để đồng bộ hóa tất cả các hoạt động bên trong bộ xử lý, đảm bảo các giai đoạn như nạp, giải mã, thực thi diễn ra theo đúng thứ tự và thời gian.

### Câu 80
What does CISC stand for?
A. Complex Instruction Set Computer
B. Computer Instruction Set Complex
C. Complex Instruction Summarize Computer
D. Computer Instruction Summarize Complex
> **Giải thích:**
> **Đáp án đúng là A.** CISC là viết tắt của Complex Instruction Set Computer, tức là Máy tính có tập lệnh phức tạp.

### Câu 81
Which is the correct choice for the description: "A single machine instruction controls the simultaneous execution of a number of processing elements such as vector and array processors"?
A. Single instruction, single data (SISD)
B. Single instruction, multiple data (SIMD)
C. Multiple instruction, single data (MISD)
D. Multiple instruction, multiple data (MIMD)
> **Giải thích:**
> **Đáp án đúng là B.** Đây là định nghĩa của kiến trúc SIMD (Single Instruction, Multiple Data): một chỉ thị duy nhất được thực thi đồng thời trên nhiều luồng dữ liệu khác nhau.

### Câu 82
Which of the following components does not belong to the central processing unit (CPU)?
A. System interconnection
B. Arithmetic and logic unit
C. Registers
D. Control unit
> **Giải thích:**
> **Đáp án đúng là A.** Đơn vị xử lý trung tâm (CPU) bao gồm ba thành phần chính: Đơn vị Số học & Logic (ALU), Đơn vị Điều khiển (Control Unit), và các Thanh ghi (Registers). Kết nối hệ thống (System interconnection), như system bus, là thành phần kết nối CPU với các bộ phận khác như bộ nhớ chính và module I/O, chứ không phải là một phần của CPU.

### Câu 83
Which of the following memory devices has the lowest access speed?
A. ROM
B. Flash memory
C. Magnetic tape
D. HDD
E. Cache
> **Giải thích:**
> **Đáp án đúng là C.** Băng từ (Magnetic tape) là một thiết bị lưu trữ tuần tự (sequential access), có nghĩa là để đọc dữ liệu ở cuối, phải tua qua toàn bộ băng. Do đó, nó có tốc độ truy cập (access speed) chậm nhất so với các thiết bị truy cập ngẫu nhiên hoặc trực tiếp khác.

### Câu 84
Which of the following components was used in the first ENIAC computer?
A. Bipolar transistors
B. Field transistors
C. Vacuum tubes
D. Semiconductor ICs
> **Giải thích:**
> **Đáp án đúng là C.** ENIAC, một trong những máy tính điện tử đa năng đầu tiên, thuộc thế hệ máy tính thứ nhất và sử dụng bóng đèn chân không (vacuum tubes) làm thành phần chuyển mạch chính.

### Câu 85
Which of the following algorithms is not typically used in cache memory replacement?
A. Least Recently Used (LRU)
B. First-In-First-Out (FIFO)
C. Least Frequently Used (LFU)
D. Round Robin (RR)
> **Giải thích:**
> **Đáp án đúng là D.** Các thuật toán thay thế cache phổ biến bao gồm LRU, FIFO, và LFU. Round Robin (RR) là một thuật toán lập lịch cho tiến trình (process scheduling) của CPU, không phải là một thuật toán thay thế trang/dòng cache điển hình.

### Câu 86
Which of the following components of the CPU is responsible to direct the system to execute instructions?
A. Arithmetic and Logic Unit (ALU)
B. Control Unit (CU)
C. Registers
D. Random Access Memory (RAM)
> **Giải thích:**
> **Đáp án đúng là B.** Đơn vị Điều khiển (Control Unit - CU) chịu trách nhiệm giải mã các chỉ thị và tạo ra các tín hiệu điều khiển để điều hướng các thành phần khác của hệ thống thực hiện các hành động cần thiết.

### Câu 87
Which addressing mode allows direct specification of the memory address within the instruction?
A. Direct
B. Indirect
C. Register Indirect
D. Displacement
> **Giải thích:**
> **Đáp án đúng là A.** Trong chế độ địa chỉ trực tiếp (Direct addressing), trường địa chỉ trong lệnh chứa chính địa chỉ hiệu dụng (effective address) của toán hạng trong bộ nhớ.

### Câu 88
Which architectural concept involves replicating register banks to facilitate the sharing of pipeline resources among multiple threads?
A. Pipelining
B. Superscalar
C. Simultaneous multithreading
D. Superpipelining
> **Giải thích:**
> **Đáp án đúng là C.** Đa luồng đồng thời (Simultaneous multithreading - SMT) cho phép nhiều luồng (threads) cùng chia sẻ và thực thi trên các tài nguyên của một lõi xử lý duy nhất. Để làm được điều này, phần cứng phải nhân bản các thanh ghi (register banks) để mỗi luồng có một bộ thanh ghi riêng.

### Câu 89
Which memory has the fastest speed and smallest capacity?
A. Cache
B. Main memory
C. HDD
D. Magnetic Disk
> **Giải thích:**
> **Đáp án đúng là A.** Trong hệ thống phân cấp bộ nhớ, bộ nhớ đệm (Cache) nằm gần CPU nhất, do đó nó có tốc độ truy cập nhanh nhất nhưng cũng có dung lượng nhỏ nhất và giá thành cao nhất trên mỗi bit.

### Câu 90
Which write technique ensures that all write operations are made to main memory as well as to the cache, ensuring that main memory is always valid?
A. Write through
B. Write back
C. Write around
D. No write allocate
> **Giải thích:**
> **Đáp án đúng là A.** Kỹ thuật ghi xuyên (Write-through) yêu cầu mỗi thao tác ghi dữ liệu phải được thực hiện đồng thời lên cả cache và bộ nhớ chính. Điều này đảm bảo dữ liệu trong bộ nhớ chính luôn được cập nhật, nhưng có thể làm chậm hiệu suất ghi.

### Câu 91
Which one of the four basic functions of a computer describes the following statement? "The paths among components are used to move data from memory to memory and from memory through gates to memory".
A. Data storage
B. Data processing
C. Data movement
D. Control
> **Giải thích:**
> **Đáp án đúng là C.** Câu này mô tả việc di chuyển dữ liệu (Data movement) giữa các thành phần khác nhau của máy tính (bộ nhớ, các module I/O). Đây là một trong bốn chức năng cơ bản của máy tính.

### Câu 92
Which registers can be assigned to a variety of functions by the programmer?
A. Data registers
B. General purpose registers
C. Address registers
D. Condition codes (flags)
> **Giải thích:**
> **Đáp án đúng là B.** Thanh ghi đa dụng (General-purpose registers) là các thanh ghi mà lập trình viên có thể linh hoạt sử dụng cho nhiều mục đích khác nhau như lưu trữ dữ liệu tạm thời, địa chỉ, hoặc kết quả trung gian của các phép toán.

### Câu 93
Which representation is most efficient to perform arithmetic operations on signed integer numbers?
A. Sign-magnitude
B. 2's complement
C. 1's & 2's complement
D. 1's complement
> **Giải thích:**
> **Đáp án đúng là B.** Biểu diễn bù hai (2's complement) là hiệu quả nhất cho các phép toán số học trên số nguyên có dấu vì các phép cộng và trừ có thể được thực hiện bằng cùng một mạch phần cứng mà không cần xử lý đặc biệt cho dấu, và nó chỉ có một biểu diễn duy nhất cho số 0.

### Câu 94
Which state indicates that a process is currently being executed by the processor?
A. Running
B. Ready
C. NewBorn
D. Halted
> **Giải thích:**
> **Đáp án đúng là A.** Trạng thái Đang chạy (Running) có nghĩa là tiến trình đó hiện đang được cấp phát CPU và các chỉ thị của nó đang được thực thi.

### Câu 95
Which component defines the system call interface to the operating system and facilitates binary portability?
A. Application Binary Interface (ABI)
B. Application Programming Interface (API)
C. Instruction Set Architecture (ISA)
D. Central Processing Unit (CPU)
> **Giải thích:**
> **Đáp án đúng là A.** Giao diện nhị phân ứng dụng (Application Binary Interface - ABI) định nghĩa các quy ước cấp thấp, bao gồm cả giao diện gọi hệ thống (system call), cho phép các chương trình đã được biên dịch có thể chạy trên bất kỳ hệ thống nào tuân thủ ABI đó.

### Câu 96
Which method of accessing units of data is used to copy a block in main memory into cache memory?
A. Direct access
B. Random access
C. Sequential access
D. Associative
> **Giải thích:**
> **Đáp án đúng là D.** Truy cập liên kết (Associative access) là phương pháp được sử dụng trong bộ nhớ cache. Khi CPU cần một dữ liệu, nó sẽ gửi một phần của địa chỉ (tag) đến cache, và cache sẽ so sánh đồng thời tag này với tag của tất cả các dòng để tìm ra dữ liệu tương ứng.

### Câu 97
Which method allows the programmer to view memory as consisting of multiple address spaces and is used to map logical addresses of variable length onto physical memory?
A. Paging
B. Overlays
C. Segmentation
D. Paging with segmentation
> **Giải thích:**
> **Đáp án đúng là C.** Phân đoạn (Segmentation) là một kỹ thuật quản lý bộ nhớ cho phép chia không gian địa chỉ logic của một chương trình thành các đoạn (segments) có độ dài thay đổi và ý nghĩa logic khác nhau (ví dụ: đoạn mã, đoạn dữ liệu, đoạn stack).

### Câu 99
(1) An I/O module must recognize one unique address for each peripheral it controls.
(2) I/O channels are commonly seen on microcomputers, whereas I/O controllers are used on mainframes.
The statement (1) is \_\_\_\_\_\_ and (2) is \_\_\_\_\_\_.
A. true, false
B. true, true
C. false, true
D. false, false
> **Giải thích:**
> **Đáp án đúng là A.**
> *   **(1) là Đúng:** Mỗi thiết bị ngoại vi được điều khiển bởi một module I/O phải có một địa chỉ duy nhất để CPU có thể phân biệt và giao tiếp với nó.
> *   **(2) là Sai:** Ngược lại mới đúng. Bộ điều khiển I/O (I/O controllers) đơn giản hơn và thường được dùng trong các máy tính cá nhân/vi mô (microcomputers). Kênh I/O (I/O channels), là các bộ xử lý chuyên dụng cho I/O, phức tạp và mạnh mẽ hơn, thường được sử dụng trên các máy tính lớn (mainframes).

### Câu 100
Control and status registers are used by which entities to control the operation of the processor?
A. Privileged, operating system programs
B. Machine or assembly language programmers
C. External I/O devices
D. Main memory modules
> **Giải thích:**
> **Đáp án đúng là A.** Các thanh ghi điều khiển và trạng thái (Control and status registers), ví dụ như thanh ghi chứa con trỏ lệnh hoặc các cờ trạng thái, được sử dụng để quản lý hoạt động của CPU. Việc truy cập và thay đổi chúng thường yêu cầu quyền ưu tiên (privileged mode), do đó chúng chủ yếu được sử dụng bởi hệ điều hành (operating system).

### Câu 101
For interrupts, all I/O modules share a common interrupt request line. When the processor senses an interrupt, it sends out an interrupt acknowledge. This signal propagates through a series of I/O modules until it gets to a requesting module. Which kind of interrupt technique is it?
A. Multiple interrupt lines
B. Software poll
C. Daisy chain
D. Bus arbitration
> **Giải thích:**
> **Đáp án đúng là C.** Đây là mô tả chính xác của kỹ thuật ngắt chuỗi (Daisy chain). Một tín hiệu xác nhận ngắt được truyền tuần tự qua các module I/O cho đến khi nó đến được module đã gửi yêu cầu ngắt.

### Câu 102
In MASM32, which OPCODE is used to compare two values?
A. COM
B. CMP
C. IF ... ELSE
D. TEST
> **Giải thích:**
> **Đáp án đúng là B.** Lệnh `CMP` (Compare) trong hợp ngữ được sử dụng để so sánh hai toán hạng. Về cơ bản, nó thực hiện một phép trừ nhưng không lưu kết quả, chỉ cập nhật các cờ (flags) trạng thái để các lệnh nhảy có điều kiện sau đó có thể sử dụng.

# References

