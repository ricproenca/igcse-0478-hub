# 4.1 Types of software and interrupts

> Source: https://moshikur.com/igcse-o-level-cs/ch-04-software/4-1-types-of-software-and-interrupts/

# 4.1 Types of software and interrupts

---

>> Syllabus

- **4.1.1 System** So**ftware and Application Software**
  - Differences between system software and application software.
  - Examples of system software (e.g., operating systems, utility software) and application software.
- **4.1.2 Role and Functions of an Operating System**
  - Managing files.
  - Handling interrupts.
  - Providing an interface.
  - Managing peripherals and drivers.
  - Managing memory.
  - Managing multitasking.
  - Providing a platform for running applications.
  - Providing system security.
  - Managing user accounts.
- **4.1.3 Running Applications**
  - How hardware, firmware, and an operating system work together to run applications.
  - Role of the bootloader (firmware).
- **4.1.4 Interrupts**
  - Role and operation of interrupts.
  - How interrupts are generated and handled.
  - Examples:
    - Software interrupts (e.g., division by zero, memory access errors).
    - Hardware interrupts (e.g., pressing keys, mouse movement).

---

## **4.1.1 System Software and Application Software**

#### **What is Software?**

Software is a set of instructions that tells the computer what to do. It helps the computer hardware perform useful tasks.

There are two main types of software:

[![A graphic illustrating the differences between System Software and Application Software, showing system software management of hardware and resources on one side, and application software supporting specific user tasks on the other.](images/topic4_software/4_1_types_of_software_and_interrupts/img_001.png)](https://i0.wp.com/moshikur.com/wp-content/uploads/2025/12/image.png?ssl=1)

---

#### **What is System Software?**

System software manages and controls the hardware and basic functions of the computer. It acts as a bridge between the hardware and application software.

**Examples of System Software:**

**Operating Systems (OS):**

Manages the overall operations of the computer.

Examples: Windows, macOS, Linux, Android.

**Utility Software:**

Performs specific tasks to maintain the computer’s health.

Examples: Antivirus software, file compression tools, and backup programs.

---

#### **What is Application Software?**

Application software is designed to help users perform specific tasks. It relies on the system software to function.

**Examples of Application Software:**

**Word Processors:**

Used to create documents.

**Web Browsers:**

Used to browse the internet.

**Games and Entertainment Software:**

Used for leisure activities.

---

#### **Differences Between System Software and Application Software**

| Feature | System Software | Application Software |
| --- | --- | --- |
| Purpose | Manages computer hardware and software. | Helps users perform specific tasks. |
| Examples | Operating systems, utility programs. | Word processors, web browsers, games. |
| Interaction with Hardware | Directly interacts with hardware. | Depends on system software to interact with hardware. |
| Visibility | Mostly works in the background. | Directly used by the user. |

---

# **Activity 4.1.1**

### **Task 1: Match the Software**

You are given a list of software programs. Categorize each as **system software** or **application software**.

#### **List of Software:**

- Antivirus
- Google Chrome
- Windows 11
- Microsoft Word
- Disk Cleanup
- Spotify

**Hint:**  
  
**System software** runs in the background to manage the computer. Think about software like operating systems and utilities.  
  
**Application software** is what you use to perform specific tasks, like creating a document or listening to music.

---

### **Task 2: Create a Comparison Chart**

Create a comparison chart showing **3 differences** and **2 similarities** between system software and application software.

**Hint:** To compare, think about their purpose, visibility, and interaction with hardware. System software manages the entire system, often working behind the scenes, while application software focuses on specific user tasks, like editing a photo or playing a game. For similarities, remember that both are essential for a computer to function, and both depend on the hardware to execute tasks.

---

### **Task 3: Software Scavenger Hunt**

Look at the software installed on your own computer or device. Identify two pieces of system software and three pieces of application software.

**Hint:** Look at what you use the computer for. If the software helps you do things like browse the internet, create documents, or watch videos, it’s application software. If it ensures the computer functions properly, like the operating system or a disk cleanup tool, it’s system software.

---

## **4.1.2 Role and Functions of an Operating System**

#### **What is an Operating System?**

An operating system (OS) is system software that manages the hardware and software of a computer. It allows the user to interact with the computer and ensures all parts of the computer work together properly.

[![Infographic illustrating the role and functions of an operating system, highlighting aspects like managing files, handling interrupts, providing user interface, managing peripherals, managing memory, multitasking, and ensuring system security.](images/topic4_software/4_1_types_of_software_and_interrupts/img_002.png)](https://i0.wp.com/moshikur.com/wp-content/uploads/2025/12/image-1.png?ssl=1)

---

#### **Key Roles of an Operating System**

**1. Managing Files**

The OS organizes files and folders on a computer.

It allows users to create, delete, move, and open files.

Example: Saving your school project as a Word file and finding it later in a folder.

**2. Handling Interrupts**

An interrupt is a signal sent to the OS that requires immediate attention.

The OS pauses its current tasks to deal with the interrupt and then resumes its work.

Example: Pressing a key on the keyboard or clicking the mouse sends an interrupt.

**3. Providing a User Interface (UI)**

The OS gives users a way to interact with the computer.

**Types of User Interfaces:**

- **Graphical User Interface (GUI):** Uses icons and menus (e.g., Windows desktop).
- **Command Line Interface (CLI):** Uses text-based commands (e.g., Linux terminal).

#### **4. Managing Peripherals and Drivers**

**Peripherals** are external devices like printers, keyboards, mice, or scanners.

The OS uses **device drivers** (special software) to help the computer communicate with these devices.

**Examples:**

When you print a document, the OS sends the instructions from your application (e.g., Word) to the printer through the printer driver.

When you move a mouse, the OS ensures the pointer moves on the screen.

#### **5. Managing Memory**

The OS is responsible for allocating memory (RAM) to different programs running on the computer.

**It ensures that:**

- No two programs interfere with each other’s memory space.
- Memory is freed up when a program is closed.

**Example:** If you’re watching a video and opening a game, the OS ensures both get enough memory to run smoothly.

#### **6. Managing Multitasking**

- The OS enables **multitasking**, which means running multiple applications at the same time.
- It does this by:
  - Dividing the CPU’s time between tasks using scheduling.
  - Quickly switching between tasks so it seems like everything is running simultaneously.
- **Example:**
  - Browsing the internet while listening to music on a media player.

#### **7. Providing a Platform for Applications**

- The OS provides an environment where application software can run.
- It ensures that applications can access the resources they need, such as memory, CPU, and storage.
- **Example:**
  - Running Microsoft Word to create a document or Chrome to browse the web.

#### **8. Providing System Security**

- The OS protects the computer from unauthorized access and malware.
- Key security features include:
  - Password-protected user accounts.
  - File permissions (e.g., allowing only certain users to edit files).
  - Firewalls and antivirus integration.
- **Example:**
  - You need to enter a password to log in to your computer.

#### **9. Managing User Accounts**

- The OS allows multiple users to have their own accounts on the same computer.
- Each user can have personalized settings, files, and permissions.
- **Example:**
  - Family members can have separate accounts on the same laptop, ensuring their files remain private.

---

> ## **Activity** 4.1.2.1
>
> 1. What is the main job of an operating system when managing files?
> 2. What happens when you press a key on your keyboard? How does the OS handle this?
> 3. Explain the difference between a GUI and CLI. Give one example of each.

---

> ## **Activity** 4.1.2.2
>
> 1. What does the operating system do to manage memory? Why is this important?
> 2. How does the OS allow multitasking? Give an example.
> 3. Why are device drivers necessary for peripherals?
> 4. What are two ways the OS ensures the system is secure?
> 5. Explain how user accounts help manage multiple users on one computer.

---

## **4.1.3 Running Applications**

#### **How Hardware, Firmware, and OS Work Together**

To run applications like games or word processors, the **hardware**, **firmware**, and **operating system** must work together.

[![Flowchart illustrating the process of running applications, including hardware and firmware initialization, operating system loading, and application launch, with labeled steps.](images/topic4_software/4_1_types_of_software_and_interrupts/img_003.png)](https://i0.wp.com/moshikur.com/wp-content/uploads/2025/12/image-2.png?ssl=1)

**Hardware**

The physical parts of the computer, like the CPU, RAM, and hard drive, provide the resources (e.g., processing power, storage).

Example: The CPU executes the instructions needed to run an application.

**Firmware**

Firmware is a type of software stored in the computer’s hardware. It helps the hardware work with the OS.

Example: The firmware in your computer’s motherboard helps start the system when you turn it on.

**Operating System (OS)**

The OS coordinates between the application and hardware.

Example: When you open a game, the OS ensures the CPU processes the game’s instructions, the RAM stores temporary data, and the GPU displays graphics.

---

#### **Role of the Bootloader (Firmware)**

The **bootloader** is a small program stored in the computer’s firmware.

It runs when the computer starts and loads the operating system into memory.

Without the bootloader, the computer wouldn’t know how to start the OS.

**Example:**

When you press the power button on your computer, the bootloader initializes and loads Windows, macOS, or Linux.

---

> ## **Activity 4.1.3**
>
> 1. What are the roles of hardware, firmware, and the OS in running applications?
> 2. Explain how the bootloader helps start the computer.
> 3. Why is firmware important for hardware to work with the OS?
> 4. Describe what happens from the moment you press the power button until the OS is loaded.

---

# **4.1.4 Interrupts**

#### **What are Interrupts?**

An **interrupt** is a signal sent to the CPU that tells it something important has happened and needs immediate attention. Interrupts ensure that urgent tasks are handled quickly, even if the CPU is busy with other work.

[![Diagram illustrating the interrupt process in operating systems, showing three main steps: event occurrence, CPU interruption, and interrupt handling.](images/topic4_software/4_1_types_of_software_and_interrupts/img_004.png)](https://i0.wp.com/moshikur.com/wp-content/uploads/2025/12/image-3.png?ssl=1)

---

#### **Role of Interrupts**

**Prioritizing Tasks**

Interrupts allow the system to pause its current task and switch to a more urgent one.

Example: If you’re typing, pressing a key sends an interrupt to the CPU to register the keypress.

**Efficient Task Management**

By using interrupts, the system can handle tasks as soon as they occur without constantly checking for them (a process called “polling”).

This saves processing power and ensures faster responses.

---

#### **How Interrupts Work (Operation of Interrupts)**

1. **Interrupt Generation**
   - Interrupts are generated by hardware devices (like a mouse or keyboard) or software programs.
   - Example:
     - **Hardware Interrupt:** Pressing a key or moving the mouse.
     - **Software Interrupt:** A program encountering a division by zero error.
2. **Interrupt Signal Sent to CPU**
   - The interrupt signal is sent to the CPU, asking it to pause its current task.
3. **Interrupt Service Routine (ISR)**
   - The CPU runs a special program called the **Interrupt Service Routine** to handle the interrupt.
   - Example: If you press a key, the ISR processes which key was pressed.
4. **Resume Work**
   - After the interrupt is handled, the CPU goes back to its original task.

---

#### **Examples of Interrupts**

1. **Hardware Interrupts**
   - These are triggered by external devices or hardware.
   - Examples:
     - **Keyboard Interrupt:** Pressing a key on the keyboard.
     - **Mouse Interrupt:** Moving the mouse or clicking a button.
     - **Printer Interrupt:** A printer notifying the CPU that it has finished printing a document.

1. **Software Interrupts**
   - These are triggered by programs or software issues.
   - Examples:
     - **Division by Zero Error:** When a program tries to divide a number by zero, it generates an interrupt to handle the error.
     - **Memory Access Error:** If a program tries to access a part of memory it is not allowed to use, it sends an interrupt to notify the OS.

---

### **Why Are Interrupts Important?**

- Interrupts ensure that critical tasks are handled immediately.
- They allow the system to multitask effectively.
- Without interrupts, the CPU would waste time constantly checking for events (polling), slowing down the system.

---

### **Real-Life Example**

Imagine you’re using a computer to write an essay, listen to music, and print a document. Here’s how interrupts help:

1. You press a key on the keyboard → **Keyboard interrupt** tells the CPU to display the letter.
2. The printer finishes printing → **Printer interrupt** notifies the CPU to update the print status.
3. The music player needs to load the next song → **Software interrupt** ensures the transition happens smoothly.

---

## **Activity 4.1.4**

### **Short Questions**

1. What is an interrupt? Why is it important?
2. Give one example each of a hardware interrupt and a software interrupt.
3. What is the Interrupt Service Routine (ISR), and what does it do?

### **Long Questions**

1. Explain how interrupts work, starting from when they are generated to when the CPU resumes its task. Include an example.
2. Compare hardware interrupts and software interrupts. Provide one example for each.

---