# TỔNG HỢP CÁC CÂU HỎI VÀ GIẢI THÍCH

Câu 1: Làm thế nào để khởi tạo một mảng ký tự trong C?

A. char arr] "Hello";
B. char arr[]=['H', 'e', 'T', 'T', 'o','/e'];
**(ĐÁP ÁN ĐÚNG)** C. char arr[] = "Hello";
D. char arr[] = {'H', 'e', 'T', 'I', '0', '0'};


**Giải thích:** Trong C, cách khởi tạo mảng ký tự bằng chuỗi ký tự là `char arr[] = "Hello";`.  Ký tự null kết thúc (`\0`) sẽ được tự động thêm vào cuối chuỗi. Các lựa chọn khác có lỗi cú pháp hoặc khởi tạo mảng bằng từng ký tự riêng lẻ.

---

Câu 2: How can you initialize a character array in C?

A. `char arr[] = "Hello";` (**ĐÁP ÁN ĐÚNG**)
B. `char arr[] = ['H', 'e', 'T', 'T', 'o','/e'];`
C. `Char[] arr = "Hello";`


**Giải thích:** Ghi chú đáp án là "A", tương ứng với lựa chọn A.  Đây là cách khởi tạo mảng ký tự bằng chuỗi ký tự trong C. Lựa chọn B sai vì sử dụng dấu ngoặc vuông `[]` thay vì ngoặc nhọn `{}` khi khởi tạo mảng ký tự bằng các ký tự riêng lẻ.  Lựa chọn C sai vì kiểu dữ liệu `char` phải viết thường.

---

Câu 3: How can you initialize a character array in C?

A. `char arr[] = "Hello";` (**ĐÁP ÁN ĐÚNG**)
B. `char arr[] = ['H', 'e', 'T', 'T', 'o','/e'];`
C. `Char[] arr = "Hello";`

**Giải thích:** Ghi chú "A" cùng với thời gian cho thấy đây là đáp án được chọn. Trong C, cách khởi tạo mảng ký tự bằng chuỗi ký tự như đáp án A là đúng. Đáp án B sai vì sử dụng dấu ngoặc vuông `[]` như khởi tạo mảng các ký tự riêng lẻ, đồng thời chứa ký tự `/e` không hợp lệ. Đáp án C sai về kiểu dữ liệu (phải là `char`, không phải `Char`).

---

Câu 4: Which of the following statements is invalid?

A. `printf('\\\');` (**ĐÁP ÁN ĐÚNG**)
B. `printf("abc");`
C. `printf("%%");`
D. `printf("\n");`


**Giải thích:**

Ký tự `\` trong chuỗi ký tự được đặt trong dấu nháy đơn `'` phải được escape bằng một ký tự `\` khác.  Đáp án A chỉ có một ký tự `\` sau dấu nháy đơn, dẫn đến lỗi biên dịch.  Để in ra ký tự `\`, cần phải viết `printf('\\');`  trong đó có hai ký tự `\`. Các đáp án khác đều hợp lệ: B in ra chuỗi "abc", C in ra ký tự `%` (bằng cách escape nó với một `%` khác), và D in ra ký tự newline.

---

Câu 5: Which of the following is an incorrect iteration construct?

A. (condition)? True Value: False_Value (**ĐÁP ÁN ĐÚNG**)
B. for (InitBlock; Condition; Task2) Task1;
C. do{ statements;} while (condition);
D. while (condition){ statements; }

**Giải thích:** Toán tử ba ngôi (ternary operator) `(condition)? True_Value : False_Value` được dùng để lựa chọn giữa hai giá trị dựa trên một điều kiện, chứ không phải là một cấu trúc lặp. Các lựa chọn B, C và D đều là các cấu trúc lặp hợp lệ (for, do-while, while).

---

Câu 6: Cú pháp của toán tử điều kiện trong C là gì?

A. `condition ? expression1 : expression2` (**ĐÁP ÁN ĐÚNG**)
B. `condition ? expression1, expression2`
C. `condition expression1 ? expression2`
D. `expression1 condition ? expression2`

**Giải thích:** Toán tử điều kiện trong C (còn gọi là toán tử ba ngôi) có cú pháp `condition ? expression1 : expression2`.  Nếu `condition` là đúng, `expression1` được đánh giá; ngược lại, `expression2` được đánh giá.  Ghi chú chỉ ra đáp án A là đúng.

---

Câu 7: Hàm nào sẽ tính trung bình của hai số thực?

A. `int average( double, double);`
B. `double average( double, double);` (**ĐÁP ÁN ĐÚNG**)
C. `char average( double, double);`
D. `void average( double, double);`

**Giải thích:** Hàm tính trung bình của hai số thực nên trả về một giá trị là số thực. Kiểu dữ liệu `double` đại diện cho số thực trong C/C++.  Đáp án B khai báo hàm `average` trả về kiểu `double`, phù hợp với yêu cầu.

---

Câu 8: Cú pháp nào sau đây là đúng của câu lệnh while?

A. `while (condition) { statements; }` (**ĐÁP ÁN ĐÚNG**)
B. `(condition){ statements ;}`
C. `while (condition) { statements };`
D. `{ statements } while (condition);`

**Giải thích:** Đáp án A là cú pháp chính xác của vòng lặp `while` trong hầu hết các ngôn ngữ lập trình giống C (như C++, Java, JavaScript, C#...).  Nó bao gồm từ khóa `while`, theo sau là một điều kiện trong dấu ngoặc đơn.  Nếu điều kiện đúng, các câu lệnh bên trong khối mã `{}` sẽ được thực thi.

---

Câu 9: What commands are used to write data appended to the end of the file? (Choose 2 answers)

A. `FILE *f=fwrite("output.txt", "a");`
B. `FILE *f= fopen("output.txt", "a");` (**ĐÁP ÁN ĐÚNG**)
C. `FILE *f= fopen("output.txt", "a+");` (**ĐÁP ÁN ĐÚNG**)
D. `FILE *f= fopen("output.txt", "w+");`
E. `FILE *f= fopen("output.txt", "w");`


**Giải thích:**

Ghi chú đáp án là "BC".  Trong C, hàm `fopen()` được dùng để mở file.  `"a"` là chế độ mở file để ghi tiếp vào cuối file (append). `"a+"` cũng là chế độ append, nhưng cho phép vừa đọc vừa ghi.  Vì câu hỏi yêu cầu chọn 2 đáp án, B và C đều đúng.  `fwrite()` không được dùng để mở file. `"w+"` sẽ ghi đè lên file hiện có, còn `"w"` cũng ghi đè và chỉ cho phép ghi.

---

Câu 10:

`int *ptr = malloc(sizeof(int));`

Để cấp phát lại `ptr` thành một mảng 5 phần tử, câu lệnh nào sau đây tạo ra lỗi?

A. `ptr = realloc(ptr, 5 * sizeof(int));`
B. `realloc(ptr, 5 * sizeof(int));`
C. `ptr += malloc(5 * sizeof(int));` (**ĐÁP ÁN ĐÚNG**)
D. `realloc(ptr, 20);`
E. `ptr = realloc(ptr, 20);`


**Giải thích:**

`realloc` trả về một con trỏ tới vùng nhớ được cấp phát lại.  Câu lệnh B không gán lại giá trị này cho `ptr`, dẫn đến rò rỉ bộ nhớ, nhưng không phải là lỗi. Tương tự, D cũng cấp phát 20 byte (tương đương 5 phần tử int trên nhiều hệ thống), nhưng cũng bị rò rỉ bộ nhớ.  Câu lệnh C cộng một con trỏ tới vùng nhớ mới được cấp phát bởi `malloc` vào con trỏ `ptr` ban đầu. Điều này không hợp lệ và sẽ dẫn đến lỗi, vì `ptr` sẽ trỏ đến một vị trí không xác định trong bộ nhớ.  A và E là cách sử dụng `realloc` đúng.