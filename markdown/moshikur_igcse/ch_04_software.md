# CH 04 Software

> Source: https://moshikur.com/igcse-o-level-cs/ch-04-software/

# Ch 04 Software

---

# [4.1](https://moshikur.com/igcse-o-level-cs/ch-04-software/4-1-types-of-software-and-interrupts/)

---

## [Learn Software Types & Interrupts](https://moshikur.com/igcse-o-level-cs/ch-04-software/4-1-types-of-software-and-interrupts/)

*[Explore the differences between system and application software, the role of operating systems, and how interrupts work in computer systems.](https://moshikur.com/igcse-o-level-cs/ch-04-software/4-1-types-of-software-and-interrupts/)*

# [4.2](https://moshikur.com/igcse-o-level-cs/ch-04-software/4-2-types-of-programming-language-translators-and-integrated-development-environments-ides/)

---

## [Understand Programming Languages & IDEs](https://moshikur.com/igcse-o-level-cs/ch-04-software/4-2-types-of-programming-language-translators-and-integrated-development-environments-ides/)

[Compare high- and low-level languages, understand translators like compilers and interpreters, and learn how IDEs support coding.](https://moshikur.com/igcse-o-level-cs/ch-04-software/4-2-types-of-programming-language-translators-and-integrated-development-environments-ides/)

---

# Exam Style Questions

### **4.1 Types of Software and Interrupts**

**Question 1: System Software vs. Application Software** *(6 marks)*

A school installs a new set of software on its computers, including:

- An **operating system**
- **Word processing software**
- **Antivirus software**
- **A video editing program**
- **A disk cleanup utility**

(a) Identify two pieces of **system software** and two pieces of **application software** from the list above. *(4 marks)*  
(b) Explain why system software is essential for application software to function properly. *(2 marks)*

**Hint:** System software manages the computer’s hardware and operations, while application software helps users perform specific tasks. Think about which software runs in the background and which ones users interact with directly.

---

**Question 2: Functions of an Operating System** *(5 marks)*

An operating system performs many key tasks. Explain how an operating system:  
(a) Manages memory when multiple programs are open at the same time. *(2 marks)*  
(b) Handles file management when saving, retrieving, and deleting files. *(2 marks)*  
(c) Uses interrupts to respond when a user presses a key on the keyboard. *(1 mark)*

**Hint:** Think about how the OS ensures that programs do not interfere with each other, how it organizes files, and how it prioritizes user input.

---

**Question 3: GUI vs CLI** *(4 marks)*

A new operating system is being developed, and designers are debating whether to include a **Graphical User Interface (GUI)** or a **Command Line Interface (CLI)**.

(a) Describe one advantage and one disadvantage of using a **GUI**. *(2 marks)*  
(b) Describe one advantage and one disadvantage of using a **CLI**. *(2 marks)*

**Hint:** GUIs are visually intuitive but require more system resources. CLIs are efficient for experienced users but have a steep learning curve.

---

### **Question 4: Utility Software** *(4 marks)*

A company notices that their computers are running slowly and some files have been accidentally deleted.  
(a) Identify two types of utility software that could help resolve these issues. *(2 marks)*  
(b) Explain how each type of utility software improves the system’s performance. *(2 marks)*

**Hint:** Utility software helps maintain system performance. Consider tools for file recovery and optimizing system speed.

---

### **Question 5: Real-Life Interrupt Handling** *(6 marks)*

A user is watching a video on a computer when suddenly an **email notification** appears, and the video pauses.  
(a) What type of interrupt is triggered by the email notification? *(1 mark)*  
(b) Describe how the operating system handles this interrupt while ensuring the video can continue playing afterward. *(3 marks)*  
(c) Explain why interrupts are more efficient than polling in managing system events. *(2 marks)*

**Hint:** Think about how the CPU prioritizes tasks, processes the interrupt, and returns to the original task.

---

### **4.1.3 Running Applications**

**Question 6: How Software Works with Hardware** *(6 marks)*

A **photo editing program** is used to edit high-resolution images on a computer. Describe how each of the following contributes to running this application:  
(a) The operating system *(2 marks)*  
(b) The hardware (CPU and RAM) *(2 marks)*  
(c) The firmware *(2 marks)*

**Hint:** The OS allocates resources, the hardware processes data, and firmware helps start the system and control hardware components.

---

**Question 7: Role of the Bootloader** *(4 marks)*

(a) What is the function of the bootloader when a computer is powered on? *(2 marks)*  
(b) Explain what would happen if the bootloader failed to load properly. *(2 marks)*

**Hint:** The bootloader helps load the operating system. Without it, the computer cannot start.

---

### **4.1.4 Interrupts**

**Question 8: How Interrupts Work** *(5 marks)*

An interrupt is a signal sent to the processor to indicate that an event requires immediate attention.

(a) Explain the purpose of interrupts in a computer system. *(2 marks)*  
(b) Describe the steps the operating system takes when an interrupt occurs. *(3 marks)*

**Hint:** Interrupts allow the OS to handle urgent tasks first. Think about how the CPU pauses its current task, processes the interrupt, and then resumes work.

---

**Question 9: Hardware vs Software Interrupts** *(6 marks)*

(a) Define the difference between **hardware interrupts** and **software interrupts**. *(2 marks)*  
(b) Give one example of a **hardware interrupt** and one example of a **software interrupt**. *(2 marks)*  
(c) Explain why handling software interrupts efficiently is important for system stability. *(2 marks)*

**Hint:** Hardware interrupts come from physical devices (e.g., keyboard, mouse), while software interrupts occur from programs or errors (e.g., division by zero).

---

### **4.2.1 High-Level and Low-Level Languages**

**Question 10: Choosing the Right Language** *(5 marks)*

A company is developing software for a **self-driving car**. The software needs to be **fast and directly control the hardware**.

(a) Would a high-level or low-level language be more suitable? *(1 mark)*  
(b) Explain why this type of language is best for the project. *(2 marks)*  
(c) What challenges might a programmer face when writing code in this language? *(2 marks)*

**Hint:** Think about speed, hardware control, and ease of programming.

---

### **Question 11: Selecting a Language for Different Projects** *(6 marks)*

For each of the following projects, decide whether a high-level or low-level language is best suited. Explain your choice.

(a) A **website** that allows users to book flights online. *(2 marks)*  
(b) A **real-time operating system** for a **medical heart monitor** that must respond instantly to changes. *(2 marks)*  
(c) A **computer game** that requires high-speed processing and complex graphics. *(2 marks)*

**Hint:** Consider ease of development, execution speed, and hardware control.

---

### **4.2.2 Assembly Language**

**Question 12: Understanding Assembly Language** *(5 marks)*

(a) Why do programmers use mnemonics in assembly language instead of writing programs in machine code? *(2 marks)*  
(b) What is the role of an **assembler** in translating assembly language? *(3 marks)*

**Hint:** Mnemonics make code readable, while assemblers convert it into machine code for execution.

---

### **Question 13: Why Use Assembly Language?** *(5 marks)*

A scientist is designing a small **microcontroller** to control a **temperature sensor** in a laboratory.  
(a) Explain why they might choose assembly language instead of a high-level language. *(3 marks)*  
(b) Describe one disadvantage of using assembly language for this project. *(2 marks)*

**Hint:** Assembly provides direct hardware control and efficiency but can be difficult to program.

---

### **Question 14: Mnemonics vs. Machine Code** *(4 marks)*

Below is an assembly language instruction:

```
MOV AL, 5
ADD AL, 3
```

(a) What is the purpose of using mnemonics like `MOV` and `ADD` instead of writing in binary? *(2 marks)*

**Hint:** Mnemonics make code readable, while machine code is what the CPU actually executes.

---

### **4.2.3 Compilers and Interpreters**

**Question 15: Compiler vs. Interpreter** *(6 marks)*

A student is writing a **Python program** and notices that the program runs line-by-line instead of all at once.

(a) Is Python using a compiler or an interpreter? *(1 mark)*  
(b) Explain how a compiler and an interpreter differ in translating high-level language. *(3 marks)*  
(c) Why might an interpreter be more useful than a compiler during program development? *(2 marks)*

**Hint:** Interpreters translate and run code line-by-line, while compilers process everything before execution.

---

### **Question 16: Compilation Process** *(5 marks)*

A software developer writes a program in **C++** and uses a **compiler** to translate the code.  
(a) Describe the steps that occur from writing the code to executing the compiled program. *(3 marks)*  
(b) Explain one advantage and one disadvantage of using a compiler instead of an interpreter. *(2 marks)*

**Hint:** Think about how the compiler processes all code at once before execution.

---

### **Question 17: Debugging with Interpreters** *(5 marks)*

A student is writing a Python program and notices that the **program stops running immediately after an error appears**.  
(a) What type of translator is being used? *(1 mark)*  
(b) Why is this behavior helpful for debugging? *(2 marks)*  
(c) Give one reason why an interpreter may be **slower** than a compiler. *(2 marks)*

**Hint:** Interpreters translate and execute line-by-line, making errors easier to fix but slowing execution.

---

### **4.2.4 Advantages and Disadvantages of Translators**

**Question 18: Translator Selection for a New Programming Language** *(6 marks)*

A team of developers is creating a **new programming language**. They are deciding whether to build a **compiler** or an **interpreter** for it.

(a) Explain one situation where using a **compiler** would be beneficial. *(2 marks)*  
(b) Explain one situation where using an **interpreter** would be beneficial. *(2 marks)*  
(c) What challenges might developers face if they decide to create both a compiler and an interpreter for their new language? *(2 marks)*

**Hint:** Consider execution speed, error detection, and software development time.

---

### **4.2.5 Integrated Development Environments (IDEs)**

**Question 19: Features of an IDE** *(5 marks)*

A programmer is using an **Integrated Development Environment (IDE)** to develop a new software application.  
(a) List three features of an IDE and explain how each helps the programmer. *(3 marks)*  
(b) Why do IDEs include both a compiler and an interpreter for some programming languages? *(2 marks)*

**Hint:** Think about features like debugging tools, auto-completion, and syntax highlighting.

---

### **Question 20: The Importance of Debugging Tools in an IDE** *(4 marks)*

A software company is training new programmers and wants to emphasize the importance of debugging tools.  
(a) Explain how a **debugger** in an IDE helps find and fix errors in code. *(2 marks)*  
(b) Why might a programmer use **breakpoints** while debugging? *(2 marks)*

**Hint:** Debugging tools help identify errors in specific lines of code without running the entire program.