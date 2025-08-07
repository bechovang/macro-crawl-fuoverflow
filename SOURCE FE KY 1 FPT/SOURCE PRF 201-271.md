
2025-08-07 21:05

Status:

Tags: [[source]]  [[PRF]]
Disable spell check :`teh`
# SOURCE PRF 201-271


## III. Ngân hàng câu hỏi trắc nghiệm (Câu 201 - 271)

### Câu 201
Which of the following functions provide buffered input facilities on the standard input stream?
A. `getchar()`, `scanf()`
B. `getchar()`, `fgets()`
C. `scanf()`, `fgetc()`
D. `fgets()`, `fgetc()`
> **Giải thích:**
> **Đáp án đúng là B.** Cả `getchar()` và `fgets()` đều là các hàm nhập liệu có bộ đệm (buffered input). Điều này có nghĩa là khi bạn nhập từ bàn phím, dữ liệu sẽ được lưu tạm vào một bộ đệm, và các hàm này sẽ đọc từ bộ đệm đó. `scanf()` cũng có bộ đệm, nhưng `fgetc()` thường được dùng với tệp. Trong các lựa chọn, B là cặp phù hợp nhất cho luồng nhập chuẩn.

### Câu 202
Which function is used to write a string to a file in C?
A. `fputs()`
B. `fscanf()`
C. `fgets()`
D. `fopen()`
> **Giải thích:**
> **Đáp án đúng là A.** Hàm `fputs()` (file put string) được sử dụng để ghi một chuỗi ký tự vào một tệp đã được mở.

### Câu 203
To read an entire line from a file in C, which function is commonly used?
A. `fgets()`
B. `gets()`
C. `readLine()`
D. `scanLine()`
> **Giải thích:**
> **Đáp án đúng là A.** Hàm `fgets()` (file get string) là cách an toàn và phổ biến nhất để đọc một dòng từ một tệp (hoặc bất kỳ luồng nào) trong C, vì nó cho phép giới hạn số ký tự tối đa có thể đọc để tránh tràn bộ đệm.

### Câu 204
Which function is used to read a single character from the standard input in C?
A. `getchar()`
B. `fscanf()`
C. `fgets()`
D. `getc()`
> **Giải thích:**
> **Đáp án đúng là A.** Hàm `getchar()` được thiết kế đặc biệt để đọc một ký tự duy nhất từ luồng nhập chuẩn (standard input), thường là bàn phím. `getc(stdin)` cũng có chức năng tương tự.

### Câu 205
What function is used to find the length of a string in C?
A. `strlen()`
B. `lenstr()`
C. `strnlen()`
D. `strength()`
> **Giải thích:**
> **Đáp án đúng là A.** Hàm `strlen()` (string length) trong thư viện `<string.h>` được sử dụng để tính và trả về độ dài của một chuỗi (không bao gồm ký tự null `\0`).

### Câu 206
Which function is used to concatenate two strings in C?
A. `strcat()`
B. `strcmp()`
C. `strmerge()`
D. `strconnect()`
> **Giải thích:**
> **Đáp án đúng là A.** Hàm `strcat()` (string concatenate) được sử dụng để nối chuỗi nguồn vào cuối chuỗi đích.

### Câu 207
Which of the following functions is used to find the first occurrence of a given string in another string?
A. `strchr()`
B. `strrchr()`
C. `strstr()`
D. `strnset()`
> **Giải thích:**
> **Đáp án đúng là C.** Hàm `strstr()` (string in string) được sử dụng để tìm lần xuất hiện đầu tiên của một chuỗi con (substring) bên trong một chuỗi chính.

### Câu 208
To avoid the generated random number sequence being identical after the program is run again and again, we need to use the \_\_\_\_\_\_ library and the \_\_\_\_\_\_ function before using the `rand()` function.
A. `stdlib.h`, `randomize()`
B. `stdlib.h`, `reset()`
C. `time.h`, `randomize()`
D. `time.h`, `srand()`
> **Giải thích:**
> **Đáp án đúng là D.** Để tạo ra một chuỗi số ngẫu nhiên khác nhau mỗi khi chạy chương trình, ta cần "gieo mầm" (seed) cho bộ sinh số ngẫu nhiên. Điều này thường được thực hiện bằng cách gọi hàm `srand()` (seed random) với một giá trị thay đổi, chẳng hạn như thời gian hiện tại của hệ thống. Thời gian hiện tại được lấy bằng hàm `time()` từ thư viện `<time.h>`.

### Câu 209
The correct function to remove characters that remain in the keyboard buffer in C programming is \_\_\_\_\_\_.
A. `clearbuffer()`
B. `cleanbuffer()`
C. `flushall(in)`
D. `fflush(stdin)`
> **Giải thích:**
> **Đáp án đúng là D.** Mặc dù việc sử dụng `fflush(stdin)` không được định nghĩa trong chuẩn ANSI C và có thể không hoạt động trên tất cả các trình biên dịch, nó là một cách làm phổ biến (nhưng không an toàn) trên nhiều hệ thống (như Windows) để xóa bộ đệm đầu vào. Cách làm đúng chuẩn hơn là đọc và loại bỏ các ký tự còn lại bằng một vòng lặp.

### Câu 210
Which function is used to open a file for reading in C?
A. `fopen("file.txt", "r")`
B. `open("file.txt", "r")`
C. `fopen("file.txt", "w")`
D. `open("file.txt", "w")`
> **Giải thích:**
> **Đáp án đúng là A.** Hàm `fopen()` được sử dụng để mở một tệp. Chế độ (mode) `"r"` được sử dụng để mở một tệp chỉ để đọc (reading).

### Câu 211
Which format specifier is used to print the value of a `double` variable with `printf`?
A. `%lf`
B. `%d`
C. `%c`
D. `%f`
> **Giải thích:**
> **Đáp án đúng là D.** Trong hàm `printf`, cả `%f` và `%lf` đều có thể được sử dụng để in giá trị của một biến kiểu `double` (do các đối số `float` sẽ tự động được thăng cấp thành `double`). Tuy nhiên, `%f` là đặc tả phổ biến và đủ dùng. Ngược lại, với `scanf`, bạn bắt buộc phải dùng `%lf` cho `double`.

### Câu 212
Which mode is only used to append data to a file?
A. `"a"`
B. `"append+"`
C. `"r+"`
D. `"w+"`
> **Giải thích:**
> **Đáp án đúng là A.** Chế độ `"a"` (append) được sử dụng để mở một tệp và ghi nối dữ liệu vào cuối tệp mà không xóa nội dung cũ.

### Câu 213
Which character is commonly used to mark the end of a string in C?
A. `'\0'`
B. `'\n'`
C. `'\t'`
D. `'\'`
> **Giải thích:**
> **Đáp án đúng là A.** Ký tự null `\0` được sử dụng để đánh dấu sự kết thúc của một chuỗi ký tự.

### Câu 214
Which of the following symbols is used to force the cursor to change its position to the beginning of the next line on the screen?
A. `\n`
B. `\t`
C. `\f`
D. `\b`
> **Giải thích:**
> **Đáp án đúng là A.** Ký tự xuống dòng (newline) `\n` được sử dụng để di chuyển con trỏ đến đầu dòng tiếp theo.

### Câu 215
Which of these is NOT a relational or logical operator?
A. `=`
B. `||`
C. `==`
D. `!=`
> **Giải thích:**
> **Đáp án đúng là A.** Dấu `=` là toán tử gán (assignment operator). Các toán tử còn lại là OR logic (`||`), so sánh bằng (`==`), và so sánh khác (`!=`).

### Câu 216
Which of the following operators has the lowest priority?
A. `+=`
B. `+`
C. `++`
D. `-`
> **Giải thích:**
> **Đáp án đúng là A.** Trong các lựa chọn này, toán tử gán (`+=`) có độ ưu tiên thấp nhất. Toán tử tăng/giảm (`++`) có độ ưu tiên cao nhất, tiếp theo là các toán tử số học (`+`, `-`).

### Câu 217
Which of the following operators has the highest priority?
A. `++`
B. `+=`
C. `*`
D. `+`
> **Giải thích:**
> **Đáp án đúng là A.** Toán tử tăng/giảm hậu tố và tiền tố (`++`, `--`) có độ ưu tiên cao hơn các toán tử số học (`*`, `+`) và toán tử gán (`+=`).

### Câu 219
What is the purpose of the `calloc` function in C?
A. Allocate memory and initialize it to zero
B. Free memory allocated
C. Deallocate memory
D. Copy memory from one location to another
> **Giải thích:**
> **Đáp án đúng là A.** Hàm `calloc()` (contiguous allocation) cấp phát một vùng nhớ cho một mảng các phần tử và tự động khởi tạo tất cả các byte trong vùng nhớ đó về 0.

### Câu 220
What is the `rewind()` function used for?
A. To reset the file pointer to the beginning of the file.
B. To read the entire file into memory.
C. To close the file.
D. To move the file pointer to the end of the file.
> **Giải thích:**
> **Đáp án đúng là A.** Hàm `rewind()` di chuyển con trỏ vị trí tệp (file pointer) về lại đầu tệp, tương đương với `fseek(file_ptr, 0L, SEEK_SET);`.

### Câu 221
What is the purpose of the `sizeof` operator in C?
A. It returns the size of a variable or data type in bytes.
B. It returns the value of a variable.
C. It declares the size of an array.
D. It calculates the sum of two numbers.
> **Giải thích:**
> **Đáp án đúng là A.** Toán tử `sizeof` trả về kích thước (tính bằng byte) của một biến hoặc một kiểu dữ liệu.

### Câu 222
What is the `fseek()` function used for?
A. To move the file position indicator to a specific location.
B. To close a file.
C. To read characters from a file.
D. To write characters to a file.
> **Giải thích:**
> **Đáp án đúng là A.** Hàm `fseek()` được sử dụng để di chuyển con trỏ vị trí tệp đến một vị trí cụ thể trong tệp, cho phép truy cập ngẫu nhiên vào nội dung tệp.

### Câu 223
What is the purpose of the `continue` statement in a loop?
A. To skip the rest of the code inside the loop and move to the next iteration.
B. To jump to the beginning of the loop.
C. To exit the entire program.
D. To increment/decrement a variable in the loop.
> **Giải thích:**
> **Đáp án đúng là A.** Lệnh `continue` sẽ bỏ qua phần còn lại của thân vòng lặp trong lần lặp hiện tại và bắt đầu ngay lần lặp tiếp theo.

### Câu 224
What is the purpose of an `if-else` statement in programming?
A. It is used to decide whether a part of the code will be executed or not based on a specified condition.
B. It allows you to repeat a block of code a specified number of times.
C. It is used to define a function in a programming language.
D. It is used to declare variables and assign values to them.
> **Giải thích:**
> **Đáp án đúng là A.** Cấu trúc `if-else` là một cấu trúc điều khiển rẽ nhánh, cho phép chương trình thực hiện các khối mã khác nhau dựa trên việc một điều kiện là đúng hay sai.

### Câu 225
What is the purpose of the increment or decrement expression in a `for` loop?
A. It is executed after each iteration of the loop to update loop control variables.
B. It determines when the loop should stop.
C. It is executed before the loop starts to initialize loop control variables.
D. It specifies the condition to be checked.
> **Giải thích:**
> **Đáp án đúng là A.** Phần thứ ba trong câu lệnh `for` (ví dụ: `i++`) được thực thi sau mỗi lần lặp, thường được dùng để cập nhật biến điều khiển vòng lặp.

### Câu 226
What is the difference between a `while` loop and a `do-while` loop?
A. The way the condition is checked.
B. They are essentially the same.
C. The type of tasks they can perform.
D. The variable in the loop construct.
> **Giải thích:**
> **Đáp án đúng là A.** Sự khác biệt cơ bản là thời điểm kiểm tra điều kiện:
> *   **`while`:** Kiểm tra điều kiện *trước* khi thực hiện thân vòng lặp.
> *   **`do-while`:** Thực hiện thân vòng lặp *trước*, sau đó mới kiểm tra điều kiện.

### Câu 227
What is a pointer in C programming?
A. A variable that stores anything.
B. A variable that stores the address of another variable or the address of dynamically allocated memory.
C. An address in memory.
D. A variable that stores any number.
> **Giải thích:**
> **Đáp án đúng là B.** Con trỏ là một loại biến đặc biệt có giá trị là một địa chỉ bộ nhớ.

### Câu 228
What is the scope of a global variable in C?
A. Throughout the entire program.
B. Only within the function where it's declared.
C. Only within the block where it's declared.
D. Within the structure where it's defined.
> **Giải thích:**
> **Đáp án đúng là A.** Một biến toàn cục (global variable), được khai báo bên ngoài tất cả các hàm, có thể được truy cập từ bất kỳ đâu trong chương trình sau điểm khai báo của nó.

### Câu 229
What is the `main()` function in C?
A. It is the function where the program's execution starts.
B. Every program has exactly one `main` function.
C. The `main` function always returns an integer value or `void`.
D. All answers are correct.
> **Giải thích:**
> **Đáp án đúng là D.** Tất cả các phát biểu trên đều đúng về hàm `main` trong một chương trình C.

### Câu 230
What is correct about the heap?
A. One of the sections of a program which contains executable instructions.
B. Common variables all functions can access.
C. Dynamically allocated data through explicit statements for memory allocation.
D. Variables defined in functions.
> **Giải thích:**
> **Đáp án đúng là C.** Heap là một vùng nhớ được sử dụng để cấp phát bộ nhớ động (dynamically allocated memory) trong quá trình chạy chương trình, thông qua các hàm như `malloc()` và `calloc()`.

### Câu 231
Which of the following is an incorrect definition?
A. Algorithm: a way to find out a solution.
B. Data: Values are used to describe information.
C. Solution: A situation in which something is hidden.
D. Information: Knowledge about something.
> **Giải thích:**
> **Đáp án đúng là C.** Định nghĩa về "giải pháp" (Solution) là không chính xác. Một giải pháp là một câu trả lời cho một vấn đề, không phải là một tình huống mà cái gì đó bị che giấu.

### Câu 232
What is incorrect about a pointer?
A. Pointers are containers for storing data values, like numbers and characters.
B. If one variable contains the address of another variable, the first variable is said to point to the second.
C. A pointer provides an indirect method of accessing the value of a data item.
D. Pointers can point to variables of other fundamental data types.
> **Giải thích:**
> **Đáp án đúng là A.** Phát biểu A là không chính xác. Con trỏ (Pointers) không lưu trữ giá trị dữ liệu trực tiếp; chúng lưu trữ địa chỉ bộ nhớ nơi giá trị dữ liệu được lưu.

### Câu 233
What is incorrect about the `getchar()` function?
A. The `getchar()` function is defined in the `<stdio.h>` header file.
B. `getchar()` gets a string from stdin.
C. `getchar()` retrieves a single character from the standard input stream buffer.
D. `getchar()` gets a character (an unsigned char) from stdin.
> **Giải thích:**
> **Đáp án đúng là B.** Phát biểu B là sai. Hàm `getchar()` chỉ đọc một ký tự duy nhất, không phải một chuỗi (string).

### Câu 234
What is the correct order of the main components in a function definition?
A. Return type, function name, parameters, and function body.
B. Return type, function name, return value, and function body.
C. Return type, function name, parameters, and return value.
D. Return value, function name, parameters, and function body.
> **Giải thích:**
> **Đáp án đúng là A.** Một định nghĩa hàm đầy đủ bao gồm: Kiểu trả về (Return type), tên hàm (function name), danh sách tham số (parameters), và thân hàm (function body) chứa các câu lệnh.

### Câu 235
What is the function of the `fflush(stdin);` command?
A. Print string out to screen.
B. Receive a string entered from the keyboard.
C. Remove characters being entered from the keyboard.
D. Remove characters that remained in the keyboard buffer.
> **Giải thích:**
> **Đáp án đúng là D.** Lệnh `fflush(stdin)` (trên các hệ thống hỗ trợ) được sử dụng để xóa (remove) các ký tự còn sót lại trong bộ đệm đầu vào (keyboard buffer).

### Câu 236
What is the primary use of the `const` keyword when used with function parameters in C?
A. It prevents the function from modifying the parameter's value.
B. It ensures the parameter is passed by reference.
C. It restricts the parameter's scope to the function.
D. It specifies that the parameter should be initialized.
> **Giải thích:**
> **Đáp án đúng là A.** Khi một tham số hàm được khai báo với từ khóa `const` (ví dụ: `void func(const int x)`), điều đó có nghĩa là giá trị của tham số đó không thể bị thay đổi bên trong hàm.

### Câu 237
What is the primary difference between global variables and local variables in C?
A. Global variables have a wider scope, while local variables are limited to their function's scope.
B. Global variables are initialized automatically to zero, while local variables require explicit initialization.
C. Local variables cannot be modified, while global variables allow modification.
D. Global variables can only be used within the `main` function.
> **Giải thích:**
> **Đáp án đúng là A.** Sự khác biệt chính là về phạm vi (scope). Biến toàn cục (global) có thể được truy cập từ mọi nơi trong chương trình, trong khi biến cục bộ (local) chỉ có thể được truy cập bên trong hàm hoặc khối lệnh mà nó được khai báo.

### Câu 238
What does the return value of the `scanf` function indicate?
A. The function returns the number of items successfully read and assigned.
B. The function returns the total number of items in the argument list.
C. The function returns the number of items that were not successfully filled.
D. The function does not return any value.
> **Giải thích:**
> **Đáp án đúng là A.** Hàm `scanf` trả về số lượng mục đã được đọc và gán thành công. Giá trị này có thể được dùng để kiểm tra xem việc nhập liệu có thành công hay không.

### Câu 239
What does the statement `rewind(fp);` do?
A. Bring the pointer `fp` back to the beginning of the file.
B. Assign to the pointer `fp` the address `0x00` (NULL).
C. Bring the pointer `fp` to the end of the file.
D. Bring the pointer `fp` back to the beginning of the current line.
> **Giải thích:**
> **Đáp án đúng là A.** Hàm `rewind()` đặt lại con trỏ vị trí tệp về đầu tệp.

### Câu 240
What does the expression `sizeof(arr) / sizeof(arr[0])` evaluate to, where `arr` is an array?
A. The number of elements in `arr`.
B. The size of `arr` in bytes.
C. The number of bytes occupied by each element in `arr`.
D. The total size of `arr` in bits.
> **Giải thích:**
> **Đáp án đúng là A.** Đây là một thành ngữ (idiom) phổ biến trong C để tính số lượng phần tử của một mảng. `sizeof(arr)` trả về tổng kích thước của mảng tính bằng byte, và `sizeof(arr[0])` trả về kích thước của một phần tử. Phép chia này sẽ cho ra số lượng phần tử.

### Câu 242
What will happen if the loop's condition is always true?
A. Loop infinitely.
B. No Output will be printed.
C. Compile time error.
D. The loop will not work.
> **Giải thích:**
> **Đáp án đúng là A.** Nếu điều kiện của một vòng lặp (`while` hoặc `for`) không bao giờ trở thành sai, vòng lặp sẽ tiếp tục chạy mãi mãi, gây ra một vòng lặp vô hạn (infinite loop).

### Câu 243
What benefit does `#define` offer when dealing with "magic values" in code?
A. It improves code readability and maintainability.
B. It makes the code shorter.
C. It prevents the use of symbolic names.
D. It increases code complexity.
> **Giải thích:**
> **Đáp án đúng là A.** Sử dụng `#define` để đặt tên cho các hằng số (thay vì dùng trực tiếp các giá trị "ma thuật" như `3.14` hay `100`) giúp mã nguồn dễ đọc hơn. Nếu cần thay đổi giá trị, bạn chỉ cần sửa ở một nơi duy nhất, giúp cải thiện khả năng bảo trì.
> *(Câu trả lời đã được diễn giải lại cho chính xác hơn)*.

### Câu 244
What happens when the return statement has a `double` expression and the function return type is `int`?
A. There is an error.
B. This causes a run-time error.
C. This is system dependent.
D. There is a conversion from `double` to `int`.
> **Giải thích:**
> **Đáp án đúng là D.** Trình biên dịch sẽ tự động thực hiện một phép ép kiểu thu hẹp (narrowing conversion) từ `double` sang `int`. Phần thập phân của giá trị `double` sẽ bị cắt bỏ. Đây không phải là lỗi nhưng có thể gây mất mát dữ liệu và trình biên dịch thường sẽ đưa ra một cảnh báo (warning).

### Câu 246
Which is an incorrect statement in C programming?
A. `#define` is a preprocessor command often used to introduce named constants.
B. `double` and `goto` are keywords for declaring data types.
C. `return 0;` is normally the last statement in `main()`.
D. The file `stdio.h` is the library where the compiler finds `scanf()`.
> **Giải thích:**
> **Đáp án đúng là B.** Phát biểu B là sai. `double` là một từ khóa để khai báo kiểu dữ liệu, nhưng `goto` là một từ khóa cho lệnh nhảy, không phải là kiểu dữ liệu.

### Câu 247
Which of the following statements is incorrect?
A. To make our programs longer, we use higher-level languages.
B. Program code in a high-level language must be translated to binary code before running.
C. C is based on a view of structured programming.
D. Programs that perform simple tasks written in assembly language contain a large number of statements.
> **Giải thích:**
> **Đáp án đúng là A.** Phát biểu A là sai. Chúng ta sử dụng ngôn ngữ bậc cao để làm cho chương trình dễ viết, dễ đọc và dễ bảo trì hơn, thường dẫn đến mã nguồn ngắn gọn hơn so với hợp ngữ, chứ không phải để làm cho chúng dài ra.

### Câu 248
Which of the following statements about the `strstr` function in C is true?
A. Compares two strings.
B. Returns a pointer to the first occurrence of the given substring in the main string.
C. Concatenates the source string to the end of the destination string.
D. Copies the source string to the destination string.
> **Giải thích:**
> **Đáp án đúng là B.** Hàm `strstr()` được dùng để tìm một chuỗi con bên trong một chuỗi chính.

### Câu 249
Which of the following accurately describes the scope of a local variable in C?
A. It is visible only within the function or block where it's declared.
B. It is accessible throughout the entire program.
C. It can be accessed by any function within the same source file.
D. It is available globally but with restricted modification rights.
> **Giải thích:**
> **Đáp án đúng là A.** Biến cục bộ (local variable) chỉ tồn tại và có thể được truy cập bên trong hàm hoặc khối lệnh (`{...}`) mà nó được khai báo.

### Câu 250
Which of the following is TRUE about the `while` loop in C?
A. The loop will always execute at least once.
B. The condition is checked after each iteration.
C. The loop will never execute if the condition is initially false.
D. The loop requires an increment statement inside the body.
> **Giải thích:**
> **Đáp án đúng là C.** Vòng lặp `while` là một vòng lặp kiểm tra trước (pre-test loop). Nếu điều kiện sai ngay từ lần kiểm tra đầu tiên, thân vòng lặp sẽ không được thực thi lần nào.

### Câu 251
Which of the following is true regarding the declaration of a two-dimensional array in C?
A. Both the number of rows and columns must be specified.
B. The number of columns must be specified.
C. The number of rows must be specified.
D. The number of rows and columns can be determined dynamically at runtime.
> **Giải thích:**
> **Đáp án đúng là B.** Khi khai báo một mảng hai chiều (hoặc nhiều chiều), bạn có thể bỏ qua kích thước của chiều đầu tiên *nếu* bạn khởi tạo mảng ngay lúc đó. Tuy nhiên, bạn bắt buộc phải chỉ định kích thước của tất cả các chiều còn lại (chiều cột, chiều sâu, v.v.) để trình biên dịch biết cách tính toán vị trí của các phần tử.

### Câu 253
How can you check if a file was successfully opened for writing in C?
A. Checking the return value of `fopen()`.
B. Using `ferror()`.
C. Using `feof()`.
D. Using `fprintf()`.
> **Giải thích:**
> **Đáp án đúng là A.** Hàm `fopen()` sẽ trả về một con trỏ `NULL` nếu nó không thể mở tệp vì một lý do nào đó. Do đó, cách kiểm tra phổ biến là: `if (file_ptr == NULL) { ... handle error ... }`.

### Câu 255
How does compilation differ from interpretation in the context of the C programming language?
A. Compilation involves converting the entire source code to machine code before execution, while interpretation involves executing code line by line.
B. Compilation and interpretation are two terms that are used interchangeably.
C. Algorithm is another term for interpretation.
D. IDE tools are responsible for both processes.
> **Giải thích:**
> **Đáp án đúng là A.**
> *   **Biên dịch (Compilation):** Toàn bộ mã nguồn được dịch một lần sang ngôn ngữ máy, tạo ra một tệp thực thi. Tệp này sau đó có thể được chạy độc lập. C là ngôn ngữ biên dịch.
> *   **Thông dịch (Interpretation):** Một chương trình (trình thông dịch) đọc mã nguồn và thực thi nó theo từng dòng một, mà không tạo ra tệp thực thi riêng.

### Câu 256
How does a "for" loop differ from a "while" loop in C programming?
A. A "for" loop is typically used for iterating over a sequence a known number of times, while a "while" loop is used to execute a block of code repeatedly as long as a condition is true.
B. A "for" loop is for conditional statements, while a "while" loop is for sequential processing.
C. The use of "for" and "while" loops is interchangeable.
D. A "for" loop is exclusively used with arrays.
> **Giải thích:**
> **Đáp án đúng là A.** Mặc dù về mặt kỹ thuật, bất kỳ vòng lặp `for` nào cũng có thể được viết lại bằng `while` và ngược lại, nhưng chúng có mục đích sử dụng khác nhau. `for` thường được dùng khi bạn biết trước số lần lặp hoặc có một biến đếm rõ ràng. `while` thường được dùng khi điều kiện dừng không phụ thuộc vào một chuỗi đếm đơn giản.

### Câu 259
Choose the correct statement related to the array.
A. Arrays provide constant-time access to elements.
B. Arrays allow for dynamic resizing during runtime.
C. Arrays can store elements of different data types.
D. Arrays automatically adjust their size.
> **Giải thích:**
> **Đáp án đúng là A.** Ưu điểm lớn nhất của mảng là khả năng truy cập ngẫu nhiên với thời gian không đổi (constant-time access), O(1). Tức là, thời gian để truy cập `arr[i]` không phụ thuộc vào giá trị của `i`. Các mảng tĩnh trong C không thể thay đổi kích thước.

### Câu 260
Choose the correct definition for "Simple data types" in C programming.
A. Changing from one form of representation to another.
B. A category of data that represents individual, non-complex elements such as integers, floating-point numbers, and characters.
C. Performing operations and expressions on data.
D. Storing a collection of elements accessible by an index.
> **Giải thích:**
> **Đáp án đúng là B.** Kiểu dữ liệu đơn giản (còn gọi là kiểu nguyên thủy - primitive) là các kiểu dữ liệu cơ bản nhất, dùng để biểu diễn các giá trị đơn lẻ như `int`, `char`, `float`, `double`.

### Câu 262
During the compilation process, what will be done with comments?
A. The comment mark will be removed, but the content will be compiled.
B. The comment is treated as an array of characters.
C. Comments are removed in the pre-processing step.
D. Each comment is compiled as a statement that does nothing.
> **Giải thích:**
> **Đáp án đúng là C.** Trong giai đoạn tiền xử lý (pre-processing), trước khi quá trình biên dịch thực sự bắt đầu, bộ tiền xử lý sẽ loại bỏ tất cả các chú thích (comments) khỏi mã nguồn.

### Câu 263
A real-world example of a `switch` statement in C is:
A. Checking the day of the week.
B. Sorting an array ascending.
C. Sorting an array descending.
D. Finding the average value of a sequence.
> **Giải thích:**
> **Đáp án đúng là A.** Cấu trúc `switch` rất phù hợp cho các tình huống cần thực hiện các hành động khác nhau dựa trên một số lượng hữu hạn các giá trị cụ thể của một biến, ví dụ như kiểm tra một biến số nguyên đại diện cho các ngày trong tuần (1=Thứ hai, 2=Thứ ba, v.v.).

### Câu 264
In C, what is the purpose of the `|` operator?
A. It is a bitwise OR operator.
B. It is a logical AND operator.
C. It is a bitwise AND operator.
D. It is a logical OR operator.
> **Giải thích:**
> **Đáp án đúng là A.** Toán tử `|` là toán tử OR trên bit (bitwise OR). Toán tử OR logic là `||`.

### Câu 265
In the C programming language, what is the function `fprintf()` used for?
A. Writing formatted data to a file.
B. Reading formatted data from a file.
C. Appending formatted data to a file.
D. Closing a file.
> **Giải thích:**
> **Đáp án đúng là A.** Hàm `fprintf()` hoạt động giống như `printf` nhưng ghi dữ liệu đã được định dạng vào một tệp (file).

### Câu 266
In a C program, what happens if none of the conditions in an `if-else if-...` statement are true, and there is no final `else` block?
A. The program will skip the `if-else if` block and continue with the next statement.
B. The program will raise an error.
C. The last `else if` block will be executed.
D. The program will terminate abruptly.
> **Giải thích:**
> **Đáp án đúng là A.** Nếu không có điều kiện nào trong chuỗi `if-else if` là đúng và không có khối `else` cuối cùng, toàn bộ cấu trúc sẽ bị bỏ qua và chương trình sẽ tiếp tục thực thi từ câu lệnh ngay sau nó.

### Câu 267
In computers, what are the basic number systems and their corresponding bases used?
A. Decimal (Base-10), Binary (Base-2), Octal (Base-8), Hexadecimal (Base-16).
B. Only Decimal and Binary.
C. Only Binary.
D. Only Decimal.
> **Giải thích:**
> **Đáp án đúng là A.** Tất cả bốn hệ đếm này đều được sử dụng phổ biến trong khoa học máy tính.
> *(Câu trả lời đã được tổng hợp lại từ các lựa chọn)*.

### Câu 268
In bubble sort for an array to be sorted in ascending order, after each pass, where is the largest element in the unsorted part of the array located?
A. It is moved to the end of the unsorted part.
B. It is moved to the beginning of the sorted part.
C. It stays in its position.
D. It is removed from the array.
> **Giải thích:**
> **Đáp án đúng là A.** Sau mỗi lượt của thuật toán sắp xếp nổi bọt (bubble sort), phần tử lớn nhất trong phần chưa sắp xếp sẽ "nổi" lên vị trí cuối cùng của phần đó, trở thành một phần của vùng đã sắp xếp.

### Câu 269
In the context of arrays in the C language, what does traversal refer to?
A. The process of accessing each element in an array sequentially.
B. The process of searching for a specific element in an array.
C. The process of resizing the array during runtime.
D. The process of inserting elements into an array.
> **Giải thích:**
> **Đáp án đúng là A.** Duyệt mảng (traversal) là quá trình đi qua và xử lý từng phần tử của mảng, thường là theo thứ tự từ đầu đến cuối.

### Câu 270
The `rand()` function in C is used for:
A. Generating a pseudo-random integer.
B. Generating a random integer from min to max.
C. Generating a random float from min to max.
D. Generating a random float.
> **Giải thích:**
> **Đáp án đúng là A.** Hàm `rand()` trong `stdlib.h` trả về một số nguyên ngẫu nhiên giả (pseudo-random integer) trong khoảng từ 0 đến `RAND_MAX`. Để có một số trong khoảng `[min, max]`, bạn cần thực hiện thêm các phép toán (thường là modulo và cộng).

### Câu 271
The `^` operator in the C programming language is used to \_\_\_\_\_\_.
A. XOR two bit sequences.
B. OR two bit sequences.
C. AND two bit sequences.
D. SHIFT UP a bit sequence.
E. Calculate the exponential value.
> **Giải thích:**
> **Đáp án đúng là A.** Toán tử `^` trong C là toán tử XOR trên bit (bitwise XOR). Nó không phải là toán tử lũy thừa.

# References

