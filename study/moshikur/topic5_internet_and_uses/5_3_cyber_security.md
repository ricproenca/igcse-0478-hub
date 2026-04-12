# 5.3 Cyber Security

> Source: https://moshikur.com/igcse-o-level-cs/ch-05-the-internet-and-its-uses/5-3-cyber-security/

# 5.3 Cyber Security

---

Syllabus

## **5.3 Cyber Security**

- **5.3.1** Describe cyber threats:
  - Brute-force attack
  - Data interception
  - Distributed denial of service (DDoS) attack
  - Hacking
  - Malware (virus, worm, Trojan horse, spyware, adware, ransomware)
  - Pharming
  - Phishing
  - Social engineering
- **5.3.2** Explain how to protect against these threats using:
  - Access levels
  - Anti-malware software
  - Authentication methods (e.g. passwords, biometrics, 2FA)
  - Automated updates
  - URL and communication checks
  - Firewalls
  - Privacy settings
  - Proxy servers
  - SSL (Secure Socket Layer)

---

## **What is Cyber Security?**

Cyber security refers to the measures taken to protect computer systems, networks, and data from unauthorized access, damage, or theft. It helps keep our personal and sensitive information safe when using computers and the internet.

[![Infographic titled 'Chapter 5.3 Cybersecurity' illustrating the importance of cybersecurity in protecting digital systems and data, with icons representing devices, a shield symbol, and various cyber threats.](images/topic5_internet_and_uses/5_3_cyber_security/img_001.png)](https://i0.wp.com/moshikur.com/wp-content/uploads/2025/12/image-18.png?ssl=1)

## **Why is Cyber Security Important?**

In today’s world, where we rely heavily on technology for communication, banking, shopping, and work, protecting our digital assets is crucial. Cyber threats can harm individuals, businesses, and even governments by:

1. **Stealing sensitive data**: Like passwords, bank details, or private information.
2. **Disrupting services**: Cyber attacks can shut down websites or services people rely on.
3. **Spreading malware**: Viruses can infect devices, causing them to malfunction or lose data.

---

# **Common Cyber Security Threats**

### **Brute-Force Attack**

An attacker repeatedly guesses usernames and passwords to gain access to a system.

Example: Trying every possible password until the correct one is found.

### **Data Interception**

When data being transferred between devices is “captured” by hackers.

Example: Intercepting messages or files shared over an unsecured Wi-Fi network.

### **DDoS Attack**

In distributed denial of service attack hackers overload a website or server with too many requests, making it unavailable to legitimate users.

Example: A shopping website becoming inaccessible during a sale due to a DDoS attack.

### **Hacking**

Gaining unauthorized access to computer systems.

Example: Breaking into someone’s email or social media account.

### **Malware**

Malicious software designed to harm computers or steal data. Types include:

**Viruses**: Attach to files and spread when the file is shared.

**Worms**: Spread automatically without needing a host file.

**Trojan Horses**: Disguised as useful software but harmful when installed.

**Spyware**: Secretly collects information about the user.

**Adware**: Displays unwanted ads and can slow down devices.

**Ransomware**: Locks files or systems and demands payment to unlock them.

---

> ### **Activity 1**
>
> 1. What is cyber security, and why is it important?
> 2. Define a brute-force attack and give an example.
> 3. What happens during a DDoS attack?
> 4. Name three types of malware and briefly describe each one.
> 5. How can data interception occur during communication?

## **Social Engineering**

Manipulating people into giving away confidential information.

Example: Someone pretending to be an IT technician calls you and asks for your system password. Common social engineering techniques:

**Pretexting**: Creating a false story to gain trust.

**Impersonation**: Pretending to be someone you trust.

**Tailgating**: Following someone into a restricted area without authorization.

# Phishing and Pharming

Phishing and pharming are **cyber attacks**. They try to **trick people** into giving away **personal or financial information**, such as passwords, bank details, or login credentials.

---

# What is **Phishing**?

**Phishing** is when an attacker **pretends to be someone you trust** (like your bank or school) to trick you into giving personal information.

[![Infographic about phishing in cyber security, detailing deceptive messages and data theft. It includes two illustrated steps: 1. A person receiving a deceptive email asking to verify their account, and 2. An illustration of data theft associated with the phishing attack.](images/topic5_internet_and_uses/5_3_cyber_security/img_002.png)](https://i0.wp.com/moshikur.com/wp-content/uploads/2025/12/image-9.png?ssl=1)

#### How it works:

- You get an **email or message** that looks real.
- It may say there’s a problem with your account or a prize you’ve won.
- You’re asked to **click a link** or **open an attachment**.
- The link takes you to a **fake website** that looks real.
- You type in your **password or card number**, and the attacker steals it.

#### Example:

You get an email saying:

> “Your bank account is blocked. Click here to log in and fix it.”

But it’s a **fake link**, and when you type in your password, it’s sent to the attacker.

#### How to stay safe:

- Check the **sender’s email address**.
- Don’t click on **suspicious links**.
- Look for **HTTPS** and a **padlock icon** on websites.
- Never share **personal info** through emails or unknown websites.

---

# What is **Pharming**?

**Pharming** is when an attacker redirects you from a **real website to a fake one**, even if you type the correct web address.

[![Illustration showing cyber security threats related to pharming, explaining DNS poisoning and modification of host files. The graphic depicts the attacker tampering with DNS, redirecting traffic, and users being sent to a fake website that appears real. Emphasizes the threat of hijacked traffic to steal login credentials and financial information.](images/topic5_internet_and_uses/5_3_cyber_security/img_003.png)](https://i0.wp.com/moshikur.com/wp-content/uploads/2025/12/image-10.png?ssl=1)

### How it works

You type a real address like `www.bank.com`.

But due to a **virus** or **DNS attack**, you are sent to a **fake website**.

You enter your **login details**, thinking it’s the real site.

The attacker captures your information.

### Example:

You open your browser and go to `www.mybank.com`, but without you knowing, it opens a fake version of the site.

### How to stay safe:

Use **antivirus software** and **firewalls**.

Keep your computer and browser **up to date**.

Check the **URL carefully** – even one wrong letter means it could be fake.

Use **two-factor authentication**.

---

### 🧩 Difference between Phishing and Pharming

| Feature | Phishing | Pharming |
| --- | --- | --- |
| Method | Fake emails/messages | Redirection to fake websites |
| Requires click | Yes | No – happens automatically |
| User tricked | By clicking and typing info | By thinking the site is real |

---

> ### Activity 1.2
>
> 1. What does a phishing email usually ask you to do?
> 2. How does pharming trick users?
> 3. Name one way to protect yourself from phishing.
> 4. Which attack needs you to click a link?
> 5. How can antivirus software help against pharming?

Answers:

## 🎓 Quick Revision Quiz – **Answers**

1. **What does a phishing email usually ask you to do?**  
   → Click a **link** or open an **attachment** to provide **personal information**.
2. **How does pharming trick users?**  
   → It **redirects** users from a **real website** to a **fake one** even if the correct web address is typed.
3. **Name one way to protect yourself from phishing.**  
   → Do not click on **suspicious links**, check the **sender’s email address**, and look for **HTTPS and a padlock icon** on websites.
4. **Which attack needs you to click a link?**  
   → **Phishing**
5. **How can antivirus software help against pharming?**  
   → It can **detect and remove malware** that redirects users to fake websites.

---

---

# DDoS Attack

**DDoS** stands for **Distributed Denial of Service**.

It is a **cyber attack** where many computers (often hacked or infected) try to **overload a website or server** so that it **crashes** or becomes too slow for real users.

[![Diagram explaining DDoS (Distributed Denial of Service) attack, illustrating how an attacker sends malware to create a botnet that overwhelms a server with requests, resulting in service unavailability.](images/topic5_internet_and_uses/5_3_cyber_security/img_004.png)](https://i0.wp.com/moshikur.com/wp-content/uploads/2025/12/image-12.png?ssl=1)

---

### Think of it like this:

Imagine your school’s main gate. Normally, students walk through it easily.

But one day, **hundreds of strangers crowd the gate** at the same time. Real students can’t get in. The gate is blocked.

That’s what a DDoS attack does – it **blocks access** to a service by **flooding it with fake traffic**.

---

### How does it work?

1. **Botnet is created** – The attacker infects many computers around the world with malware.
2. **All infected computers (bots)** are controlled from one central place.
3. At the same time, all these bots **send requests** to a target website/server.
4. The target **gets overwhelmed** and can’t respond to real users.

---

### Why do attackers launch DDoS attacks?

- To **take down websites** (e.g. a business or school website).
- To cause **financial loss** or **reputation damage**.
- To **distract security teams** while launching other attacks.
- For **revenge, protest, or fun** (hacktivism or trolling).

---

### How can we protect against it?

- **Firewalls** – Block unusual traffic.
- **Rate-limiting** – Limits how many requests a user can make.
- **Load balancing** – Spreads traffic across multiple servers.
- **Cloud protection services** – Detect and stop DDoS attacks quickly.

---

> ### Activity 1.3
>
> 1. What does DDoS stand for?
> 2. What is the goal of a DDoS attack?
> 3. What is a botnet?
> 4. Name one way to reduce the risk of a DDoS attack.

Answers:

## 🎓 Quick Quiz – **Answers**

1. **What does DDoS stand for?**  
   → **Distributed Denial of Service**
2. **What is the goal of a DDoS attack?**  
   → To **overload** a website or server so that it **crashes** or becomes **unavailable** to real users.
3. **What is a botnet?**  
   → A **group of infected computers** controlled by an attacker and used to send huge amounts of traffic in a DDoS attack.
4. **Name one way to reduce the risk of a DDoS attack.**  
   → Use a **firewall**, **rate-limiting**, **load balancer**, or **cloud-based DDoS protection**.

---

---

## **How Cyber Threats Impact Systems**

1. **Data Loss**
   - Sensitive data can be stolen, deleted, or corrupted.
   - Example: A ransomware attack locks your files, and you can’t access them without paying.
2. **Financial Loss**
   - Cyber criminals may steal money directly or trick victims into transferring funds.
   - Example: Phishing emails tricking users into sending money to fake accounts.
3. **Reputation Damage**
   - Businesses lose customer trust when a data breach occurs.
   - Example: A company’s customer database is hacked, exposing client information.
4. **System Disruption**
   - Attacks like DDoS can make websites or services unavailable.
   - Example: An online store is taken offline, causing a loss of sales.

---

**Key Steps Attackers Use in Cyber Threats**

1. **Research**: Attackers learn about their target (e.g., employees of a company or the type of system in use).
2. **Delivery**: Sending phishing emails or malware to the target.
3. **Exploitation**: Using vulnerabilities in the system to gain access.
4. **Execution**: Stealing data, disrupting services, or spreading malware.

---

> ### **Activity 2**
>
> 1. What is phishing, and how does it work?
> 2. Give an example of social engineering and explain how it manipulates a person.
> 3. List two impacts of cyber threats on individuals or organizations.
> 4. Describe the steps attackers use in executing cyber threats.
> 5. What is the difference between phishing and social engineering?

# 5.3.2

# **How to Protect Against Cyber Threats**

[![Infographic outlining methods to protect against cyber security threats, including access levels, anti-malware, authentication, software updates, and firewalls, with key principles of layered defense, user awareness, and proactive protection.](images/topic5_internet_and_uses/5_3_cyber_security/img_005.png)](https://i0.wp.com/moshikur.com/wp-content/uploads/2025/12/image-13.png?ssl=1)

Cyber security measures help protect systems, data, and individuals from attacks. Below are various solutions to combat cyber threats:

---

### **1. Access Levels**

Restricting access to sensitive information based on a user’s role.

- Example: Only a manager can access confidential employee data, while regular employees cannot.

Minimizes the risk of unauthorized access to sensitive data.

### **2. Anti-Malware Software**

Programs designed to detect and remove malware from computers and networks.

- Examples:
  - **Antivirus**: Protects against viruses.
  - **Anti-spyware**: Blocks spyware.

Prevents malware from infecting systems or stealing data.

### **3. Authentication**

Verifying the identity of users before granting access to systems or data.

- **Passwords**
- **Two-Factor Authentication (2FA)**
- **Biometrics**

Prevents unauthorized users from accessing sensitive systems.

---

### **4. Automating Software Updates**

Ensuring that operating systems, apps, and software are updated automatically to fix known security issues.

Example: Your computer automatically installs the latest security patches for Windows.

Reduces vulnerabilities that attackers could exploit.

### **5. Checking Communication Links**

Being cautious about clicking links or downloading files from unknown sources.

Steps to take:

- Check the spelling of URLs (e.g., avoid “amaz0n.com” instead of “amazon.com”).
- Avoid downloading attachments from unknown emails.

Protects against phishing attacks and malware downloads.

### **6. Firewalls**

Software or hardware that monitors and controls incoming and outgoing network traffic.

Example: A firewall can block access to unauthorized websites or prevent hackers from connecting to your system.

Acts as the first line of defense against cyber threats.

---

### **7. Privacy Settings**

Configuring account settings to control what information is shared online.

- Example: Limiting who can view your social media posts.
- **Why it helps**: Reduces the risk of social engineering and data theft.

### **8. Proxy Servers**

Servers that act as intermediaries between users and the Internet.

- Example: Schools use proxy servers to block access to inappropriate content.
- **Why it helps**: Enhances privacy and filters harmful content.

### **9. Secure Socket Layer (SSL)**

A security protocol that encrypts data sent between your browser and a website.

- Example: Look for the padlock symbol and “https” in a website’s URL.
- **Why it helps**: Protects sensitive information, like credit card details, during online transactions.

---

**How to Stay Safe Online**

1. **Use Strong Passwords**: Create passwords with a mix of letters, numbers, and symbols.
2. **Enable Two-Factor Authentication (2FA)**: Add an extra layer of security to your accounts.
3. **Be Cautious with Links**: Avoid clicking suspicious links in emails or messages.
4. **Install Updates**: Regularly update your operating system and apps.
5. **Backup Data**: Keep copies of important files in case of a ransomware attack.

---

> ### **Activity 3**
>
> 1. What is two-factor authentication, and why is it important?
> 2. How does a firewall protect a system from cyber threats?
> 3. Give an example of how automating software updates can improve security.
> 4. Explain the role of SSL in securing online transactions.
> 5. List three tips to stay safe online and explain why they are effective.

---

# 5.1.6 Cookies

**Cookies** are **small files** saved on your computer by a **website**.

They **remember things** about you – like your **preferences**, **login status**, or **items in your shopping cart** – so that the website works better for you.

[![Infographic illustrating the concept of cookies on the web, depicting the process of how a server sends a cookie to a client and how the client stores and sends it back in subsequent requests, with emphasis on tracking and personalization.](images/topic5_internet_and_uses/5_3_cyber_security/img_006.png)](https://i0.wp.com/moshikur.com/wp-content/uploads/2025/12/image-14.png?ssl=1)

---

### Imagine This:

You visit a website, and it says:

> “Hello again! Would you like to continue shopping where you left off?”

It can do that because it **stored a cookie** on your device the last time you visited.

---

### What Information Can a Cookie Store?

Your **login session** (so you stay logged in)

Your **shopping cart** items

Your **language or theme preferences**

Your **visit history** or page views

Cookies **don’t usually store personal data** unless you enter it yourself.

---

# Types of Cookies

# 1. **Session Cookies**

Stored **temporarily**

Get **deleted** when you close your browser

Used for things like **shopping carts**

[![Infographic explaining session cookies: it shows tracking activity during a session, including how a session ID is generated, a session cookie is sent by the server, and how the cookie is deleted after the browser is closed.](images/topic5_internet_and_uses/5_3_cyber_security/img_007.png)](https://i0.wp.com/moshikur.com/wp-content/uploads/2025/12/image-16.png?ssl=1)

> A **session cookie** is stored temporarily while the browser is open and is deleted when the browser is closed.

**Characteristics:**

- **Lifetime:**
  - Exists **only for the current browsing session**.
  - Once the user **closes the browser**, session cookies are deleted automatically.
- **Storage:**
  - Held in memory by the browser.
- **Use cases in your tutorial/website:**
  - Keeping items in a shopping cart **for the current visit**.
  - Remembering which page of a multi-step form the user is on.
  - Keeping a user logged in **only until they close the browser**.

**Example scenario:**

User visits your site and adds items to their cart.

Your site stores a **session cookie** with a code for that cart.

When the user goes to another page (e.g. “Checkout”), the cookie is sent and the server knows *which* cart belongs to this user.

When the user closes the browser, the cart is automatically forgotten because the session cookie disappears.

---

# 2. **Persistent Cookies**

Stay on your computer **even after you close the browser**

Can **remember login details** or site preferences for your next visit

[![Diagram explaining persistent cookies, illustrating user activity tracking during a session and after it ends, with notes on expiry or manual deletion.](images/topic5_internet_and_uses/5_3_cyber_security/img_008.png)](https://i0.wp.com/moshikur.com/wp-content/uploads/2025/12/image-17.png?ssl=1)

> A **persistent cookie** stays on the user’s device even after the browser is closed, until it reaches its expiry date or is deleted.

**Characteristics:**

- **Lifetime:**
  - Has an **expiry date** set by the website.
  - Stays on the user’s device across **multiple sessions** (days, weeks, or months) until it expires or the user deletes it.
- **Storage:**
  - Saved in a cookie file or cookie storage on the device.
- **Use cases in your tutorial/website:**
  - “Remember me” logins (storing a token so users don’t have to log in every time).
  - Saving **personal details** like preferred language, theme (dark/light mode), or layout.
  - **Tracking user preferences** for the next visit (e.g. which sections they expanded, their favourite topics).

**Example scenario:**

User logs into your site and ticks **“Remember me on this device”**.

Your site stores a **persistent cookie** that identifies this user’s account.

Next week, the user comes back. The browser sends the persistent cookie.

Your site reads it and automatically logs the user in, because it recognises the cookie.

This matches the syllabus use: “saving personal details”, “tracking user preferences”, “storing login details”.

---

## How cookies work with a website

You can use this sequence diagram description directly in your web notes:

1. **User enters a URL**
   - Browser sends a request to the web server.
2. **Server responds with a page**
   - Inside the response, the server **may include cookies** for the browser to store (for tracking preferences, login state, etc).
3. **Browser stores the cookies**
   - If it’s a **session cookie**, it keeps it until the browser closes.
   - If it’s a **persistent cookie**, it stores it with an expiry date on the device.
4. **User visits another page on the same site**
   - Browser **automatically includes relevant cookies** with the request to the server.
   - The server reads the cookies and recognises the user or their settings.
5. **Later session (only for persistent cookies)**
   - Even after closing and reopening the browser, **persistent cookies** are still there (unless they expired or were deleted).
   - The website can still recognise the user.

---

## Session vs Persistent Cookies

You can copy this comparison table into your website:

| Feature | Session cookie | Persistent cookie |
| --- | --- | --- |
| Lifetime | Until browser is closed | Until expiry date or manual deletion |
| Stored where | In browser memory for the current session | On the device (browser’s cookie storage) |
| Used for | Shopping cart for current visit, temporary login | Remember me login, preferences, saved personal details |
| Survives browser close? | ❌ No | ✅ Yes |
| Mentioned in syllabus as | Session cookie | Persistent cookie used to save details and preferences |

---

### Are Cookies Dangerous?

- Cookies **cannot run programs or viruses**
- But they can be used to **track your activity**
- Some users clear cookies or **block third-party cookies** for **privacy reasons**

---

### Why Are Cookies Useful?

- Save time (no need to log in again)
- Improve user experience (e.g., keep dark mode on)
- Help websites remember your choices

---

> ### Quick Quiz
>
> 1. What is a cookie?
> 2. What is the difference between session and persistent cookies?
> 3. Name one use of cookies on a website.
> 4. Do cookies store viruses?
> 5. Why might someone delete cookies?

Solution:

Here are the **answers** to the quiz on **Cookies**:

---

### 🎓 Quick Quiz – **Answers**

1. **What is a cookie?**  
   → A cookie is a **small file** saved by a website on your computer to **store information** like preferences or login details.
2. **What is the difference between session and persistent cookies?**  
   → **Session cookies** are **temporary** and deleted when the browser is closed.  
   → **Persistent cookies** stay on the device even after closing the browser.
3. **Name one use of cookies on a website.**  
   → To **keep you logged in**, remember **shopping cart items**, or save your **language preference**.
4. **Do cookies store viruses?**  
   → **No**, cookies **cannot run programs or store viruses**.
5. **Why might someone delete cookies?**  
   → To **protect their privacy**, clear **tracking data**, or fix website issues.

---

---