# 2.3 Encryption

> Source: https://moshikur.com/igcse-o-level-cs/ch-02-data-transmission/2-3-encryption/

# 2.3 Encryption

---

Syllabus

**2.3.1 Purpose of Encryption**  
2.3.1.1 Ensuring data security during transmission  
  
**2.3.2 Types of Encryption**  
2.3.2.1 Symmetric Encryption  
2.3.2.2 Asymmetric Encryption

# **2.3 Encryption**

[![Diagram illustrating the process of encryption and decryption, showing interactions between plain text, cipher text, and the use of a key.](images/topic2_data_transmission/2_3_encryption/img_001.png)](https://i0.wp.com/moshikur.com/wp-content/uploads/2026/04/image-9.png?ssl=1)

Encryption is the process of converting data into a coded format so that only authorized users can access and understand it. Encryption ensures that data remains secure during transmission, protecting it from unauthorized access or tampering.

[Take the quiz](https://moshikur.com/quizzes/chapter-2-3-encryption-blooms-taxonomy/)

---

## **2.3.1 Purpose of Encryption**

### **2.3.1.1 Ensuring Data Security During Transmission**

When data is sent over a network, it is vulnerable to interception by unauthorized parties. Encryption protects the confidentiality and integrity of data by encoding it into an unreadable format. Only the intended recipient, with the correct decryption key, can decode and access the data.

**How It Works**:

1. The sender uses an encryption key to transform the original message (plaintext) into a scrambled format (ciphertext).
2. The receiver uses a decryption key to convert the ciphertext back into readable plaintext.

**Why Encryption is Important**:

**Data Confidentiality**: Prevents unauthorized users from reading the data.

**Data Integrity**: Ensures that the data hasn’t been altered during transmission.

**Protection Against Cyber Threats**: Shields sensitive information like passwords, credit card numbers, and personal messages.

**Example**: When you shop online, your payment information is encrypted to ensure that only the e-commerce platform and your bank can process it.

---

## **2.3.2 Types of Encryption**

There are two main types of encryption, each with different methods for securing data: **Symmetric Encryption** and **Asymmetric Encryption**.

---

### **2.3.2.1 Symmetric Encryption**

[![Diagram illustrating the process of symmetric encryption, showing plain text being encrypted to cipher text using a single key (Alice's key), and then decrypted back to plain text.](images/topic2_data_transmission/2_3_encryption/img_002.png)](https://i0.wp.com/moshikur.com/wp-content/uploads/2026/04/image-10.png?ssl=1)

In symmetric encryption, the same key is used to encrypt and decrypt the data.

**How It Works**:

1. The sender uses a shared secret key to encrypt the data.
2. The receiver uses the same key to decrypt the data.

---

**Advantages**:

- Fast and efficient for encrypting large amounts of data.
- Simple to implement.

**Disadvantages**:

Key Distribution Problem: Both the sender and receiver must securely share the key. If the key is intercepted, the data becomes vulnerable.

**Example**: AES (Advanced Encryption Standard) is a widely used symmetric encryption method, commonly applied in file encryption and secure messaging.

---

### **2.3.2.2 Asymmetric Encryption**

[![An infographic illustrating asymmetric encryption between Alice and Bob, detailing the steps of secure message exchange, including key pairs, encryption, cipher text, decryption, and plain text.](images/topic2_data_transmission/2_3_encryption/img_003.png)](https://i0.wp.com/moshikur.com/wp-content/uploads/2026/04/image-12.png?ssl=1)

In asymmetric encryption, two keys are used: a **public key** and a **private key**. The public key is shared openly, while the private key is kept secret.

**How It Works**:

1. The sender encrypts the data using the receiver’s public key.
2. The receiver decrypts the data using their private key.

---

**Advantages**:

- No need to share a single secret key, reducing the risk of interception.
- Ideal for secure communication over public networks.

**Disadvantages**:

- Slower compared to symmetric encryption.
- Computationally intensive for encrypting large datasets.

**Example**: RSA (Rivest-Shamir-Adleman) is a popular asymmetric encryption method used in secure email and website connections (HTTPS).

---

### **Summary**

| Encryption Type | Key Used | Advantages | Disadvantages |
| --- | --- | --- | --- |
| Symmetric Encryption | One key for encryption and decryption | Fast and efficient for large data | Key distribution is challenging. |
| Asymmetric Encryption | Public and private keys | No need to share secret keys | Slower and resource-intensive. |

---

### **Activity 1**

1. What is the purpose of encryption? [2]
2. How does symmetric encryption work? [2]
3. What is the key difference between symmetric and asymmetric encryption? [2]
4. Explain how encryption ensures data security during transmission. Include examples of where encryption is commonly used. [6]
5. Compare symmetric and asymmetric encryption. Discuss their strengths, weaknesses, and appropriate use cases. [6]

---

## **2.3.1 Purpose of Encryption Revisited**

#### Practical Applications of Encryption

**Online Transactions**: When shopping online or making bank transfers, encryption ensures that sensitive information, like credit card details, cannot be intercepted by unauthorized parties.

**Secure Communication**: Messaging apps (e.g., WhatsApp, Signal) use encryption to ensure that only the sender and receiver can read the messages.

**Data Storage**: Encrypting files and databases prevents unauthorized access to sensitive information stored on devices or in the cloud.

**Government and Military Data**: Highly classified data is encrypted to prevent espionage or breaches.

---

### **Real-World Use Cases of Encryption**

#### Symmetric Encryption Use Cases

**File Encryption**: Encrypting a file on your computer so only users with the password (key) can open it.

**Network Communication**: Used in Wi-Fi protocols (e.g., WPA2) to secure local networks.

#### Asymmetric Encryption Use Cases

**Secure Websites (HTTPS)**: Websites use asymmetric encryption to create a secure connection between the browser and the server.

**Email Encryption**: Tools like PGP (Pretty Good Privacy) encrypt email content so only the intended recipient can read it.

**Digital Signatures**: Ensures that a document or message is authentic and hasn’t been tampered with.

---

### **Advantages of Encryption**

**Confidentiality**: Prevents unauthorized access to sensitive data.

**Data Integrity**: Ensures that transmitted data hasn’t been altered during transmission.

**Authentication**: Confirms the sender’s identity in online communication.

**Compliance**: Many industries require encryption to meet legal and regulatory standards.

---

### **Disadvantages of Encryption**

**Performance Impact**: Encrypting and decrypting data requires processing power, which can slow down systems, especially with asymmetric encryption.

**Key Management Challenges**: Losing the decryption key means permanent loss of access to encrypted data.

**Complexity**: Implementing and managing encryption, especially for large-scale systems, can be technically challenging.

---

### **Summary**

Encryption is essential for securing communication, protecting sensitive data, and ensuring privacy in the digital world. Both symmetric and asymmetric encryption play a role, with their use depending on the scenario:

- **Symmetric Encryption** is best for fast, large-scale data encryption where the key can be shared securely.
- **Asymmetric Encryption** is ideal for secure communication over public networks, like web browsing or email.

---

> ### **Activity 2**
>
> 1. Name two practical applications of symmetric encryption. [2]
> 2. Why is asymmetric encryption commonly used in HTTPS? [2]
> 3. List one advantage and one disadvantage of encryption. [2]
> 4. Describe how encryption is used to secure online transactions. Explain the role of encryption in protecting sensitive information like payment details. [6]
> 5. Discuss the advantages and disadvantages of encryption. Provide examples of situations where these factors are significant. [6]