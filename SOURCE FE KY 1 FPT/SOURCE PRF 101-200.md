
2025-08-07 20:40

Status:

Tags: [[source]]  [[PRF]]
Disable spell check :`teh`
# SOURCE PRF 101-200


## III. Ngân hàng câu hỏi trắc nghiệm (Câu 101 - 200)

### Câu 101
Given the following code snippet:
```c
#include <stdio.h>
#define MONTHS_IN_YEAR 12

int main() {
    const int WORKING_DAYS = 22;
    printf("%d", MONTHS_IN_YEAR);
    printf("%d", WORKING_DAYS);
    return 0;
}
```
Choose the correct statement:
A. The output will be: 1222
B. No output
C. Compile error
D. Runtime error
> **Giải thích:**
> **Đáp án đúng là A.**
> *   `#define MONTHS_IN_YEAR 12` là một macro tiền xử lý, nó sẽ thay thế tất cả các lần xuất hiện của `MONTHS_IN_YEAR` bằng `12` trước khi biên dịch.
> *   `const int WORKING_DAYS = 22;` khai báo một hằng số.
> *   Hai lệnh `printf` không có ký tự xuống dòng (`\n`) hay khoảng trắng, do đó chúng sẽ in ra các giá trị liền nhau. Kết quả là `1222`.

### Câu 102
What is the output when the sample code below is executed?
```c
#include <stdio.h>
int main() {
    int n = 50, m = 60;
    if (n > 50)
        if (m > 50)
            printf("True");
    else
        printf("False");
    return 0;
}
```
A. No output
B. True
C. False
D. Compile time error
> **Giải thích:**
> **Đáp án đúng là A.**
> 1.  Câu lệnh `if` đầu tiên, `if (n > 50)`, có điều kiện là `50 > 50`, kết quả là `false`.
> 2.  Do điều kiện của `if` đầu tiên là `false`, toàn bộ khối lệnh bên trong nó (bao gồm cả `if (m > 50)` và `else`) sẽ bị bỏ qua.
> 3.  Chương trình không thực hiện bất kỳ lệnh `printf` nào, do đó không có gì được in ra màn hình.

### Câu 103
What does the following code print?
```c
int i = 0;
while (i < 5) {
    printf("%d ", i);
    i--;
}
```
A. infinite loop
B. 0 1 2 3 4
C. 5 4 3 2 1 0
D. 0
> **Giải thích:**
> **Đáp án đúng là A.**
> *   Vòng lặp bắt đầu với `i = 0`.
> *   Điều kiện `i < 5` là đúng.
> *   `printf` in ra `0`.
> *   `i--` làm `i` giảm xuống `-1`.
> *   Trong các lần lặp tiếp theo, `i` sẽ tiếp tục giảm (`-2`, `-3`, ...). Giá trị của `i` sẽ luôn nhỏ hơn 5.
> *   Do đó, điều kiện của vòng lặp `while` sẽ không bao giờ sai, tạo ra một vòng lặp vô hạn (infinite loop).

### Câu 104
What does the following code print?
```c
#include <stdio.h>
void swap(int a, int *b) {
    int temp = a;
    a = *b;
    *b = temp;
}
int main() {
    int x = 5;
    int y = 10;
    swap(x, &y);
    printf("x = %d, y = %d\n", x, y);
    return 0;
}
```
A. x = 5, y = 5
B. Compiler error
C. x = 5, y = 10
D. x = 10, y = 5
> **Giải thích:**
> **Đáp án đúng là A (diễn giải lại từ OCR).**
> *   Trong `main`, `swap(x, &y)` được gọi.
> *   Bên trong `swap`, `a` nhận một bản sao của `x` (giá trị là 5). `b` nhận địa chỉ của `y`.
> *   `temp = a;` -> `temp = 5`.
> *   `a = *b;` -> `a` (bản sao cục bộ) nhận giá trị của `y` (là 10). `a` trở thành 10.
> *   `*b = temp;` -> giá trị tại ô nhớ của `y` được thay đổi thành `temp` (là 5). `y` trong `main` bây giờ là 5.
> *   Biến `x` trong `main` không hề thay đổi.
> *   Do đó, kết quả in ra là `x = 5, y = 5`.

### Câu 105
What will be the output of the following code?
```c
printf("%c", tolower('C'));
```
A. 'c'
B. 'C'
C. 'c' or 'C' (depending on IDE)
D. Compilation error
> **Giải thích:**
> **Đáp án đúng là A.** Hàm `tolower()` trong thư viện `<ctype.h>` sẽ chuyển đổi một ký tự chữ hoa thành chữ thường tương ứng. `tolower('C')` sẽ trả về `'c'`.

### Câu 106
What is the issue with the following code?
```c
char str[1];
gets(str);
printf("%s", str);
```
A. Runtime error (Buffer Overflow)
B. Logical error
C. Compilation error
D. No issue
> **Giải thích:**
> **Đáp án đúng là A.** Mảng `str` chỉ có thể chứa 1 ký tự (là ký tự `\0`). Hàm `gets()` không kiểm tra kích thước bộ đệm, nếu người dùng nhập bất kỳ ký tự nào, nó sẽ ghi đè lên vùng nhớ không thuộc về `str`, gây ra lỗi tràn bộ đệm (Buffer Overflow), một dạng lỗi thực thi (runtime error) nghiêm trọng.

### Câu 108
What represents dynamic allocation in C?
A. `int* a = (int*)malloc(5*sizeof(int));`
B. `int a[5];`
C. `int a[5][5];`
D. `free(a);`
> **Giải thích:**
> **Đáp án đúng là A.** Hàm `malloc` (memory allocation) được sử dụng để cấp phát động (dynamic allocation) một khối bộ nhớ. Lựa chọn B và C là cấp phát tĩnh. Lựa chọn D là hàm để giải phóng bộ nhớ đã được cấp phát động.

### Câu 109
Given a matrix named `mat` with dimensions 6x6, what is the correct way to access the element in the last row and last column?
A. `mat[5][5]`
B. `mat[5][6]`
C. `mat[6][5]`
D. `mat[-1][-1]`
> **Giải thích:**
> **Đáp án đúng là A.** Mảng trong C có chỉ số bắt đầu từ 0. Một mảng có 6 hàng sẽ có chỉ số hàng từ 0 đến 5. Tương tự, 6 cột sẽ có chỉ số cột từ 0 đến 5. Do đó, phần tử cuối cùng nằm ở `mat[5][5]`.

### Câu 110
Which of the following correctly represents the updated array after the execution of the below code?
```c
int a[] = {1, 2, 3, 4, 5};
int i;
for (i = 2; i < 4; i++) {
    a[i] = a[i + 1];
}
```
A. `{1, 2, 4, 5, 5}`
B. `{1, 2, 4, 5}`
C. `{1, 3, 4, 5}`
D. `{1, 2, 3, 4}`
> **Giải thích:**
> **Đáp án đúng là A.**
> *   Ban đầu: `a = {1, 2, 3, 4, 5}`
> *   Khi `i = 2`: `a[2] = a[3]`. Mảng trở thành `{1, 2, 4, 4, 5}`.
> *   Khi `i = 3`: `a[3] = a[4]`. Mảng trở thành `{1, 2, 4, 5, 5}`.
> *   Vòng lặp kết thúc.

### Câu 111
Consider the following array of integers: `{8, 1, 2, 7, 9}`. What will be the state of the array after one pass of selection sort?
A. `{1, 8, 2, 7, 9}`
B. `{8, 1, 2, 7, 9}`
C. `{1, 2, 8, 7, 9}`
D. `{1, 2, 7, 8, 9}`
> **Giải thích:**
> **Đáp án đúng là A.** Thuật toán sắp xếp chọn (selection sort) trong lượt đầu tiên sẽ:
> 1.  Tìm phần tử nhỏ nhất trong toàn bộ mảng. Ở đây là `1`.
> 2.  Hoán đổi (swap) phần tử nhỏ nhất đó với phần tử ở vị trí đầu tiên (là `8`).
> 3.  Kết quả sau một lượt là `{1, 8, 2, 7, 9}`.

### Câu 112
Consider the following program. What is the result displayed on the screen?
```c
#include<stdio.h>
void updatePosition(int *time, float* position, float v) {
    if ((*position < 5) && (*position > -5))
        *position += v;
    else
        *position += -0.1 * (*position);
    (*time) += 1;
}

int main() {
    float p = 4.0, v = 1;
    int t = 0;
    printf("t = %d, p = %f\n", t, p);
    updatePosition(&t, &p, v);
    updatePosition(&t, &p, v);
    printf("t = %d, p = %f\n", t, p);
}
```
A. t = 0, p = 4.000000, t = 2, p = 5.000000
B. t = 0, p = 4.000000, t = 2, p = 4.500000
C. t = 0, p = 4.000000, t = 0, p = 5.000000
D. Compile error.
> **Giải thích:**
> **Đáp án đúng là B.**
> *   Ban đầu: `t=0`, `p=4.0`. Dòng `printf` đầu tiên in ra `t = 0, p = 4.000000`.
> *   **Lần gọi `updatePosition` thứ nhất:**
>     *   `p` (4.0) < 5 là đúng, nên `p = p + v = 4.0 + 1.0 = 5.0`.
>     *   `t` tăng lên 1.
> *   **Lần gọi `updatePosition` thứ hai:**
>     *   `p` (5.0) < 5 là sai. Nhánh `else` được thực hiện: `p = p + (-0.1 * p) = 5.0 - 0.5 = 4.5`.
>     *   `t` tăng lên 2.
> *   Dòng `printf` thứ hai in ra giá trị cuối cùng của `t` và `p`: `t = 2, p = 4.500000`.

### Câu 113
What is the size of the `char` data type in bytes?
A. 1 byte
B. 2 bytes
C. 4 bytes
D. It depends on the system
> **Giải thích:**
> **Đáp án đúng là A.** Theo tiêu chuẩn của ngôn ngữ C, kiểu `char` được đảm bảo có kích thước là 1 byte.

### Câu 114
What is the size of a `float` variable in bytes?
A. 2 bytes
B. 1 byte
C. 8 bytes
D. 4 bytes
> **Giải thích:**
> **Đáp án đúng là D.** Trong hầu hết các hệ thống hiện đại, một biến kiểu `float` (số thực độ chính xác đơn) chiếm 4 bytes bộ nhớ.

### Câu 116
What is the maximum size required to store the string "Hello" in C?
A. 5 bytes
B. 6 bytes
C. 4 bytes
D. 10 bytes
> **Giải thích:**
> **Đáp án đúng là B.** Chuỗi "Hello" có 5 ký tự. Trong C, một chuỗi ký tự phải được kết thúc bằng một ký tự null `\0` để các hàm xử lý chuỗi biết điểm kết thúc. Do đó, cần `5 (ký tự) + 1 (ký tự null) = 6` bytes.

### Câu 117
What is the maximum size of a `double` variable?
A. 8 bytes
B. 4 bytes
C. 2 bytes
D. 16 bytes
> **Giải thích:**
> **Đáp án đúng là A.** Trong hầu hết các hệ thống hiện đại, một biến kiểu `double` (số thực độ chính xác kép) chiếm 8 bytes bộ nhớ.

### Câu 118
What is the result of `floor(-5.9)` and `floor(5.9)`?
A. -6.0 and 5.0
B. -5.0 and 5.0
C. -6.0 and 6.0
D. -5.0 and 6.0
> **Giải thích:**
> **Đáp án đúng là A.** Hàm `floor()` (sàn) làm tròn một số thực xuống số nguyên gần nhất nhỏ hơn hoặc bằng nó.
> *   `floor(-5.9)` -> -6.0
> *   `floor(5.9)` -> 5.0

### Câu 119
What are the sizes of the memory blocks allocated for `d` and `e`?
```c
int size = 100;
float *d = malloc(size);
float *e = calloc(size, sizeof(float));```
A. 400 bytes and 400 bytes
B. 400 bytes and 100 bytes
C. 100 bytes and 800 bytes
D. 100 bytes and 400 bytes
> **Giải thích:**
> **Đáp án đúng là D.**
> *   `malloc(size)`: Cấp phát chính xác `size` bytes. Ở đây, `size = 100`, vậy `d` được cấp phát 100 bytes.
> *   `calloc(size, sizeof(float))`: Cấp phát một khối bộ nhớ đủ cho `size` phần tử, mỗi phần tử có kích thước là `sizeof(float)`. `sizeof(float)` là 4 bytes. Tổng cộng: `100 * 4 = 400` bytes.

### Câu 121
In linear search, if the size of the array is `n` and the expected value does NOT exist in the array, how many comparisons will be made?
A. n
B. 2n + 1
C. n - 1
D. n + 1
> **Giải thích:**
> **Đáp án đúng là A.** Tìm kiếm tuyến tính (linear search) hoạt động bằng cách so sánh lần lượt từng phần tử của mảng với giá trị cần tìm. Nếu giá trị không tồn tại, thuật toán sẽ phải so sánh với tất cả `n` phần tử để kết luận rằng nó không có trong mảng.

### Câu 122
What will be the output of the C program?
```c
int a = 5;
printf("%dha" + 2, a);
```
A. 5ha
B. ha
C. dha
D. 7
> **Giải thích:**
> **Đáp án đúng là B.** Trong C, một chuỗi hằng như `"%dha"` thực chất là một con trỏ trỏ đến ký tự đầu tiên (`%`). Biểu thức `"%dha" + 2` thực hiện phép toán con trỏ, tạo ra một con trỏ mới trỏ đến ký tự thứ ba của chuỗi, tức là `'h'`. Do đó, `printf` sẽ bắt đầu in từ vị trí này và kết quả là `ha`.

### Câu 123
What is the result displayed on the screen of the following program?
```c
#include<stdio.h>
#include<ctype.h>
int main() {
    char a[] = "hello world";
    int i = 0;
    while (!isspace(a[i]))
        i++;
    printf("%d, %c", i, a[i-1]);
    return 0;
}
```
A. 0, h
B. 5, o
C. 5, (a space)
D. 5, w
> **Giải thích:**
> **Đáp án đúng là B.**
> *   Hàm `isspace()` kiểm tra xem một ký tự có phải là khoảng trắng hay không. `!isspace()` sẽ đúng khi ký tự đó *không* phải là khoảng trắng.
> *   Vòng lặp `while` sẽ chạy qua các ký tự 'h', 'e', 'l', 'l', 'o'.
> *   Khi `i=5`, `a[5]` là ký tự khoảng trắng. `!isspace(' ')` là sai, vòng lặp dừng lại.
> *   Lúc này, giá trị của `i` là 5.
> *   `printf` in ra `i` (là 5) và `a[i-1]` (tức `a[4]`, là 'o').

### Câu 124
What is the value of variable `a` after executing the following lines of code:
```c
int a = 0;
char line1[] = "Hi";
char line2[] = "Hello";
a = strcmp(line1, line2);
```
A. 0
B. A positive value
C. A negative value
D. NaN
> **Giải thích:**
> **Đáp án đúng là B.** Hàm `strcmp` so sánh theo thứ tự từ điển dựa trên mã ASCII.
> *   Ký tự đầu tiên: `'H'` và `'H'` bằng nhau.
> *   Ký tự thứ hai: `'i'` (mã ASCII 105) lớn hơn `'e'` (mã ASCII 101).
> *   Do đó, chuỗi "Hi" được coi là lớn hơn "Hello", và hàm `strcmp` sẽ trả về một giá trị dương.

### Câu 126
What is the result of the `printf("%c %c %c %c", 'A', 0x42, 0103, 68);` command?
A. A B C D
B. A B C C
C. A C C D
D. A B D C
> **Giải thích:**
> **Đáp án đúng là A.** Đặc tả `%c` in ra ký tự tương ứng với mã ASCII.
> *   `'A'`: in ra 'A'.
> *   `0x42` (hệ hexa) = 4*16 + 2 = 66, là mã ASCII của 'B'.
> *   `0103` (hệ octal) = 1*8² + 0*8¹ + 3*8⁰ = 64 + 3 = 67, là mã ASCII của 'C'.
> *   `68` (hệ thập phân) là mã ASCII của 'D'.
> Vậy kết quả là `A B C D`.

### Câu 127
What will be the output of the following C code?
```c
#include <stdio.h>
void main() {
    int x = 0;
    if (x == 0)
        printf("Hi");
    else
        printf("How are you");
    printf("Hello");
}```
A. Hi
B. How are you
C. Hello
D. HiHello
> **Giải thích:**
> **Đáp án đúng là D.**
> *   Điều kiện `if (x == 0)` là đúng, do đó `printf("Hi");` được thực thi.
> *   Vì không có dấu ngoặc `{}` cho khối lệnh `if`, chỉ có câu lệnh ngay sau `if` (là `printf("Hi");`) thuộc về `if`.
> *   Câu lệnh `else` bị bỏ qua.
> *   Câu lệnh `printf("Hello");` nằm ngoài cấu trúc `if-else` và sẽ luôn được thực thi.
> *   Do không có ký tự xuống dòng, hai chuỗi được in liền nhau: `HiHello`.

### Câu 128
What is the output of the following code snippet?
```c
char words[4][11];
strcpy(words[0], "apple");
strcat(words[0], "juice");
printf("%s\n", words[0]);
```
A. applejuice
B. apple
C. juice
D. juiceapple
> **Giải thích:**
> **Đáp án đúng là A.**
> *   `strcpy(words[0], "apple");`: Sao chép chuỗi "apple" vào `words[0]`. `words[0]` bây giờ là "apple".
> *   `strcat(words[0], "juice");`: Nối (concatenate) chuỗi "juice" vào cuối chuỗi `words[0]`.
> *   `words[0]` bây giờ trở thành "applejuice".

### Câu 129
What will be the output of the C program?
```c
int i = 5, j = 8;
while (++i < --j) {
    printf("loop ");
}
```
A. loop
B. infinite loop
C. loop loop
D. No output
> **Giải thích:**
> **Đáp án đúng là A.**
> *   **Lần 1:** `++i` -> `i` thành 6. `--j` -> `j` thành 7. Điều kiện `6 < 7` là đúng. "loop " được in ra.
> *   **Lần 2:** `++i` -> `i` thành 7. `--j` -> `j` thành 6. Điều kiện `7 < 6` là sai. Vòng lặp kết thúc.
> Kết quả là "loop " được in ra một lần.

### Câu 130
What is the result displayed on the screen after executing the following code:
```c
char a[] = "AbCdEf";
char *s = a;
for (; *s; s += 3)
    printf("%s", s);
```
A. Runtime error
B. Ad
C. AbCdEfdEf
D. AbC
> **Giải thích:**
> **Đáp án đúng là C (diễn giải lại từ OCR).**
> *   **Lần 1:** `s` trỏ đến `a[0]`. `*s` là `'A'` (khác null), điều kiện đúng. `printf("%s", s)` in ra toàn bộ chuỗi từ vị trí hiện tại: "AbCdEf". Sau đó `s` trỏ đến `a[3]`.
> *   **Lần 2:** `s` trỏ đến `a[3]`. `*s` là `'d'` (khác null), điều kiện đúng. `printf("%s", s)` in ra chuỗi từ vị trí này: "dEf". Sau đó `s` trỏ đến `a[6]`.
> *   **Lần 3:** `s` trỏ đến `a[6]`, là ký tự null `\0`. `*s` là null, điều kiện sai, vòng lặp kết thúc.
> Output là `AbCdEfdEf`.

### Câu 131
What is the output when the sample code below is executed?
```c
#include <stdio.h>
int main() {
    int x = 7;
    for (; x > 3;)
        printf("Yes");
    return 0;
}
```
A. Infinite loop
B. Compile time error
C. YesYesYesYes
D. Yes
> **Giải thích:**
> **Đáp án đúng là A.** Vòng lặp `for` này không có phần cập nhật (phần thứ ba). Biến `x` luôn giữ giá trị 7. Do đó, điều kiện `x > 3` sẽ luôn đúng, tạo ra một vòng lặp vô hạn (infinite loop) in ra chuỗi "Yes" liên tục.

### Câu 132
What is the output when the sample code below is executed?
```c
#include<stdio.h>
int main() {
    int x = 10, i;
    for (i = 0; i < x; i += 3) {
        printf("One");
        continue;
        printf("Two");
    }
    return 0;
}
```
A. OneOneOneOne
B. OneTwoOneOne
C. OneTwoTwoTwo
D. TwoTwoTwoOne
> **Giải thích:**
> **Đáp án đúng là A.** Lệnh `continue` sẽ ngay lập tức bỏ qua phần còn lại của thân vòng lặp và chuyển sang lần lặp tiếp theo. Do đó, `printf("Two");` không bao giờ được thực thi.
> *   i=0: in "One".
> *   i=3: in "One".
> *   i=6: in "One".
> *   i=9: in "One".
> Vòng lặp chạy 4 lần, in ra "One" 4 lần.

### Câu 133
What is the output when the sample code below is executed?
```c
#include <stdio.h>
int main() {
    int a = 1;
    switch (a) {
        case 2: printf("Two");
        case 1: printf("One");
        case 3: printf("Three");
        case 4: printf("Four");
    }
    return 0;
}
```
A. OneThreeFour
B. OneTwoThreeFour
C. One
D. TwoOneThreeFour
> **Giải thích:**
> **Đáp án đúng là A.** Cấu trúc `switch` trong C có tính chất "rơi xuống" (fall-through).
> 1.  `a` có giá trị 1, chương trình nhảy đến `case 1`.
> 2.  `printf("One");` được thực thi.
> 3.  Vì không có lệnh `break` ở `case 1`, chương trình sẽ tiếp tục thực thi các `case` tiếp theo.
> 4.  `printf("Three");` được thực thi.
> 5.  `printf("Four");` được thực thi.
> Kết quả là `OneThreeFour`.

### Câu 135
Choose the best comment about the output of the following C code:
```c
#include <stdio.h>
void main() {
    int i = 0;
    while (i < 5) {
        i++;
        printf("Hi-");
        while (i < 4) {
            i++;
            printf("Hello-");
        }
    }
}
```
A. Hi-Hello-Hello-Hello-Hi-
B. Hi-Hi-Hi-Hi-Hello-Hello-Hello-Hi-
C. Hi-Hello-Hello-Hello-Hi-Hi-
D. Hi-Hi-Hi-Hi-Hi
> **Giải thích:**
> **Đáp án đúng là A.**
> *   **Lần 1 (vòng ngoài), i=0:**
>     *   `i++` -> `i` thành 1.
>     *   In "Hi-".
>     *   Vòng trong `while(i < 4)` (1<4) đúng:
>         *   `i++` -> `i` thành 2. In "Hello-".
>         *   `i++` -> `i` thành 3. In "Hello-".
>         *   `i++` -> `i` thành 4. In "Hello-".
>         *   Bây giờ `i=4`, `i<4` sai, vòng trong kết thúc.
> *   **Lần 2 (vòng ngoài), i=4:**
>     *   `i++` -> `i` thành 5.
>     *   In "Hi-".
>     *   Vòng trong `while(i < 4)` (5<4) sai.
> *   **Lần 3 (vòng ngoài), i=5:** `i<5` sai, vòng ngoài kết thúc.
> Kết quả cuối cùng là `Hi-Hello-Hello-Hello-Hi-`.

### Câu 136
Consider the following program. What will be printed to the screen?
```c
#include<stdio.h>
int main() {
    char i, j;
    for (i = 'A'; i <= 'D'; i++) {
        for (j = 'A'; j <= i; j++) {
            printf("%c", i);
        }
        printf("\n");
    }
}
```
> **Giải thích:**
> **Đáp án là:**
> ```
> A
> BB
> CCC
> DDDD
> ```
> Vòng lặp ngoài chạy từ 'A' đến 'D'. Vòng lặp trong chạy từ 'A' đến giá trị hiện tại của `i`, và in ra chính ký tự `i`.
> *   Khi i='A', in 'A' 1 lần.
> *   Khi i='B', in 'B' 2 lần.
> *   Khi i='C', in 'C' 3 lần.
> *   Khi i='D', in 'D' 4 lần.

### Câu 137
What is the output of the following code snippet?
```c
#include <stdio.h>
int main() {
    char char_array[] = {'a', 'b', 'c', 'd', 'e'};
    int array_size = sizeof(char_array) / sizeof(char);
    for (int i = 0; i < array_size; i++) {
        char_array[i] = char_array[i] + 1;
    }
    for (int i = 0; i < array_size; i++) {
        printf("%c ", char_array[i]);
    }
    return 0;
}
```
A. b c d e f
B. a b c d e
C. 98 99 100 101 102
D. c d e f g
> **Giải thích:**
> **Đáp án đúng là A.**
> *   Vòng lặp đầu tiên duyệt qua mảng và cộng 1 vào mã ASCII của mỗi ký tự.
>     *   'a' (97) -> 'b' (98)
>     *   'b' (98) -> 'c' (99)
>     *   ...
>     *   'e' (101) -> 'f' (102)
> *   Vòng lặp thứ hai in ra các ký tự mới trong mảng, cách nhau bởi dấu cách. Kết quả là `b c d e f`.

### Câu 142
What will the following program output?
```c
#include <stdio.h>
int main() {
    int a = -5;
    if (a % 2 == 0)
        printf("a is a positive number.");
    else if (a == 0)
        printf("a is zero.");
    printf("a is a negative number.");
    return 0;
}
```
A. a is a positive number.
B. a is a negative number.
C. a is zero.
D. a is a negative number.
> **Giải thích:**
> **Đáp án đúng là D.**
> 1.  `a % 2 == 0` (-5 % 2 là -1) -> sai.
> 2.  `else if (a == 0)` (-5 == 0) -> sai.
> 3.  Vì không có `else` cho `if` thứ hai, chương trình sẽ thực thi câu lệnh tiếp theo sau khối `if-else if`.
> 4.  `printf("a is a negative number.");` được thực thi.
> *(Lưu ý: Logic của chương trình này bị sai. Nó sẽ in "a is a negative number." cho mọi số lẻ, kể cả số dương)*.

### Câu 143
Why is the following code wrong?
```c
#include<stdio.h>
int main() {
    int choice;
    scanf("%d", &choice);
    switch (choice) {
        case 1.5:
            printf("You chose 1.5");
        case 2.3:
            printf("You chose 2.3");
    }
    return 0;
}
```
A. The case label is a real number
B. Missing "break" command
C. Missing "default" command
D. The variable name is wrong
> **Giải thích:**
> **Đáp án đúng là A.** Nhãn `case` trong câu lệnh `switch` của C phải là một hằng số kiểu số nguyên (integer) hoặc ký tự (character). Sử dụng một số thực (real number) như `1.5` làm nhãn `case` là sai cú pháp và sẽ gây lỗi biên dịch.

### Câu 144
What does the following code snippet do?
```c
char str1[10] = "Hello";
char str2[10];
strcpy(str2, str1);
```
A. Copies the content of str1 into str2
B. Compares str1 with str2
C. Retrieves the length of str1
D. Assigns str2 to an empty string
> **Giải thích:**
> **Đáp án đúng là A.** Hàm `strcpy(destination, source)` sao chép (copies) nội dung của chuỗi nguồn (`str1`) vào chuỗi đích (`str2`).

### Câu 145
What is correct about the `strcpy(s1, s2)` function?
A. Compares the two strings s1 and s2
B. Copies the s2 string to the s1 string
C. Copies the s1 string to the s2 string
D. Concatenates string s2 to the end of s1
> **Giải thích:**
> **Đáp án đúng là B.** Cú pháp là `strcpy(destination, source)`. Do đó, `strcpy(s1, s2)` sẽ sao chép nội dung của `s2` vào `s1`.

### Câu 146
What is the result displayed on the screen of the following program?
```c
#include <stdio.h>
void level2(int** ppa) {
    printf("%d\n", **ppa);
}
void level1(int* pa) {
    level2(&pa);
}
int main() {
    int a = 10;
    level1(&a);
}
```
A. The address of variable a
B. The address of the pointer pa
C. The address of the double pointer ppa
D. 10
> **Giải thích:**
> **Đáp án đúng là D.**
> 1.  Trong `main`, `level1(&a)` được gọi, truyền vào địa chỉ của `a`.
> 2.  Trong `level1`, `pa` nhận địa chỉ của `a`. Sau đó, `level2(&pa)` được gọi, truyền vào địa chỉ của con trỏ `pa`.
> 3.  Trong `level2`, `ppa` nhận địa chỉ của `pa`.
>     *   `*ppa` sẽ là giá trị của `pa`, tức là địa chỉ của `a`.
>     *   `**ppa` sẽ là giá trị tại địa chỉ của `a`, tức là 10.
> 4.  Chương trình in ra 10.

### Câu 147
Choose the best comment about the output of the following C code:
```c
#include <stdio.h>
int main() {
    int a = 1;
    switch (a) {
        case 1:
            printf("%d", a);
        case 2:
            printf("%d", a);
        case 3:
            printf("%d", a);
    }
    return 0;
}
```
A. No error, output is 111
B. No error, output is 1
C. Compile time error, no break statements
D. Compile time error, case label outside switch statement
> **Giải thích:**
> **Đáp án đúng là A.** Đoạn mã này không có lỗi biên dịch. Việc thiếu `break` là hợp lệ. Do tính chất "rơi xuống" (fall-through):
> 1.  Chương trình nhảy đến `case 1`, in ra `1`.
> 2.  Tiếp tục thực thi `case 2`, in ra `1`.
> 3.  Tiếp tục thực thi `case 3`, in ra `1`.
> Kết quả cuối cùng là `111`.

### Câu 148
What does the following code print?
```c
int x = 10;
if (x = 0)
    printf("Zero");
else
    printf("Non-zero");
```
A. Runs and prints "Non-zero".
B. Compiler error.
C. Runs and prints "Zero".
D. Runtime error.
> **Giải thích:**
> **Đáp án đúng là A.** Đây là một lỗi logic phổ biến.
> *   `x = 0` là một phép gán, không phải phép so sánh `==`.
> *   Phép gán `x = 0` sẽ thực hiện việc gán 0 cho `x`, và bản thân biểu thức gán này trả về giá trị đã được gán, là 0.
> *   Câu lệnh `if` sẽ kiểm tra giá trị 0. Trong C, 0 được coi là `false`.
> *   Do điều kiện là `false`, khối lệnh `else` sẽ được thực thi.
> *   Kết quả là "Non-zero" được in ra.

### Câu 150
Assume we have a function such as:
```c
void swap(int a, int b) {
    int t = a;
    a = b;
    b = t;
}
```
What is the problem with variables `a` and `b` in the calling function after executing `swap(a, b)`?
A. a and b do not change values.
B. cannot execute the swap(a,b) function.
C. a has the old value of b, and b has the old value of a.
D. a and b change values for each other.
> **Giải thích:**
> **Đáp án đúng là A.** Do C sử dụng cơ chế truyền tham trị (pass-by-value), hàm `swap` chỉ nhận được bản sao của giá trị các biến được truyền vào. Mọi thay đổi trên các bản sao `a` và `b` bên trong hàm `swap` không ảnh hưởng đến các biến gốc ở hàm gọi.

### Câu 151
Consider an array `a` with `n` elements. Which of the following options correctly describes the value of `s` after executing the code snippet?
```c
int a[MAX_SIZE];
int s = 0;
for (int i = 0; i < n; i++) {
    s = s + a[i] * a[i];
}```
A. The sum of squares of all elements in the array `a`
B. The sum of all even elements in the array `a`
C. The sum of all odd elements in the array `a`
D. The sum of all elements in the array `a`
> **Giải thích:**
> **Đáp án đúng là A.** Biểu thức `a[i] * a[i]` tính bình phương của phần tử thứ `i`. Vòng lặp cộng dồn các giá trị bình phương này vào biến `s`. Do đó, `s` là tổng bình phương của tất cả các phần tử (the sum of squares of all elements).

### Câu 152
What does the above code snippet do?
```c
int func(int* a, int n) {
    int S = 0;
    for (int i = 0; i < n; i++) {
        S = S + (a[i] % 2) * a[i];
    }
    return S;
}
```
A. Calculates the sum of the absolute value of all odd elements in the array `a` of size `n`.
B. Calculates the sum of all odd elements in the array `a` of size `n`.
C. Calculates the sum of all even elements in the array `a` of size `n`.
D. Calculates the sum of squares of all elements in the array `a` of size `n`.
> **Giải thích:**
> **Đáp án đúng là B.**
> *   Biểu thức `(a[i] % 2)` sẽ trả về 1 nếu `a[i]` là số lẻ (hoặc -1 nếu là số lẻ âm), và trả về 0 nếu `a[i]` là số chẵn.
> *   Nếu `a[i]` chẵn, `S = S + 0 * a[i]`, `S` không đổi.
> *   Nếu `a[i]` lẻ, `S = S + 1 * a[i]`, `S` được cộng thêm chính giá trị của `a[i]`.
> *   Do đó, đoạn mã này tính tổng của tất cả các phần tử lẻ.

### Câu 153
Choose the correct statement about the following statement:
```c
scanf("%d, %d", &a, &b);
```
A. scanf will expect two integers inputted by user and write them to variables a and b.
B. scanf will expect two floating-point numbers.
C. scanf will expect two integers separated by a comma, and write the first to a, the comma to b.
D. scanf will expect two integers separated by a comma, and write the first integer to a, the second integer to b.
> **Giải thích:**
> **Đáp án đúng là D.** Khi chuỗi định dạng của `scanf` chứa một ký tự không phải khoảng trắng (ở đây là dấu phẩy `,`), nó yêu cầu người dùng phải nhập chính xác ký tự đó vào giữa các giá trị. Do đó, người dùng phải nhập `số_nguyên_1, số_nguyên_2`.

### Câu 157
In C programming, when declaring a variable of type integer, the computer stores it in a numbered storage location. What is this numbered location called?
A. Address
B. Pointer
C. Integer
D. Byte
> **Giải thích:**
> **Đáp án đúng là A.** Mỗi vị trí lưu trữ trong bộ nhớ máy tính được xác định bởi một con số duy nhất, được gọi là địa chỉ (Address).

### Câu 158
In C programming, a variable is frequently used to store the address of another variable. What is the name of this variable?
A. Pointer
B. Address
C. Integer
D. Byte
> **Giải thích:**
> **Đáp án đúng là A.** Một biến được thiết kế đặc biệt để lưu trữ địa chỉ của một biến khác được gọi là con trỏ (Pointer).

### Câu 161
What is the `&` operator when used in expressions like `x & y`?
A. Bitwise AND
B. Address-of operator
C. Logical AND
D. Bitwise OR
> **Giải thích:**
> **Đáp án đúng là A.** Khi được sử dụng giữa hai biến (`x & y`), `&` là toán tử AND trên bit (Bitwise AND). Khi đứng trước một biến (`&x`), nó là toán tử lấy địa chỉ (Address-of operator).

### Câu 162
What is not a loop in the C programming language?
A. While
B. Do while
C. For
D. Repeat until
> **Giải thích:**
> **Đáp án đúng là D.** C có 3 cấu trúc vòng lặp chính: `for`, `while`, và `do-while`. `Repeat-until` là cú pháp vòng lặp trong các ngôn ngữ khác như Pascal.

### Câu 163
What is the purpose of the `fscanf()` function in the C programming language?
A. Read formatted data from a file.
B. Print to the screen.
C. Read data from the keyboard.
D. Open a file.
> **Giải thích:**
> **Đáp án đúng là A.** Hàm `fscanf` (file scan formatted) hoạt động tương tự `scanf` nhưng đọc dữ liệu đã được định dạng từ một tệp (file) thay vì từ bàn phím.

### Câu 164
What term is commonly used to specify both the type and name of a variable or constant in the C programming language?
A. Identification
B. Name
C. Declaration
D. Definition
> **Giải thích:**
> **Đáp án đúng là C.** Khai báo (Declaration) là quá trình giới thiệu một định danh mới (tên biến, hàm) cho trình biên dịch và chỉ định kiểu của nó. Định nghĩa (Definition) là một khai báo mà còn cấp phát bộ nhớ cho biến đó.

### Câu 165
What translates a C source file into machine language so that the computer can execute it?
A. A compiler
B. A text editor
C. A file
D. A program
> **Giải thích:**
> **Đáp án đúng là A.** Trình biên dịch (compiler) là một chương trình đặc biệt có nhiệm vụ dịch mã nguồn được viết bằng ngôn ngữ bậc cao (như C) sang ngôn ngữ máy mà CPU có thể hiểu và thực thi.

### Câu 166
What technique in programming to solve a complex problem is to break the program into a series of smaller programs?
A. Modularity
B. Repeat
C. Select
D. Sequentially
> **Giải thích:**
> **Đáp án đúng là A.** Tính module hóa (Modularity) là nguyên tắc thiết kế phần mềm bằng cách chia một chương trình phức tạp thành các phần nhỏ hơn, độc lập tương đối gọi là các module hoặc hàm.

### Câu 167
What will happen if the `while` loop condition is always false?
A. Compile time error
B. Loop infinitely
C. The loop will not execute
D. The loop will execute once
> **Giải thích:**
> **Đáp án đúng là C.** Vòng lặp `while` luôn kiểm tra điều kiện trước khi thực hiện thân vòng lặp. Nếu điều kiện sai ngay từ đầu, thân vòng lặp sẽ không bao giờ được thực thi.

### Câu 168
What algorithms can be used to sort the elements in an array?
A. Bubble sort, Linear search
B. Binary search, Linear search
C. Selection sort, Bubble sort
D. Binary search, Selection sort
> **Giải thích:**
> **Đáp án đúng là C.** Linear search và Binary search là các thuật toán tìm kiếm, không phải sắp xếp. Selection sort và Bubble sort đều là các thuật toán sắp xếp (sorting).

### Câu 170
Which of the following operators can be applied to pointer variables?
A. Increments/Decrements
B. Square root
C. Division
D. Multiplication
> **Giải thích:**
> **Đáp án đúng là A.** Các phép toán số học hợp lệ trên con trỏ bao gồm: cộng/trừ với một số nguyên (để di chuyển con trỏ), tăng/giảm (`++`, `--`), và trừ hai con trỏ (cùng kiểu) để tìm khoảng cách. Phép nhân, chia, căn bậc hai không có ý nghĩa đối với con trỏ.

### Câu 171
Which sorting algorithm repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order?
A. Bubble sort
B. Selection sort
C. Binary sort
D. None of the others
> **Giải thích:**
> **Đáp án đúng là A.** Đây là mô tả chính xác của thuật toán sắp xếp nổi bọt (Bubble sort).

### Câu 172
When a C program compiles without any errors or warnings, it means that the syntax of the program is correct. However, a program can still produce incorrect results if there are \_\_\_\_\_\_ in the code.
A. compilation errors
B. runtime errors
C. logic or semantic errors
D. interpreter errors
> **Giải thích:**
> **Đáp án đúng là C.** Một chương trình có thể đúng về mặt cú pháp nhưng vẫn chạy sai do lỗi logic hoặc lỗi ngữ nghĩa (logic or semantic errors) - tức là, chương trình làm đúng những gì bạn viết, nhưng những gì bạn viết lại không đúng với điều bạn muốn nó làm.

### Câu 173
How are strings typically represented in C?
A. As an array of characters
B. As an array of strings
C. As individual characters
D. As integers referencing ASCII values
> **Giải thích:**
> **Đáp án đúng là A.** Chuỗi trong C được biểu diễn dưới dạng một mảng các ký tự (an array of characters), được kết thúc bằng một ký tự null (`\0`).

### Câu 174
Who is the inventor of the C programming language?
A. Dennis Ritchie
B. Bjarne Stroustrup
C. Brian Kernighan
D. Niklaus Wirth
> **Giải thích:**
> **Đáp án đúng là A.** Dennis Ritchie đã phát triển ngôn ngữ lập trình C tại Bell Labs vào đầu những năm 1970.

### Câu 176
Binary search can be applied to which type of the below data structure in C?
A. A sorted one-dimensional array
B. A two-dimensional array
C. Every kind of array
D. All of the others
> **Giải thích:**
> **Đáp án đúng là A.** Tìm kiếm nhị phân (Binary search) yêu cầu cấu trúc dữ liệu phải được sắp xếp (sorted) và có khả năng truy cập ngẫu nhiên hiệu quả. Một mảng một chiều đã được sắp xếp là cấu trúc dữ liệu lý tưởng cho thuật toán này.

### Câu 177
Errors that occur due to syntax violations belong to which of the following categories?
A. Compile time error
B. Run time error
C. Input error
D. Linking error
> **Giải thích:**
> **Đáp án đúng là A.** Lỗi cú pháp (syntax errors), chẳng hạn như thiếu dấu chấm phẩy hoặc sai tên từ khóa, sẽ được trình biên dịch (compiler) phát hiện trong quá trình dịch mã nguồn, do đó chúng được gọi là lỗi thời gian biên dịch (compile time error).

### Câu 178
Values used to describe information in programming are typically referred to as \_\_\_\_\_\_.
A. Data
B. Information
C. Algorithm
D. Computer program
> **Giải thích:**
> **Đáp án đúng là A.** Trong lập trình, các giá trị thô (số, ký tự, chuỗi...) được sử dụng để biểu diễn thông tin được gọi là dữ liệu (Data).

### Câu 181
The statement `for (;;)` represents an infinite loop. This loop can still be terminated by using \_\_\_\_\_\_.
A. `exit(0)`
B. `abort()`
C. `break`
D. `return`
> **Giải thích:**
> **Đáp án đúng là C.** Lệnh `break` được sử dụng để thoát ngay lập tức khỏi vòng lặp (`for`, `while`, `do-while`) hoặc `switch` gần nhất mà nó nằm bên trong. `return` sẽ thoát khỏi toàn bộ hàm, trong khi `exit` và `abort` sẽ chấm dứt toàn bộ chương trình.

### Câu 182
The `strcpy` function in C programming is used to \_\_\_\_\_\_.
A. copy strings
B. concatenate (join) two strings
C. compare two strings
> **Giải thích:**
> **Đáp án đúng là A.** `strcpy` là viết tắt của "string copy" và được dùng để sao chép chuỗi.

### Câu 183
The function `islower()` returns a non-zero value if a character is:
A. A lowercase letter
B. An uppercase letter
C. A digit
D. A punctuation character
> **Giải thích:**
> **Đáp án đúng là A.** Hàm `islower()` trong `<ctype.h>` kiểm tra xem một ký tự có phải là một chữ cái viết thường (a lowercase letter) hay không.

### Câu 184
The `&` operator in the C programming language is used to \_\_\_\_\_\_.
A. AND two bit sequences
B. AND two conditionals
C. OR two bit sequences
D. OR two conditionals
> **Giải thích:**
> **Đáp án đúng là A.** Toán tử `&` là toán tử AND trên bit (bitwise AND). Toán tử AND logic là `&&`.

### Câu 186
Which library contains the `abs()` function?
A. `time.h`
B. `conio.h`
C. `math.h`
D. `stdlib.h`
> **Giải thích:**
> **Đáp án đúng là D.** Hàm `abs()` (tính giá trị tuyệt đối của số nguyên) được định nghĩa trong thư viện chuẩn `stdlib.h`. Hàm `fabs()` (cho số thực) nằm trong `math.h`.

### Câu 187
Which library contains the function `rand()` to generate pseudo-random integers?
A. `ctype.h`
B. `stdlib.h`
C. `math.h`
D. `conio.h`
> **Giải thích:**
> **Đáp án đúng là B.** Hàm `rand()` và `srand()` để sinh số ngẫu nhiên được định nghĩa trong thư viện chuẩn `stdlib.h`.

### Câu 189
Which of the following statements is used to move to the next iteration of a loop without executing the remaining part of the loop body?
A. `continue`
B. `goto`
C. `return`
D. `break`
> **Giải thích:**
> **Đáp án đúng là A.** Lệnh `continue` sẽ bỏ qua các câu lệnh còn lại trong lần lặp hiện tại và bắt đầu ngay lần lặp tiếp theo của vòng lặp.

### Câu 190
Which of the following statements is used to stop a selection or loop statement?
A. `break`
B. `goto`
C. `continue`
D. `while`
> **Giải thích:**
> **Đáp án đúng là A.** Lệnh `break` được sử dụng để thoát hoàn toàn ra khỏi một vòng lặp (`for`, `while`, `do-while`) hoặc một cấu trúc `switch`.

### Câu 191
What is the return type of the `sqrt()` function from the `math.h` library in C?
A. double
B. float
C. int
D. long
> **Giải thích:**
> **Đáp án đúng là A.** Hàm `sqrt()` (tính căn bậc hai) trong `math.h` nhận một đối số kiểu `double` và trả về một giá trị kiểu `double`.

### Câu 192
The `pow()` function in the `math.h` library is used to calculate the value of a number raised to a specified power. What is the return value type of the `pow()` function?
A. double
B. int
C. long double
D. float
> **Giải thích:**
> **Đáp án đúng là A.** Hàm `pow()` nhận hai đối số kiểu `double` và trả về kết quả cũng là kiểu `double`.

### Câu 193
What is the return type of the `putchar()` function?
A. int
B. char
C. void
D. string
> **Giải thích:**
> **Đáp án đúng là A.** Mặc dù `putchar` được dùng để in một ký tự, nó trả về một giá trị kiểu `int`: mã ASCII của ký tự được ghi nếu thành công, và `EOF` (một hằng số kiểu `int`) nếu có lỗi.

### Câu 194
Which keyword is used to define a named constant in C?
A. `const`
B. `#define`
C. `constant`
D. `named`
> **Giải thích:**
> **Đáp án đúng là A.** Từ khóa `const` được sử dụng để khai báo một biến có giá trị không thể thay đổi sau khi khởi tạo, biến nó thành một hằng số. `#define` là một chỉ thị tiền xử lý, cũng được dùng để tạo hằng số nhưng hoạt động theo cơ chế thay thế văn bản.

### Câu 195
Which of the following identifiers is invalid?
A. `4me2`
B. `Primes`
C. `Max`
D. `PI_NUMBER`
> **Giải thích:**
> **Đáp án đúng là A.** Tên định danh (identifier) trong C không được phép bắt đầu bằng một chữ số.

### Câu 196
What functions can be used to output strings? (Select all that apply)
A. `printf()`
B. `putc()`
C. `gets()`
D. `puts()`
E. `getc()`
> **Giải thích:**
> **Đáp án đúng là A và D.**
> *   `printf()`: Có thể in chuỗi bằng đặc tả `%s`.
> *   `puts()`: Chuyên dùng để in một chuỗi, và tự động thêm ký tự xuống dòng.
> *   `putc()` chỉ in một ký tự. `gets()` và `getc()` là hàm nhập liệu.

### Câu 197
What is an incorrect way to output a string?
A. `putc(s)`
B. `puts(s)`
C. `printf(s)`
D. `printf("%s", s)`
> **Giải thích:**
> **Đáp án đúng là A.**
> *   `putc(s)` là sai vì nó mong đợi một ký tự (`char` hoặc `int`), không phải một con trỏ chuỗi (`char*`).
> *   `printf(s)` (lựa chọn C) tuy có thể chạy nhưng rất không an toàn và nên tránh, vì nếu chuỗi `s` chứa các ký tự định dạng (`%`), nó có thể gây ra lỗi.

### Câu 198
Which is a valid function name in the C language?
A. `is_prime`
B. `#include`
C. `int()`
D. `if`
E. `return`
> **Giải thích:**
> **Đáp án đúng là A.** `is_prime` là một tên định danh hợp lệ (chữ cái, gạch dưới). Các lựa chọn khác là chỉ thị tiền xử lý (`#include`), tên kiểu dữ liệu (`int`), hoặc từ khóa (`if`, `return`).

### Câu 199
What function is used to send formatted output to a file?
A. `fprintf()`
B. `fwritef()`
C. `fsendf()`
D. `fputs()`
> **Giải thích:**
> **Đáp án đúng là A.** Hàm `fprintf` (file print formatted) hoạt động tương tự như `printf` nhưng ghi output đã được định dạng vào một tệp (file) thay vì ra màn hình.

### Câu 200
What function is used to read a line from the specified stream and store it in the string pointed to by `str`?
A. `fgets()`
B. `fgetc()`
C. `fputs()`
D. `fputc()`
> **Giải thích:**
> **Đáp án đúng là A (diễn giải từ câu hỏi).** Hàm `fgets` (file get string) được sử dụng để đọc một dòng từ một luồng (stream), thường là một tệp, và lưu nó vào một chuỗi. Nó an toàn hơn `gets` vì nó cho phép chỉ định kích thước bộ đệm tối đa.


# References

