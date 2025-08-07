
2025-08-07 18:43

Status:

Tags: [[source]]   [[PRF]] 
Disable spell check :`teh`
# SOURCE PRF 1-100

---

## I. Thông tin chung & Tài liệu tham khảo

Phần này bao gồm các thông báo và liên kết tài liệu được trích xuất từ các slide đầu.

*   **Nhóm Facebook:** Mọi người nên tham gia nhóm Facebook để cập nhật thông tin và truy cập các đề thi mới (đặc biệt là đề FE SU25 cho các bạn thi lại).
*   **Tài liệu học tập & Source Code:**
    *   **Source code, PT, EBS:** [Google Drive](https://drive.google.com/drive/folders/1UCa3IxRv0fyyKJxNR18Xu7tD9zxqHUeq?usp=sharing)
    *   **Facebook liên hệ:** [Vũ Hoàng](https://www.facebook.com/vu.hoang.79219/)
    *   **Luyện tập Flashcard:** [Quizlet PRF192](https://quizlet.com/vn/504065032/tong-hop-prf-192-flash-card)
*   **Lộ trình học tập (Tham khảo):**
    *   **Youtube:** [Lộ trình học](https://www.youtube.com/watch?v=_LooQ5QmEo)
    *   **Website:** [https://4user.net/home/courses](https://4user.net/home/courses)

---

## II. Kiến thức nền tảng

Đây là phần tổng hợp các khái niệm, công thức và quy tắc quan trọng trong lập trình C.

### 1. Các kiểu dữ liệu cơ bản trong C

| Kiểu dữ liệu | Kích thước | Giá trị lưu trữ | Dải giá trị | Đặc tả định dạng |
| :--- | :--- | :--- | :--- | :--- |
| `char` | 1 byte | Ký tự / Số nguyên | -128 đến 127 | `%c` |
| `unsigned char` | 1 byte | Ký tự / Số nguyên | 0 đến 255 | `%c` |
| `short` | 2 bytes | Số nguyên | -32,768 đến 32,767 | `%hi` |
| `unsigned short`| 2 bytes | Số nguyên | 0 đến 65,535 | `%hu` |
| `int` | 4 bytes | Số nguyên | -2,147,483,648 đến 2,147,483,647 | `%d` |
| `unsigned int` | 4 bytes | Số nguyên | 0 đến 4,294,967,295 | `%u` |
| `long long` | 8 bytes | Số nguyên | ~-9.2 x 10¹⁸ đến ~9.2 x 10¹⁸ | `%lld` |
| `unsigned long long`| 8 bytes| Số nguyên | 0 đến ~1.8 x 10¹⁹ | `%llu` |
| `float` | 4 bytes | Số thực | 3.4E-38 đến 3.4E+38 | `%f` |
| `double` | 8 bytes | Số thực | 1.7E-308 đến 1.7E+308 | `%lf` |

### 2. Ép kiểu (Casting)

*   **Ép kiểu mở rộng (Widening Casting - Tự động):** Chuyển từ kiểu dữ liệu nhỏ sang kiểu lớn hơn, không làm mất dữ liệu.
    *   `byte` → `short` → `int` → `long` → `float` → `double`
*   **Ép kiểu thu hẹp (Narrowing Casting - Tường minh):** Chuyển từ kiểu lớn sang kiểu nhỏ hơn, có thể làm mất dữ liệu, cần phải thực hiện tường minh.
    *   **Ví dụ:** `int i = (int)3.14;`

### 3. Toán tử (Operators)

*   **Toán tử số học:** `+`, `-`, `*`, `/`, `%` (chia lấy dư).
*   **Toán tử logic:**
    *   `&&` (AND): Nếu vế trái là `false`, sẽ không xét vế phải.
    *   `||` (OR): Nếu vế trái là `true`, sẽ không xét vế phải.
*   **Toán tử so sánh:** `==` (so sánh bằng), `!=` (không bằng), `>`, `<`, `>=`, `<=`.
*   **Lưu ý:** `==` so sánh giá trị cho các kiểu nguyên thủy. Đối với chuỗi, dùng hàm `strcmp()`.

### 4. Mảng (Arrays)

*   **Khái niệm:** Là một tập hợp các phần tử có cùng kiểu dữ liệu, được lưu trữ ở các vị trí bộ nhớ liền kề. Kích thước cố định.
*   **Khai báo:**
    *   `int arr[5] = {1, 2, 3, 4, 5};`
    *   `int arr[5];`
*   **Truy cập phần tử:** `arr[index]` (chỉ số `index` bắt đầu từ 0).
*   **Mảng hai chiều:** Là mảng của các mảng. `int arr[3][4];`

### 5. Vòng lặp và cấu trúc điều khiển

*   **`for`:** Lặp lại một khối lệnh với số lần xác định.
*   **`while`:** Lặp lại một khối lệnh khi điều kiện còn đúng. Kiểm tra điều kiện trước khi thực hiện.
*   **`do-while`:** Giống `while` nhưng luôn thực hiện khối lệnh ít nhất một lần trước khi kiểm tra điều kiện.
*   **`if`, `else if`, `else`:** Thực hiện các khối lệnh khác nhau dựa trên các điều kiện.
*   **`switch-case`:** Rẽ nhánh dựa trên giá trị của một biến (int, char).
*   **`break`:** Thoát khỏi vòng lặp (`for`, `while`, `do-while`) hoặc `switch` gần nhất.
*   **`continue`:** Bỏ qua phần còn lại của vòng lặp hiện tại và chuyển sang lần lặp tiếp theo.

### 6. Con trỏ (Pointers)

*   Là một biến lưu trữ địa chỉ bộ nhớ của một biến khác.
*   **Khai báo:** `data_type *pointer_name;` (Ví dụ: `int *ptr;`)
*   **Toán tử `&` (Address-of):** Lấy địa chỉ của một biến. (Ví dụ: `ptr = &var;`)
*   **Toán tử `*` (Dereference):** Truy cập giá trị tại địa chỉ mà con trỏ đang trỏ tới. (Ví dụ: `value = *ptr;`)

---

## III. Ngân hàng câu hỏi trắc nghiệm

### Câu 16
Which of the following statements is invalid?
A. `printf(1ll);`
B. `printf("abc");`
C. `printf("%%");`
D. `printf("\n");`
> **Giải thích:**
> **Đáp án đúng là A.** Hàm `printf` yêu cầu đối số đầu tiên phải là một chuỗi hằng (a constant character string) làm chuỗi định dạng. `1ll` là một hằng số kiểu `long long`, không phải là một chuỗi. Do đó, câu lệnh này sẽ gây ra lỗi biên dịch (compiler error).

### Câu 17
What is incorrect when inputting a string?
A. `scanf("%s", s);`
B. `scanf("%[^\n]", s);`
C. `getc(stdin);`
D. `gets(s);`
E. `scanf(s);`
> **Giải thích:**
> **Đáp án đúng là E.**
> *   A và B là các cách hợp lệ để đọc chuỗi bằng `scanf`.
> *   D (`gets`) là một hàm hợp lệ để đọc chuỗi nhưng không an toàn và đã bị loại bỏ khỏi các chuẩn C mới.
> *   C (`getc`) chỉ đọc một ký tự, không phải một chuỗi.
> *   E (`scanf(s)`) là sai cú pháp. Hàm `scanf` cần một chuỗi định dạng làm đối số đầu tiên.

### Câu 18
Choose the correct statement for declaring a float pointer:
A. `float* ptr;`
B. `float ptr;`
C. `*float ptr;`
D. `float ptr*;`
> **Giải thích:**
> **Đáp án đúng là A.** Cú pháp chính xác để khai báo một con trỏ (pointer) trong C là `data_type *pointer_name;`. Dấu `*` có thể được đặt ngay sau kiểu dữ liệu (`float* ptr;`) hoặc ngay trước tên biến (`float *ptr;`), cả hai đều hợp lệ.

### Câu 19
Which of the following declarations is not supported by C?
A. `string a;`
B. `float a = 3e2;`
C. `int* a;`
D. `float *a;`
E. `char *a;`
> **Giải thích:**
> **Đáp án đúng là A.** Ngôn ngữ C chuẩn không có kiểu dữ liệu `string` tích hợp sẵn. Chuỗi trong C được xử lý bằng mảng ký tự (`char[]`) hoặc con trỏ ký tự (`char*`). `string` là một kiểu đối tượng trong C++.

### Câu 20
Which of the following statements correctly declares a function that receives a float pointer parameter and returns a float pointer?
A. `float* fun(float *p);`
B. `float fun(float *p);`
C. `float* fun(double *p);`
D. `float* fun(int *p);`
> **Giải thích:**
> **Đáp án đúng là A.**
> *   Kiểu trả về là một con trỏ float: `float*`
> *   Tên hàm là `fun`.
> *   Tham số đầu vào là một con trỏ float: `(float *p)`
> Cú pháp đầy đủ là `float* fun(float *p);`.

### Câu 21
Which of the following is not a valid variable name declaration?
A. `int _a3;`
B. `int a_3;`
C. `int 3_a;`
D. `int _3a;`
> **Giải thích:**
> **Đáp án đúng là C.** Trong C, tên biến (variable name) không được phép bắt đầu bằng một chữ số. Nó có thể bắt đầu bằng một chữ cái hoặc dấu gạch dưới (`_`).

### Câu 22
Which of the following is a valid variable definition?
A. `int 1student_ID;`
B. `int _Student_ID1;`
C. `int Age$;`
D. `int long;`
> **Giải thích:**
> **Đáp án đúng là B.**
> *   A sai vì bắt đầu bằng số.
> *   C sai vì chứa ký tự không hợp lệ (`$`).
> *   D sai vì `long` là một từ khóa (keyword) của ngôn ngữ C.
> *   B hợp lệ vì bắt đầu bằng dấu gạch dưới và chỉ chứa các ký tự hợp lệ.

### Câu 23
Choose the correct statement for declaring a pointer variable to an integer variable.
A. `int *p;`
B. `int p*;`
C. `int +p;`
D. `int $p;`
> **Giải thích:**
> **Đáp án đúng là A.** Cú pháp chính xác để khai báo một con trỏ (pointer) tới một số nguyên (integer) là `int *p;` hoặc `int* p;`.

### Câu 24
Which of the following is a valid code to declare and initialize a two-dimensional array?
A. `int a[2,3] = {{1,2,3},{4,5,6}};`
B. `int a[][] = {{1,2,3},{4,5,6}};`
C. `int a[2][3] = {{1,2,3},{4,5,6}};`
D. `int a[][3] = {{1,2,3},{4,5,6}};`
> **Giải thích:**
> **Đáp án đúng là C và D.**
> *   **C:** Khai báo và khởi tạo đầy đủ, chỉ định cả hai chiều. Đây là cách rõ ràng nhất.
> *   **D:** Cũng hợp lệ. Khi khởi tạo mảng hai chiều, bạn có thể bỏ qua kích thước của chiều đầu tiên, trình biên dịch sẽ tự động xác định nó dựa trên danh sách khởi tạo. Tuy nhiên, bạn phải chỉ định kích thước của các chiều còn lại.
> *   A sai cú pháp (`[2,3]`).
> *   B sai vì phải chỉ định kích thước của chiều thứ hai.
> *(Trong bối cảnh trắc nghiệm, C thường được coi là câu trả lời chuẩn mực nhất)*.

### Câu 25
Which of the following correctly declares an integer array of size 5 in C/C++?
A. `int arr[5];`
B. `array int arr = [5];`
C. `int arr = new int[5];`
D. `int arr(5);`
> **Giải thích:**
> **Đáp án đúng là A.** Đây là cú pháp chuẩn để khai báo một mảng tĩnh (static array) trong C/C++. Lựa chọn C là cú pháp cấp phát động trong C++/Java/C#, không phải là khai báo mảng tĩnh cơ bản.

### Câu 26
What represents dynamic allocation in C?
A. `int* a = (int*)malloc(5*sizeof(int));`
B. `int a[5];`
C. `int a[5][5];`
D. `free(a);`
> **Giải thích:**
> **Đáp án đúng là A.** Hàm `malloc` (memory allocation) được sử dụng để cấp phát động (dynamic allocation) một khối bộ nhớ. Lựa chọn B và C là cấp phát tĩnh. Lựa chọn D là hàm để giải phóng bộ nhớ đã được cấp phát động.

### Câu 27
Which is the correct function definition that will run without errors?
A. `int minus(int a, int b) {return (a - b);}`
B. `int minus(int a, b) {return (a - b);}`
C. `int minus(int a; int b) {return (a - b);}`
D. `int minus(int a, int b); {return (a - b);}`
> **Giải thích:**
> **Đáp án đúng là A.** Cú pháp định nghĩa hàm chính xác yêu cầu kiểu dữ liệu cho mỗi tham số và các tham số được phân cách bằng dấu phẩy. Khối mã của hàm được đặt trong cặp dấu `{}`.
> *   B sai vì thiếu kiểu dữ liệu cho `b`.
> *   C sai vì dùng dấu `;` thay vì `,`.
> *   D sai vì có dấu `;` sau phần khai báo tham số.

### Câu 28
What is an incorrect function prototype?
A. `void printSum(int* a, int b);`
B. `int printSum(int* a, int b);`
C. `int printSum(int a, b);`
D. `int* printSum(int* a, int b);`
> **Giải thích:**
> **Đáp án đúng là C.** Một khai báo nguyên mẫu hàm (function prototype) yêu cầu phải có kiểu dữ liệu cho tất cả các tham số. Trong lựa chọn C, tham số `b` không có kiểu dữ liệu.

### Câu 29
Which of the following is the correct syntax of the for statement?
A. `for (Init1, Init2; Condition; Task1, Task2);`
B. `for (Init1; Condition; Task1);`
C. `for (Condition; Init1; Task1);`
D. `for (Init1; Init2, Condition; Task2);`
> **Giải thích:**
> **Đáp án đúng là B.** Cú pháp cơ bản của vòng lặp `for` là `for (khởi tạo; điều kiện; cập nhật) { ... }`.
> *   Lựa chọn A có thể hợp lệ nếu `Init1, Init2` và `Task1, Task2` sử dụng toán tử dấu phẩy, nhưng nó không phải là cú pháp cơ bản.
> *   Lựa chọn B là cú pháp chuẩn và phổ biến nhất.

### Câu 30
The function which will compute the average of two real numbers should be prototyped as:
A. `int average(double, double);`
B. `double average(double, double);`
C. `char average(double, double);`
D. `void average(double, double);`
> **Giải thích:**
> **Đáp án đúng là B.** Trung bình của hai số thực (real numbers) có thể là một số thực. Do đó, kiểu trả về (return type) của hàm cũng nên là một kiểu số thực như `double` để đảm bảo tính chính xác.

### Câu 32
How can you initialize a character array in C?
A. `char arr[] = "Hello";`
B. `char arr[] = {'H', 'e', 'l', 'l', 'o'};`
C. `char arr = "Hello";`
D. `char arr[] = {"H", "e", "l", "l", "o"};`
> **Giải thích:**
> **Đáp án đúng là A và B.**
> *   **A:** Đây là cách phổ biến và tiện lợi nhất. Trình biên dịch sẽ tự động thêm ký tự kết thúc chuỗi `\0` vào cuối.
> *   **B:** Cách này cũng hợp lệ nhưng bạn phải tự thêm `\0` nếu muốn sử dụng nó với các hàm xử lý chuỗi: `{'H', 'e', 'l', 'l', 'o', '\0'}`.
> *   C sai vì `arr` là mảng nhưng được khai báo như biến đơn.
> *   D sai vì dùng dấu ngoặc kép (chuỗi) thay vì ngoặc đơn (ký tự).

### Câu 33
Which of the following statements has a different result from the other statements?
A. `char c1 = 'B'; printf("%c", c1);`
B. `char c2 = 066; printf("%c", c2);`
C. `char c3 = 0x42; printf("%c", c3);`
D. `char c4 = 0102; printf("%c", c4);`
> **Giải thích:**
> **Đáp án đúng là B.**
> *   A: In ra ký tự 'B'.
> *   C: `0x42` trong hệ hexa (hexadecimal) là `4*16 + 2 = 66` trong hệ thập phân, là mã ASCII của 'B'.
> *   D: `0102` trong hệ bát phân (octal) là `1*8² + 0*8¹ + 2*8⁰ = 64 + 2 = 66` trong hệ thập phân, là mã ASCII của 'B'.
> *   B: `066` trong hệ bát phân là `6*8¹ + 6*8⁰ = 48 + 6 = 54` trong hệ thập phân, là mã ASCII của '6', không phải 'B'.

### Câu 35
Which of the following is an incorrect iteration construct?
A. `(condition) ? True_Value : False_Value`
B. `for (InitBlock; Condition; Task) Statement;`
C. `do { statements; } while (condition);`
D. `while (condition) { statements; }`
> **Giải thích:**
> **Đáp án đúng là A.** Lựa chọn A là toán tử điều kiện ba ngôi (ternary conditional operator), đây là một cấu trúc rẽ nhánh, không phải là một cấu trúc lặp (iteration construct). B, C, và D là các vòng lặp hợp lệ.

### Câu 36
What is the syntax of the conditional operator in C?
A. `condition ? expression1 : expression2`
B. `condition ? expression1, expression2`
C. `condition : expression1 ? expression2`
D. `expression1 : condition ? expression2`
> **Giải thích:**
> **Đáp án đúng là A.** Cú pháp của toán tử điều kiện ba ngôi (ternary conditional operator) là: `điều_kiện ? giá_trị_nếu_đúng : giá_trị_nếu_sai`.

### Câu 39
What commands are used to write data appended to the end of the file? (Choose 2 answers)
A. `FILE *f = fwrite("output.txt", "a");`
B. `FILE *f = fopen("output.txt", "a");`
C. `FILE *f = fopen("output.txt", "a+");`
D. `FILE *f = fopen("output.txt", "w+");`
E. `FILE *f = fopen("output.txt", "w");`
> **Giải thích:**
> **Đáp án đúng là B và C.** Hàm `fopen` được sử dụng để mở tệp. Chế độ (mode) để ghi nối vào cuối tệp là:
> *   `"a"` (append): Mở để ghi nối. Con trỏ tệp được đặt ở cuối. Nếu tệp không tồn tại, nó sẽ được tạo.
> *   `"a+"` (append and read): Mở để đọc và ghi nối.

### Câu 40
```c
int *ptr = malloc(sizeof(int));
```
To reallocate `ptr` to be an array of 5 elements, which of the following statements generates an error?
A. `ptr = realloc(ptr, 5 * sizeof(int));`
B. `realloc(ptr, 5 * sizeof(int));`
C. `ptr += malloc(5 * sizeof(int));`
D. `realloc(ptr, 20);`
E. `ptr = realloc(ptr, 20);`
> **Giải thích:**
> **Đáp án đúng là C.** Câu lệnh `ptr += malloc(...)` là không hợp lệ cho việc tái cấp phát. Nó cố gắng thực hiện phép toán con trỏ bằng cách cộng một địa chỉ (từ `malloc`) vào một địa chỉ khác, điều này không có ý nghĩa và sai cú pháp. Các lựa chọn khác sử dụng `realloc` là đúng về mặt cú pháp (mặc dù B và D có thể gây rò rỉ bộ nhớ nếu không gán lại).

### Câu 41
What is the correct syntax to output "Hello, World!" in C?
A. `printf("Hello, World!");`
B. `cout << "Hello, World!" << endl;`
C. `System.out.println("Hello, World!");`
D. `echo "Hello, World!";`
> **Giải thích:**
> **Đáp án đúng là A.** `printf` là hàm xuất chuẩn trong thư viện `stdio.h` của ngôn ngữ C. `cout` là của C++, `System.out.println` là của Java, `echo` là lệnh của shell.

### Câu 43
What is the binary representation of 0xA2?
A. 0b01100010
B. 0b10100010
C. 0b10010010
D. 0b10110010
> **Giải thích:**
> **Đáp án đúng là B.** Chuyển đổi từng ký tự hexa sang 4 bit nhị phân:
> *   `A` (hệ 16) = `10` (hệ 10) = `1010` (hệ 2)
> *   `2` (hệ 16) = `2` (hệ 10) = `0010` (hệ 2)
> Ghép lại ta được `10100010`.

### Câu 44
The `strcmp()` compares two strings character by character. If the strings are equal, the function returns...
A. 1
B. 0
C. -1
> **Giải thích:**
> **Đáp án đúng là B.** Hàm `strcmp` trả về:
> *   `0` nếu hai chuỗi bằng nhau.
> *   Giá trị âm (`< 0`) nếu chuỗi 1 nhỏ hơn chuỗi 2.
> *   Giá trị dương (`> 0`) nếu chuỗi 1 lớn hơn chuỗi 2.

### Câu 45
What is the result of the statement `strcmp("abcdef", "abdo")`?
A. 1
B. 0
C. -1
> **Giải thích:**
> **Đáp án đúng là C.** Hàm `strcmp` so sánh từng ký tự. Tại vị trí thứ 3 (index 2), nó so sánh `'c'` và `'d'`. Vì mã ASCII của `'c'` nhỏ hơn mã ASCII của `'d'`, chuỗi "abcdef" được coi là nhỏ hơn chuỗi "abdo", và hàm sẽ trả về một giá trị âm (thường là -1).

### Câu 46
If the two strings have the same value, then the `strcmp()` function returns \_\_.
A. True
B. 1
C. 0
D. -1
> **Giải thích:**
> **Đáp án đúng là C.** Theo định nghĩa, `strcmp` trả về 0 khi hai chuỗi giống hệt nhau.

### Câu 47
Given two character strings `s1 = "C"` and `s2 = "C and C++"`, the function `strcmp(s1, s2)` will return a value that is:
A. 0
B. 1
C. < 0
D. > 0
> **Giải thích:**
> **Đáp án đúng là C.** Chuỗi `s1` là một tiền tố của chuỗi `s2`. Trong trường hợp này, `s1` được coi là "nhỏ hơn" vì nó ngắn hơn. Hàm `strcmp` sẽ trả về một giá trị âm (`< 0`).

### Câu 48
Given the following code snippet:
```c
int a[10] = {1, 2, 3};
```
What is the value of `a[3]`?
A. 0
B. 1
C. 2
D. 3
> **Giải thích:**
> **Đáp án đúng là A.** Khi một mảng được khởi tạo với ít phần tử hơn kích thước của nó, các phần tử còn lại sẽ được tự động khởi tạo bằng 0. Ở đây, `a[0] = 1`, `a[1] = 2`, `a[2] = 3`. Các phần tử từ `a[3]` đến `a[9]` đều bằng 0.

### Câu 49
What is the result of the expression `10 % 3`?
A. 1
B. 3
C. 2
D. 0
> **Giải thích:**
> **Đáp án đúng là A.** Toán tử `%` (modulo) trả về phần dư của phép chia số nguyên. 10 chia cho 3 được 3, dư 1.

### Câu 50
What is the return value of the `strcmp("abc", "Abcdef")` function?
A. A positive value (e.g., 1)
B. 0
C. A negative value (e.g., -1)
D. 2
> **Giải thích:**
> **Đáp án đúng là A.** So sánh dựa trên mã ASCII. Mã ASCII của `'a'` (97) lớn hơn mã ASCII của `'A'` (65). Do đó, chuỗi "abc" được coi là lớn hơn "Abcdef", và hàm sẽ trả về một giá trị dương.

### Câu 51
What will be the output of the C program?
```c
char temp;
char arr[10] = {1, 2, 3, 4, 5, 6, 7, 8};
temp = (arr + 1)[2];
printf("%d\n", temp);```
A. 1
B. 2
C. 3
D. 4
> **Giải thích:**
> **Đáp án đúng là D.**
> *   `arr` là con trỏ trỏ đến phần tử đầu tiên, `arr[0]`.
> *   `(arr + 1)` là một con trỏ trỏ đến phần tử thứ hai, `arr[1]`.
> *   `(arr + 1)[2]` truy cập phần tử ở vị trí index 2 tính từ con trỏ `(arr + 1)`. Điều này tương đương với `arr[1 + 2]`, tức là `arr[3]`.
> *   Giá trị của `arr[3]` là 4.

### Câu 52
What is the output of the following code snippet?
```c
void main() {
    int x = 4;
    int *p = &x;
    int *k = p++;
    int r = p - k;
    printf("%d", r);
}
```
A. 1
B. 4
C. 5
D. 0
> **Giải thích:**
> **Đáp án đúng là A.**
> *   `p = &x;`: `p` trỏ đến `x`.
> *   `int *k = p++;`: Đây là phép gán với toán tử tăng hậu tố (post-increment). `k` sẽ nhận giá trị *hiện tại* của `p` (là `&x`), sau đó `p` mới được tăng lên để trỏ đến vị trí bộ nhớ của số nguyên tiếp theo (`&x + 1`).
> *   `int r = p - k;`: Phép trừ con trỏ (pointer subtraction) trả về số lượng phần tử (cùng kiểu) nằm giữa hai con trỏ. Ở đây, `p` và `k` trỏ đến hai vị trí số nguyên liền kề nhau, nên hiệu số là 1.

### Câu 53
What is the value of `ceil(2.55)` from the `math.h` library?
A. 3.0
B. 2.0
C. 2.5
D. 2.6
> **Giải thích:**
> **Đáp án đúng là A.** Hàm `ceil` (ceiling) làm tròn một số thực lên số nguyên gần nhất lớn hơn hoặc bằng nó. `ceil(2.55)` sẽ trả về `3.0`.

### Câu 54
Suppose there is a function in C as follows:
```c
double g(double x, double y) {
    return (x - 2)*(x - 2) + y*y;
}
```
What is the value of `z` after executing the statement `z = g(2, 0);`?
A. 0
B. 4
C. 2
D. 8
> **Giải thích:**
> **Đáp án đúng là A.** Thay `x = 2` và `y = 0` vào hàm:
> `return (2 - 2)*(2 - 2) + 0*0;`
> `return 0 * 0 + 0;`
> `return 0;`

### Câu 55
What is the maximum index of the last character in a character array initialized with a size of 10?
A. 9
B. 10
C. 8
D. It depends on the contents of the array
> **Giải thích:**
> **Đáp án đúng là A.** Mảng trong C có chỉ số (index) bắt đầu từ 0. Một mảng có kích thước 10 sẽ có các phần tử được đánh chỉ số từ 0 đến 9. Do đó, chỉ số lớn nhất là 9.

### Câu 56
What is the result of the expression `!1`?
A. 0
B. 1
C. 10
D. 11
> **Giải thích:**
> **Đáp án đúng là A.** Trong C, bất kỳ giá trị nào khác 0 đều được coi là `true`. Do đó, `1` là `true`. Toán tử `!` (NOT logic) sẽ đảo ngược giá trị logic. `!true` sẽ là `false`. Trong ngữ cảnh số nguyên, `false` được biểu diễn bằng 0.

### Câu 57
What will be the output of the C program?
```c
int a = 4, b = 2;
printf("a^b = %d", a^b);
```
A. 2
B. 8
C. 16
D. 6
> **Giải thích:**
> **Đáp án đúng là D.** Toán tử `^` trong C là phép toán XOR trên bit (bitwise XOR).
> *   `a = 4` trong hệ nhị phân là `100`.
> *   `b = 2` trong hệ nhị phân là `010`.
> *   `100 XOR 010 = 110`.
> *   `110` trong hệ nhị phân là `4 + 2 = 6` trong hệ thập phân.

### Câu 58
What is the output when the sample code below is executed?
```c
#include<stdio.h>
int main() {
    int x = 10, i;
    for (i = 9; i < x; i += 3) {
        printf("%d", i++);
        break;
    }
    printf("%d", --i); // This line is never reached
    return 0;
}
```
A. 9
B. 8
C. 12
D. 10
> **Giải thích:**
> **Đáp án đúng là A.**
> 1.  Vòng lặp bắt đầu với `i = 9`.
> 2.  Điều kiện `i < x` (9 < 10) là đúng, vòng lặp được thực thi.
> 3.  `printf("%d", i++);`: Toán tử `++` hậu tố (postfix) sẽ in ra giá trị hiện tại của `i` (là 9), *sau đó* mới tăng `i` lên 10.
> 4.  `break;`: Lệnh `break` ngay lập tức thoát khỏi vòng lặp `for`.
> 5.  Chương trình kết thúc. Câu lệnh `printf` thứ hai không bao giờ được thực thi.
> Do đó, kết quả duy nhất được in ra là 9.

### Câu 59
What is the result of the `printf("%d", 0x11 | 010);` command?
A. 5
B. 22
C. 18
D. 25
E. 28
> **Giải thích:**
> **Đáp án đúng là D.** Đây là phép toán OR trên bit (bitwise OR).
> *   `0x11` (hệ hexa) = `1*16 + 1 = 17` (hệ 10) = `0001 0001` (hệ 2).
> *   `010` (hệ bát phân - octal) = `1*8 + 0 = 8` (hệ 10) = `0000 1000` (hệ 2).
> *   `0001 0001 | 0000 1000 = 0001 1001`.
> *   `0001 1001` (hệ 2) = `16 + 8 + 1 = 25` (hệ 10).

### Câu 60
In the sample code `int a = 0x10 | 011;`, the variable `a` will contain the value (in decimal):
A. 3
B. 13
C. 19
D. 25
E. 27
> **Giải thích:**
> **Đáp án đúng là D.**
> *   `0x10` (hệ hexa) = `16` (hệ 10) = `0001 0000` (hệ 2).
> *   `011` (hệ bát phân) = `1*8 + 1 = 9` (hệ 10) = `0000 1001` (hệ 2).
> *   `0001 0000 | 0000 1001 = 0001 1001`.
> *   `0001 1001` (hệ 2) = `16 + 8 + 1 = 25` (hệ 10).

### Câu 61
Assume we have the following code:
```c
int i = 4;
int *p = &i;
```
What is the result of the following expression: `++*p`?
A. 5
B. 4
C. 9
D. 12
> **Giải thích:**
> **Đáp án đúng là A.** Do độ ưu tiên, `*p` được thực hiện trước, trả về giá trị của `i`, là 4. Sau đó, toán tử tăng tiền tố (`++`) được áp dụng, làm tăng giá trị này lên 5. Giá trị của biến `i` cũng sẽ được cập nhật thành 5. Biểu thức trả về giá trị sau khi tăng, là 5.

### Câu 62
Assume we have a snippet of code in C:
```c
int main() {
    int *p = NULL;
    printf("%d", p);
    getchar();
    return 0;
}
```
The output will be:
A. 0
B. 1
C. 10
D. 100
> **Giải thích:**
> **Đáp án đúng là A.** Trong C, `NULL` là một macro thường được định nghĩa là `(void*)0` hoặc `0`. Khi in một con trỏ `NULL` bằng đặc tả `%d` (dù không phải là cách làm đúng chuẩn), nó sẽ in ra giá trị số nguyên tương ứng, là 0.

### Câu 63
What will be the output of the following program?
```c
void func(int *p) {
    int j = 11;
    *p = j;
}
int main() {
    int i = 1;
    int *p = &i;
    func(p);
    printf("%d,%d", i, *p);
    getchar();
    return 0;
}
```
A. 11,11
B. 1,1
C. 0,0
D. 0,1
> **Giải thích:**
> **Đáp án đúng là A.**
> 1.  Trong `main`, `i = 1` và `p` trỏ đến `i`.
> 2.  Hàm `func` được gọi với `p` (địa chỉ của `i`).
> 3.  Bên trong `func`, `*p = j;` có nghĩa là "gán giá trị của `j` (là 11) vào ô nhớ mà `p` đang trỏ tới". Điều này làm thay đổi giá trị của `i` trong `main` thành 11.
> 4.  Khi quay trở lại `main`, `i` bây giờ là 11, và `*p` (giá trị mà `p` trỏ tới) cũng là 11. Do đó, `11,11` được in ra.

### Câu 64
What is the output of the following code snippet?
```c
#include <stdio.h>
int num(int a, int b) {
    int sum;
    sum = a + b;
    return sum;
}
int main() {
    int a, b, result;
    a = 10;
    b = 12;
    result = num(a, b);
    printf("%d", result);
    return 0;
}
```
A. 22
B. 10
C. 12
D. 21
> **Giải thích:**
> **Đáp án đúng là A.** Hàm `num` nhận hai số nguyên `a` và `b`, tính tổng của chúng và trả về kết quả. Trong `main`, `num(10, 12)` được gọi, trả về 22. Giá trị này được gán cho `result` và sau đó được in ra màn hình.

### Câu 65
What is the value of `z` after the `int a = 8, b = 6, c = 4; z = b++ * ++c + --a;` command?
A. 16
B. 28
C. 37
D. 32
E. 38
> **Giải thích:**
> **Đáp án đúng là C.**
> 1.  **Thứ tự ưu tiên:** Các toán tử tiền tố (`++c`, `--a`) được thực hiện trước.
>     *   `++c`: `c` tăng lên 5.
>     *   `--a`: `a` giảm xuống 7.
> 2.  **Phép nhân:** `b++ * c`. Toán tử hậu tố `b++` sử dụng giá trị hiện tại của `b` (là 6) cho phép nhân, *sau đó* mới tăng `b` lên 7.
>     *   `6 * 5 = 30`.
> 3.  **Phép cộng:** `30 + a`. Giá trị của `a` đã là 7.
>     *   `30 + 7 = 37`.
> Vậy `z` sẽ có giá trị là 37.

### Câu 66
What is the result when converting 01001010 from the binary system to the decimal system?
A. 78
B. 76
C. 74
D. 72
> **Giải thích:**
> **Đáp án đúng là C.**
> `01001010` = 0*2⁷ + 1*2⁶ + 0*2⁵ + 0*2⁴ + 1*2³ + 0*2² + 1*2¹ + 0*2⁰
> = 64 + 0 + 0 + 8 + 0 + 2 + 0 = 74.

### Câu 67
What will be the output of the following program?
```c
int main() {
    int i = 101;
    int *p = &i;
    printf("%d\n", *p++);
    return 0;
}
```
A. 101
B. 102
C. 0
D. Address of i
> **Giải thích:**
> **Đáp án đúng là A.** Do độ ưu tiên của toán tử, `p++` (toán tử tăng hậu tố) có độ ưu tiên cao hơn `*` (toán tử tham chiếu ngược). Tuy nhiên, vì là hậu tố, nó sẽ trả về giá trị *hiện tại* của `p` để `*` sử dụng, *sau đó* mới tăng địa chỉ của `p`.
> 1.  Biểu thức `*p++` được hiểu là `*(p++)`.
> 2.  `p++` trả về địa chỉ của `i`.
> 3.  `*` lấy giá trị tại địa chỉ của `i`, là 101.
> 4.  `printf` in ra 101.
> 5.  Sau đó, `p` được tăng lên để trỏ đến vị trí bộ nhớ tiếp theo.

### Câu 68
Assume we have the following code:
```c
double d = 9;
double *p = &d;
```
Suppose that a `double` occupies 8 bytes of memory, and the address of `d` is 1200. What is the result of the expression `p + 8`?
A. 1264
B. 1200
C. 1208
D. 1209
> **Giải thích:**
> **Đáp án đúng là A.** Phép cộng con trỏ (pointer arithmetic) hoạt động theo đơn vị kích thước của kiểu dữ liệu mà nó trỏ tới.
> *   `p + 8` có nghĩa là `địa_chỉ_của_p + 8 * sizeof(double)`.
> *   `1200 + 8 * 8 = 1200 + 64 = 1264`.

### Câu 69
What will be the output of the following C code?
```c
#include <stdio.h>
void main() {
    int total = 0;
    for (int s = 1; s < 15; s++) {
        total = total + s;
    }
    printf("%d", total);
}
```
A. 105
B. 150
C. 120
D. 210
> **Giải thích:**
> **Đáp án đúng là A.** Đoạn mã này tính tổng các số từ 1 đến 14.
> Tổng của một chuỗi số tự nhiên từ 1 đến `n` được tính bằng công thức `n * (n + 1) / 2`.
> Ở đây, `n = 14`.
> `14 * (14 + 1) / 2 = 14 * 15 / 2 = 210 / 2 = 105`.

### Câu 70
What will be the output of the following C code?
```c
#include <stdio.h>
void main() {
    char result = 125;
    result = result + 5;
    printf("%d", result);
}
```
A. 130
B. -130
C. 126
D. -126
> **Giải thích:**
> **Đáp án đúng là D.** Kiểu `char` trong hầu hết các trình biên dịch C là kiểu số nguyên có dấu (signed char) 8-bit, có dải giá trị từ -128 đến 127.
> 1.  `result = 125 + 5 = 130`.
> 2.  Giá trị 130 vượt quá giới hạn trên (127), gây ra hiện tượng tràn số (integer overflow).
> 3.  130 trong hệ nhị phân 8-bit là `10000010`.
> 4.  Trong biểu diễn bù hai, vì bit đầu tiên là 1, đây là một số âm. Giá trị của nó là `-(2⁸ - 130) = -(256 - 130) = -126`.

### Câu 71
What will be the output of the C program?
```c
int arr[5] = {2, 3, 5, 4, 7};
int *ptr = (&arr + 1);
printf("%d %d\n", *(arr + 1), *(ptr - 1));
```A. 2 3
B. 3 2
C. 3 7
D. An address followed by 7
> **Giải thích:**
> **Đáp án đúng là C.**
> *   `&arr` là con trỏ trỏ đến toàn bộ mảng `int[5]`. Kiểu của nó là `int (*)[5]`.
> *   `(&arr + 1)` thực hiện phép cộng con trỏ, di chuyển con trỏ đến vị trí bộ nhớ ngay sau khi mảng `arr` kết thúc.
> *   `ptr = (&arr + 1);`: Gán địa chỉ này cho `ptr`. `ptr` lúc này là một con trỏ kiểu `int*` trỏ đến vị trí "ngoài mảng".
> *   `*(arr + 1)`: tương đương `arr[1]`, có giá trị là `3`.
> *   `*(ptr - 1)`: `ptr - 1` sẽ di chuyển con trỏ `ptr` lùi lại một đơn vị `int`, trỏ đến phần tử cuối cùng của mảng `arr`, tức `arr[4]`. Giá trị của `arr[4]` là `7`.
> Do đó, kết quả in ra là `3 7`.

### Câu 73
What will be the output of the following code snippet?
```c
#include <stdlib.h>
#include <stdio.h>
int main() {
    int a = 5;
    {
        int a = 10;
        printf("%d ", a);
    }
    printf("%d", a);
    return 0;
}
```
A. 10 5
B. 5 10
C. 5 5
D. 10 10
> **Giải thích:**
> **Đáp án đúng là A.** Biến `a` được khai báo hai lần ở hai phạm vi (scope) khác nhau.
> 1.  Bên trong khối `{ ... }`, `a = 10` là một biến cục bộ, nó che (shadows) biến `a` bên ngoài. `printf` đầu tiên sẽ in ra giá trị của biến cục bộ này, là `10`.
> 2.  Sau khi khối lệnh kết thúc, biến `a = 10` bị hủy.
> 3.  `printf` thứ hai nằm ngoài khối, nó sẽ tham chiếu đến biến `a = 5` được khai báo ở đầu hàm `main`. Kết quả là `5`.
> Vậy, output là `10 5`.

### Câu 74
What is the output of the following code snippet?
```c
#include <stdio.h>
int x = 9; // Global variable
void someFunction() {
    int x = 8; // Local variable
    printf("%d ", x);
}
int main() {
    someFunction();
    printf("%d", x);
    return 0;
}
```
A. 8 9
B. 9 8
C. 8 8
D. 9 9
> **Giải thích:**
> **Đáp án đúng là A.**
> 1.  Trong hàm `someFunction`, biến cục bộ `x = 8` được ưu tiên sử dụng. `printf` đầu tiên in ra `8`.
> 2.  Trong hàm `main`, `printf` thứ hai tham chiếu đến biến toàn cục `x = 9` vì không có biến cục bộ nào tên `x` trong `main`. Kết quả là `9`.
> Vậy, output là `8 9`.

### Câu 75
What will be the output of the following C code?```c
#include <stdio.h>
void main() {
    int *ptr, a = 10;
    ptr = &a;
    *ptr += 1;
    printf("%d, %d\n", *ptr, a);
}
```
A. 10, 10
B. 10, 11
C. 11, 10
D. 11, 11
> **Giải thích:**
> **Đáp án đúng là D.**
> *   `ptr = &a;`: Con trỏ `ptr` bây giờ chứa địa chỉ của biến `a`.
> *   `*ptr += 1;`: Lệnh này có nghĩa là "lấy giá trị tại địa chỉ mà `ptr` đang trỏ tới (tức là giá trị của `a`), cộng thêm 1, rồi gán kết quả ngược lại vào chính ô nhớ đó".
> *   Do đó, giá trị của `a` được tăng từ 10 lên 11.
> *   `printf` sẽ in ra giá trị của `*ptr` (là 11) và giá trị của `a` (cũng là 11).

### Câu 76
What is the result of the `printf("%d %d", 12 & 5, 12 | 5);` command?
A. 4 13
B. 5 12
C. 4 12
D. 5 13
> **Giải thích:**
> **Đáp án đúng là A.**
> *   **Phép AND trên bit (`&`):**
>     *   `12` = `1100`
>     *   `5`  = `0101`
>     *   `1100 & 0101` = `0100` = `4` (hệ 10).
> *   **Phép OR trên bit (`|`):**
>     *   `12` = `1100`
>     *   `5`  = `0101`
>     *   `1100 | 0101` = `1101` = `8 + 4 + 1 = 13` (hệ 10).
> Vậy kết quả là `4 13`.

### Câu 77
What will be the output of the following program?
```c
int main() {
    int i = 100;
    int *p = &i;
    *p += 2;
    printf("%d, %d", i, *p);
    getchar();
    return 0;
}
```
A. 102, 102
B. 100, 102
C. 100, 100
D. 102, 100
> **Giải thích:**
> **Đáp án đúng là A.** Lệnh `*p += 2;` làm thay đổi giá trị của ô nhớ mà `p` trỏ tới, tức là thay đổi giá trị của `i`. `i` sẽ tăng từ 100 lên 102. Do đó, cả `i` và `*p` đều có giá trị là 102 khi in ra.

### Câu 80
What are the results that will be displayed on the screen after executing the following code:
```c
char s[] = "AbCd";
printf("%d; %d; %d; %d", s[1], s[2], s[3], s[4]);
```
A. 97; 98; 99; 100
B. 65; 66; 67; 68
C. 65; 98; 67; 100
D. 98; 67; 100; 0
> **Giải thích:**
> **Đáp án đúng là D.**
> *   Mảng `s` chứa: `s[0]='A'`, `s[1]='b'`, `s[2]='C'`, `s[3]='d'`, `s[4]='\0'`.
> *   Đặc tả `%d` sẽ in ra mã ASCII của các ký tự.
> *   `s[1]` là `'b'`, mã ASCII là 98.
> *   `s[2]` là `'C'`, mã ASCII là 67.
> *   `s[3]` là `'d'`, mã ASCII là 100.
> *   `s[4]` là ký tự null `\0`, mã ASCII là 0.
> Vậy kết quả là `98; 67; 100; 0`.

### Câu 81
What is the output when the sample code below is executed?
```c
#include <stdio.h>
int main() {
    int i = 10;
    do {
        printf("%d ", i);
        i -= 2;
    } while (i >= 1);
    return 0;
}
```
A. 10 8 6 4 2
B. 10 8 6 4 2 0
C. 10 8 6 4 2 0 -2 ...
D. 10 9 8 7 6 5 4 3 2 1
> **Giải thích:**
> **Đáp án đúng là A.** Vòng lặp `do-while` sẽ in ra giá trị của `i` rồi giảm `i` đi 2. Vòng lặp tiếp tục khi `i >= 1`.
> *   Lần 1: in `10`, `i` thành 8.
> *   Lần 2: in `8`, `i` thành 6.
> *   Lần 3: in `6`, `i` thành 4.
> *   Lần 4: in `4`, `i` thành 2.
> *   Lần 5: in `2`, `i` thành 0.
> *   Sau đó, điều kiện `i >= 1` (0 >= 1) là sai, vòng lặp kết thúc.
> Vậy output là `10 8 6 4 2`.

### Câu 82
What is the result displayed on the screen of the following program?
```c
#include <stdio.h>
int main(void) {
    int a[] = {1, 2, 3, 5, 6, 7};
    for (int i = 0; i < 6; ++i)
        printf("%3d", a[i/2]);
    return 0;
}
```
A. 1 1 2 3 3 4
B. 1 1 2 2 3 3
C. 1 2 3 5 6 7
D. 0 1 1 2 2 3
> **Giải thích:**
> **Đáp án đúng là B (diễn giải lại từ OCR).** Vòng lặp chạy 6 lần, với `i` từ 0 đến 5. Chỉ số của mảng là `i/2` (phép chia số nguyên).
> *   i=0: `a[0/2]` -> `a[0]` -> in `1`
> *   i=1: `a[1/2]` -> `a[0]` -> in `1`
> *   i=2: `a[2/2]` -> `a[1]` -> in `2`
> *   i=3: `a[3/2]` -> `a[1]` -> in `2`
> *   i=4: `a[4/2]` -> `a[2]` -> in `3`
> *   i=5: `a[5/2]` -> `a[2]` -> in `3`
> Vậy output là `1 1 2 2 3 3`.

### Câu 84
What does the following code print?
```c
float a = 3.0;
float b = 2.0;
int r = a % b;
printf("%d", r);
```
A. Compiler error
B. 1.000000
C. 1
> **Giải thích:**
> **Đáp án đúng là A.** Toán tử modulo (`%`) trong C chỉ có thể được áp dụng cho các toán hạng kiểu số nguyên (integer). Việc sử dụng nó với các toán hạng kiểu `float` hoặc `double` sẽ gây ra lỗi biên dịch (compiler error).

### Câu 85
What will be the result displayed on the screen after executing the following code?
```c
int a[] = {1, 2, 3, 4};
int i = 0, s = 0;
for (; a[i]; ++i)
    s += a[i];
printf("%d", s);
```
A. 10
B. Compiler error
C. Runtime error
D. Garbage value
> **Giải thích:**
> **Đáp án đúng là B hoặc C/D.** Đoạn mã này có hành vi không xác định (undefined behavior).
> *   Điều kiện lặp `a[i]` sẽ đúng khi `a[i]` khác 0.
> *   Mảng `a` có 4 phần tử. Vòng lặp sẽ chạy cho `i=0,1,2,3` và cộng `1+2+3+4=10` vào `s`.
> *   Khi `i=4`, `a[4]` là một truy cập ngoài giới hạn (out-of-bounds access). Giá trị tại đây là không xác định (garbage).
> *   Nếu giá trị rác đó là 0, vòng lặp dừng và in ra 10.
> *   Nếu nó khác 0, vòng lặp tiếp tục, dẫn đến lỗi runtime hoặc kết quả không đoán trước.
> Do đó, mã này không an toàn. Lựa chọn "Compiler error" có thể không đúng vì một số trình biên dịch có thể chỉ cảnh báo. Lựa chọn đúng nhất là "Runtime error" hoặc "Garbage value".

### Câu 86
What will be the output of the C program?
```c
#include<stdio.h>
void myFunction(int i) {
    printf("%d", i);
}
int main() {
    myFunction();
    return 0;
}
```
A. 0
B. 2
C. Compiler error
D. 4
> **Giải thích:**
> **Đáp án đúng là C.** Hàm `myFunction` được khai báo là nhận một tham số kiểu `int`, nhưng khi gọi trong `main`, không có đối số nào được truyền vào (`myFunction();`). Điều này không khớp với khai báo và sẽ gây ra lỗi biên dịch (compiler error).

### Câu 87
How many times will a `do-while` loop execute its code if the condition is false from the beginning?
A. 1
B. 0
C. Loop infinitely
D. Compile time error
> **Giải thích:**
> **Đáp án đúng là A.** Vòng lặp `do-while` có đặc điểm là luôn thực thi khối lệnh bên trong *ít nhất một lần*, sau đó mới kiểm tra điều kiện lặp.

### Câu 88
What is the output when the sample code below is executed?
```c
#include <stdio.h>
int main() {
    20 > 30 ? return 1 : return 2;
}
```
A. Compile time error
B. 1
C. 2
D. "return 1:return 2"
> **Giải thích:**
> **Đáp án đúng là A.** Các biểu thức sau `?` và `:` trong toán tử ba ngôi phải là các giá trị hoặc biểu thức trả về giá trị, không thể là các câu lệnh như `return`. Cú pháp này sẽ gây ra lỗi biên dịch (compile time error).

### Câu 89
What does the following program display?
```c
#include <stdio.h>
int main() {
    int x[] = {1, 2, 3, 4, 5};
    int y = 3;
    printf("%d", x[y]);
    return 0;
}
```
A. 2
B. 3
C. 4
D. An error will be raised.
> **Giải thích:**
> **Đáp án đúng là C.** Lệnh `printf` sẽ in ra giá trị của `x[y]`, tức là `x[3]`. Trong mảng `x`, phần tử có chỉ số 3 là số 4 (`x[0]=1, x[1]=2, x[2]=3, x[3]=4`).

### Câu 90
What will be the output of the C program?
```c
int default = 5, a = 3;
if (a > 2)
    printf("%d", default);
```
A. 2
B. 5
C. Compilation error
D. 3
> **Giải thích:**
> **Đáp án đúng là C.** `default` là một từ khóa (keyword) được sử dụng trong cấu trúc `switch-case` của C. Nó không thể được dùng làm tên biến. Đoạn mã này sẽ gây ra lỗi biên dịch (compilation error).

### Câu 91
What is the output when the sample code below is executed?
```c
#include<stdio.h>
int main() {
    const int a = 5;
    if (a > 3) {
        a++;
        break;
    } else {
        a--;
    }
    printf("%d", a);
    return 0;
}
```
A. Compile time error
B. 6
C. 4
D. 5
> **Giải thích:**
> **Đáp án đúng là A.** Biến `a` được khai báo là một hằng số (`const int`). Lệnh `a++` và `a--` cố gắng thay đổi giá trị của một hằng số, điều này là không được phép và sẽ gây ra lỗi biên dịch (compile time error). Ngoài ra, `break` chỉ có thể được dùng trong vòng lặp hoặc `switch`.

### Câu 92
What is the output of the following code snippet?
```c
void main() {
    int const *p = 5;
    printf("%d", ++(*p));
    getchar();
}
```
A. Compile error
B. 5
C. NULL
D. 6
> **Giải thích:**
> **Đáp án đúng là A.** Có hai lỗi ở đây:
> 1.  `int const *p = 5;`: Dòng này cố gắng gán một giá trị số nguyên (`5`) cho một con trỏ. Con trỏ phải được gán một địa chỉ.
> 2.  Ngay cả khi nó được gán đúng (ví dụ: `int x=5; int const *p = &x;`), `int const *p` khai báo một con trỏ tới một số nguyên không đổi. Lệnh `++(*p)` cố gắng thay đổi giá trị mà `p` trỏ tới, điều này vi phạm khai báo `const` và gây ra lỗi biên dịch.

### Câu 93
What will be the output of the following C code?
```c
#include <stdio.h>
void main() {
    int k = 5;
    int *p = &k;
    int **m = &p;
    **m = 6;
    printf("%d\n", k);
}
```
A. 5
B. Run time error
C. 6
D. Junk
> **Giải thích:**
> **Đáp án đúng là C.**
> *   `p` trỏ đến `k`.
> *   `m` là con trỏ trỏ đến con trỏ `p`.
> *   `*m` sẽ trả về giá trị của `p`, tức là địa chỉ của `k`.
> *   `**m` (tức `*(*m)`) sẽ trả về giá trị tại địa chỉ của `k`.
> *   Lệnh `**m = 6;` gán giá trị 6 vào ô nhớ mà `m` trỏ tới gián tiếp, tức là thay đổi giá trị của `k` thành 6.

### Câu 94
What is the output of the following code snippet?
```c
#include <stdio.h>
int change(int a) {
    a = 10;
    return a;
}
void main() {
    int i = 5;
    change(i);
    printf("%d", i);
}
```
A. 10
B. 5
C. 15
D. Compiler error
> **Giải thích:**
> **Đáp án đúng là B.** Ngôn ngữ C sử dụng cơ chế truyền tham trị (pass-by-value) cho các tham số hàm.
> 1.  Khi gọi `change(i)`, một bản sao của giá trị của `i` (là 5) được tạo và truyền vào hàm.
> 2.  Bên trong hàm `change`, biến cục bộ `a` (là bản sao) được thay đổi thành 10.
> 3.  Điều này không ảnh hưởng gì đến biến `i` gốc trong hàm `main`.
> 4.  Do đó, `printf` trong `main` vẫn in ra giá trị ban đầu của `i`, là 5.

### Câu 95
What is the output of the following code if the user enters the value "20" followed by Enter?
```c
int n;
char c;
scanf("%d", &n);
c = getchar();
printf("'%d'", c);
```
A. 10
B. 20
C. ' ' (space)
D. An undefined value
> **Giải thích:**
> **Đáp án đúng là A (giá trị ASCII của newline).**
> 1.  `scanf("%d", &n);` đọc số `20` từ input.
> 2.  Khi người dùng nhấn Enter, ký tự newline (`\n`) vẫn còn lại trong bộ đệm đầu vào (input buffer).
> 3.  `c = getchar();` sẽ đọc ký tự tiếp theo trong bộ đệm, chính là ký tự `\n`.
> 4.  `printf("'%d'", c)` in ra giá trị số nguyên (mã ASCII) của ký tự `c`. Mã ASCII của `\n` là 10.

### Câu 96
What will be the output of the following code snippet?
```c
#include<stdio.h>
int main() {
    const int *p;
    int a = 100;
    p = &a;
    printf("%d", *p);
    return 0;
}
```
A. 100
B. 0
C. 101
D. Compile error
> **Giải thích:**
> **Đáp án đúng là A.** Khai báo `const int *p` có nghĩa là "p là một con trỏ tới một số nguyên không đổi". Điều này có nghĩa là bạn không thể thay đổi giá trị của `a` *thông qua* con trỏ `p` (ví dụ: `*p = 5;` sẽ lỗi). Tuy nhiên, bạn hoàn toàn có thể đọc giá trị đó. Lệnh `printf` chỉ đọc giá trị tại địa chỉ `p` đang trỏ tới (là `a`), do đó nó sẽ in ra 100.

### Câu 97
What will be the output of the following program?
```c
int main() {
    int i = 1;
    int *p = &i;
    int **k = &p;
    i += 2;
    printf("%d %d %d", *p, **k, *(*k));
    getchar();
    return 0;
}
```
A. 3 3 3
B. 1 1 1
C. 2 2 2
D. Compile error
> **Giải thích:**
> **Đáp án đúng là A.**
> 1.  `i` ban đầu là 1. `p` trỏ đến `i`. `k` trỏ đến `p`.
> 2.  `i += 2;` làm `i` tăng lên 3.
> 3.  Bây giờ ta phân tích các biểu thức trong `printf`:
>     *   `*p`: Giá trị tại địa chỉ `p` trỏ tới, chính là `i`, bằng 3.
>     *   `**k`: `*k` là `p`, `*(*k)` là `*p`, chính là `i`, bằng 3.
>     *   `*(*k)`: Giống hệt biểu thức trên, bằng 3.
> 4.  Do đó, chương trình sẽ in ra `3 3 3`.

### Câu 98
What will be the output of the following C code?
```c
#include <stdio.h>
void main() {
    int i = 10, j = 3, k = 3;
    printf("%d %d ", i, j, k);
}
```
A. Compile time error
B. 10 3 3
C. 10 3
D. 10 3 some_garbage_value
> **Giải thích:**
> **Đáp án đúng là C.** Hàm `printf` sẽ xử lý các đối số dựa trên chuỗi định dạng.
> *   Chuỗi định dạng là `"%d %d "`. Nó chỉ yêu cầu hai đối số kiểu `int`.
> *   `printf` sẽ lấy hai đối số đầu tiên được cung cấp là `i` và `j`.
> *   Đối số thứ ba, `k`, sẽ bị bỏ qua vì không có đặc tả định dạng nào cho nó.
> *   Kết quả in ra là `10 3`.

### Câu 99
What will be the output of the C program?
```c
int 2_var = 15;
printf("%d", 2_var);
```
A. 0
B. 15
C. Compilation error
D. Runtime error
> **Giải thích:**
> **Đáp án đúng là C.** Tên biến trong C không được phép bắt đầu bằng một chữ số. `2_var` là một tên biến không hợp lệ và sẽ gây ra lỗi biên dịch (compilation error).

### Câu 100
What will be the result displayed on the screen after executing the following code:
```c
int a[] = {1, 2, 3, 4};
int i = 0, s = 0;
for (; a[i]; ++i)
    s += a[i];
printf("%d", s);
```
A. 10
B. Compiler error
C. Runtime error or Undefined behavior
D. Garbage value
> **Giải thích:**
> **Đáp án đúng là C.** Đoạn mã này có hành vi không xác định (undefined behavior).
> *   Điều kiện lặp `a[i]` sẽ đúng khi `a[i]` khác 0.
> *   Mảng `a` có 4 phần tử. Vòng lặp sẽ chạy cho `i=0,1,2,3` và cộng `1+2+3+4=10` vào `s`.
> *   Khi `i=4`, `a[4]` là một truy cập ngoài giới hạn (out-of-bounds access). Giá trị tại đây là không xác định (garbage).
> *   Nếu giá trị rác đó tình cờ là 0, vòng lặp dừng và in ra 10.
> *   Nếu nó khác 0, vòng lặp tiếp tục, dẫn đến lỗi runtime (ví dụ: segmentation fault) hoặc kết quả không đoán trước. Do tính không an toàn này, "Runtime error" hoặc "Undefined behavior" là mô tả chính xác nhất.

# References

