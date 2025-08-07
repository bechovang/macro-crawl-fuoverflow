
2025-08-06 23:52

Status:

Tags: [[source]] [[CEA]]
Disable spell check :`teh`
# SOURCE CEA 103-201

## III. Ngân hàng câu hỏi trắc nghiệm (tiếp theo)

### Câu 103
In modern computers, which of the following memory types usually has the smallest capacity?
A. RAM
B. Magnetic Tape
C. Hard Disk Drive
D. Cache Memory
> **Giải thích:**
> **Đáp án đúng là D.** Trong hệ thống phân cấp bộ nhớ, bộ nhớ đệm (Cache Memory) là bộ nhớ có dung lượng nhỏ nhất nhưng tốc độ nhanh nhất, nằm gần CPU nhất để tăng tốc độ truy cập dữ liệu.

### Câu 104
"Multiple processors share a single memory or pool of memory by means of a shared bus or other interconnection mechanism; a distinguishing feature is that the memory access time to any region of memory is approximately the same for each processor". Which concept does this statement belong to?
A. Symmetric multiprocessor (SMP)
B. Nonuniform memory access (NUMA)
C. Cluster
D. Single instruction, multiple data (SIMD)
> **Giải thích:**
> **Đáp án đúng là A.** Đây là định nghĩa của kiến trúc đa xử lý đối xứng (Symmetric Multiprocessor - SMP), còn được gọi là UMA (Uniform Memory Access). Đặc điểm chính là tất cả các bộ xử lý chia sẻ chung một bộ nhớ và có thời gian truy cập bộ nhớ đồng đều.

### Câu 105
Which component performs the computer's data processing functions?
A. Arithmetic and logic unit (ALU)
B. Control unit
C. CPU interconnection
D. Registers
> **Giải thích:**
> **Đáp án đúng là A.** Đơn vị Số học và Logic (Arithmetic and Logic Unit - ALU) là thành phần bên trong CPU chịu trách nhiệm thực hiện các chức năng xử lý dữ liệu, bao gồm các phép toán số học (cộng, trừ) và logic (AND, OR, NOT).

### Câu 106
The pulse rate in the clock system is known as the \_\_\_\_\_\_.
A. clock cycle
B. clock speed
C. clock time
D. clock tick
> **Giải thích:**
> **Đáp án đúng là B.** Tốc độ xung nhịp (Clock speed), hay tần số xung nhịp, là số chu kỳ (xung tín hiệu) mà CPU có thể thực hiện trong một giây, thường được đo bằng Hertz (Hz), Megahertz (MHz) hoặc Gigahertz (GHz).

### Câu 107
The first generation of computers used \_\_\_\_\_\_ for digital logic elements and memory.
A. Transistor
B. Integrated Circuits
C. Large-scale integration
D. Vacuum Tubes
> **Giải thích:**
> **Đáp án đúng là D.** Thế hệ máy tính đầu tiên (khoảng thập niên 1940-1950) sử dụng bóng đèn chân không (Vacuum Tubes) làm thành phần điện tử chính cho các mạch logic và bộ nhớ.

### Câu 108
The I/O technique where the processor "busy waits" for an I/O operation to complete is called \_\_\_\_\_\_.
A. Programmed I/O or DMA
B. Interrupt-driven I/O
C. Direct Memory Access (DMA)
D. Programmed I/O
> **Giải thích:**
> **Đáp án đúng là D.** Trong kỹ thuật Vào/Ra được lập trình (Programmed I/O), CPU phải liên tục kiểm tra trạng thái của thiết bị I/O để xem thao tác đã hoàn thành chưa. Quá trình chờ đợi và kiểm tra liên tục này được gọi là "busy waiting".

### Câu 109
The task of subdivision of memory is carried out dynamically by the OS and is known as \_\_\_\_\_\_.
A. Scheduling
B. Memory management
C. Virtual Memory
D. All of the mentioned
> **Giải thích:**
> **Đáp án đúng là B.** Quản lý bộ nhớ (Memory management) là một trong những chức năng chính của hệ điều hành, bao gồm việc cấp phát và thu hồi các phần bộ nhớ cho các tiến trình một cách linh động.

### Câu 110
The PC, IR, MAR, MBR registers belong to which of the following groups?
A. Control and Status Registers
B. User-Visible Registers
C. General Registers
D. Handle Registers
> **Giải thích:**
> **Đáp án đúng là A.** Các thanh ghi này rất quan trọng cho việc điều khiển hoạt động của CPU và không thể được lập trình viên truy cập trực tiếp.
> *   PC (Program Counter): Chứa địa chỉ lệnh kế tiếp.
> *   IR (Instruction Register): Chứa lệnh đang được thực thi.
> *   MAR (Memory Address Register): Chứa địa chỉ bộ nhớ cần truy cập.
> *   MBR (Memory Buffer Register): Chứa dữ liệu đọc/ghi từ bộ nhớ.
> Chúng thuộc nhóm thanh ghi Điều khiển và Trạng thái (Control and Status Registers).

### Câu 111
To enhance performance in a superscalar processor, which method(s) can be applied?
A. Duplication of resources
B. Out-of-order issue
C. Renaming registers
D. All of the mentioned
> **Giải thích:**
> **Đáp án đúng là D.** Để tăng hiệu năng của một bộ xử lý siêu vô hướng (superscalar processor), người ta có thể áp dụng tất cả các kỹ thuật trên: nhân bản tài nguyên (Duplication of resources) như có nhiều ALU, thực thi ngoài thứ tự (Out-of-order issue) để giảm thời gian chờ, và đổi tên thanh ghi (Renaming registers) để giải quyết các xung đột dữ liệu.

### Câu 112
The hardware mechanism that allows a device to notify the CPU is called \_\_\_\_\_\_.
A. polling
B. interrupt
C. driver
D. controlling
> **Giải thích:**
> **Đáp án đúng là B.** Ngắt (Interrupt) là một tín hiệu phần cứng từ một thiết bị gửi đến CPU để thông báo rằng nó cần sự chú ý hoặc đã hoàn thành một tác vụ, cho phép CPU dừng công việc hiện tại để xử lý yêu cầu.

### Câu 113
The process where chunks of a program, known as pages, are assigned to available chunks of memory, known as frames, is called \_\_\_\_\_\_.
A. Swapping
B. Partitioning
C. Paging
D. Virtual Memory
E. Segmentation
> **Giải thích:**
> **Đáp án đúng là C.** Phân trang (Paging) là một kỹ thuật quản lý bộ nhớ trong đó không gian địa chỉ logic của một tiến trình được chia thành các khối có kích thước cố định gọi là trang (pages), và bộ nhớ vật lý được chia thành các khối cùng kích thước gọi là khung (frames).

### Câu 114
The decision as to which process's pending I/O request shall be handled by an available I/O device is called \_\_\_\_\_\_.
A. Medium-term scheduling
B. Short-term scheduling
C. I/O scheduling
D. Long-term scheduling
> **Giải thích:**
> **Đáp án đúng là C.** Lập lịch Vào/Ra (I/O scheduling) là nhiệm vụ của hệ điều hành trong việc quyết định thứ tự các yêu cầu I/O đang chờ sẽ được phục vụ bởi một thiết bị I/O.

### Câu 115
With the hard disk data layout, the set of all the tracks in the same relative position on the platters is called a \_\_\_\_\_\_.
A. Cylinder
B. Track
C. Inter-track gap
D. Sector
> **Giải thích:**
> **Đáp án đúng là A.** Một trụ (Cylinder) là một tập hợp các rãnh (tracks) có cùng bán kính trên tất cả các mặt đĩa của một ổ đĩa cứng.

### Câu 116
The long-term queue of process requests is typically stored on \_\_\_\_\_\_.
A. main memory
B. disk
C. cache memory
D. registers
> **Giải thích:**
> **Đáp án đúng là B.** Hàng đợi dài hạn (long-term queue), hay hàng đợi công việc (job queue), chứa tất cả các tiến trình trong hệ thống đang chờ được cấp phát tài nguyên và đưa vào bộ nhớ. Hàng đợi này thường được lưu trữ trên đĩa (disk).

### Câu 118
What are the most important general categories of data that machine instructions operate on?
A. Addresses, numbers, characters, and logical data
B. Text, images, and audio
C. Variables, functions, and arrays
D. Instructions, control signals, and registers
> **Giải thích:**
> **Đáp án đúng là A.** Các lệnh máy tính ở mức cơ bản hoạt động trên các loại dữ liệu sau:
> *   **Địa chỉ (Addresses):** Để truy cập bộ nhớ.
> *   **Số (Numbers):** Số nguyên hoặc số thực để tính toán.
> *   **Ký tự (Characters):** Ví dụ như mã ASCII để xử lý văn bản.
> *   **Dữ liệu logic (Logical data):** Các giá trị bit (0, 1) cho các phép toán logic.

### Câu 119
What is the correct order of memory access speed from fastest to slowest?
A. Registers > Cache > RAM > SSD
B. Cache > Registers > RAM > SSD
C. Registers > Cache > SSD > RAM
D. Cache > Registers > SSD > RAM
> **Giải thích:**
> **Đáp án đúng là A.** Theo hệ thống phân cấp bộ nhớ (memory hierarchy), tốc độ truy cập giảm dần theo thứ tự: Thanh ghi (Registers) -> Bộ nhớ đệm (Cache) -> Bộ nhớ chính (RAM) -> Bộ nhớ thứ cấp (SSD/HDD).

### Câu 120
Sort the following memory types in ascending order by access speed (slowest to fastest):
A. HDD -> Main Memory -> L2 cache -> L1 cache
B. HDD -> Main Memory -> L1 cache -> L2 cache
C. HDD -> L2 cache -> L1 cache -> Main Memory
D. Main Memory -> L2 cache -> L1 cache -> HDD
> **Giải thích:**
> **Đáp án đúng là A.** Sắp xếp theo tốc độ truy cập tăng dần (từ chậm nhất đến nhanh nhất): Ổ đĩa cứng (HDD) là chậm nhất, tiếp theo là Bộ nhớ chính (Main Memory/RAM), sau đó đến các cấp cache. Cache L2 chậm hơn L1, nên thứ tự đúng là HDD -> Main Memory -> L2 cache -> L1 cache.

### Câu 121
Which order is correct for increasing performance and endurance?
A. Hard Disk -> DRAM -> NAND Flash -> SRAM
B. Hard Disk -> NAND Flash -> DRAM -> SRAM
C. NAND Flash -> Hard Disk -> SRAM -> DRAM
D. Hard Disk -> DRAM -> SRAM -> NAND Flash
> **Giải thích:**
> **Đáp án đúng là B.**
> *   **Hiệu năng (Performance):** SRAM (dùng cho cache) nhanh nhất, tiếp đến là DRAM (RAM chính), rồi đến NAND Flash (SSD), và cuối cùng là Hard Disk (HDD).
> *   **Độ bền (Endurance):** SRAM và DRAM có độ bền gần như vô hạn. NAND Flash có số chu kỳ ghi/xóa giới hạn. Hard Disk dễ bị hỏng do các bộ phận cơ học.
> Kết hợp cả hai, thứ tự tăng dần hợp lý nhất trong các lựa chọn là: Hard Disk -> NAND Flash -> DRAM -> SRAM.

### Câu 122
The speed of data delivery is your main concern when configuring a RAID drive for a Media Streaming Server. This server has two hard disks installed. What type of RAID should you use?
A. RAID 0
B. RAID 0, with data mirrored
C. RAID 1
D. RAID 1, with data striped
> **Giải thích:**
> **Đáp án đúng là A.** Khi ưu tiên hàng đầu là tốc độ, RAID 0 là lựa chọn tốt nhất. RAID 0 sử dụng kỹ thuật xé nhỏ dữ liệu (striping), ghi dữ liệu đồng thời lên nhiều ổ đĩa để tăng tốc độ đọc/ghi. Nó không cung cấp khả năng chịu lỗi (fault tolerance). Các lựa chọn B và D mô tả mâu thuẫn (RAID 0 không mirror, RAID 1 không stripe).

### Câu 123
Which of the following are the four basic functions that a computer performs?
A. Data processing, Data storage, Data movement, Control
B. Data processing, Data storage, Data movement, Interrupt
C. Data processing, Data storage, Interrupt, Control
D. Data processing, Interrupt, Data movement, Control
> **Giải thích:**
> **Đáp án đúng là A.** Bốn chức năng cơ bản của một máy tính là:
> 1.  **Xử lý dữ liệu (Data processing)**
> 2.  **Lưu trữ dữ liệu (Data storage)**
> 3.  **Di chuyển dữ liệu (Data movement)**
> 4.  **Điều khiển (Control)**

### Câu 124
What methods can be used to access units of data in memory?
A. Indirect access, Direct access, Random access, Associative
B. Sequential access, Indirect access, Random access, Associative
C. Sequential access, Direct access, Random access, Associative
D. Sequential access, Direct access, Random access, Indirect access
> **Giải thích:**
> **Đáp án đúng là C.** Bốn phương pháp truy cập dữ liệu chính là:
> 1.  **Tuần tự (Sequential access):** Phải duyệt qua các đơn vị dữ liệu theo thứ tự (ví dụ: băng từ).
> 2.  **Trực tiếp (Direct access):** Có thể nhảy đến một vùng gần đúng rồi tìm tuần tự (ví dụ: đĩa cứng).
> 3.  **Ngẫu nhiên (Random access):** Có thể truy cập bất kỳ vị trí nào với thời gian gần như không đổi (ví dụ: RAM).
> 4.  **Liên kết (Associative access):** Tìm kiếm dữ liệu dựa trên nội dung thay vì địa chỉ (ví dụ: cache).

### Câu 125
The basic components of a computer are:
A. Main memory, CPU, I/O modules and system interconnection
B. Main memory, CPU, I/O modules and Storage device
C. Main Memory, CPU, Peripherals and Storage device
D. Main memory, CPU, I/O modules and Peripherals
> **Giải thích:**
> **Đáp án đúng là A.** Bốn thành phần cấu trúc cơ bản nhất của một máy tính ở mức độ tổng quan là: Bộ xử lý trung tâm (CPU), Bộ nhớ chính (Main memory), các Module Vào/Ra (I/O modules), và Kết nối hệ thống (System Interconnection) để liên kết chúng lại với nhau.

### Câu 127
What is the primary purpose of the "Fetch instruction" phase in the operation of a processor?
A. To read an instruction from memory
B. To interpret the instruction
C. To perform arithmetic operations on data
D. To write data to memory
> **Giải thích:**
> **Đáp án đúng là A.** Giai đoạn nạp lệnh (Fetch instruction) là bước đầu tiên trong chu kỳ lệnh, trong đó CPU đọc (read) một chỉ thị từ bộ nhớ tại địa chỉ được chỉ định bởi con trỏ lệnh (Program Counter).

### Câu 128
What is the main benefit of using ARM processors over other processors?
A. Low cost and low power consumption
B. Higher degree of multi-tasking
C. Lower error or glitches
D. Efficient memory management
> **Giải thích:**
> **Đáp án đúng là A.** Kiến trúc ARM (Advanced RISC Machine) nổi tiếng với thiết kế tập trung vào hiệu quả năng lượng, dẫn đến chi phí thấp và mức tiêu thụ điện năng thấp (low power consumption), khiến nó trở nên lý tưởng cho các thiết bị di động và nhúng.

### Câu 129
What is an interrupt vector?
A. Part of memory which contains the addresses of interrupt handlers
B. A signal an I/O device sends to CPU
C. A signal an I/O software sends to CPU
D. None of the mentioned
> **Giải thích:**
> **Đáp án đúng là A.** Bảng vector ngắt (Interrupt Vector Table) là một vùng trong bộ nhớ chứa địa chỉ của các chương trình con phục vụ ngắt (interrupt handlers). Khi một ngắt xảy ra, CPU sẽ sử dụng số hiệu ngắt để tra cứu địa chỉ của trình xử lý tương ứng trong bảng này.

### Câu 130
What is the function of the bus system in the computer?
A. Extend the communication function of the computer
B. Connect components in the computer
C. Control peripherals
D. Transform signals in the computer
E. All of the mentioned
> **Giải thích:**
> **Đáp án đúng là B.** Chức năng chính của hệ thống bus (bus system) là cung cấp một đường dẫn truyền thông để kết nối các thành phần chính của máy tính (connect components) như CPU, bộ nhớ, và các module I/O, cho phép chúng trao đổi dữ liệu và tín hiệu điều khiển.

### Câu 131
What is a special feature of Cache Memory?
A. Allows faster access than DRAM memory
B. Memory cache is outboard storage memory
C. Allows faster access than CPU registers
D. Fixed memory - Read Only Memory
E. Has a larger capacity than HDD
> **Giải thích:**
> **Đáp án đúng là A.** Đặc điểm chính của bộ nhớ đệm (Cache Memory), thường được làm từ SRAM, là nó cho phép tốc độ truy cập nhanh hơn đáng kể so với bộ nhớ chính (DRAM memory).

### Câu 132
What is the primary function of the Arithmetic and Logic Unit (ALU) in a processor?
A. Perform actual computations and data processing
B. Control the movement of data and instructions
C. Act as an interface to the system bus
D. Manage the internal processor memory
> **Giải thích:**
> **Đáp án đúng là A.** Chức năng chính của Đơn vị Số học và Logic (ALU) là thực hiện các phép tính toán (computations) và xử lý dữ liệu (data processing) thực tế, như cộng, trừ, và các phép toán logic.

### Câu 133
What is one of the advantages of using a register file in computer architecture?
A. Reduction in memory accesses, saving time
B. More efficient use of space due to dynamic adaptation
C. Efficient handling of both local and global variables
D. Easier management of cache residency
> **Giải thích:**
> **Đáp án đúng là A.** Việc sử dụng một tập các thanh ghi (register file) bên trong CPU cho phép lưu trữ các biến và kết quả trung gian thường xuyên được sử dụng. Điều này làm giảm (reduction) số lần phải truy cập bộ nhớ chính (memory accesses) vốn chậm hơn nhiều, do đó tiết kiệm thời gian và tăng hiệu năng.

### Câu 134
What is true about IAS Memory Formats?
A. The memory of the IAS consists of 1000 storage locations (called words) of 32 bits each
B. Only data is stored in the memory
C. Both data and instructions are stored in the memory
D. Only instructions are stored in the memory
> **Giải thích:**
> **Đáp án đúng là C.** Máy tính IAS là một ví dụ kinh điển của kiến trúc Von Neumann. Một trong những nguyên lý chính của kiến trúc này là cả dữ liệu (data) và chỉ thị (instructions) đều được lưu trữ chung trong cùng một bộ nhớ.

### Câu 135
What is the benefit of using a superscalar organization over a scalar organization?
A. It increases the instruction throughput and improves performance
B. It reduces the power consumption and the heat dissipation
C. It simplifies the instruction set and the compiler design
D. All of the mentioned
> **Giải thích:**
> **Đáp án đúng là A.** Tổ chức siêu vô hướng (superscalar) cho phép thực thi nhiều hơn một chỉ thị trong mỗi chu kỳ xung nhịp bằng cách sử dụng các tài nguyên phần cứng song song. Điều này làm tăng thông lượng lệnh (instruction throughput) và cải thiện hiệu năng tổng thể.

### Câu 136
What is the benefit of cache memory in terms of computer performance?
A. It reduces the computer's power consumption.
B. It speeds up data access and improves system performance.
C. It increases the storage capacity of the computer.
D. It serves as a backup storage for critical files.
> **Giải thích:**
> **Đáp án đúng là B.** Lợi ích chính của bộ nhớ đệm (cache memory) là nó tăng tốc độ truy cập dữ liệu (speeds up data access) bằng cách lưu trữ các dữ liệu thường được sử dụng ở một nơi gần CPU hơn, qua đó cải thiện hiệu năng hệ thống.

### Câu 137
What is the most important characteristic of the Synchronous Bus?
A. Data is transmitted at the same time
B. The occurrence of one event on a bus follows and depends on the occurrence of a previous event.
C. The occurrence of events on the bus is determined by a clock
D. No common clock signal controlling operation
> **Giải thích:**
> **Đáp án đúng là C.** Đặc điểm quan trọng nhất của bus đồng bộ (Synchronous Bus) là mọi sự kiện (truyền địa chỉ, dữ liệu) trên bus đều được điều khiển và đồng bộ hóa bởi một tín hiệu đồng hồ chung (a clock).

### Câu 138
What is one advantage of Nonuniform Memory Access (NUMA) over Uniform Memory Access (UMA)?
A. NUMA provides each processor with its own local memory, reducing memory access times
B. NUMA allows all processors to access the same memory location simultaneously
C. NUMA is easier to implement than UMA
D. NUMA provides limited memory capacity
> **Giải thích:**
> **Đáp án đúng là A.** Trong kiến trúc NUMA, mỗi bộ xử lý có một vùng bộ nhớ cục bộ (local memory) mà nó có thể truy cập nhanh hơn nhiều so với việc truy cập bộ nhớ của các bộ xử lý khác. Điều này giúp giảm thời gian truy cập bộ nhớ và giảm tắc nghẽn trên bus hệ thống.

### Câu 139
What is a branch instruction?
A. The instructions that are used to divide a program into multiple subprograms
B. The instructions that have as one of its operands the address of the next instruction to be executed
C. The instructions that are used to pause the program
D. The instructions that are used to return to the beginning of the program
> **Giải thích:**
> **Đáp án đúng là B.** Lệnh rẽ nhánh (branch instruction), hay lệnh nhảy (jump), là lệnh làm thay đổi luồng thực thi tuần tự của chương trình. Nó chứa địa chỉ của lệnh tiếp theo sẽ được thực thi, thay vì chỉ đơn giản là lệnh nằm ngay sau nó trong bộ nhớ.

### Câu 140
What is the most important function of the control unit (CU)?
A. It manages the order of running instructions.
B. It will read and process data from main memory.
C. It directs the operation of the other CPU components.
D. It will read instructions from main memory then decode them.
> **Giải thích:**
> **Đáp án đúng là C.** Chức năng quan trọng nhất của Đơn vị điều khiển (Control Unit) là điều khiển và phối hợp hoạt động của tất cả các thành phần khác trong CPU (directs the operation of the other CPU components) và cả hệ thống để thực thi các chỉ thị. Các lựa chọn A, B, D là các phần trong chức năng tổng thể đó.

### Câu 141
What is the main difference between x86 and ARM instruction formats?
A. x86 instructions are variable in length, while ARM instructions are fixed
B. x86 instructions are fixed in length, while ARM instructions are variable
C. Both x86 and ARM instructions are fixed in length
D. Both x86 and ARM instructions are variable in length
> **Giải thích:**
> **Đáp án đúng là A.** Một trong những khác biệt cơ bản là kiến trúc CISC của x86 sử dụng các lệnh có độ dài thay đổi (variable in length), trong khi kiến trúc RISC của ARM sử dụng các lệnh có độ dài cố định (fixed), thường là 32-bit.

### Câu 142
What is the main benefit of using RISC over CISC?
A. RISC has more instructions and addressing modes than CISC
B. RISC has faster instruction execution and simpler instruction decoding than CISC
C. RISC has variable-length instruction formats and direct memory access than CISC
D. RISC has more registers and pipelines than CISC
> **Giải thích:**
> **Đáp án đúng là B.** Lợi ích chính của kiến trúc RISC (Máy tính có tập lệnh rút gọn) so với CISC là các lệnh đơn giản và có định dạng cố định, dẫn đến việc giải mã lệnh đơn giản hơn (simpler instruction decoding) và thực thi lệnh nhanh hơn (faster instruction execution), thường là trong một chu kỳ xung nhịp.

### Câu 143
What is the main distinction between Interrupt-Driven I/O and Direct Memory Access (DMA)?
A. Interrupt-Driven I/O involves the CPU in every data transfer, while DMA bypasses the CPU and transfers data directly between the I/O device and memory
B. Interrupt-Driven I/O requires special hardware and software support, while DMA does not need any additional components
C. Interrupt-Driven I/O is suitable for small and frequent data transfers, while DMA is suitable for large and infrequent data transfers
D. All of the mentioned
> **Giải thích:**
> **Đáp án đúng là A.**
> *   **Interrupt-Driven I/O:** CPU vẫn phải thực hiện việc di chuyển từng đơn vị dữ liệu (ví dụ: từng byte) giữa module I/O và bộ nhớ.
> *   **DMA:** CPU chỉ cần khởi tạo việc truyền dữ liệu, sau đó module DMA sẽ tự quản lý việc truyền cả một khối dữ liệu lớn trực tiếp giữa thiết bị I/O và bộ nhớ, giải phóng CPU để làm việc khác.

### Câu 144
What is the Memory Address Register (MAR)?
A. Contains a word to be stored in memory or sent to the I/O unit, or is used to receive a word from memory or from the I/O unit.
B. Employed to hold temporarily the right-hand instruction from a word in memory.
C. Contains the address in memory of the word to be written from or read into the MBR.
D. Contains the address of the next instruction pair to be fetched from memory.
> **Giải thích:**
> **Đáp án đúng là C.** Thanh ghi địa chỉ bộ nhớ (Memory Address Register - MAR) chứa địa chỉ của vị trí trong bộ nhớ mà CPU muốn đọc hoặc ghi dữ liệu. Nó kết nối với bus địa chỉ. Lựa chọn A là mô tả của MBR (Memory Buffer Register).

### Câu 145
What is false about the von Neumann architecture?
A. Data and instructions are stored in a single read-write memory.
B. The contents of this memory are addressable by location, without regard to the type of data contained.
C. Execution occurs in a sequential fashion (unless explicitly modified) from one instruction to the next.
D. Data is stored in main memory and instructions are stored in cache memory.
> **Giải thích:**
> **Đáp án đúng là D.** Điều sai là D. Nguyên lý cốt lõi của kiến trúc Von Neumann là cả dữ liệu và chỉ thị đều được lưu trữ chung trong một bộ nhớ chính duy nhất. Cache chỉ là một bộ nhớ đệm tạm thời chứa bản sao của cả dữ liệu và chỉ thị từ bộ nhớ chính để tăng tốc độ truy cập.

### Câu 146
What is the significance of the program counter (PC) in the fetch phase of the instruction cycle?
A. The program counter (PC) is not used in the fetch phase.
B. The program counter (PC) in the fetch phase holds the memory address of the next instruction to be fetched.
C. The program counter (PC) is responsible for executing instructions.
D. The program counter (PC) is only relevant in multi-core processors.
> **Giải thích:**
> **Đáp án đúng là B.** Vai trò quan trọng của con trỏ lệnh (Program Counter - PC) là nó luôn chứa địa chỉ của lệnh tiếp theo sẽ được nạp (fetched) từ bộ nhớ để thực thi.

### Câu 147
What is the distinction between Computer Architecture and Computer Organization?
A. Computer Architecture is the way the system is structured, while Computer Organization is those attributes of a system that are visible to the user.
B. Computer Architecture is those attributes of a system that are visible to the user, while Computer Organization is the way the system is structured.
C. Computer Architecture and Computer Organization are the same.
D. Computer Architecture is slower than Computer Organization.
> **Giải thích:**
> **Đáp án đúng là B.**
> *   **Kiến trúc máy tính (Computer Architecture):** Là những thuộc tính của hệ thống mà lập trình viên có thể thấy được, ảnh hưởng trực tiếp đến việc lập trình (ví dụ: tập lệnh, số bit biểu diễn dữ liệu, chế độ địa chỉ). Trả lời câu hỏi "Cái gì?".
> *   **Tổ chức máy tính (Computer Organization):** Là cách các thành phần phần cứng được hiện thực hóa và kết nối với nhau để thực thi kiến trúc đó. Nó không hiển thị với lập trình viên (ví dụ: tín hiệu điều khiển, công nghệ bộ nhớ). Trả lời câu hỏi "Như thế nào?".

### Câu 148
What is incorrect about the advantages of SSDs over HDDs?
A. Higher access times and latency rates: Over 10 times slower than the HDD.
B. Durability: Less susceptible to physical shock and vibration.
C. Longer lifespan: SSDs are not susceptible to mechanical wear.
D. Lower power consumption: SSDs use considerably less power than comparable-size HDDs.
E. Quieter and cooler running capabilities.
> **Giải thích:**
> **Đáp án đúng là A.** Phát biểu A là không chính xác. SSD (Solid State Drive) có thời gian truy cập (access times) và độ trễ (latency) thấp hơn nhiều (tức là nhanh hơn) so với HDD (Hard Disk Drive). Các phát biểu còn lại đều là những ưu điểm đúng của SSD.

### Câu 149
What is the role of registers in a processor?
A. Registers in a processor provide fast, temporary storage for data and instructions, facilitating efficient access during instruction execution.
B. Registers are only used to store data temporarily.
C. Registers are solely responsible for storing data from the main memory.
D. Registers have no impact on the speed or efficiency of instruction execution.
> **Giải thích:**
> **Đáp án đúng là A.** Thanh ghi (Registers) là bộ nhớ tạm thời, tốc độ cực cao nằm bên trong CPU. Chúng lưu trữ cả dữ liệu và địa chỉ đang được xử lý, giúp truy cập cực kỳ hiệu quả trong quá trình thực thi lệnh, qua đó tăng tốc độ tổng thể.

### Câu 150
What is the role of the control unit in a processor?
A. The control unit's primary role is to perform arithmetic and logical operations.
B. The control unit only manages the flow of data between the CPU and external devices.
C. The control unit is solely responsible for managing the flow of instructions from secondary storage to RAM.
D. The control unit in a processor directs and coordinates the execution of instructions, interpreting and managing the flow of operations within the CPU.
> **Giải thích:**
> **Đáp án đúng là D.** Đơn vị điều khiển (Control Unit) là "bộ não" của CPU, có vai trò điều khiển và phối hợp tất cả các hoạt động. Nó nạp lệnh, giải mã lệnh, và gửi các tín hiệu điều khiển đến các bộ phận khác (như ALU, thanh ghi) để thực thi lệnh đó.

### Câu 151
What is the main idea of using Hamming code for error correction?
A. Adding extra parity bits to the data bits such that the number of 1s in each subset of bits is even.
B. Adding extra parity bits to the data bits such that the number of 1s in each subset of bits is odd.
C. Adding extra parity bits to the data bits such that the parity bits form a binary number indicating the position of the error bit.
D. Adding extra parity bits to the data bits such that the parity bits form a binary number indicating the number of errors.
> **Giải thích:**
> **Đáp án đúng là C.** Ý tưởng chính của mã Hamming là thêm vào các bit chẵn lẻ (parity bits). Khi kiểm tra, các bit chẵn lẻ này sẽ tạo thành một số nhị phân (gọi là syndrome). Nếu syndrome khác 0, giá trị của nó sẽ chỉ ra chính xác vị trí (position) của bit bị lỗi, cho phép sửa lỗi đó.

### Câu 152
What are the key differences in the architecture of NOR and NAND flash memory?
A. NOR flash memory cells are connected in series, while NAND flash memory cells are connected in parallel.
B. NOR flash memory cells are connected in parallel, while NAND flash memory cells are connected in series.
C. Both NOR and NAND flash memory cells are connected in series.
D. Both NOR and NAND flash memory cells are connected in parallel.
> **Giải thích:**
> **Đáp án đúng là B.**
> *   **NOR Flash:** Các ô nhớ được kết nối song song (parallel) với đường bit, cho phép truy cập ngẫu nhiên nhanh (giống như RAM), phù hợp để lưu trữ mã thực thi.
> *   **NAND Flash:** Các ô nhớ được kết nối nối tiếp (series) thành các chuỗi, giúp tiết kiệm diện tích và có mật độ cao hơn, phù hợp để lưu trữ dữ liệu lớn (như trong SSD).

### Câu 153
What does CISC stand for?
A. Complex Instruction Set Computer
B. Computer Instruction Set Complex
C. Complex Instruction Summarize Computer
D. Computer Instruction Summarize Complex
> **Giải thích:**
> **Đáp án đúng là A.** CISC là viết tắt của Complex Instruction Set Computer, tức là Máy tính có tập lệnh phức tạp.

### Câu 154
What does the x86 assembly instruction "jmp label" typically do?
A. Jumps to the memory address stored in the label.
B. Jumps to the next instruction.
C. Jumps to the label if a specific condition is met.
D. Moves the label's address to the EIP register.
> **Giải thích:**
> **Đáp án đúng là D.** Lệnh `jmp label` là một lệnh nhảy không điều kiện. Về mặt kỹ thuật, nó hoạt động bằng cách thay đổi giá trị của thanh ghi con trỏ lệnh (Instruction Pointer - EIP trong kiến trúc 32-bit) thành địa chỉ của nhãn (label), khiến cho lệnh tiếp theo được nạp và thực thi sẽ là lệnh tại nhãn đó.

### Câu 155
What does the term "instruction-level parallelism" refer to in computer architecture?
A. The degree to which instructions in a program can be executed in parallel.
B. The number of processor cores in a multi-core CPU.
C. The complexity of the instruction set architecture.
D. The length of an instruction cycle.
> **Giải thích:**
> **Đáp án đúng là A.** Song song ở cấp độ lệnh (Instruction-Level Parallelism - ILP) đề cập đến khả năng của một bộ xử lý trong việc thực thi nhiều chỉ thị từ một chương trình một cách song song hoặc chồng chéo (ví dụ: thông qua pipelining, superscalar).

### Câu 156
What role does an Application Programming Interface (API) play in software development?
A. It allows programs to access hardware resources using high-level language libraries.
B. It defines low-level machine instructions.
C. It provides a standard for binary portability.
D. It manages system resources.
> **Giải thích:**
> **Đáp án đúng là A.** Giao diện lập trình ứng dụng (Application Programming Interface - API) cung cấp một tập hợp các hàm, thủ tục, và quy tắc được định nghĩa trước. Nó cho phép các chương trình ứng dụng tương tác với các thư viện hoặc dịch vụ của hệ điều hành để truy cập tài nguyên phần cứng hoặc các chức năng khác một cách dễ dàng, mà không cần biết chi tiết triển khai cấp thấp.

### Câu 158
Which of the following determines the Bus Width?
A. The clock speed of the CPU
B. The number of cores in the processor
C. The size of the motherboard
D. The number of parallel lines in the data bus
E. Number of components connected to Bus
> **Giải thích:**
> **Đáp án đúng là D.** Độ rộng của bus (Bus Width), đặc biệt là bus dữ liệu, được xác định bởi số lượng đường dây song song (number of parallel lines) mà nó có. Ví dụ, một bus dữ liệu 64-bit có 64 đường dây, cho phép truyền 64 bit cùng một lúc.

### Câu 159
Which one of the following is an invalid statement about RAM?
A. Both static and dynamic RAMs are volatile.
B. A dynamic memory cell is simpler and smaller than a static memory cell.
C. Both static and dynamic RAMs require supporting refresh circuitry.
D. SRAMs are somewhat faster than DRAMs.
> **Giải thích:**
> **Đáp án đúng là C.** Phát biểu C là không hợp lệ. Chỉ có DRAM (Dynamic RAM) mới cần mạch làm mới (refresh circuitry) để nạp lại các tụ điện lưu trữ bit một cách định kỳ. SRAM (Static RAM) không cần làm mới, nó sẽ giữ dữ liệu miễn là có nguồn điện.

### Câu 160
Which of the following statements is true for a strict Von Neumann architecture?
A. A shared bus between the program memory and data memory.
B. A separate bus between the program memory and data memory.
C. An external bus for program memory and data memory.
D. An external bus for data memory only.
> **Giải thích:**
> **Đáp án đúng là A.** Một đặc điểm của kiến trúc Von Neumann là nó sử dụng một bộ nhớ duy nhất và một bus chung (shared bus) cho cả chỉ thị và dữ liệu. Điều này tạo ra một nút thắt cổ chai (Von Neumann bottleneck) vì không thể nạp lệnh và truy cập dữ liệu cùng một lúc.

### Câu 161
Which of the following statements is NOT part of the Von Neumann principles?
A. Computers can operate according to a stored program.
B. The computer uses a program counter to indicate the location of the next statement.
C. A computer's memory is addressable.
D. Each instruction must have a memory area containing the address of the next instruction.
> **Giải thích:**
> **Đáp án đúng là D.** Phát biểu D là sai. Trong kiến trúc Von Neumann, địa chỉ của lệnh tiếp theo thường được xác định bằng cách tăng con trỏ lệnh (program counter), chứ không phải mỗi lệnh đều phải chứa địa chỉ của lệnh kế tiếp. Lệnh chứa địa chỉ kế tiếp chỉ xảy ra với các lệnh rẽ nhánh (branch/jump).

### Câu 162
Which of the following statements is part of the Von Neumann principles?
A. The computer uses a program counter to indicate the location of the next instruction.
B. The computer can control all operations with a single program.
C. Computer memory is not addressable.
D. Each instruction must have a memory area containing the address of the next instruction.
> **Giải thích:**
> **Đáp án đúng là A.** Một trong những nguyên lý của kiến trúc Von Neumann là sử dụng một con trỏ lệnh (program counter) để theo dõi và chỉ đến địa chỉ của lệnh tiếp theo sẽ được thực thi.

### Câu 163
Which of the following statements is incorrect about the Translation Look-aside Buffer (TLB)?
A. The use of TLB eliminates the need for keeping a page table in memory.
B. TLB only maintains a subset of the entries stored in the full memory-based page table.
C. When there is a TLB miss, the system needs to access the page table.
D. A translation lookaside buffer (TLB) is a memory cache that stores recent translations of virtual memory to physical memory.
> **Giải thích:**
> **Đáp án đúng là A.** Phát biểu A là không chính xác. TLB chỉ là một bộ nhớ đệm (cache) cho một phần nhỏ của bảng trang (page table). Nó không loại bỏ sự cần thiết của bảng trang đầy đủ vẫn phải được lưu trong bộ nhớ chính.

### Câu 164
Which of the following statements is correct in the context of Instruction Pipelining?
A. Instruction Pipelining reduces the efficiency of instruction execution.
B. Instruction Pipelining is only effective for specific types of instructions.
C. Instruction Pipelining enhances efficiency by enabling simultaneous execution of multiple instructions in different stages.
D. Instruction Pipelining improves efficiency, but it can face challenges like hazards, introducing delays.
> **Giải thích:**
> **Đáp án đúng là D.** Đường ống lệnh (Instruction Pipelining) cải thiện hiệu suất bằng cách cho phép nhiều lệnh được xử lý đồng thời ở các giai đoạn khác nhau. Tuy nhiên, nó không phải lúc nào cũng hoàn hảo và có thể đối mặt với các vấn đề như xung đột tài nguyên hoặc phụ thuộc dữ liệu (gọi là hazards), gây ra sự chậm trễ. Đáp án D mô tả đầy đủ cả ưu điểm và thách thức.

### Câu 165
Which of the following statements is correct about addressing modes?
A. They define how the operands of an instruction are specified, including immediate, register, direct, and indirect addressing modes.
B. Addressing modes are irrelevant in computer architecture.
C. Addressing modes are limited to only immediate and direct modes.
D. All instructions in computer architecture use indirect addressing modes.
> **Giải thích:**
> **Đáp án đúng là A.** Chế độ địa chỉ (Addressing modes) là các quy tắc định nghĩa cách CPU diễn giải các toán hạng trong một lệnh. Các chế độ phổ biến bao gồm tức thì (immediate), thanh ghi (register), trực tiếp (direct), gián tiếp (indirect), và nhiều chế độ khác.

### Câu 166
Which statement is incorrect about RISC and CISC architecture?
A. CISC architecture is more convenient for programmers than RISC architecture.
B. CISC architecture has more operands in an instruction compared to RISC architecture.
C. CISC architecture has a more flexible instruction set than RISC architecture.
D. CISC architecture requires more general-purpose registers than RISC architecture.
> **Giải thích:**
> **Đáp án đúng là D.** Phát biểu D là không chính xác. Ngược lại mới đúng, kiến trúc RISC (tập lệnh rút gọn) thường có nhiều thanh ghi đa dụng hơn để giảm thiểu số lần truy cập bộ nhớ. Kiến trúc CISC (tập lệnh phức tạp) lại dựa nhiều vào các lệnh phức tạp có thể thao tác trực tiếp với bộ nhớ, do đó không nhấn mạnh vào số lượng lớn thanh ghi.

### Câu 168
How do data registers and address registers differ in some computer systems?
A. Address registers can be employed in calculating operand addresses, while data registers hold data.
B. Data registers are only used for stack-related operations.
C. Data registers are used for indexed addressing, while address registers are used for data storage.
D. Address registers are reserved for segmented addressing, while data registers are general-purpose.
> **Giải thích:**
> **Đáp án đúng là A.** Trong các kiến trúc có sự phân biệt, thanh ghi địa chỉ (address registers) được tối ưu hóa cho việc chứa và tính toán địa chỉ bộ nhớ (ví dụ: dùng trong các chế độ địa chỉ gián tiếp, chỉ số), trong khi thanh ghi dữ liệu (data registers) được dùng để chứa dữ liệu cho các phép toán.

### Câu 169
How does Boolean algebra contribute to the design of digital circuits?
A. It simplifies the implementation of desired functions.
B. It helps in the analysis of economic data.
C. It facilitates the design of analog circuits.
D. It is primarily used for chemical engineering.
> **Giải thích:**
> **Đáp án đúng là A.** Đại số Boole cung cấp một nền tảng toán học để biểu diễn và thao tác các hàm logic. Nó cho phép các nhà thiết kế mạch số đơn giản hóa (simplify) các biểu thức logic, dẫn đến các mạch ít cổng hơn, rẻ hơn và nhanh hơn để thực hiện cùng một chức năng.

### Câu 170
How does pipelining in a RISC architecture handle branch instructions?
A. By using NOOP instructions inserted by the compiler or assembler.
B. By eliminating branch instructions from the instruction stream.
C. By executing branch instructions in a separate pipeline.
D. By delaying all instructions until the branch is executed.
> **Giải thích:**
> **Đáp án đúng là A.** Một trong những kỹ thuật ban đầu để xử lý xung đột điều khiển (control hazard) do lệnh rẽ nhánh trong đường ống (pipeline) là khe trễ rẽ nhánh (branch delay slot). Trình biên dịch sẽ cố gắng điền một lệnh hữu ích vào vị trí ngay sau lệnh rẽ nhánh. Nếu không tìm thấy, nó sẽ chèn một lệnh không làm gì cả (No-Operation - NOOP) để đảm bảo đường ống không bị nạp sai lệnh.

### Câu 171
How does multithreading improve the performance of a processor?
A. It increases the instruction-level parallelism by issuing multiple instructions from different threads in the same cycle.
B. It increases the thread-level parallelism by executing multiple threads on different cores or processors.
C. It increases the utilization of processor resources by hiding the latency of long-latency events such as cache misses.
D. All of the mentioned.
> **Giải thích:**
> **Đáp án đúng là D.** Đa luồng (Multithreading) cải thiện hiệu năng qua nhiều cách:
> *   SMT (Simultaneous Multithreading) tăng ILP (A).
> *   Hệ thống đa lõi tăng TLP (Thread-Level Parallelism) (B).
> *   Khi một luồng bị dừng (ví dụ: chờ cache miss), CPU có thể chuyển sang thực thi một luồng khác, giúp che giấu độ trễ và tăng hiệu suất sử dụng tài nguyên (C).

### Câu 172
When considering the number of pipeline stages, what trade-offs must be made in computer architecture?
A. Trade-offs between potential speedup and increased cost and delays.
B. Trade-offs between software and hardware.
C. Trade-offs between speed and efficiency.
D. Trade-offs between branching and executing instructions.
> **Giải thích:**
> **Đáp án đúng là A.** Tăng số lượng giai đoạn của đường ống (pipeline) có thể làm tăng tốc độ xung nhịp và thông lượng lý thuyết. Tuy nhiên, nó cũng làm tăng chi phí phần cứng (nhiều chốt hơn), tăng độ trễ do các xung đột (hazards) gây ra, và có thể làm tăng độ trễ tổng thể của một lệnh đơn lẻ. Do đó, có một sự đánh đổi giữa tốc độ tiềm năng và chi phí/độ trễ tăng thêm.

### Câu 173
Why is it essential to use symbolic representation of machine instructions?
A. It makes machine instructions more human-readable and understandable.
B. It reduces the overall complexity of computer systems.
C. It minimizes the need for memory storage.
D. It enables fastest execution of high-level language instructions.
> **Giải thích:**
> **Đáp án đúng là A.** Biểu diễn ký hiệu (Symbolic representation), tức là hợp ngữ (assembly language), thay thế các mã nhị phân khó nhớ của lệnh máy bằng các từ gợi nhớ (mnemonics) dễ đọc và dễ hiểu hơn đối với con người.

### Câu 176
Control and status registers are used by which entities to control the operation of the processor?
A. Privileged, operating system programs
B. Machine or assembly language programmers
C. External I/O devices
D. Main memory modules
> **Giải thích:**
> **Đáp án đúng là A.** Các thanh ghi điều khiển và trạng thái (Control and status registers), ví dụ như thanh ghi chứa con trỏ lệnh hoặc các cờ trạng thái, được sử dụng để quản lý hoạt động của CPU. Việc truy cập và thay đổi chúng thường yêu cầu quyền ưu tiên (privileged mode), do đó chúng chủ yếu được sử dụng bởi hệ điều hành (operating system).

### Câu 177
The central processing unit (CPU) of the IAS computer consists of \_\_\_\_\_\_.
A. Main memory and ALU (arithmetic and logic unit)
B. ALU (Arithmetic and Logic Unit) and CU (Control Unit)
C. CU (Control Unit) and IO Module
D. ALU (Arithmetic and Logic Unit) and IO Module
> **Giải thích:**
> **Đáp án đúng là B.** Trong mô hình máy tính IAS, cũng như các máy tính hiện đại, bộ xử lý trung tâm (CPU) bao gồm hai thành phần chính là Đơn vị Số học và Logic (ALU) và Đơn vị Điều khiển (Control Unit - CU), cùng với các thanh ghi.

### Câu 178
During the development process of the computer, which of the following statements is false?
A. The second generation uses transistors.
B. The first generation uses vacuum tubes.
C. The fourth generation uses large-scale integration (LSI).
D. The third generation uses transistors.
> **Giải thích:**
> **Đáp án đúng là D.** Phát biểu D là sai. Thế hệ thứ ba sử dụng Mạch tích hợp (Integrated Circuits - IC). Thế hệ thứ hai mới là thế hệ sử dụng bóng bán dẫn (transistors).

### Câu 179
In the context of instruction execution, how is a product on an assembly line conceptually similar to an instruction in a pipeline?
A. Both undergo multiple stages of production/processing.
B. Both are executed in a single clock cycle.
C. Both follow a linear sequence of tasks.
D. Both are processed by the control unit.
> **Giải thích:**
> **Đáp án đúng là A.** Phép loại suy (analogy) phổ biến nhất cho đường ống lệnh (instruction pipeline) là một dây chuyền lắp ráp (assembly line). Giống như một sản phẩm đi qua nhiều giai đoạn lắp ráp khác nhau trên dây chuyền, một chỉ thị cũng đi qua nhiều giai đoạn xử lý khác nhau (nạp, giải mã, thực thi...) trong đường ống.

### Câu 180
In the context of the basic instruction cycle, when the fifth instruction is executing, which of the following is the correct statement, assuming a simple pipeline?
A. The sixth instruction is being fetched.
B. The fifth instruction is being fetched.
C. The fourth instruction is being fetched.
D. All program's instructions are fetched.
> **Giải thích:**
> **Đáp án đúng là A.** Trong một đường ống lệnh (pipeline) đơn giản, các giai đoạn được thực hiện chồng chéo. Khi lệnh thứ `n` đang ở giai đoạn thực thi (execute), lệnh thứ `n+1` sẽ đang ở giai đoạn giải mã (decode), và lệnh thứ `n+2` sẽ đang được nạp (fetch). Do đó, khi lệnh thứ 5 đang thực thi, lệnh thứ 6 có thể đang được giải mã và lệnh thứ 7 đang được nạp. Lựa chọn A là hợp lý nhất.

### Câu 181
In the CPU, what is the functionality of the control unit?
A. To decode program instructions.
B. To control the sequence of operations.
C. To store program instructions.
D. To transfer data to primary storage.
> **Giải thích:**
> **Đáp án đúng là B.** Mặc dù giải mã lệnh (A) là một phần công việc của nó, chức năng bao quát và quan trọng nhất của Đơn vị điều khiển (Control Unit) là điều khiển chuỗi các hoạt động (control the sequence of operations) cần thiết để thực thi một chỉ thị.

### Câu 182
In terms of performance, what is the main advantage of a solid state drive over a magnetic disk?
A. A solid state drive has faster access time, lower latency, and higher reliability.
B. A solid state drive has larger capacity, lower power consumption, and lower cost.
C. A solid state drive has better compatibility, longer lifespan, and higher security.
D. A solid state drive has none of the mentioned advantages over a magnetic disk.
> **Giải thích:**
> **Đáp án đúng là A.** Ưu điểm chính về hiệu năng của SSD so với HDD (magnetic disk) là thời gian truy cập nhanh hơn (faster access time) và độ trễ thấp hơn (lower latency) do không có các bộ phận cơ học chuyển động. Nó cũng có độ tin cậy (reliability) cao hơn do khả năng chống sốc tốt hơn.

### Câu 183
In SuperScalar computer architecture, the primary goal of utilizing multiple processors concurrently is to \_\_\_\_\_\_.
A. increase processing speed by increasing CPU frequency
B. improve performance by executing more than one instruction per machine cycle
C. reduce the size of the CPU to conserve energy
D. enhance computational power by increasing the number of CPU cores
> **Giải thích:**
> **Đáp án đúng là B.** Mục tiêu chính của kiến trúc siêu vô hướng (SuperScalar) là cải thiện hiệu năng bằng cách có khả năng thực thi nhiều hơn một chỉ thị trong mỗi chu kỳ máy (executing more than one instruction per machine cycle). Điều này đạt được bằng cách có nhiều đường ống (pipelines) và đơn vị chức năng song song.

### Câu 184
In isolated I/O, \_\_\_\_\_\_.
A. the I/O devices and the memory share the same address space
B. the I/O devices have a separate address space from memory
C. the memory and I/O devices have an associated address space
D. a part of the memory is specifically set aside for the I/O operation
> **Giải thích:**
> **Đáp án đúng là B.** Trong kỹ thuật I/O độc lập (isolated I/O), các thiết bị I/O có một không gian địa chỉ riêng biệt (separate address space) so với bộ nhớ. Cần có các lệnh đặc biệt (ví dụ: `IN`, `OUT`) để giao tiếp với các địa chỉ I/O này.

### Câu 191
Which of the following Boolean expressions is equivalent to `F = (A + B')(C' + A + B)`?
A. `F = A + B'C'`
B. `F = A' + BC`
C. `F = A + BC`
D. `F = A' + B'C'`
> **Giải thích:**
> **Đáp án đúng là A.**
> Ta có thể rút gọn biểu thức bằng các luật trong đại số Boole:
> `F = (A + B')( (A+C') + B )`
> `F = A(A+C') + AB + B'(A+C') + B'B` (Luật phân phối)
> `F = (AA + AC') + AB + (AB' + B'C') + 0` (Luật phân phối, `B'B = 0`)
> `F = (A + AC') + AB + AB' + B'C'` (`AA = A`)
> `F = A + AB + AB' + B'C'` (Luật hấp thụ: `A + AC' = A`)
> `F = A + A(B+B') + B'C'` (Luật phân phối)
> `F = A + A(1) + B'C'` (`B+B' = 1`)
> `F = A + A + B'C'`
> `F = A + B'C'` (`A+A = A`)

### Câu 198
From the Karnaugh map below, derive a simplified Boolean expression.
*(Giả sử K-map có các ô được đánh số 1 như trong đề nhưng không hiển thị rõ, ta sẽ phân tích các nhóm lớn nhất có thể)*
> **Giải thích:**
> *(Do K-map trong OCR không rõ ràng, không thể đưa ra đáp án chính xác. Phần giải thích này giả định một kịch bản phổ biến)*
> Để rút gọn một biểu thức từ bản đồ Karnaugh (Karnaugh map), ta cần tìm các nhóm hình chữ nhật lớn nhất có thể chứa các ô có giá trị 1, với kích thước là lũy thừa của 2 (1, 2, 4, 8...). Mỗi nhóm sẽ tương ứng với một số hạng (term) trong biểu thức rút gọn. Biến nào thay đổi giá trị trong một nhóm sẽ bị loại bỏ khỏi số hạng đó.

### Câu 199/200
Write the Boolean expression for each of the logic circuits.
*(Câu hỏi yêu cầu phân tích một sơ đồ mạch logic)*
> **Giải thích:**
> *(Không thể trả lời vì hình ảnh của mạch logic không được cung cấp trong văn bản OCR)*
> Để xác định biểu thức Boole từ một mạch logic, ta cần phân tích từng cổng một, bắt đầu từ các đầu vào và đi dần đến đầu ra. Viết biểu thức cho đầu ra của mỗi cổng dựa trên các đầu vào của nó, sau đó thay thế các biểu thức trung gian này vào các cổng tiếp theo cho đến khi có được biểu thức cuối cùng tại đầu ra F.


lý thuyết dạng khó cuối :
https://docs.google.com/document/d/1T_WAo9KZt-uuJuhY7wYACBwiiHYUnycV/edit?usp=sharing&ouid=110209365547435823800&rtpof=true&sd=true

video giải dạng khó cuối 1:
http://www.youtube.com/watch?v=pgsZ5uFiXcA

video giải dạng khó cuối 2:
http://www.youtube.com/watch?v=J5PksJfhL_U
# References

