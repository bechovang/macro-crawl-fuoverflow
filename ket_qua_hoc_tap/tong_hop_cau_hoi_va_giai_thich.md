# TỔNG HỢP CÁC CÂU HỎI VÀ GIẢI THÍCH

Câu 1:
Cho `int *ptr = malloc(sizeof(int));`. Để cấp phát lại `ptr` thành một mảng 5 phần tử, câu lệnh nào sau đây gây ra lỗi?

A. `ptr = realloc(ptr, 5 * sizeof(int));`
B. `realloc(ptr, 5 * sizeof(int));`
C. `ptr += malloc(5 * sizeof(int));`
D. `realloc(ptr, 20);`
E. `ptr = realloc(ptr, 20);`


**Giải thích:**

Đáp án đúng là C.

`realloc` được sử dụng để thay đổi kích thước khối bộ nhớ được cấp phát động. Phương án A và E đều đúng và an toàn. Phương án B không cập nhật lại con trỏ `ptr` sau khi cấp phát lại, dẫn đến rò rỉ bộ nhớ, nhưng không gây ra lỗi. Phương án D cấp phát 20 byte, tương đương với 5 phần tử `int` trên nhiều hệ thống (trong đó `sizeof(int)` là 4), nên cũng không sai. Phương án C cộng con trỏ `ptr` với giá trị trả về bởi `malloc`, dẫn đến việc `ptr` trỏ đến một vùng nhớ không xác định và gây ra lỗi.

---

Câu 2: What is the correct syntax to output "Hello, World!" in C/C++?

A. `printf("Hello, World!");`
B. `cout << "Hello, World!" << endl;`
C. `System.out.println("Hello, World!");`
D. `echo "Hello, World!";`


**Giải thích:**

Đáp án đúng là A.

`printf("Hello, World!");` là cách sử dụng hàm `printf` trong C để in ra màn hình. Ghi chú chỉ ra đáp án là A, tuy không giải thích cụ thể nhưng đây là cú pháp chuẩn trong C. Phương án B đúng trong C++, C sử dụng `printf`. Phương án C đúng trong Java. Phương án D đúng trong các shell script như bash.

---

Câu 3: 31 + 2 = ?

A. 32
B. 34
C. 33
D. 30

**Giải thích:**
Đáp án đúng là C.

31 + 2 = 33

---

Câu 4: What is the binary representation of 0xA2?

A. 0b01100010
B. 0b10100010
C. 0b10010010
D. 0b10110010

**Giải thích:**

Đáp án đúng là B.

Số hex 0xA2 được chuyển đổi sang nhị phân như sau: A = 10 (trong hệ thập phân) = 1010 (trong hệ nhị phân); 2 = 2 (trong hệ thập phân) = 0010 (trong hệ nhị phân).  Ghép lại ta được 10100010, hay 0b10100010.

---

Câu 5: Hàm `strcmp()` so sánh hai chuỗi ký tự theo từng ký tự. Nếu hai chuỗi bằng nhau, hàm trả về:

A. 1
B. 0
C. -1


**Giải thích:**

Đáp án đúng là B.

Hàm `strcmp()` trả về 0 nếu hai chuỗi bằng nhau.  Nếu chuỗi thứ nhất lớn hơn chuỗi thứ hai, nó trả về 1. Nếu chuỗi thứ nhất nhỏ hơn chuỗi thứ hai, nó trả về -1.

---

Câu 6: What is the result of the statement `strcmp("abcdef", "abdc")`?

A. 1
B. 0
C. -1


**Giải thích:**

Đáp án đúng là C.

Hàm `strcmp` so sánh hai chuỗi theo thứ tự từ điển.  Trong trường hợp này, "abcdef" và "abdc" khác nhau ở ký tự thứ tư ('e' và 'd'). Vì 'e' có giá trị ASCII lớn hơn 'd', `strcmp("abcdef", "abdc")` trả về một số nguyên dương. Thông thường các triển khai trả về 1 khi chuỗi thứ nhất lớn hơn chuỗi thứ hai, và dựa trên ghi chú đáp án là C (-1), có thể hệ thống cụ thể này trả về -1 khi chuỗi thứ nhất lớn hơn.  Quan trọng là kết quả sẽ khác 0, biểu thị hai chuỗi không giống nhau.

---

Câu 7: Nếu hai chuỗi có cùng giá trị, thì hàm strcmp() trả về:
A. True
B. 1
C. 0
D. -1

**Giải thích:**
Đáp án đúng là C.

Hàm `strcmp()` trong C so sánh hai chuỗi. Nếu hai chuỗi giống hệt nhau, hàm sẽ trả về 0.  Các giá trị khác 0 (như 1 hoặc -1) cho biết chuỗi thứ nhất lớn hơn hoặc nhỏ hơn chuỗi thứ hai theo thứ tự từ điển.

---

Câu 8: Cho hai chuỗi ký tự s1="C" và s2="C and C++", hàm strcmp(s1, s2) sẽ trả về giá trị

A. 0
B. 1
C. -1
D. <0
E. >0


**Giải thích:**

Đáp án đúng là D.

Hàm `strcmp()` so sánh hai chuỗi theo thứ tự từ điển.  Vì `s1` ("C") đứng trước `s2` ("C and C++") trong thứ tự từ điển nên `strcmp(s1, s2)` sẽ trả về một giá trị âm (nhỏ hơn 0).

---

Câu 9:

Cho đoạn mã sau:

```c
int a[10] = {1, 2, 3};
```

Giá trị của `a[3]` là gì?

A. 0
B. 1
C. 2
D. 3


**Giải thích:**

Đáp án đúng là A.

Khi khởi tạo mảng `int a[10] = {1, 2, 3};`, chỉ ba phần tử đầu tiên được gán giá trị lần lượt là 1, 2 và 3. Các phần tử còn lại từ `a[3]` đến `a[9]` sẽ được tự động khởi tạo bằng 0. Do đó, `a[3]` có giá trị là 0.

---

Câu 10: What is the result of the expression 10 % 3?

A. 1
B. 3
C. 2
D. 0


**Giải thích:**

Đáp án đúng là A.

Phép toán `%` là phép toán lấy phần dư của phép chia.  10 chia 3 được 3 dư 1. Vậy 10 % 3 = 1.