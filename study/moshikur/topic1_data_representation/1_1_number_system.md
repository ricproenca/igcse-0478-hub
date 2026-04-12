# 1.1 Number System

> Source: https://moshikur.com/igcse-o-level-cs/ch-01-data-representation/1-1-data-representation/

# 1.1 Number System

---

[Take the quiz](https://moshikur.com/courses/cambridge-igcse-o-level-computer-science-complete-structured-course/lessons/lesson-1-data-representation/topics/1-1-number-systems/quizzes/1-1-number-systems-quiz/)

# **1.1.**1

# [How Computer Uses Binary](#1.1.1)

# **1.1.**2

### [Number Systems](#1.1.2)

---

### [Binary](#binary)

---

### [Hexadecimal](#hexa)

---

### [Binary Coded Decimal](#bcd)

---

### [Two’s Complement](#twos)

---

# **1.1.**3

### [Binary Arithmetic](#1.1.3)

---

### [Binary Addition](#1.1.3.1)

---

### [Binary Subtraction](#1.1.3.2)

---

### [Overflow](#1.1.3.3)

---

# **1.1.**4

## [Logical Shift](http://1.1.4)

---

---

# 1.1.1 How Computer Uses Binary

---

Computers are built using electronic components that work with only two states:

| 1 | 0 |
| --- | --- |

| ON | OFF |
| --- | --- |

These two states are represented using **binary digits** or **bits**. A bit can only be:

- `1` (representing ON)
- `0` (representing OFF)

This is why **binary** (also called **base 2**) is the language of all computers.

---

### **What is Binary?**

**Binary** is a number system that uses only two digits: **0** and **1**.

Examples of binary numbers:

- `1010`
- `1101`
- `0001 1110`

Each digit in a binary number is called a **bit** (short for **binary digit**).

---

### **Why Do Computers Use Binary?**

Computers use binary because it matches the physical structure of their hardware:

- In electronic circuits, there is either **voltage** (1) or **no voltage** (0)
- It is easier, cheaper, and more reliable to design circuits that only detect these two states

By using just 0s and 1s, computers can:

- Store data
- Perform calculations
- Send and receive instructions

---

### **How Binary Represents Data**

All types of data — numbers, text, images, sounds — are **converted into binary** inside the computer.

Let’s see how different types of data are handled:

---

### **1. Binary for Numbers**

Computers store numbers in binary form.

**Example:**  
The decimal number `13` is stored as:

```
00001101 (in binary, 8-bit)
```

Binary values can be easily converted to and from **denary** (base 10).

---

### **2. Binary for Text (Character Encoding)**

Characters (letters, numbers, symbols) are stored using **binary codes**.

For example, in the **ASCII system**:

- `A` is `01000001`
- `B` is `01000010`
- `a` is `01100001`

Each character is stored as an 8-bit binary code.

---

### **3. Binary for Images**

Images are made up of small squares called **pixels**. Each pixel’s **color** is stored as a **binary value**.

Example:

- In grayscale, `00000000` = black, `11111111` = white
- In color images, 24-bit binary values are used for RGB (Red, Green, Blue)

---

### **4. Binary for Sound**

Sounds are stored by **sampling** the sound wave and converting each sample to a binary value.

Example:

- CD-quality audio uses 16 bits per sample
- A sample might be stored as `0101011101011001`

---

### **5. Binary for Instructions (Machine Code)**

All instructions that a CPU understands are in binary.

For example, an instruction like **“add 2 numbers”** is stored as a series of binary bits called **machine code**.

A simple instruction might look like this:

```
1011 0001
```

The CPU reads these binary instructions and performs the operation.

---

### **Storage Units in Binary**

Data is grouped into standard units:

| Unit | Binary Size |
| --- | --- |
| 1 bit | Single binary digit (0 or 1) |
| 1 nibble | 4 bits |
| 1 byte | 8 bits |
| 1 kilobyte | 1024 bytes |
| 1 megabyte | 1024 KB |

---

### **How Binary is Processed**

1. **Input**: User types a number or clicks a button
2. **Binary conversion**: The input is converted to binary
3. **Processing**: CPU processes the binary data
4. **Storage**: Data is stored as binary on memory (RAM, hard drive, etc.)
5. **Output**: Results are converted from binary to a form the user understands (text, image, sound)

---

### **Real-Life Examples**

| Activity | Binary Representation |
| --- | --- |
| Typing a letter “A” | Converted to 01000001 |
| Saving a photo | Stored as millions of binary pixels |
| Listening to music | Audio is stored as a stream of bits |
| Playing a video | Binary values for frames and audio |
| Running a game | Game code is binary instructions |

---

Binary is the foundation of all computer systems. From simple calculations to complex multimedia processing, everything is handled using 1s and 0s. Understanding binary helps us understand how computers truly work at the lowest level.

---

### **Binary Units of Measurement**

Binary units are based on powers of 2, because computers operate using binary logic. Below is a table showing common binary units and how many **bytes** they represent.

| Prefix | Symbol | Size in Bytes | Size in Bits | Type | Used In |
| --- | --- | --- | --- | --- | --- |
| Bit | b | 1/8 Byte | 1 bit | Fundamental unit | Single binary values (on/off, true/false) |
| Byte | B | 1 Byte | 8 bits | Base unit | Characters, ASCII codes, small data |
| Kibibyte | KiB | 1,024 Bytes | 8,192 bits | Binary (2¹⁰) | RAM size, system memory, file buffers |
| Kilobyte | kB | 1,000 Bytes | 8,000 bits | Decimal (10³) | Document sizes, storage devices |
| Mebibyte | MiB | 1,048,576 Bytes | 8,388,608 bits | Binary (2²⁰) | Memory modules, embedded system storage |
| Megabyte | MB | 1,000,000 Bytes | 8,000,000 bits | Decimal (10⁶) | Software sizes, download sizes |
| Gibibyte | GiB | 1,073,741,824 Bytes | 8,589,934,592 bits | Binary (2³⁰) | RAM capacity, OS memory management |
| Gigabyte | GB | 1,000,000,000 Bytes | 8,000,000,000 bits | Decimal (10⁹) | USB drives, SSDs, smartphone storage |
| Tebibyte | TiB | 1,099,511,627,776 Bytes | 8,796,093,022,208 bits | Binary (2⁴⁰) | Large database servers, backup systems |
| Terabyte | TB | 1,000,000,000,000 Bytes | 8,000,000,000,000 bits | Decimal (10¹²) | Hard drives, cloud storage |
| Pebibyte | PiB | 1,125,899,906,842,624 Bytes | 9,007,199,254,740,992 bits | Binary (2⁵⁰) | Enterprise backup servers, supercomputers |
| Petabyte | PB | 1,000,000,000,000,000 Bytes | 8,000,000,000,000,000 bits | Decimal (10¹⁵) | Data centers, national archives |
| Exbibyte | EiB | 1,152,921,504,606,846,976 Bytes | 9,223,372,036,854,775,808 bits | Binary (2⁶⁰) | Large-scale distributed storage, cloud infrastructure |
| Exabyte | EB | 1,000,000,000,000,000,000 Bytes | 8,000,000,000,000,000,000 bits | Decimal (10¹⁸) | Global internet traffic, massive data aggregation |

### Notes:

- **Binary units** are used by **computer systems** and **operating systems** because memory and processor architecture rely on powers of 2.
- **Decimal units** are used by **storage manufacturers** and in **marketing** because powers of 10 are easier to calculate for end-users.
- The **difference between binary and decimal units becomes more noticeable** at higher magnitudes. For example:
  - 1 TB (Terabyte) ≠ 1 TiB (Tebibyte)
  - 1 TB = 1000³ bytes = 1,000,000,000,000 bytes
  - 1 TiB = 1024⁴ bytes = 1,099,511,627,776 bytes

---

### **Binary vs Decimal Prefixes**

There are two different systems used to measure data sizes: **binary prefixes** and **decimal prefixes**. While both are used in computing, they are not the same.

#### **Binary Prefixes (Used by Operating Systems)**

- 1 **KiB** (Kibibyte) = **1024 Bytes**
- 1 **MiB** (Mebibyte) = **1024 KiB**
- 1 **GiB** (Gibibyte) = **1024 MiB**
- 1 **TiB** (Tebibyte) = **1024 GiB**

#### **Decimal Prefixes (Used by Manufacturers)**

- 1 **kB** (Kilobyte) = **1000 Bytes**
- 1 **MB** (Megabyte) = **1000 kB**
- 1 **GB** (Gigabyte) = **1000 MB**
- 1 **TB** (Terabyte) = **1000 GB**

---

### **Why Is This Important?**

Understanding binary magnitudes is important for the following reasons:

- It helps you understand how much data a file, folder, or storage device contains.
- It allows you to compare system specifications correctly.
- It explains why a “500 GB” hard drive only shows around “465 GiB” when viewed in your operating system. This is because the operating system uses binary prefixes, while the manufacturer uses decimal prefixes.

---

### **Example**

You download a file that is 2048 bytes in size. How big is that in kibibytes?

- Since 1 KiB = 1024 bytes:
- 2048 ÷ 1024 = **2 KiB**

---

# **1.1.2 Number Systems**

---

[![An illustration showing different number systems, including binary (1010), decimal (10), hexadecimal (A3), and binary-coded decimal (0001 0000).](images/topic1_data_representation/1_1_number_system/img_001.png)](https://i0.wp.com/moshikur.com/wp-content/uploads/2025/09/image-94.png?ssl=1)

Computers do not understand denary (decimal) numbers directly. Instead, they use number systems such as **binary**, **hexadecimal**, and sometimes **BCD (Binary Coded Decimal)** to store and process data efficiently. In this section, you will learn:

- What these number systems are
- How to read and write numbers in them
- How they are used in computing

# **Binary (Base 2)**

---

A single bit can store either 0 or 1 because it is the smallest unit of data in computing. Computers use the binary system (base 2) to process and store data. In binary, only two states are possible:

# 0

## 1

**0** Typically represents the “off” state (no electrical signal or low voltage).

**1** Represents the “on” state (presence of an electrical signal or high voltage).

## SO HOW DO WE REPRESENT ANY NUMBER USING BINARY?

| 1 | 1 | 0 | 1 |
| --- | --- | --- | --- |

| 2 3 | 2 2 | 2 1 | 2 0 |
| --- | --- | --- | --- |
| 8 | 4 | 2 | 1 |

The binary number above (**1101)** represents the decimal value **13**, calculated by adding the place values of the bits set to 1 (8 + 4 + 1).

## Activity 1.1.1.1 Find the binary values for these numbers:

Some are done for you

| 0 | 0 | 0 | 0 | 0 |
| --- | --- | --- | --- | --- |
| 1 | | | | |
| 2 | 0 | 0 | 1 | 0 |
| 3 | | | | |
| 4 | | | | |
| 5 | 0 | 1 | 0 | 1 |
| 6 | | | | |
| 7 | 0 | 1 | 1 | 1 |
| PLACE VALUES | 8 | 4 | 2 | 1 |

| 8 | | | | |
| --- | --- | --- | --- | --- |
| 9 | | | | |
| 10 | 1 | 0 | 1 | 0 |
| 11 | 1 | 0 | 1 | 1 |
| 12 | | | | |
| 13 | | | | |
| 14 | 1 | 1 | 1 | 0 |
| 15 | | | | |
| PLACE VALUES | 8 | 4 | 2 | 1 |

## What is the highest number we can represent in 4 bits?

Show

| 1 | 1 | 1 | 1 |
| --- | --- | --- | --- |

Which is 15

---

## How many numbers  can be represented using 4 bits?

Show

0 to 15, a total of **16** numbers.

---

# WHAT IF THE NUMBER IS GREATER THAN 15?

| 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 |
| --- | --- | --- | --- | --- | --- | --- | --- |

| 2 7 | 2 6 | 2 5 | 2 4 | 2 3 | 2 2 | 2 1 | 2 0 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |

We introduce more number of bits. For example the number above represents the value 17

## **Place Values in Binary:**

| Position | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Power of 2 | 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
> Example:  
> Binary `10101010` = 128 + 32 + 8 + 2 = **170 (denary)**

#### **Used in:**

- Computer memory
- IP addresses
- Machine-level operations

## What is the highest number we can represent in 8 bits?

| 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| --- | --- | --- | --- | --- | --- | --- | --- |

| 2 7 | 2 6 | 2 5 | 2 4 | 2 3 | 2 2 | 2 1 | 2 0 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
Show

The binary value 11111111 represents the value 255 in denary.

---

## How many numbers  can be represented using 8 bits?

Show

0 to 255, a total of **256** numbers.

---

## Activity 1.1.1.2

Convert these denary numbers to binary:  
1. 65  
2. 100  
3. 128  
4. 255

Here is the full tutorial for:

---

## **Converting Between Denary and Binary**

---

Denary numbers use digits from 0 to 9. Binary numbers use only two digits: 0 and 1. To convert a denary number to binary, we divide the number by 2 repeatedly and record the remainders.

### Method: Repeated Division by 2 (**Converting Denary to Binary**)

**Steps:**

1. Start with the denary number.
2. Divide it by 2.
3. Write down the remainder (0 or 1).
4. Repeat the division with the quotient.
5. Stop when the quotient becomes 0.
6. Read the remainders from **bottom to top** to get the binary number.

### Example 1: Convert 23 to binary

| Division | Quotient | Remainder |
| --- | --- | --- |
| 23 ÷ 2 | 11 | 1 |
| 11 ÷ 2 | 5 | 1 |
| 5 ÷ 2 | 2 | 1 |
| 2 ÷ 2 | 1 | 0 |
| 1 ÷ 2 | 0 | 1 |

Read the remainders from bottom to top:  
**23 in binary = 10111**

### Example 2: Convert 56 to binary

| Division | Quotient | Remainder |
| --- | --- | --- |
| 56 ÷ 2 | 28 | 0 |
| 28 ÷ 2 | 14 | 0 |
| 14 ÷ 2 | 7 | 0 |
| 7 ÷ 2 | 3 | 1 |
| 3 ÷ 2 | 1 | 1 |
| 1 ÷ 2 | 0 | 1 |

Read the remainders from bottom to top:  
**56 in binary = 111000**

---

### Method: Add Place Values **Converting Binary to denary**

**Steps:**

1. Label each bit in the binary number with its place value (powers of 2), starting from the right.
2. Multiply each binary digit by its place value.
3. Add all the results.

### Example 3: Convert 1101 to denary

| Binary Digit | 1 | 1 | 0 | 1 |
| --- | --- | --- | --- | --- |
| Place Value | 8 | 4 | 2 | 1 |

Multiply the bits where the value is 1:

- 1 × 8 = 8
- 1 × 4 = 4
- 0 × 2 = 0
- 1 × 1 = 1

Total = 8 + 4 + 0 + 1 = **13**  
**1101 in denary = 13**

### Example 4: Convert 100101 to denary

| Binary Digit | 1 | 0 | 0 | 1 | 0 | 1 |
| --- | --- | --- | --- | --- | --- | --- |
| Place Value | 32 | 16 | 8 | 4 | 2 | 1 |

Multiply the bits where the value is 1:

- 1 × 32 = 32
- 0 × 16 = 0
- 0 × 8 = 0
- 1 × 4 = 4
- 0 × 2 = 0
- 1 × 1 = 1

Total = 32 + 0 + 0 + 4 + 0 + 1 = **37**  
**100101 in denary = 37**

---

### **Denary (Decimal / Base 10)**

Denary is the standard number system used in everyday life. It uses **ten digits: 0 to 9**.

#### **Place Values in Decimal:**

| Position | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- |
| Power of 10 | 1000 | 100 | 10 | 1 |
> Example:  
> `194` = 1×100 + 9×10 + 4 = **194**

---

# **Hexadecimal (Base 16)**

---

[![An infographic illustrating the hexadecimal number system, featuring the numbers 1, 2, 3, 4, A, B, C, D, along with their binary equivalents: 0101, 0010, 1011, and 0010. The design includes a prominent '16' and the website www.moshikur.com.](images/topic1_data_representation/1_1_number_system/img_002.png)](https://i0.wp.com/moshikur.com/wp-content/uploads/2025/09/image-92.png?ssl=1)

**What is the Hexadecimal Number System?**

The **hexadecimal** number system is a **base-16** system. That means it uses **16 different symbols** to represent values.

Instead of just digits 0–9 (like in denary), hexadecimal also uses letters **A to F** to represent the values from 10 to 15.

### **Why Are Letters Used in Hexadecimal?**

The **hexadecimal number system** is a **base-16 system**, which means it needs **16 unique symbols** to represent values.

In the decimal (denary) system, we use 10 digits:  
**0, 1, 2, 3, 4, 5, 6, 7, 8, 9**

However, hexadecimal needs **six more digits** after 9 to reach 16. But since there are **no single-digit numerals beyond 9**, we use **letters** to represent the remaining values:

So, in hexadecimal:

- **A = 10**
- **B = 11**
- **C = 12**
- **D = 13**
- **E = 14**
- **F = 15**

This way, the complete set of hexadecimal symbols becomes:

**0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F**

---

### **Why not just use 10, 11, 12, etc.?**

If we used numbers like “10”, “11”, and “12” to represent values 10, 11, and 12, it would cause confusion. For example:

- In **decimal**, “10” means ten.
- In **hexadecimal**, “10” actually means **sixteen**.

To avoid this confusion and keep hexadecimal compact and readable, **single letters** are used for values 10 to 15.

---

| Denary | Binary | Hexadecimal |
| --- | --- | --- |
| 0 | 0000 | 0 |
| 1 | 0001 | 1 |
| 2 | 0010 | 2 |
| 3 | 0011 | 3 |
| 4 | 0100 | 4 |
| 5 | 0101 | 5 |
| 6 | 0110 | 6 |
| 7 | 0111 | 7 |
| 8 | 1000 | 8 |
| 9 | 1001 | 9 |
| 10 | 1010 | A |
| 11 | 1011 | B |
| 12 | 1100 | C |
| 13 | 1101 | D |
| 14 | 1110 | E |
| 15 | 1111 | F |
> Example:  
> Hex `2F` = (2 × 16) + 15 = **47 (denary)**  
> Binary equivalent of `2F` = `0010 1111`

---

## **Where Is Hexadecimal Used in Real Life?**

Here are some of the most important uses of hexadecimal in computing and electronics:

---

### **1. Memory Addresses**

- Computers use **memory addresses** to locate data in RAM.
- These addresses are usually **very large binary numbers**.
- Hexadecimal makes them **shorter and easier to work with**.

#### **Example:**

- Binary address: `1101001110101111`
- Hexadecimal: `D3AF`

Instead of writing long binary addresses, programmers and debuggers use hex to make memory maps and logs more readable.

---

### **2. Machine Code and Assembly Language**

- **Low-level programming languages** like Assembly use hexadecimal to represent:
  - **Instructions**
  - **Registers**
  - **Data values**
- It allows direct interaction with hardware using **short, readable representations** of binary instructions.

#### **Example:**

- Machine instruction in binary: `1010110000000001`
- In hexadecimal: `AC01`

---

### **3. Colour Codes in Web Design (HTML/CSS)**

[![Color picker interface displaying a gradient spectrum, a red color selection, and RGB values.](images/topic1_data_representation/1_1_number_system/img_003.png)](https://i0.wp.com/moshikur.com/wp-content/uploads/2025/09/image-85.png?ssl=1)

In HTML and CSS, colours are defined using hexadecimal values.

- Each colour is made from three values:
  - **Red**
  - **Green**
  - **Blue**

Each of these values is given in hexadecimal, ranging from **00** (0) to **FF** (255 in decimal).

#### **Example:**

| Hex Code | Colour |
| --- | --- |
| #FF0000 | Red |
| #00FF00 | Green |
| #0000FF | Blue |
| #FFFFFF | White |
| #000000 | Black |
| #FF5733 | Orange |

---

### **4. Debugging and Error Messages**

- Operating systems and software often display **error codes** in hexadecimal.
- These codes help developers find the **exact location** or **cause** of the error.

#### **Example:**

- Blue Screen Error Code: `STOP: 0x0000007E`

The `0x` prefix indicates that the number following is in hexadecimal.

---

### **5. MAC Addresses in Networking**

- A **MAC address** (used to identify a device on a network) is written in hexadecimal.

#### **Example:**

- `00:1A:2B:3C:4D:5E`

Each pair represents one **byte** (8 bits), written in hexadecimal.

---

## **Summary Table: Uses of Hexadecimal**

| Use | Description | Example |
| --- | --- | --- |
| Memory Addressing | Shorter way to represent binary memory locations | 0x7F3A |
| Assembly Language | Represent binary machine code in readable format | MOV AX, 4C00h |
| Colour Codes | Define RGB values in web design using 6-digit hex | #FF5733 |
| Error Codes | System errors often reported as hexadecimal codes | STOP: 0x0000007E |
| MAC Addresses | Network devices use hex-formatted hardware addresses | A4:5E:60:BC:9F:0D |

---

## **Why Hexadecimal Is Better Than Binary (for Humans)**

| Feature | Binary | Hexadecimal |
| --- | --- | --- |
| Length | Long (e.g., 10111010) | Short (e.g., BA) |
| Easy to Read | Hard to scan visually | Easy to recognise |
| Used by Computers | Yes | Indirectly (via binary) |
| Used by Programmers | Rarely | Often |

Here is a detailed and student-friendly tutorial for:

---

## **Converting Hexadecimal to Denary and Binary**

---

### **Hexadecimal (Base-16)**

Hexadecimal is a number system with **16 symbols**:

**0 1 2 3 4 5 6 7 8 9 A B C D E F**

- A = 10
- B = 11
- C = 12
- D = 13
- E = 14
- F = 15

Each hexadecimal digit can be directly converted to **4 binary digits** (bits), making it useful in computing.

---

## **Section A: Converting Hexadecimal to Denary (Decimal)**

To convert a hexadecimal number to denary:

1. Multiply each digit by **16 raised to a power**, based on its position.
2. Start from the rightmost digit (position 0).
3. Add all the results.

---

### **Step-by-step Example 1: Convert 2F to denary**

**Step 1: Identify the values**

- 2 is in the 16¹ position
- F is in the 16⁰ position → F = 15

**Step 2: Multiply**

- 2 × 16 = 32
- 15 × 1 = 15

**Step 3: Add the results**

32 + 15 = **47**

✔ **Answer:** 2F₁₆ = 47₁₀

---

### **Step-by-step Example 2: Convert A3 to denary**

- A = 10 (16¹ place)
- 3 = 3 (16⁰ place)

**Calculation:**

10 × 16 = 160  
3 × 1 = 3  
160 + 3 = **163**

✔ **Answer:** A3₁₆ = 163₁₀

---

## **Section B: Converting Hexadecimal to Binary**

To convert a hexadecimal number to binary:

1. Convert **each hex digit** to its **4-bit binary equivalent**.
2. Join all the binary groups together.

---

### **Hex to Binary Reference Table**

| Hex | Binary |
| --- | --- |
| 0 | 0000 |
| 1 | 0001 |
| 2 | 0010 |
| 3 | 0011 |
| 4 | 0100 |
| 5 | 0101 |
| 6 | 0110 |
| 7 | 0111 |
| 8 | 1000 |
| 9 | 1001 |
| A | 1010 |
| B | 1011 |
| C | 1100 |
| D | 1101 |
| E | 1110 |
| F | 1111 |

---

### **Step-by-step Example 3: Convert 2F to binary**

Split the digits:

- 2 = 0010
- F = 1111

Join them:  
**2F₁₆ = 00101111₂**

---

### **Step-by-step Example 4: Convert 9A to binary**

- 9 = 1001
- A = 1010

✔ **Answer:** 9A₁₆ = 10011010₂

---

## **Summary**

| Conversion | Method |
| --- | --- |
| Hex → Denary | Multiply each digit by 16ⁿ (based on position), then add all values |
| Hex → Binary | Convert each hex digit to 4-bit binary using the table above |

---

### **Activity 1.1.1.3**

Try converting the following:

1. Convert **3C** to denary
2. Convert **7F** to binary
3. Convert **B2** to denary and binary

---

# **Denary and Binary to Hexadecimal Conversion**

---

### **Denary (Decimal) to Hexadecimal**

We use **repeated division by 16**, and convert the **quotient and remainder** to hex digits.

---

### **Example 1: Convert 75 to hexadecimal**

75 ÷ 16 = 4 remainder **11** → 11 = **B**

✔ **75₁₀ = 4B₁₆**

---

### **Example 2: Convert 255 to hexadecimal**

255 ÷ 16 = 15 remainder **15**  
15 = F, so answer is:

✔ **255₁₀ = FF₁₆**

---

### **Example 3: Convert 330 to hexadecimal**

**Step 1: Divide by 16**

330 ÷ 16 = 20 remainder **10** → 10 = **A**  
20 ÷ 16 = 1 remainder **4**  
1 ÷ 16 = 0 remainder **1**

**Step 2: Read remainders from bottom to top:**  
1 → 4 → A

✔ **Answer:** **330₁₀ = 14A₁₆**

---

### **Example 4: Convert 480 to hexadecimal**

**Step 1: Divide by 16**

480 ÷ 16 = 30 remainder **0**  
30 ÷ 16 = 1 remainder **14** → 14 = **E**  
1 ÷ 16 = 0 remainder **1**

**Step 2: Read remainders from bottom to top:**  
1 → E → 0

✔ **Answer:** **480₁₀ = 1E0₁₆**

---

### **Section B: Binary to Hexadecimal**

We group binary digits into **4-bit chunks** from **right to left**, then convert each group to its hex equivalent.

---

### **Example 5: Convert 101001010₂ to hexadecimal**

**Step 1: Pad to 12 bits for grouping**  
→ 0001 0100 1010

**Step 2: Convert each group**

- 0001 = 1
- 0100 = 4
- 1010 = A

✔ **Answer:** 101001010₂ = **14A₁₆**

---

### **Example 6: Convert 111100000₂ to hexadecimal**

**Step 1: Pad to 12 bits**  
→ 0001 1110 0000

**Step 2: Convert**

- 0001 = 1
- 1110 = E
- 0000 = 0

✔ **Answer:** 111100000₂ = **1E0₁₆**

## Activity 1.1.1.4

---

## **Task 1: Convert Denary to Hexadecimal**

### Q1. Convert 212 to hexadecimal

Answer

**Answer:** D4₁₆

### Q2. Convert 1000 to hexadecimal

Answer

**Answer:** 3E8₁₆

---

## **Task 2: Convert Binary to Hexadecimal**

### Q3. Convert 11011110 to hexadecimal

Answer

**Answer:** DE₁₆

### Q4. Convert 1001110110 to hexadecimal

Answer

**Answer:** 13B6₁₆

---

## **Task 3: Convert Hexadecimal to Denary**

### Q5. Convert 7F to denary

Answer

**Answer:** 127₁₀

### Q6. Convert C3 to denary

Answer

**Answer:** 195₁₀

---

## **Task 4: Convert Hexadecimal to Binary**

### Q7. Convert 1A2 to binary

Answer

**Answer:** 000110100010₂

### Q8. Convert 3E8 to binary

Answer

**Answer:** 001111101000₂

---

# **Binary Coded Decimal (BCD)**

---

[![An illustration showing the binary-coded decimal representation of the number 75, displayed in a digital format with the binary digits 0111 and 0101 positioned below each digit.](images/topic1_data_representation/1_1_number_system/img_004.png)](https://i0.wp.com/moshikur.com/wp-content/uploads/2025/09/image-91.png?ssl=1)

### **What is BCD?**

**BCD** stands for **Binary Coded Decimal**.

It is a method of representing **decimal digits (0–9)** using **4-bit binary codes**.

> Example:  
> Denary `59` =  
> 5 → `0101`  
> 9 → `1001`  
> BCD = `0101 1001`

- Each decimal digit is stored **separately** as a **4-bit binary number**.
- This is different from converting the **entire number** into binary.

---

### **How BCD Works**

| Decimal Digit | BCD (4-bit Binary) |
| --- | --- |
| 0 | 0000 |
| 1 | 0001 |
| 2 | 0010 |
| 3 | 0011 |
| 4 | 0100 |
| 5 | 0101 |
| 6 | 0110 |
| 7 | 0111 |
| 8 | 1000 |
| 9 | 1001 |
> Any decimal digit **above 9 is not valid** in standard BCD.

---

### **Example: Convert 47 to BCD**

- Decimal number: **47**
- Separate the digits: **4** and **7**

Now convert each digit to 4-bit binary:

- 4 → 0100
- 7 → 0111

**BCD Representation of 47:**  
**0100 0111**

---

### **Important:**

BCD **is not** the same as binary conversion.

Let’s compare:

| Representation | Decimal | BCD | Binary (whole number) |
| --- | --- | --- | --- |
| | 47 | 0100 0111 | 101111 |

So:

- **BCD of 47 = 0100 0111**
- **Binary of 47 = 101111**

> ✅ **In BCD, each digit is converted separately.**  
> ❌ **In binary, the whole number is converted directly.**

---

## **Uses of BCD**

BCD is used in systems where it is **important to display decimal digits clearly**, especially in hardware that **interacts with humans**.

---

### **1. Digital Displays (Clocks, Calculators, Meters)**

- Devices like **digital clocks** or **calculators** use BCD to represent each digit so it can be sent directly to a **7-segment display**.

Example:

- Time: 12:45
- BCD:
  - 1 → 0001
  - 2 → 0010
  - 4 → 0100
  - 5 → 0101
- BCD sent to display controller → shows “12:45”

---

### **2. Financial and Commercial Systems**

- **Currency systems** (like ATMs or billing machines) use BCD to **avoid rounding errors** that can happen with binary floating-point numbers.
- It ensures **accurate representation** of decimal money values.

---

### **3. Input Devices**

- Some **keypads** send digits in BCD form directly to the processor.

---

### **4. Early Computers and Embedded Systems**

- Some older or simpler microcontrollers used BCD for storing and processing numerical input/output.

---

## **Advantages of BCD**

| Advantage | Explanation |
| --- | --- |
| Easy to convert for display | Since each digit is stored separately, it’s simple to show on a screen |
| Avoids binary rounding errors | Especially important for financial data |
| Compatible with decimal input/output | Used in calculators, digital clocks, and commercial systems |

---

## **Disadvantages of BCD**

| Disadvantage | Explanation |
| --- | --- |
| Wastes space | Uses 4 bits for each digit, even if many values are unused (e.g. 1010 to 1111) |
| Slower for arithmetic | More complex operations than binary |
| Not efficient for large computations | Binary is faster and more compact for CPU-level math |

---

## Activity 1.1.1.5

**Q1. What is the BCD of 93?**

Answer

→ 9 = 1001, 3 = 0011  
✔ **Answer:** 1001 0011

**Q2. What is the BCD of 120?**

Answer

→ 1 = 0001, 2 = 0010, 0 = 0000  
✔ **Answer:** 0001 0010 0000

---

# **Two’s Complement**

[![Illustration of Two's Complement binary representation showing '1010 1010' with a minus sign.](images/topic1_data_representation/1_1_number_system/img_005.png)](https://i0.wp.com/moshikur.com/wp-content/uploads/2025/09/image-90.png?ssl=1)

### **What is Two’s Complement?**

Two’s complement is a method used in computer systems to represent **both positive and negative integers** in binary.

In regular binary, only **positive numbers** can be represented directly. To handle **negative values**, we need a system that can:

- Represent negatives unambiguously
- Support standard binary addition and subtraction
- Avoid duplicate representations of zero

**Two’s complement** solves this problem by using the **most significant bit (MSB)** to indicate the **sign** of the number:

| 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| --- | --- | --- | --- | --- | --- | --- | --- |

| -128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
| --- | --- | --- | --- | --- | --- | --- | --- |

The number above represents the value -128 + 1 = -127

- If MSB = 0 → the number is positive or zero
- If MSB = 1 → the number is negative

## Activity 1.1.1.6: Identify these numbers:

| 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| --- | --- | --- | --- | --- | --- | --- | --- |

| -128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
| --- | --- | --- | --- | --- | --- | --- | --- |

Note: This is also the **smallest** (most negative) number that can be represented using **8-bit two’s complement.**

| 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- |

| -128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
| --- | --- | --- | --- | --- | --- | --- | --- |

Note: This is also the **largest** (most positive) number that can be represented using **8-bit two’s complement.**

---

### **Why Two’s Complement is Used**

Two’s complement is the most widely used method for representing signed integers in binary because:

- It simplifies arithmetic operations like addition and subtraction.
- It avoids the problem of having both +0 and –0 (unlike One’s complement).
- It allows a **seamless range of positive and negative values**.

For example, in an 8-bit system:

- **+5** = `00000101`
- **–5** = `11111011` (Two’s complement form)

Using these binary patterns, a CPU can perform:

`00000101 + 11111011 = 00000000`  
This correctly results in zero, without any special logic for signed numbers.

---

## **2. How Two’s Complement Works**

### **MSB as the Sign Bit**

In Two’s complement:

- The **leftmost bit (MSB)** is used as the **sign bit**.
- **0** means the number is **positive**
- **1** means the number is **negative**

This sign bit affects the value based on **weighting**. For an **N-bit** number:

- All bits except the MSB follow normal binary weights: 2⁰, 2¹, 2², …, 2ⁿ⁻²
- The MSB carries a **negative weight** of –2ⁿ⁻¹

### **Range of Values**

The Two’s complement system provides the following range for **N-bit numbers**:

- **Minimum value** = –2ⁿ⁻¹
- **Maximum value** = 2ⁿ⁻¹ – 1

| Bits | Range |
| --- | --- |
| 4-bit | –8 to +7 |
| 8-bit | –128 to +127 |
| 16-bit | –32,768 to +32,767 |

This range always includes **one more negative number** than positive.

### **Understanding the Binary Pattern of Negative Values**

In Two’s complement, **negative values are formed by inverting** the bits of the **positive value** and then **adding 1**.

For example, to find the Two’s complement of +5 in 8-bit form:

1. Start with +5 → `00000101`
2. Invert the bits → `11111010`
3. Add 1 → `11111011`

So, **–5** is represented as `11111011`.

The highest bit being 1 indicates it’s a **negative number**, and this pattern gives it the correct signed value when interpreted using Two’s complement rules.

---

### **Binary Patterns Overview (8-bit)**

| Decimal | Binary (Two’s Complement) |
| --- | --- |
| +5 | 00000101 |
| –5 | 11111011 |
| +1 | 00000001 |
| –1 | 11111111 |
| 0 | 00000000 |
| –128 | 10000000 |
| +127 | 01111111 |

---

# **1.1.3 – Binary Arithmetic**

[![Illustration explaining binary arithmetic with examples of binary addition and subtraction, highlighting carry and overflow concepts.](images/topic1_data_representation/1_1_number_system/img_006.png)](https://i0.wp.com/moshikur.com/wp-content/uploads/2025/09/image-89.png?ssl=1)

This section explains how binary arithmetic works, especially when using **two’s complement representation** for signed numbers. You will learn how to perform **addition**, **subtraction**, and understand **overflow errors**.

---

# **1.1.3.1 – Binary Addition**

Binary addition is a fundamental operation in computer systems. It works similarly to decimal addition but uses only **two digits: 0 and 1**.

---

## **Binary Addition Rules**

In binary, digits are added using these basic rules:

```
0 + 0 = 0

0 + 1 = 1

1 + 0 = 1

1 + 1 = 0 (carry 1)
```

If there’s a carry from a previous column, it must also be added.

---

## **Binary Addition Table**

| Bit A | Bit B | Sum | Carry |
| --- | --- | --- | --- |
| 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 1 |

This table helps explain how binary values are added column by column, starting from the rightmost bit (least significant bit).

[![A visual representation of binary addition, showing examples with binary digits and the process of addition, including carrying over.](images/topic1_data_representation/1_1_number_system/img_007.png)](https://i0.wp.com/moshikur.com/wp-content/uploads/2025/09/image-86.png?ssl=1)

---

## **Example 1: Adding Two Positive Binary Numbers**

### Add 9 and 5

Step 1: Convert both numbers to 8-bit binary  
9 → `00001001`  
5 → `00000101`

Step 2: Add the binary numbers

```
  00001001
+ 00000101
-----------
  00001110
```

**Result:** `00001110` = 14 in denary

---

## **Example 2: Adding a Positive and a Negative Integer**

### Add 7 + (–3)

7 → `00000111`  
–3 → `11111101` (8-bit Two’s Complement)

Now add:

```
  00000111
+ 11111101
-----------
  000000100
```

Ignore the overflow (9th bit):  
**Result:** `00000010` = 2

---

## **Example 3: Adding Two Negative Integers**

### Add (–5) + (–6)

–5 → `11111011`  
–6 → `11111010`

Now add:

```
  11111011
+ 11111010
-----------
  11110101 (Carry ignored)
```

**Result:** `11110101` = –11

[![Diagram displaying several binary addition tasks with highlighted instructions.](images/topic1_data_representation/1_1_number_system/img_008.png)](https://i0.wp.com/moshikur.com/wp-content/uploads/2025/09/image-87.png?ssl=1)

---

## **Key Points to Remember**

- Binary addition uses the same carry principle as decimal, but with just 0 and 1.
- Overflow may occur if the result exceeds the fixed number of bits (you’ll learn more about this in 1.1.3.3).
- Two’s complement makes it possible to add negative numbers using the same addition logic.

---

# **1.1.3.2 – Binary Subtraction**

Subtraction in binary is not done the same way as in decimal.  
Instead of building separate logic for subtraction, computers perform subtraction by using **Two’s Complement** and binary **addition**.  
  
This allows one circuit (an adder) to handle **both addition and subtraction** efficiently.

---

## **How Binary Subtraction Works**

### **Key Concept:**

> **A – B = A + (–B)**

So, subtraction is done by:

1. Taking the **two’s complement** of the number to subtract (B)
2. Adding it to the original number (A)
3. Ignoring overflow if it happens

---

## **Example 1: 5 – 3**

### Step 1: Convert to 8-bit binary

5 = `00000101`  
3 = `00000011`

### Step 2: Two’s complement of 3

- Invert: `11111100`
- Add 1: `11111101` → (–3)

### Step 3: Add 5 + (–3)

```
  00000101
+ 11111101
-----------
  00000010
```

**Answer:** `00000010` = 2

---

## **Example 2: 3 – 5**

### Step 1:

3 = `00000011`  
5 = `00000101`

### Step 2: Two’s complement of 5

- Invert: `11111010`
- Add 1: `11111011` → (–5)

### Step 3: Add 3 + (–5)

```
  00000011
+ 11111011
-----------
  11111110
```

**Answer:** `11111110` = –2

---

## **Example 3: –4 – 5**

Step 1:  
–4 = `11111100`  
5 = `00000101`

Step 2: Two’s complement of 5  
→ `11111011` (–5)

Step 3: Add –4 + (–5)

```
  11111100
+ 11111011
-----------
  11110111
```

**Answer:** `11110111` = –9

---

## **Important Notes**

- **Negative values** must always be converted to **Two’s Complement** format.
- **Subtraction becomes addition** of the negative value.
- You can detect if the result is negative by checking the **most significant bit (MSB)**:
  - If MSB = 1 → result is negative (in Two’s Complement)

---

# **1.1.3.3 – Overflow in Binary Arithmetic**

---

[![A table illustrating binary magnitudes and prefixes, comparing binary and decimal prefix sizes.](images/topic1_data_representation/1_1_number_system/img_009.png)](https://i0.wp.com/moshikur.com/wp-content/uploads/2025/09/image-88.png?ssl=1)

## **What is Overflow?**

**Overflow** happens when the result of a binary operation is **too large** or **too small** to be stored within the fixed number of bits available.

Computers have limited space to store numbers. If the result of an operation goes beyond this limit, an **incorrect value** is stored – this is called an **overflow error**.

---

## **Example: 8-bit Two’s Complement Range**

For an 8-bit binary number using two’s complement, the valid range is:

- **Minimum:** –128 → `10000000`
- **Maximum:** +127 → `01111111`

Any value outside this range **cannot be correctly represented** using 8 bits.

---

## **When Does Overflow Happen?**

Overflow can occur during binary **addition** or **subtraction**.

Here are the most common cases:

| Case | Result | Overflow? |
| --- | --- | --- |
| Positive + Positive → Negative | Yes | ✅ |
| Negative + Negative → Positive | Yes | ✅ |
| Positive + Negative → Within Range | No | ❌ |
| Negative + Positive → Within Range | No | ❌ |

---

## **Example 1: Positive Overflow**

### Calculate: 100 + 60

Convert to 8-bit binary:

- 100 = `01100100`
- 60 = `00111100`

**Add:**

```
  01100100
+ 00111100
-----------
  10100000
```

`10100000` = –96 (incorrect, should be 160)

This result is **wrong** because **160 > 127**, which is outside the 8-bit range.  
**→ Overflow has occurred**

---

## **Example 2: Negative Overflow**

### Calculate: (–100) + (–50)

Convert to Two’s complement (8-bit):

- –100 = `10011100`
- –50 = `11001110`

**Add:**

```
  10011100
+ 11001110
-----------
  01101010
```

`01101010` = +106 (incorrect, expected –150)

This is a **negative overflow** because the true result (–150) is less than –128.  
**→ Overflow has occurred**

---

## **How to Detect Overflow**

### Method: **Check the sign bit (MSB)**

- If you add two **positive numbers** and get a result with **MSB = 1** → overflow.
- If you add two **negative numbers** and get a result with **MSB = 0** → overflow.

Another method (used in hardware):  
Check if the **carry into the MSB** is **not equal** to the **carry out of the MSB**.  
If they are **different**, overflow occurred.

---

# 1.1.4 **Logical Shift**

### **What is a Logical Shift?**

A **logical shift** is a bitwise operation that moves all the bits in a binary number either to the left or to the right. It’s used in low-level programming, digital electronics, and computer science to quickly multiply or divide binary numbers.

There are two main types:

- **Logical Left Shift**
- **Logical Right Shift**

Logical shifts are **not the same as arithmetic shifts**. Logical shifts do **not** preserve the sign bit in two’s complement binary numbers.

---

### **1. Logical Left Shift**

#### **How it works:**

Each bit in the binary number is moved one or more places to the **left**. The **empty bit positions on the right** are filled with `0`.

#### **Effect:**

A logical left shift by 1 position is equivalent to **multiplying by 2**.

#### **Example:**

Binary number: `00101101`  
(Decimal: 45)

**Left shift by 1:**

```
Original:   00101101

Shift left: 01011010
```

**New value (in decimal):**  
`01011010` = 90  
So, 45 × 2 = 90 ✅

**General rule:**

```
Shift Left by n positions → Multiply by 2ⁿ
```

---

### **2. Logical Right Shift**

#### **How it works:**

Each bit in the binary number is moved one or more places to the **right**. The **empty bit positions on the left** are filled with `0`.

#### **Effect:**

A logical right shift by 1 position is equivalent to **dividing by 2** (rounding down if there’s a remainder).

#### **Example:**

Binary number: `00101101`  
(Decimal: 45)

**Right shift by 1:**

```
Original:    00101101

Shift right: 00010110
```

**New value (in decimal):**  
`00010110` = 22  
So, 45 ÷ 2 = 22.5 → Rounded down to 22 ✅

**General rule:**

```
Shift Right by n positions → Divide by 2ⁿ (ignores fractions)
```

---

### **Important Notes**

- **No carry-over:** Shift operations do **not** wrap bits around or remember the bits that are shifted out.
- **Leading/trailing zeros:** Depending on direction, zeros are added to either the beginning or end.
- **Sign bit:** Logical shifts **do not preserve sign** in negative binary numbers.

---

### **Table: Logical Shift Comparison**

| Operation | Binary (8-bit) | Decimal Value | Effect |
| --- | --- | --- | --- |
| Original | 00101101 | 45 | – |
| Left shift by 1 | 01011010 | 90 | Multiply by 2 |
| Left shift by 2 | 10110100 | 180 | Multiply by 4 |
| Right shift by 1 | 00010110 | 22 | Divide by 2 |
| Right shift by 2 | 00001011 | 11 | Divide by 4 |

---

### **When are Logical Shifts Used?**

- **Optimizing performance:** Faster than multiplication/division
- **Bitmasking:** Used in low-level programming to manipulate bits
- **Graphics:** Color manipulation and pixel operations
- **Encryption:** Some cryptographic algorithms use shifts
- **Embedded Systems:** Compact operations for small devices

---

# **Interactive Practice**

**Try it yourself:**

Input a binary number and shift direction:

Left
Right

Shift

---

### **Practice Questions (For Exam-Style Practice)**

1. Perform a **logical left shift** on the binary number `00011001`.  
   a) By 1 place  
   b) By 2 places  
   What are the new binary and decimal values?
2. Perform a **logical right shift** on the binary number `10101100`.  
   a) By 1 place  
   b) By 3 places  
   What are the new binary and decimal values?
3. Why do logical shifts fill with zeros instead of copying the sign bit?

---

Logical shifts are a powerful tool in computing for working with binary data. They allow us to multiply or divide numbers quickly without using arithmetic operations. Learning how to use and understand logical shifts helps you work more efficiently with low-level data in programming, memory manipulation, and computer architecture.

---

### Leave a Reply[Cancel reply](/igcse-o-level-cs/ch-01-data-representation/1-1-data-representation/#respond)