# 1.3 Compression

> Source: https://moshikur.com/igcse-o-level-cs/ch-01-data-representation/1-3-data-storage-and-compression/

# 1.3 Data Storage and Compression

---

Syllabus:

Candidates should be able to:  
  
Understand how data storage is measured

- Including:  
  i. bit  
  ii. nibble  
  iii. byte  
  iv. kibibyte (KiB)  
  v. mebibyte (MiB)  
  vi. gibibyte (GiB)  
  vii. tebibyte (TiB)  
  viii. pebibyte (PiB)  
  ix. exbibyte (EiB)
- The amount of the previous denomination present in the data storage size, e.g.:  
  i. 8 bits in a byte  
  ii. 1024 mebibytes in a gibibyte

Calculate the file size of an image file and a sound file, using information given

- Answers must be given in the units specified in the question. Calculations must use the  
  measurement of 1024 and not 1000
- Information given may include:  
  o image resolution and color depth  
  o sound sample rate, resolution and length of track

Understand the purpose of and need for data compression

- Compression exists to reduce the size of the file
- What the impact of this is, e.g.:  
  o less bandwidth required  
  o less storage space required  
  o shorter transmission time

Understand how files are compressed using lossy and lossless compression methods

- Lossy compression reduces the file size by permanently removing data, e.g. reducing resolution or  
  colour depth, reducing sample rate or resolution
- Lossless compression reduces the file size without permanent loss of data, e.g. run length  
  encoding (RLE)

---

[1.3.1 STORAGE](#storage)

[1.3.2 File Size Calculations](#calculation)

[1.3.3 Compression](#compression)

[QUIZ](https://moshikur.com/quizzes/chapter-1-3-data-storage-and-compression-quiz/)

## **1.3.1 : Understanding How Data Storage is Measured**

### **Units of Data Storage**

#### **1. Bit (b)**

- A **bit** is the smallest unit of data storage.
- A bit can store a single binary value: either **0** or **1**.
- Example: A light switch can either be ON (**1**) or OFF (**0**)—this represents one bit of information.

---

#### **2. Byte (B)**

- A **byte** consists of **8 bits**.
- One byte can store a single character in text (e.g., the letter “A”).
- Bytes are the standard unit of measurement for most file sizes.
  - Example: The word “Hello” consists of 5 characters, so it would require **5 bytes** (40 bits).

[![](images/topic1_data_representation/1_3_compression/img_001.png)](https://i0.wp.com/moshikur.com/wp-content/uploads/2024/12/image.png?ssl=1)

---

#### **3. Larger Units of Data Storage**

- As file sizes grow larger, we use bigger units to measure data. These are based on powers of 2 because computers operate in binary.

### **Why Do We Have Decimal and Binary Measurements?**

1. **Decimal Measurement (e.g., KB, MB)**:
   - Based on powers of 10.
   - Used in marketing for storage devices like hard drives and USBs.
   - Example: A 1 TB hard drive in decimal is **1 trillion bytes**.
2. **Binary Measurement (e.g., KiB, MiB)**:
   - Based on powers of 2.
   - Used in technical contexts like RAM or file sizes.
   - Example: 1 GiB in binary is **1,073,741,824 bytes**.

---

### **Examples of Data Storage Sizes**

1. A text file with 100 characters:
   - Each character = 1 byte.
   - File size = **100 bytes**.
2. A typical MP3 song:
   - Approx. **4 MB (megabytes)**.
3. A Full HD movie:
   - Approx. **4 GB (gigabytes)**.
4. A hard drive:
   - Storage capacity could be **1 TB (terabyte)**.

> ### **Activity 1.3.1**
>
> 1. What is the smallest unit of data storage? [1]
> 2. How many bits are there in a byte? [1]
> 3. A file is 5 kilobytes (KB) in size. How many bytes is this? [2]
> 4. Convert **3 MiB** (mebibytes) into bytes. [2]
> 5. Explain the difference between a kilobyte (KB) and a kibibyte (KiB). [2]
> 6. Explain how data storage is measured, starting from bits and progressing to terabytes. Provide examples of file types and their approximate sizes. [5]
> 7. A student has a USB drive with a storage capacity of **16 GB**. Explain how much data the drive can hold if each file is 4 MB in size. [4]
> 8. Discuss the practical significance of binary measurements (e.g., KiB, MiB) in computing. Why are these units important when working with files and memory? [5]

## **1.3.2 : File Size Calculations**

When working with images or sound files, understanding how to calculate their file size is essential. This helps in managing storage, transferring files, or optimizing performance. Let’s learn how to calculate the file size of **images** and **sound files** step by step.

---

### **1. File Size of an Image**

#### **Key Formula**

[![](images/topic1_data_representation/1_3_compression/img_002.png)](https://i0.wp.com/moshikur.com/wp-content/uploads/2024/12/image-1.png?ssl=1)

#### **What Each Term Means**

1. **Resolution**: The number of pixels in the image, given as **width × height**.
2. **Colour Depth**: The number of bits used to represent the color of a single pixel.
   - Examples:
     - **1-bit**: Black and white only.
     - **8-bit**: 256 colors.
     - **24-bit**: True color (16.7 million colors).

---

#### **Example 1: Calculating the File Size of an Image**

**An image has a resolution of 1920 × 1080 pixels and a colour depth of 24 bits per pixel.**

[![](images/topic1_data_representation/1_3_compression/img_003.png)](https://i0.wp.com/moshikur.com/wp-content/uploads/2024/12/image-2.png?ssl=1)

**Answer**: The file size of the image is **6.22 MB**.

---

### **2. File Size of a Sound File**

#### **Key Formula**

[![](images/topic1_data_representation/1_3_compression/img_004.png)](https://i0.wp.com/moshikur.com/wp-content/uploads/2024/12/image-3.png?ssl=1)

#### **What Each Term Means**

1. **Sample Rate**: The number of samples taken per second, measured in **Hertz (Hz)**.
   - Common values: 44,100 Hz (CD quality), 48,000 Hz.
2. **Sample Resolution**: The number of bits used to store each sample (e.g., 8 bits, 16 bits).
3. **Duration**: Length of the sound file in seconds.
4. **Number of Channels**:
   - **1** for mono sound.
   - **2** for stereo sound.

---

#### **Example 2: Calculating the File Size of a Sound File**

**A stereo sound file has a sample rate of 44,100 Hz, a sample resolution of 16 bits, and a duration of 5 seconds.**

[![](images/topic1_data_representation/1_3_compression/img_005.png)](https://i0.wp.com/moshikur.com/wp-content/uploads/2024/12/image-4.png?ssl=1)

**Answer**: The file size of the sound file is **882 KB**.

---

### **Important Notes**

1. Always check whether the colour depth or sample resolution is given in **bits** or **bytes**.
2. Convert to appropriate units (KB, MB, GB) based on the context.
3. Compression methods like **lossy** or **lossless** reduce file size but are not included in these calculations unless specified.

> ### **Activity 1.3.2**
>
> 1. Calculate the file size of an image with a resolution of 800 × 600 pixels and a colour depth of 8 bits. Give your answer in bytes. [2]
> 2. A sound file has a sample rate of 48,000 Hz, a resolution of 8 bits, a duration of 10 seconds, and is mono. Calculate its file size in kilobytes. [3]
> 3. An image has a file size of 1 MB and a resolution of 1024 × 1024 pixels. What is the colour depth of the image in bits? [2]
> 4. Explain the steps to calculate the file size of an image and a sound file. Include examples in your explanation. [5]
> 5. A movie poster is stored as an image with a resolution of **4000 × 3000 pixels** and a colour depth of **24 bits**. A movie trailer is stored as a stereo sound file with a sample rate of **48,000 Hz**, resolution of **16 bits**, and duration of **120 seconds**. Compare the sizes of these two files in megabytes. Show all your working. [5]
> 6. Discuss how increasing the resolution or colour depth of an image affects its file size. Why might a graphic designer choose to work with higher resolutions despite the larger file size? [4]

## **1.3.3: Compression**

---

### **1.3.3.1 Purpose of and Need for Data Compression**

#### **Purpose of Data Compression**

Data compression reduces the size of files, enabling efficient storage, sharing, and processing. It is widely used in applications like image storage, video streaming, audio sharing, and software packaging.

1. **Save Storage Space**:
   - Compressed files occupy less space on storage devices such as hard drives, SSDs, or memory cards.
   - Example: A compressed 10 MB image may take only 2 MB.
2. **Faster File Transfers**:
   - Smaller files can be uploaded or downloaded more quickly over the internet.
   - Important for large file transfers, especially over limited bandwidth.
3. **Reduce Bandwidth Usage**:
   - Compressed files require less bandwidth, which is crucial for online streaming services and mobile networks.
4. **Enable Streaming and Sharing**:
   - Services like YouTube, Netflix, and Spotify use compression to allow users to stream high-quality content with lower data consumption.

#### **Need for Data Compression**

- Large files, such as videos and high-resolution images, can be difficult to manage without compression.
- Compression helps in making files more accessible and less resource-intensive for devices and networks.

---

### **1.3.3.2 How Files are Compressed: Lossy vs. Lossless Compression**

#### **1. Lossy Compression**

- **Definition**:
  - Permanently removes some data to significantly reduce file size.
  - The data removed is often non-essential or imperceptible to humans.
- **Examples**:
  - **JPEG (images)**: Removes subtle details.
  - **MP3 (audio)**: Discards sounds outside the normal hearing range.
  - **MP4 (video)**: Reduces resolution, frame rate, or unnecessary details.
- **Advantages**:
  - Drastically reduces file size.
  - Ideal for applications where small file size is critical, such as streaming and sharing.
- **Disadvantages**:
  - Loss of quality; the original file cannot be restored.
  - Unsuitable for applications where precision is required (e.g., text or medical images).

---

#### **2. Lossless Compression**

- **Definition**:
  - Reduces file size without losing any data, allowing the original file to be restored perfectly.
- **Examples**:
  - **PNG (images)**: Compresses without losing quality.
  - **ZIP (files)**: Bundles and compresses files without data loss.
  - **FLAC (audio)**: Preserves high-quality sound.
- **Advantages**:
  - No loss of quality.
  - Suitable for critical applications like text files, software, and archival storage.
- **Disadvantages**:
  - File size reduction is less significant compared to lossy compression.

---

### **Key Differences: Lossy vs. Lossless Compression**

| Feature | Lossy Compression | Lossless Compression |
| --- | --- | --- |
| Data Loss | Yes | No |
| File Size Reduction | Large | Moderate |
| Examples | JPEG, MP3, MP4 | PNG, ZIP, FLAC |
| Use Cases | Streaming, sharing | Critical files, backups |

---

### **How Compression Works**

#### **Steps in Lossy Compression**:

1. Analyze the file to identify non-critical data.
2. Remove less noticeable details (e.g., sounds humans can’t hear or colors close in shade).
3. Save the file in a compressed format (e.g., JPEG or MP3).

#### **Steps in Lossless Compression**:

1. Analyze the file for repetitive data patterns.
2. Replace repetitive patterns with shorter codes (e.g., “AAABBB” → “3A3B”).
3. Store the file with the encoded patterns (e.g., ZIP).

> ### **Activity 1.3.3**
>
> 1. Why is data compression important in modern computing? [2]
> 2. What is the key difference between lossy and lossless compression? [1]
> 3. Name two file types that commonly use lossy compression and two that use lossless compression. [2]
> 4. Why would a ZIP file be preferred over a JPEG file for storing text documents? [1]
> 5. Explain the purpose of data compression and describe how it benefits online streaming services. [5]
> 6. Compare and contrast lossy and lossless compression methods. Include examples and discuss when each method would be most appropriate. [5]
> 7. Discuss the trade-offs between using lossy compression for video files and lossless compression for archival purposes. Provide examples of practical applications. [4]

### **Run-Length Encoding (RLE): A Lossless Compression Method**

**Run-Length Encoding (RLE)** is a simple and efficient **lossless compression** technique used to reduce file size by encoding repeated data. It works best with data that contains many consecutive repeated values, such as simple images, patterns, or runs of identical characters in text.

---

### **How RLE Works**

1. **Identify Repeated Data**:
   - RLE looks for sequences of repeated data, called **runs**.
   - Each run is replaced with a single instance of the value and the number of times it repeats.
2. **Encode the Data**:
   - The repeated value is stored alongside the count of repetitions.
3. **Store Encoded Data**:
   - The compressed file contains the encoded data, which is smaller than the original if there are many repeated values.

---

### **Example of RLE**

#### **Text Example**

Original data:  
`AAAAABBBCCDAA`

Steps:

1. Identify runs of repeated characters:
   - `A` repeats 5 times.
   - `B` repeats 3 times.
   - `C` repeats 2 times.
   - `D` repeats 1 time.
   - `A` repeats 2 times.
2. Encode as:
   - `5A 3B 2C 1D 2A`

**Compressed result**: `5A3B2C1D2A`

---

#### **Image Example**

For a simple black-and-white image:

```
111110000011111
```

Steps:

1. Identify runs:
   - `1` appears 5 times.
   - `0` appears 5 times.
   - `1` appears 5 times.
2. Encode as:
   - `5 1, 5 0, 5 1`

**Compressed result**: `5 1, 5 0, 5 1`

---

### **Advantages of RLE**

1. **Simple to Implement**:
   - RLE is straightforward and computationally inexpensive.
2. **Effective for Repeated Data**:
   - Highly effective for compressing files with large runs of identical data (e.g., bitmaps, black-and-white images).

---

### **Disadvantages of RLE**

1. **Inefficient for Complex Data**:
   - Files with no significant runs of repeated data may become larger after encoding.
   - Example: `ABCDEFG` would be encoded as `1A1B1C1D1E1F1G`, which is longer.
2. **Limited Compression Ratio**:
   - Works best only for specific types of data (e.g., simple graphics).

---

### **Use Cases of RLE**

1. **Bitmap Images**:
   - Frequently used in simple image formats like **BMP** and **TIFF**.
2. **Fax Machines**:
   - Encodes black-and-white fax documents.
3. **Basic Compression for Text**:
   - Useful for text files with long runs of spaces or repeated characters.

---

### **Practice Questions**

#### **Short Answer Questions**

1. What type of compression is RLE: lossy or lossless? Why? [2]
2. Apply RLE to the string `AAABBBCCCCCCDDDD` and provide the compressed result. [2]
3. Why does RLE work well for images with large areas of the same color? [1]

#### **Long Answer Questions**

1. Explain how Run-Length Encoding works with the help of an example. [4]
2. Compare the efficiency of RLE for compressing the strings `AAAAAAAAAA` and `ABCDEFG`. [3]
3. Discuss the advantages and limitations of using RLE for image compression. Include examples of when it is most effective. [4]

### Leave a Reply[Cancel reply](/igcse-o-level-cs/ch-01-data-representation/1-3-data-storage-and-compression/#respond)