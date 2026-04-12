# 1.2 Text, Sound, and Images

> Source: https://moshikur.com/igcse-o-level-cs/ch-01-data-representation/1-2-text-sound-and-images/

# 1.2 Text, Sound, and Images

---

> Syllabus

Candidates should be able to:  
  
Understand how and why a computer represents an image, including the effects of the resolution and color depth  
a. An image is a series of pixels that are converted to binary, which is processed by a computer  
b. The resolution is the number of pixels in the image  
c. The color depth is the number of bits used to represent each colour  
d. The file size and quality of the image increase as the resolution and colour depth increase  
  
Understand how and why a computer represents text and the use of character sets, including American standard code for information interchange (ASCII) and Unicode  
a. Text is converted to binary to be processed by a computer  
b. Unicode allows for a greater range of characters and symbols than ASCII, including different languages and emojis  
c. Unicode requires more bits per character than ASCII  
  
Understand how and why a computer represents sound, including the effects of the sample rate and sample resolution  
a. A sound wave is sampled for sound to be converted to binary, which is processed by a computer  
b. The sample rate is the number of samples taken in a second  
c. The sample resolution is the number of bits per sample  
d. The accuracy of the recording and the file size increases as the sample rate and resolution increase

#### [1.2.1 TEXT REPRESENTATION](#text_representation)

#### [1.2.2: Sound Representation](#sound_representation)

#### [1.2.3: Image Representation](#image_representaion)

### [Take the Quiz](https://moshikur.com/quizzes/1-2-text-sound-and-images-quiz/)

## **1.2.1: Text Representation**

Computers cannot understand letters, words, or symbols the way humans do. Instead, they represent text using **binary numbers**. Let’s explore how computers handle text and the role of character sets like **ASCII** and **Unicode** in this process.

---

**1.2.1.1 How and Why Computers Represent Text**

**How Computers Represent Text**

- Every letter, digit, or symbol is assigned a unique numeric code.
- These codes are converted into binary so the computer can store, process, and display them.

For example:

- The letter **A** is represented by the number **65** in the ASCII character set.
- In binary, **65** is written as **01000001**, which the computer uses internally.

**Why Computers Represent Text in Binary**

- Computers use binary (0s and 1s) because they rely on electronic components that have two states: **ON** and **OFF**.
- By assigning unique binary patterns to each character, computers can process and store text efficiently.

---

**1.2.1.2 Character Sets: ASCII and Unicode**

**1. ASCII (American Standard Code for Information Interchange)**

- ASCII is one of the earliest character sets developed.
- It uses **7 bits** to represent **128 characters**, including:
  - Uppercase and lowercase letters (A–Z, a–z)
  - Digits (0–9)
  - Common symbols (e.g., @, #, &, !)
  - Control characters (e.g., Enter, Tab)

**Example**:

- The letter **A** is represented as **65** in ASCII (binary: **01000001**).
- The letter **a** is represented as **97** in ASCII (binary: **01100001**).

**Limitations of ASCII**:

- ASCII can only represent English characters and a limited set of symbols.
- It cannot represent characters from other languages like Chinese, Arabic, or emojis.

---

**2. Unicode**

- Unicode was developed to overcome the limitations of ASCII.
- It uses **up to 32 bits**, allowing it to represent **over a million characters**.
- Unicode supports characters from many languages, including:
  - English, Chinese, Arabic, Hindi, etc.
  - Symbols and emojis.

**Two Common Unicode Formats**:

1. **UTF-8**:
   - Uses 1–4 bytes per character.
   - Backward-compatible with ASCII (characters 0–127 are the same).
2. **UTF-16**:
   - Uses 2 or 4 bytes per character.
   - Commonly used for non-Latin scripts and emojis.

**Example**:

- The Unicode for the letter **A** is **U+0041** (same as ASCII).
- The emoji 😊 has the Unicode **U+1F60A**.

---

**Why Use Character Sets?**

Character sets like ASCII and Unicode standardize how text is represented across different devices and systems. This ensures:

1. **Compatibility**: Text can be exchanged between computers, phones, and other devices.
2. **Globalization**: Unicode allows support for multiple languages and scripts in a single system.

---

**Key Differences Between ASCII and Unicode**

| Feature | ASCII | Unicode |
| --- | --- | --- |
| Bit Size | 7 bits (or 8 bits in extended versions) | Up to 32 bits |
| Characters Supported | 128 (or 256 in extended ASCII) | Over 1 million |
| Language Support | English and basic symbols | All major languages, symbols, and emojis |
| Examples | A = 65 (01000001 in binary) | 😊 = U+1F60A (binary: varies by format) |

---

## **Activity 1**

**Short Answer Questions**

1. Why do computers use binary to represent text? [1]
2. How many characters can ASCII represent? [1]
3. What is the primary limitation of ASCII? [1]
4. How does Unicode improve upon ASCII? [1]

**Long Answer Questions**

1. Explain how a computer represents text using binary and character sets. Include examples of ASCII and Unicode in your answer. [5]
2. Compare ASCII and Unicode in terms of character support and usage. Why is Unicode important in modern computing? [4]
3. The letter “H” is represented by the ASCII value **72**, and the letter “😊” is represented by the Unicode value **U+1F60A**. Describe the differences in how these two characters are stored and processed by a computer. [3]

---

## **1.2.2: Sound Representation**

[![](images/topic1_data_representation/1_2_text_sound_and_images/img_001.png)](https://i0.wp.com/moshikur.com/wp-content/uploads/2025/02/image-1.png?ssl=1)

Computers cannot directly process sounds like humans hear them. Instead, they convert sound waves into binary data using a process called **digital sound representation**. This allows computers to store, manipulate, and reproduce sound.

---

### **1.2.2.1 How and Why Computers Represent Sound**

#### **How Sound is Represented**

1. **Sound as an Analog Wave**:
   - Sound in the real world is a continuous wave that fluctuates smoothly over time.
   - To process this analog wave, a computer converts it into a series of discrete values using **sampling**.
2. **Sampling**:
   - The computer “samples” the sound wave at regular intervals to capture its shape.
   - Each sample records the amplitude (height) of the wave at that point in time.
3. **Converting Samples to Binary**:
   - Each sampled value is converted into a binary number based on its amplitude.
   - These binary numbers are stored and processed by the computer.

**Example**:

- A sound wave is sampled at a specific point, and the amplitude is recorded as `250`.
- In binary, `250` is stored as `11111010` (assuming 8-bit resolution).

#### **Why Computers Represent Sound**

- Computers represent sound in binary to:
  - **Store sound files** like MP3 or WAV formats.
  - **Manipulate sound**, such as editing or adding effects.
  - **Transmit sound data** over networks (e.g., during a phone call or video conference).

---

### **1.2.2.2 Effects of Sample Rate and Sample Resolution**

#### **1. Sample Rate**

- **Definition**: The number of samples taken per second.
- Measured in **Hertz (Hz)**. For example:
  - **44,100 Hz (44.1 kHz)** is commonly used in CDs, meaning 44,100 samples are taken per second.

**Effect of Sample Rate**:

- **Higher Sample Rate**:
  - Captures more detail from the sound wave.
  - Results in better sound quality.
  - Increases the file size.
- **Lower Sample Rate**:
  - Captures less detail.
  - Reduces sound quality.
  - Decreases the file size.

#### **2. Sample Resolution**

- **Definition**: The number of bits used to store each sample’s amplitude.
- Common resolutions include **8 bits**, **16 bits**, or **24 bits**.

**Effect of Sample Resolution**:

- **Higher Resolution**:
  - Records more precise amplitude values.
  - Results in better sound quality (less distortion or noise).
  - Increases the file size.
- **Lower Resolution**:
  - Reduces the accuracy of the recorded amplitude.
  - Leads to poorer sound quality.
  - Decreases the file size.

**Example**:

- A **16-bit resolution** allows for 216=65,5362^{16} = 65,536216=65,536 possible values per sample.
- An **8-bit resolution** allows for only 28=2562^8 = 25628=256 possible values, making the sound less accurate.

---

### **Key Factors in Sound Representation**

1. **File Size**:
   - File size depends on sample rate, resolution, and duration.
   - Formula: File Size (bits)=Sample Rate×Sample Resolution×Duration (seconds)×Number of Channels (e.g., Stereo = 2).
2. **Trade-Offs**:
   - Higher sample rate and resolution improve quality but require more storage.
   - Lower sample rate and resolution save storage but reduce sound fidelity.

---

## **Activity 2**

#### **Short Answer Questions**

1. Define sample rate and state how it is measured. [1]
2. What is the effect of increasing the sample resolution on the quality and size of a sound file? [2]
3. Convert a 10-second stereo sound file with a sample rate of 44,100 Hz and a resolution of 16 bits into its total file size in bits. [2]
4. Explain why sound is converted from analog to digital for a computer to process. [2]

#### **Long Answer Questions**

1. Explain how a computer represents sound, including the process of sampling and converting data into binary. [4]
2. A sound engineer is recording audio for a high-quality music file. Discuss the importance of choosing a high sample rate and sample resolution. What trade-offs should they consider? [5]
3. Compare the effects of a **48,000 Hz sample rate** and a **24-bit resolution** with a **22,050 Hz sample rate** and an **8-bit resolution** on both sound quality and file size. [5]

## 1.2.3: Image Representation

Images are an important type of data that computers handle. To process and display images, computers must represent them in a digital form using binary numbers. Let’s explore how images are represented and the impact of **resolution** and **colour depth** on image quality and file size.

---

**1.2.3.1 How and Why Computers Represent Images**

**How Computers Represent Images**

1. **Pixels**:
   - A digital image is made up of tiny squares called **pixels**.
   - Each pixel represents a single color.
   - The more pixels an image has, the more detail it can display.
2. **Binary Representation of Pixels**:
   - Each pixel’s color is stored as a binary value.
   - The binary value depends on the **colour depth** of the image.
3. **Colour Depth**:
   - **Colour depth** refers to the number of bits used to represent the color of each pixel.
   - Examples:
     - **1-bit colour depth**: Each pixel is either black or white.
     - **8-bit colour depth**: Each pixel can have 256 different colors.
     - **24-bit colour depth**: Each pixel can have over 16 million colors (True Color).

---

**Why Computers Represent Images**

- To **store images digitally** for editing, sharing, or displaying.
- To enable efficient processing of image data in applications like websites, games, or graphic design.
- To represent images in formats like **JPEG, PNG, BMP**, which use binary data to encode color and brightness.

---

**1.2.3.2 Effects of Resolution and Colour Depth**

**1. Resolution**

- **Definition**: Resolution refers to the number of pixels in an image, usually described as **width × height** (e.g., 1920 × 1080).
- **Effect on Quality**:
  - Higher resolution = more pixels = more detail in the image.
  - Lower resolution = fewer pixels = less detail (the image may appear blurry).
- **Effect on File Size**:
  - Higher resolution increases file size because more pixel data needs to be stored.

**2. Colour Depth**

- **Definition**: Colour depth is the number of bits used to represent the color of each pixel.
- **Effect on Quality**:
  - Higher colour depth allows more colors, resulting in smoother gradients and more realistic images.
  - Lower colour depth limits the number of colors, causing images to appear banded or unrealistic.
- **Effect on File Size**:
  - Higher colour depth increases file size because more bits are needed to represent each pixel.

---

**Example: Calculating File Size**

To calculate the file size of an uncompressed image:

File Size (bits)=Resolution (width × height)×Colour Depth (bits per pixel)\text{File Size (bits)} = \text{Resolution (width × height)} \times \text{Colour Depth (bits per pixel)}File Size (bits)=Resolution (width × height)×Colour Depth (bits per pixel)

- **Example**: An image with a resolution of 1920 × 1080 and a colour depth of 24 bits: File Size=1920×1080×24=49,766,400 bits (or approximately 6 MB).\text{File Size} = 1920 \times 1080 \times 24 = 49,766,400 \text{ bits (or approximately 6 MB)}.File Size=1920×1080×24=49,766,400 bits (or approximately 6 MB).

---

## **Activity 3**

**Short Answer Questions**

1. Define what is meant by a “pixel” in a digital image. [1]
2. What does “resolution” describe in a digital image? [1]
3. An image has a resolution of 100 × 200 and a colour depth of 8 bits. Calculate its file size in bytes. [2]
4. State how increasing the colour depth affects the quality and file size of an image. [2]
5. Explain why a computer uses binary to represent the colors in a digital image. [1]

**Long Answer Questions**

1. Explain how a computer represents an image using pixels and binary numbers. Include examples of how resolution and colour depth are used. [5]
2. A photographer is deciding between two cameras. One produces images with a resolution of **4000 × 3000** and a colour depth of **24 bits**, while the other produces images with a resolution of **1920 × 1080** and a colour depth of **16 bits**. Compare the quality and file size of the images produced by the two cameras. [5]
3. Discuss the trade-offs between increasing the resolution and colour depth of an image and the impact this has on storage and quality. [4]

---