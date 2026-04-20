# CAIE Computer Science IGCSE — Chapter 1: Data Representation
### Advanced Notes

---

## 1.1 Number Systems

### What are number systems?

A number system determines how values are represented using digits; a number base defines the number of unique digits used in that system.

The most common number systems are:

- **Denary (Base 10)** - used by humans for counting
- **Binary (Base 2)** - used by computers to represent all data and instructions
- **Hexadecimal (Base 16)** - used by programmers for compact representation

---

### Denary (base 10)

Denary is the number system that humans use to count, perhaps because we have ten fingers. Denary uses the ten digits 0 through to 9 to represent numbers.

Each digit in a decimal number has a place value based on powers of 10. The value of a digit depends on its position within the number. This is illustrated by the table below, which shows how the decimal number 237 is constructed using place values.

| 10² | 10¹ | 10⁰ |
|-----|-----|-----|
| 100 | 10  | 1   |
| 2   | 3   | 7   |

`237 = (2×100) + (3×10) + (7×1)`

---

### Binary (base 2)

Binary is used by computer systems to store all data and instructions. This is because it has only two states, 0 or 1, which map directly to the two states of electronic components like transistors: on (1) or off (0) and other logic gates used to process and store data. This simplicity makes it easier to design, build, and maintain computer hardware. Therefore, data needs to be converted into a binary format to be processed by a computer.

Each digit in a binary number has a place value based on powers of 2. This is illustrated by the table below, which shows how the binary number 1011 is constructed using place values — making it equal to 11 in denary.

| 2³ | 2² | 2¹ | 2⁰ |
|----|----|----|-----|
| 8  | 4  | 2  | 1   |
| 1  | 0  | 1  | 1   |

`1011 = (1×8) + (0×4) + (1×2) + (1×1) = 11 (decimal)`

---

### Hexadecimal (base 16)

In contrast to decimal, hexadecimal uses the digits 0 through to 9 followed by the uppercase characters A to F to represent the denary numbers 0 to 15.

| Decimal     | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
|-------------|---|---|---|---|---|---|---|---|---|---|----|----|----|----|----|-----|
| Hexadecimal | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | A  | B  | C  | D  | E  | F   |

Of all the number bases covered by this course, hexadecimal is the most compact. This means that it can represent the same number as binary or decimal while using far fewer digits. Each character in hexadecimal represents four bits in binary.

Each digit in a hexadecimal number has a place value based on powers of 16. This is illustrated by the table below, which shows how the hexadecimal value 2F is constructed using place values — making it equal to 47 in decimal.

| 16¹ | 16⁰ |
|-----|------|
| 16  | 1    |
| 2   | 15 (because F represents 15) |

`2F = (2×16) + (15×1) = 47 (decimal)`

---

## Converting Denary ↔ Binary

### To convert binary → denary:

You can convert from binary to decimal by using place value headers. Starting with one and increasing in powers of two, placing larger values to the left of smaller values. For example, the binary number `10110010` could have place value headers added as follows:

| 128 (2⁷) | 64 (2⁶) | 32 (2⁵) | 16 (2⁴) | 8 (2³) | 4 (2²) | 2 (2¹) | 1 (2⁰) |
|----------|---------|---------|---------|--------|--------|--------|--------|
| 1        | 0       | 1       | 1       | 0      | 0      | 1      | 0      |

The binary number could then be converted to denary by adding together all of the place values with a binary one below them.

`128 + 32 + 16 + 2 = 178`

So the binary number `10110010` is equivalent to the decimal number **178**.

---

### To convert decimal → binary:

When converting from denary to binary, you use the same place value headers. Starting from the left hand side, you place a one if the value is less than or equal to your number, and a zero otherwise.

Once you've placed a one, you must subtract the value of that position from your number and continue as before, until your decimal number becomes 0.

**Example: converting 53 to binary**

Write out place value headers in powers of two up to a value larger than 53 (go up to 64):

| 64 | 32 | 16 | 8 | 4 | 2 | 1 |
|----|----|----|---|---|---|---|

- 64 > 53 → place **0** under 64
- 32 ≤ 53 → place **1** under 32; 53 − 32 = 21 remaining
- 16 ≤ 21 → place **1** under 16; 21 − 16 = 5 remaining
- 8 > 5 → place **0** under 8
- 4 ≤ 5 → place **1** under 4; 5 − 4 = 1 remaining
- 2 > 1 → place **0** under 2
- 1 = 1 → place **1** under 1

![Diagram: step-by-step denary to binary conversion showing highlighted place value cells filled one at a time for the number 53]

| 64 | 32 | 16 | 8 | 4 | 2 | 1 |
|----|----|----|---|---|---|---|
| 0  | 1  | 1  | 0 | 1 | 0 | 1 |

`53 = 0110101 = 110101 = 00110101`

Although it's acceptable to remove any leading 0s, it may be preferable to add 0s to the start of your answer to make it a whole number of bytes (a multiple of 8 bits).

---

### Most Significant and Least Significant Bit

The **most significant bit** is the bit with the highest value, which is the leftmost 1 in a binary number. The **least significant bit** is the bit with the lowest value, which is the rightmost bit, whether it is a 0 or 1, in a binary number.

Adding additional 0s to the left of a binary number does not change its value, e.g. `11010` is the same as `00011010`.

---

## Converting Binary ↔ Hexadecimal

### To convert binary → hex:

In order to convert from binary to hexadecimal, the binary number must first be split into **nibbles**. A nibble is four binary bits, or half a byte.

**Example: `10110010` split into two nibbles:**

![Diagram: tree/branch diagram showing 10110010 split with arrows into two nibbles: 1011 (left) and 0010 (right)]

Each binary nibble is then converted to decimal:

- `1011`: 8 + 2 + 1 = **11**
- `0010`: 2 = **2**

Then each decimal value is converted to its hexadecimal equivalent:

- 11 = **B**
- 2 = **2**

Finally, the hexadecimal digits are concatenated:

`10110010 = B2`

---

**Example: 16-bit binary `1011001101101110` split into 4 nibbles:**

![Diagram: tree/branch diagram showing 1011001101101110 split with four arrows into nibbles: 1011, 0011, 0110, 1110]

Each nibble converted:

| Nibble | Binary | Decimal | Hex |
|--------|--------|---------|-----|
| 1      | 1011   | 8+2+1=11 | B  |
| 2      | 0011   | 2+1=3   | 3   |
| 3      | 0110   | 4+2=6   | 6   |
| 4      | 1110   | 8+4+2=14 | E  |

`1011001101101110 = B36E`

> For this specification, the maximum length of binary number you could be asked to convert is 16-bit.

---

### To convert hex → binary:

First, convert each hexadecimal digit to a decimal digit and then to a binary nibble before combining the nibbles to form a single binary number.

**Example: `B2` → binary**

![Diagram: flow diagram showing B2 split into digits B and 2, converted to decimal 11 and 2, then to binary nibbles 1011 and 0010, then combined into 10110010]

1. Split into hex digits: **B** and **2**
2. Convert hex to decimal: 11 and 2
3. Convert decimal to binary nibbles: **1011** and **0010**
4. Combine nibbles: `10110010`

---

## Converting Denary ↔ Hexadecimal

### To convert denary → hex:
1. Begin by converting the denary number into binary
2. Convert this binary number to hexadecimal

### To convert hex → denary:
1. Begin by converting the hexadecimal number into binary
2. Convert this binary number to denary

---

## How and why hexadecimal is used

Hexadecimal is a shorthand representation of binary: it is easier for people to read than binary, and it takes less time to type than binary. Therefore, hexadecimal representation is used because it is easier for humans to read and work with. However, hexadecimal does not offer any advantage to computers; computers always represent numbers using binary.

There are several areas within computer science where hexadecimal is used, for example:

- **Colour codes:** Hex is used to represent RGB colour values in HTML/CSS (e.g., `#FE7C1B` for a specific shade of orange).
- **Media Access Control (MAC) addresses:** Devices on a network have unique MAC addresses written in hex (e.g., `00:1A:2B:3C:4D:5E`), representing 48-bit identifiers.

---

## Binary Addition

When adding binary numbers, there are three important rules to remember:

| Binary add | Result | Carry    |
|------------|--------|----------|
| 0 + 0      | 0      | 0        |
| 1 + 0      | 1      | 0        |
| 1 + 1      | 0      | 1 (carry)|
| 1 + 1 + 1  | 1      | 1 (carry)|

You'll only be expected to add two positive binary numbers of 8 bits.

A computer or a device has a predefined limit that it can represent or store, depending on the number of bits allocated. An **overflow error** can occur when the result of a binary addition is too large to be represented by the number of bits available. For example, if the result is greater than 255 in denary, requiring more than 8 bits, and you only have 8 bits available, then an overflow error will occur.

**Example: Add binary integers 1011 and 1110**

![Diagram: step-by-step binary column addition showing 1011 + 1110, with each column highlighted in sequence, carry digits shown in small writing above, resulting in 11001]

Working from the least significant bit (right to left):
- Column 1 (rightmost): 1 + 0 = **1**
- Column 2: 1 + 1 = 0, carry **1**
- Column 3: 0 + 1 + carry 1 = 0, carry **1** (result is 10)
- Column 4: 1 + 1 + carry 1 = 1, carry **1** (result is 11)

```
  1 0 1 1
+ 1 1 1 0
---------
1 1 0 0 1
```

So `1011 + 1110 = 11001`.

> **Note:** the overflow 1 (most significant bit) should be removed in questions unless stated otherwise. You should state that you have removed the overflow bit.

---

## Binary Shifts

A logical binary shift involves moving the bits of a binary number left or right. Bits shifted from the end of the register are lost and zeros are shifted in at the opposite end of the register. This means that the most significant bit(s) or least significant bit(s) are lost.

**There are two types of binary shift:**

- **Left shift** → moves all bits to the left (adds 0s on the right)
  - Same as multiplying by 2 for each place shifted
- **Right shift** → moves all bits to the right (adds 0s on the left)
  - Same as dividing by 2 for each place shifted

**Example: left shift of 1 applied to `00101100` (44)**

```
Original:  00101100  (44)
Shifted:   01011000  (88)
```

The effect is to multiply 44 by 2, making 88.

---

## Two's Complement

When using two's complement, the most significant bit of a binary number is given a negative place value. For an 8-bit number, the place values are:

![Diagram: large display of 8-bit two's complement place values: −128  64  32  16  8  4  2  1]

| −128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
|------|----|----|----|----|---|---|---|

This allows negative numbers to be represented as low as −128. If the first bit is 1, the number is negative. If it's 0, the number is positive.

**Example:** `1011` in two's complement (4-bit):

![Diagram: large display of place values −8  4  2  1 with binary digits 1  0  1  1 beneath, and calculation −8 + 2 + 1 = −5]

| −8 | 4 | 2 | 1 |
|----|---|---|---|
| 1  | 0 | 1 | 1 |

`−8 + 2 + 1 = −5`

---

### To convert positive denary integer → 8-bit two's complement binary:

This procedure is almost identical to the standard denary to binary conversion.

If you need the result to be 8 bits, pad it with leading 0s to the left of the number. You must make sure that the most significant bit isn't a 1, otherwise the result will become an incorrect negative number.

**Example:** converting 25 to 8-bit two's complement:
- 25 in binary = `11001`
- Pad to 8 bits = `00011001`

---

### To convert positive 8-bit two's complement binary → denary integer:

This procedure is identical to the standard binary to denary conversion. Write out the place values with the most significant bit having a negative sign:

| −128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
|------|----|----|----|----|---|---|---|

---

### To convert negative 8-bit two's complement binary → denary integer:

Carry out the following procedure:
1. Confirm that the most significant bit is 1. This indicates the number is negative.
2. Invert all the bits (change 0s to 1s and 1s to 0s).
3. Add 1 to the inverted binary number.
4. Convert the result to denary as a positive binary number.
5. Add a minus sign to make the answer negative.

**Example:** convert `11101010` to denary:
- Step 1: First bit is 1, so the number is negative.
- Step 2: Invert the bits → `00010101`
- Step 3: Add 1 → `00010101 + 1 = 00010110`
- Step 4: `00010110` = 22 in denary
- Step 5: Make it negative → **−22**

---

### To convert a negative denary integer → 8-bit two's complement binary:

Carry out the following procedure:
1. Write the positive version of the number in binary.
2. Pad it with leading 0s to make it 8 bits long.
3. Invert all bits (change 0s to 1s and 1s to 0s).
4. Add 1 to the inverted binary number.

The final result should be 8 bits long and start with a 1.

**Example:** convert −37 to 8-bit two's complement binary:
- Step 1: +37 in binary = `100101`
- Step 2: Pad with leading 0s → `00100101`
- Step 3: Invert the bits → `11011010`
- Step 4: Add 1 → `11011010 + 1 = 11011011`

Result: **`11011011`**

---

### To convert negative 8-bit two's complement → positive 8-bit two's complement:

Carry out steps 2, 3, and 4 of the previous algorithm:
1. Pad with leading 1s (as it is negative).
2. Invert all bits (change 0s to 1s and 1s to 0s).
3. Add 1 to the inverted number.

**Example:** convert −61 to +61 in two's complement:
- Step 1: −61 is `1000011` (7 bits), therefore pad with 1s → `11000011`
- Step 2: Invert the bits → `00111100`
- Step 3: Add 1 → `00111101` = 61

> **Note:** the exact same process can be used to convert from positive to negative in two's complement.

---

## 1.2 Text, Sound and Images

### Representing text

Text must be converted into binary to be processed by a computer.

A **character set**, such as ASCII or Unicode, is a collection of characters and their corresponding binary values. Every character is assigned a unique binary code, known as a **character code**, using a standard such as ASCII or Unicode.

#### ASCII (American Standard Code for Information Interchange)

- Uses 7 bits to represent each character
- Can store 128 (2⁷) characters
- Includes:
  - English letters (uppercase & lowercase)
  - Digits 0–9
  - Common symbols (@, #, etc.)
  - Control codes (like newline)

#### Unicode

- Uses 8–48 bits to represent each character, allowing it to represent a much wider range of different characters than ASCII, but requiring much more space.
- Supports many different languages (not just the Latin alphabet but also alphabets like Arabic, Cyrillic, Greek and Hebrew), and more symbols (such as emojis). This means that data such as text can be represented in a wider range of languages, making computers more accessible worldwide.

---

### Representing sound

![Diagram: two waveform drawings side by side — left shows a smooth continuous analogue signal curve, right shows a stepped/blocky digital signal]

Sound is analogue, meaning that its signal is a continuous wave that can take any value, not having a singular value. Computers cannot store continuous sound waves, so they take regular snapshots (**samples**) of the sound wave's **amplitude**. A sample is a measure of amplitude at a point in time — each sample is stored as a binary number.

- The **sampling rate** is the number of samples taken in a second.
- The **sample resolution** is the number of bits per sample (gives a more precise and accurate measure of the sound's amplitude at any one point).
- The **accuracy** of the recording and the file size increases as the sample rate and resolution increase.

---

### Representing images

Digital images are made up of a series of tiny squares called **pixels** (short for "picture elements"). A pixel is a single point in an image. Each pixel has a colour value, and this is stored in binary.

The value assigned to a pixel determines the colour of the pixel. The example below shows the binary representation of a simple image in which a 1 represents a black pixel and a 0 represents a white pixel.

![Diagram: 5×5 pixel grid showing the letter "P" in black pixels on a white background, with corresponding binary values shown to the right: 01110 / 01010 / 01110 / 01000 / 01000]

The number of bits assigned to a pixel in an image is called its **colour depth**. For example, with a colour depth of one bit, there are 2 (2¹) different colours. With two bits, there are four (2²) different colours represented by bit patterns 00, 01, 10 and 11.

The **resolution** refers to the number of pixels within an image. Resolution can be found by multiplying the image width in pixels by the image height in pixels.

The **file size** and **quality** of the image increase as the resolution and colour depth increase.

---

## 1.3 Data Storage and Compression

### Unit prefixes

Each binary digit is a **bit** of data. The following prefixes are used for measuring data:

| Unit      | Symbol | Relative size    |
|-----------|--------|------------------|
| Bit       | b      | 1 bit            |
| Nibble    |        | 4 bits           |
| Byte      | B      | 8 bits           |
| Kibibyte  | KiB    | 1024 bytes       |
| Mebibyte  | MiB    | 1024 kibibytes   |
| Gibibyte  | GiB    | 1024 mebibytes   |
| Tebibyte  | TiB    | 1024 gibibytes   |
| Pebibyte  | PiB    | 1024 tebibytes   |
| Exbibyte  | EiB    | 1024 pebibytes   |

---

### File size calculations

To calculate the file sizes of sound and image files, you can use the following formulas:

- *Sound file size* = sample rate × duration (s) × bit depth
- *Image resolution* = height (px) × image width (px)
- *Image file size* = colour depth × image resolution

> **Note:** file size calculations **must** use the measurement of 1024 and **not** 1000.

---

### Data compression

Data compression is the process of reducing the file size of digital data without losing the original information (or with minimal acceptable loss). It is used to save storage space and speed up transmission, as well as reducing the bandwidth required. There are two types of image compression: lossy and lossless.

#### Lossy compression

When using lossy compression, some information is permanently lost in the process of reducing the file's size. This could cause the quality of the file to be slightly reduced; the compressed file can never be fully restored to the original. This could be done by reducing the resolution of audio or reducing the colour depth of an image.

#### Lossless compression

In contrast to lossy compression, there is no permanent loss of information when using lossless compression. The size of a file can be reduced without decreasing its quality. Lossless compression methods use algorithms to find and compress patterns (e.g. repeated data).

---

### Run Length Encoding (RLE)

Run length encoding (RLE) is a type of lossless compression, which reduces the size of a file by removing repeated information and replacing it with one occurrence of the repeated information followed by the number of times it is to be repeated.

**Example:** In a bitmap image, using RLE to replace repeated pixels with one pixel value and a number of repetitions reduces the storage space required to represent the image.

![Diagram: coloured pixel grid (7×7) showing a face-like image with yellow, black, white and red tiles, alongside its RLE-encoded binary representation with run-length subscripts]

If a row of pixels has no repeated values, it cannot be compressed by RLE. This highlights the fact that not all data is suitable for compression by run length encoding. For example, text is not suited to RLE at all, as it is unlikely to have many 'runs' of repeated letters.

---

*This work by PMT Education is licensed under CC BY-NC-ND 4.0*
