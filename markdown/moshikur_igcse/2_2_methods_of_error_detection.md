# 2.2 Methods of Error Detection

> Source: https://moshikur.com/igcse-o-level-cs/ch-02-data-transmission/2-2-methods-of-error-detection/

# 2.2 Methods of Error Detection

[![Four green icons representing data integrity techniques: Parity Check, Checksum, Check Digit, and Automatic Repeat Request (ARQ).](images/topic2_data_transmission/2_2_methods_of_error_detection/img_001.jpg)](https://i0.wp.com/moshikur.com/wp-content/uploads/2026/04/bc183ff5-bfec-44e4-875e-057bf1e67f87.jpg?ssl=1)

---

Syllabus

- **2.2.1 Need for Error Detection**
  - 2.2.1.1 Reasons for checking data after transmission
- **2.2.2 Error Detection Techniques**
  - 2.2.2.1 Parity Check (odd and even)
  - 2.2.2.2 Checksum
  - 2.2.2.3 Echo Check
  - 2.2.2.4 Parity Byte/Block Check
- **2.2.3 Check Digit**
  - 2.2.3.1 Use of check digits in error detection
  - 2.2.3.2 Applications (e.g., ISBN numbers, bar codes)
- **2.2.4 Automatic Repeat Request (ARQ)**
  - 2.2.4.1 Positive/Negative Acknowledgements
  - 2.2.4.2 Timeout Protocols

---

# **2.2.1 Need for Error Detection**

Data transmission involves sending information from one device to another over a network. During this process, various factors like noise, interference, or hardware failures can cause errors. These errors may lead to corrupted, incomplete, or incorrect data being received. To ensure reliable communication, error detection techniques are essential.

---

### **Reasons for Checking Data After Transmission**

#### **1. Data Accuracy**

The primary goal of error detection is to ensure the accuracy of transmitted data. When data is sent, the receiver must get the exact same information without any modifications. If errors go undetected, it could lead to serious issues.

**Example**: In a bank transfer, incorrect data could cause money to be sent to the wrong account or an incorrect amount to be processed.

#### **2. Preventing Miscommunication**

Errors in transmitted data can cause devices or systems to misinterpret instructions, leading to unintended outcomes. Ensuring error-free data transmission helps avoid such miscommunication.

**Example**: A corrupted command sent to a robotic arm in a factory might cause it to malfunction, potentially damaging products or the machinery.

#### **3. Network Reliability**

Reliable communication is critical for maintaining trust in a network or system. If users frequently experience errors without detection or correction, it undermines confidence in the system’s performance.

**Example**: A messaging app that frequently delivers garbled or incomplete messages will lose users’ trust.

#### **4. Reducing Costs and Saving Time**

Early detection of errors prevents further complications, reducing the time and resources spent on troubleshooting and correcting issues. This is especially important in large systems with multiple components.

**Example**: Detecting errors in a transmitted file before it’s processed saves time compared to identifying and fixing problems later during its use.

#### **5. Supporting Automated Systems**

Modern systems rely heavily on automation. Error detection ensures these systems operate smoothly without requiring constant human intervention.

**Example**: Automated online payments depend on accurate data transmission to avoid incorrect billing or transaction failures.

---

### **Summary of Why Error Detection is Needed**

**Data Integrity**: Ensures the receiver gets the correct and unaltered data.

**Avoiding Miscommunication**: Prevents wrong actions caused by corrupted data.

**Reliability**: Builds trust in communication networks.

**Efficiency**: Saves time and resources by identifying problems early.

**Automation**: Keeps automated systems running smoothly without frequent interruptions.

Error detection is the foundation of reliable and efficient data communication. Without it, our networks and systems would fail to function effectively.

> ### **Task 2.2.1**
>
> 1. Why is error detection important in data transmission? [2]
> 2. Name two reasons for checking data after transmission. [2]
> 3. How does error detection improve network reliability? [2]
> 4. Explain why error detection is necessary for modern communication systems. Include examples of what could go wrong without it. [6]
> 5. Describe five reasons why data should be checked for errors after transmission. Provide examples to support your answer. [6]

# **2.2.2 Error Detection Techniques**

Error detection techniques are methods used to identify errors in transmitted data. These techniques ensure that corrupted or incomplete data is flagged, so corrective actions can be taken.

---

### **2.2.2.1 Parity Check (Odd and Even)**

#### **How It Works**

- A parity check adds an extra bit (called the **parity bit**) to the data being sent. This bit is used to make the total number of 1s in the data either even (for even parity) or odd (for odd parity).
- The receiver recalculates the parity of the received data. If the parity doesn’t match, an error is detected.

#### **Examples**

- **Even Parity**: Data `1011` has three 1s (odd). To make it even, a parity bit of `1` is added, making the data `10111`.
- **Odd Parity**: Data `1100` has two 1s (even). To make it odd, a parity bit of `1` is added, making the data `11001`.

#### **Strengths**

- Simple to implement.
- Detects single-bit errors.

#### **Limitations**

- Cannot detect multiple-bit errors (e.g., if two bits flip, parity remains the same).

---

### **2.2.2.2 Checksum**

#### **How It Works**

- A **checksum** is a value calculated from the data being sent, often by adding up the binary values of all the data bytes.
- The checksum is sent along with the data.
- The receiver recalculates the checksum of the received data and compares it with the sent checksum. If they don’t match, an error is detected.

#### **Examples**

- Data: `1011`, `1100`, and `1001`. The checksum is calculated by adding these binary numbers. If the result is `11110`, the checksum sent would be the least significant bits (`1110`).

#### **Strengths**

- Works well for detecting errors in large data blocks.

#### **Limitations**

- Cannot identify the exact location of the error.

---

### **Echo Check**

#### **How It Works**

- The receiver sends the received data back to the sender for verification.
- The sender compares the returned data with the original data. If they don’t match, an error is detected.

#### **Examples**

- Sender transmits `101010`. Receiver echoes back `101010`. If the sender receives `101011`, it detects an error.

#### **Strengths**

- Easy to implement for small data transmissions.

#### **Limitations**

- Time-consuming because of the need to send data back and forth.
- Errors during the echo process itself may cause confusion.

---

### **2.2.2.4 Parity Byte/Block Check**

#### **How It Works**

- A **parity byte/block check** uses parity checking on entire blocks of data (e.g., rows and columns).
- A parity bit is calculated for each row and an additional parity bit (or byte) is calculated for all columns.

#### **Example**

Data Block:

| Bit 1 | Bit 2 | Bit 3 | Parity Bit (Row) |
| --- | --- | --- | --- |
| 1 | 0 | 1 | 0 |
| 0 | 1 | 1 | 1 |
| Parity Byte (Column): | 1 | 1 | 0 |

#### **Strengths**

- Can detect multiple errors within a block of data.

#### **Limitations**

- More complex to implement compared to single-bit parity checks.

> ### **Task 2.2.2**
>
> 1. What is the purpose of a parity check in error detection? [2]
> 2. How does a checksum detect errors? [2]
> 3. Why is an echo check less commonly used in modern systems? [2]
> 4. Explain how a parity check works and describe its strengths and limitations. Provide examples for odd and even parity. [6]
> 5. Compare the parity byte/block check with the checksum technique. Discuss their use cases, advantages, and disadvantages. [6]

### Check Digit

#### **What is a Check Digit?**

A **check digit** is an additional digit added to the end of a number or code to verify its accuracy. It’s calculated using a specific formula based on the other digits in the code. When the data is received, the check digit is recalculated to verify the integrity of the data.

---

#### **Use of Check Digits in Error Detection**

The sender calculates the check digit using a formula (e.g., modulo 10).

The receiver recalculates the check digit and compares it to the one sent.

If the two check digits match, the data is considered error-free; otherwise, an error is detected.

---

#### **Applications of Check Digits**

Check digits are widely used in systems where numerical data is transmitted or stored. Common applications include:

**ISBN Numbers**: Books use a 13-digit International Standard Book Number, where the last digit is a check digit to ensure the number is valid.

**Bar Codes**: Retail systems use check digits to ensure the accuracy of scanned product codes.

**Credit Card Numbers**: Check digits help verify the validity of card numbers during transactions.

---

### **Automatic Repeat Request (ARQ)**

#### **What is ARQ?**

**Automatic Repeat Request (ARQ)** is a protocol that ensures data is correctly received by automatically resending data if errors are detected.

---

#### **Positive/Negative Acknowledgements**

**Positive Acknowledgement**: If the receiver detects no errors, it sends an **ACK** (Acknowledgement) back to the sender, confirming the data was received successfully.

**Negative Acknowledgement**: If the receiver detects an error, it sends a **NAK** (Negative Acknowledgement) back to the sender, requesting a retransmission of the data.

---

#### **Timeout Protocols**

ARQ also uses a timeout mechanism:

- After sending data, the sender waits for an **ACK** or **NAK** from the receiver.
- If no response is received within the timeout period, the sender assumes the data was lost and retransmits it.

---

### **Advantages and Disadvantages of ARQ**

#### **Advantages**

1. Ensures reliable communication by resending erroneous or lost data.
2. Requires no manual intervention, making it efficient for automated systems.

#### **Disadvantages**

1. Increases data transmission time due to retransmissions.
2. Not suitable for real-time applications where delays are critical (e.g., live video calls).

Both techniques are essential for ensuring reliable communication and data accuracy in different scenarios.

> ### **Task 2.2.3**
>
> 1. What is a check digit, and how is it used in error detection? [2]
> 2. Give two examples where check digits are commonly used. [2]
> 3. What is the difference between an ACK and a NAK in ARQ? [2]
> 4. Why does ARQ use a timeout protocol? [2]
> 5. Explain the role of check digits in error detection. Include an example to show how a check digit is calculated and used to detect errors. [6]
> 6. Describe how ARQ works. Include the concepts of positive/negative acknowledgements and timeout protocols, and discuss the advantages and disadvantages of this method. [6]

---