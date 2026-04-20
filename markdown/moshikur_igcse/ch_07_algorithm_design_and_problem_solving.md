# CH 07 Algorithm Design & Problem Solving

> Source: https://moshikur.com/igcse-o-level-cs/ch-07-algorithm-design-and-problem-solving/

# CH 07 Algorithm design and problem solving

---

# **[7.1](#7.1)**

---

Program Development Life Cycle (PDLC)

# **[7.2](#7.2)**

---

Problem Decomposition

# [7.3](#7.3)

---

Understanding Algorithms

# [7.4](#7.4)

---

Standard Methods of Solution

# **[7.5](#7.1)**

---

[Validation and Verification](#7.1)

# **[7.6](#7.6)**

---

Testing

# [7.7](#7.7)

---

Trace Tables and Debugging

# [7.8](#7.8)

---

Writing and Modifying Algorithms

Syllabus

## **7.1: Program Development Life Cycle (PDLC)**

7.1.1 Understand the stages of the program development life cycle:  
7.1.1.1 Analysis: Identifying, abstracting, and decomposing the problem; identifying requirements.  
7.1.1.2 Design: Using structure diagrams, flowcharts, and pseudocode.  
7.1.1.3 Coding: Writing program code and iterative testing.  
7.1.1.4 Testing: Using test data to verify correctness.

---

## **7.2 Problem Decomposition**

7.2.1 Understand that every computer system consists of sub-systems, which themselves consist of further sub-systems.  
7.2.2 Understand how a problem can be broken down into its component parts.  
7.2.3 Use different methods to design and construct a solution, including:  
7.2.3.1 Structure diagrams.  
7.2.3.2 Flowcharts.  
7.2.3.3 Pseudocode.

---

## 7.3 Understanding Algorithms

7.3.1 Explain the purpose of a given algorithm:  
7.3.1.1 State the purpose of an algorithm.  
7.3.1.2 Describe the processes involved in an algorithm.

---

## 7.4 Standard Methods of Solution

7.4.1 Understand common algorithmic techniques, including:  
7.4.1.1 Linear search.  
7.4.1.2 Bubble sort.  
7.4.1.3 Totaling.  
7.4.1.4 Counting.  
7.4.1.5 Finding maximum, minimum, and average values.

---

## 7.5 Validation and Verification

7.5.1 Understand the need for validation checks on input data and different types of validation checks:  
7.5.1.1 Range check.  
7.5.1.2 Length check.  
7.5.1.3 Type check.  
7.5.1.4 Presence check.  
7.5.1.5 Format check.  
7.5.1.6 Check digit.  
7.5.2 Understand the need for verification checks on input data and different types of verification checks:  
7.5.2.1 Visual check.  
7.5.2.2 Double entry check.

---

## 7.6 Testing

7.6.1 Suggest and apply suitable test data, including:  
7.6.1.1 Normal test data.  
7.6.1.2 Abnormal test data.  
7.6.1.3 Extreme test data.  
7.6.1.4 Boundary test data.

---

## 7.7 Trace Tables and Debugging

7.7.1 Complete a trace table to document a dry-run of an algorithm, including tracking:  
7.7.1.1 Variables.  
7.7.1.2 Outputs.  
7.7.1.3 User prompts.  
7.7.2 Identify errors in given algorithms and suggest ways to correct them.

---

## 7.8 Writing and Modifying Algorithms

7.8.1 Write and amend algorithms for given problems or scenarios using:  
7.8.1.1 Pseudocode.  
7.8.1.2 Program code.  
7.8.1.3 Flowcharts.

---

# **7.1 Program Development Life Cycle (PDLC)**

The **Program Development Life Cycle (PDLC)** is a step-by-step process used to **develop and improve computer programs**. It consists of different **stages** that ensure the program is **well-planned, correctly implemented, and error-free**.

---

## **7.1.1 Stages of the Program Development Life Cycle**

### **1. Analysis**

🔹 In this stage, we **identify the problem** that needs to be solved.  
🔹 The main tasks in this stage are:

- **Identifying the problem** – What is the program supposed to do?
- **Abstracting** – Ignoring unnecessary details to focus on the key features.
- **Decomposing** – Breaking the problem into smaller, manageable parts.
- **Identifying requirements** – Understanding what inputs, outputs, and processes are needed.

📝 **Example:**  
A school needs a program to calculate students’ average marks.

- The problem is **calculating an average**.
- The inputs are **student marks**.
- The output is **the average mark**.

---

### **2. Design**

🔹 In this stage, we **plan** how the program will work.  
🔹 The common ways to **represent a design** are:

- **Structure diagrams** – Show how different parts of the program are connected.
- **Flowcharts** – Use symbols to represent the flow of steps.
- **Pseudocode** – A simplified way of writing program logic.

📝 **Example:**  
A **flowchart** for calculating student marks might look like this:

```
sqlCopyEditStart → Input marks → Calculate average → Output result → End
```

---

### **3. Coding**

🔹 In this stage, we **write the actual program** using a programming language.  
🔹 The main task is to **convert the plan into working code**.  
🔹 Iterative testing is done to check if the program is working as expected.

📝 **Example:**  
Using pseudocode, the program for calculating an average might look like this:

```
INPUT Mark1INPUT Mark2

INPUT Mark3

Average ← (Mark1 + Mark2 + Mark3) / 3

OUTPUT "The average is ", Average￼
```

---

### **4. Testing**

🔹 In this stage, we **test the program** to make sure it works correctly.  
🔹 The program is tested using **different types of test data**:

- **Normal data** – Expected inputs (e.g., entering marks between 0-100).
- **Abnormal data** – Unexpected inputs (e.g., entering text instead of numbers).
- **Extreme data** – The highest or lowest possible values (e.g., 0 and 100).
- **Boundary data** – Values at the limits.

📝 **Example:**  
To test the student average program:

- **Normal data:** 50, 75, 90 → Should output an average of 71.67.
- **Abnormal data:** “hello”, 80, 90 → Should show an error.
- **Extreme data:** 0, 100 → Should calculate properly.
- **Boundary data:** 0, 100, 101, -1

---

# **Task 7.1**

## **Question 1: Identify the Correct Stage**

A programmer is writing an algorithm for a weather app. She first **draws a flowchart** to show how data will be processed before writing the actual code.  
Which stage of PDLC is she currently in?

- **A) Analysis**
- **B) Design**
- **C) Coding**
- **D) Testing**

💡 **Hint:** She is planning how the program will work before coding it.

---

## **Question 2: Understanding Testing**

A company is developing a program that records employee work hours.  
Which type of test data would check if the program correctly handles **negative hours**?

- **A) Normal test data**
- **B) Extreme test data**
- **C) Abnormal test data**
- **D) Boundary test data**

💡 **Hint:** Negative hours are not expected in normal use.

---

## **Question 3: Writing Pseudocode**

Write **pseudocode** for a program that takes two numbers, adds them together, and prints the result.

💡 **Hint:** Use `INPUT`, `OUTPUT`, and `SUM` variables.

---

## **Question 4: Debugging a Code**

A student writes this pseudocode to calculate the area of a rectangle:

```
INPUT Length

INPUT Width

Area ← Length * Width

OUTPUT "The area is"
```

What is **wrong** with the pseudocode?

💡 **Hint:** The program is missing something in the OUTPUT statement.

# **7.2: Problem Decomposition**

---

**Problem Decomposition** is the process of breaking a complex problem into **smaller, manageable parts (sub-problems)**. This makes it easier to solve the problem step by step and helps with designing efficient algorithms.

In computer science, **decomposing a problem** allows programmers to focus on smaller tasks and handle them more effectively. It also helps in reusing code and improving collaboration in large projects.

One of the most effective ways to decompose a problem is by breaking it down into **four main components**:

**Input** – Data that the program receives.

**Process** – The operations performed on the input.

**Output** – The results displayed to the user.

**Storage** – Where data is saved for future use.

By categorizing tasks into these four sections, we can make problem-solving more structured and efficient.

---

## **7.2.1 Sub-Systems in a Computer System**

Every computer system is made up of **sub-systems**, and each sub-system can be broken down further into smaller sub-systems.

**Example:**  
Consider an **online shopping system**:

- **Main system:** Online shopping platform
  - **Sub-system 1:** User management (login, register)
  - **Sub-system 2:** Product catalog (view products, search)
  - **Sub-system 3:** Payment processing (checkout, payment validation)

Each of these sub-systems can be decomposed further. For example, the “User management” sub-system can be divided into tasks like “Login system” and “Registration system.”

---

## **7.2.2 How to Decompose a Problem**

When decomposing a problem, follow these steps:

1. **Identify the main problem:** What is the overall task the program must perform?
2. **Break it into sub-tasks:** Divide the main task into logical, smaller sub-tasks.
3. **Further decompose if needed:** Each sub-task can be decomposed further until the tasks are small enough to solve easily.

**Example:**  
For a **School Attendance System**, the main task might be to **record and manage student attendance**. This can be decomposed as:

- Sub-task 1: Record attendance.
- Sub-task 2: Generate attendance reports.
- Sub-task 3: Alert parents for absentees.

---

## **7.2.3 Methods to Design and Construct a Solution**

There are different methods to present and design solutions after decomposing a problem:

## **Structure Diagrams**

Show how the system and sub-systems are related.

Provide a top-down view of the problem.

## **Flowcharts**

Represent the flow of the program using symbols for inputs, processes, decisions, and outputs.

Useful for visualizing how each part of the problem will be handled.

## **Pseudocode**

A simple, structured way of writing the logic of a program using plain English.

Helps in planning the solution before writing the actual code.

---

## **Example: Solving a Real-World Problem with Decomposition**

**Problem:** Create a system to calculate the grades of students in a class.

### **Decomposition:**

1. **Input student marks.**
2. **Calculate the total and average.**
3. **Check the grade based on the average.**
4. **Output the student’s grade.**

### **Flowchart Example:**

```
Start → Input Marks → Calculate Total → Calculate Average → Determine Grade → Output Grade → End
```

### **Pseudocode Example:**

```
INPUT Mark1, Mark2, Mark3

Total ← Mark1 + Mark2 + Mark3

Average ← Total / 3

IF Average >= 90 THEN

OUTPUT "Grade A"

ELSE IF Average >= 75 THEN

OUTPUT "Grade B"

ELSE

OUTPUT "Grade C"

END IF
```

---

## **Benefits of Problem Decomposition**

1. **Simplifies complex problems** by breaking them into smaller tasks.
2. **Improves code reusability** – Some sub-tasks can be used in other programs.
3. **Enhances teamwork** – Different people can work on different sub-systems.
4. **Makes debugging easier** – Problems can be isolated in individual sub-tasks.

---

# **Task 7.2**

### **Question 1: Sub-System Identification**

A company is building a **Food Delivery App**. The main tasks are to **manage orders**, **track deliveries**, and **handle payments**.  
Identify three sub-systems for this app.

💡 **Hint:** Think about the core functionalities needed to complete these tasks.

---

### **Question 2: Structure Diagram**

Create a **structure diagram** for an **online examination system** with the following tasks:

1. Manage user login (student and admin).
2. Conduct the exam (questions, timer, submission).
3. Generate and display results.

💡 **Hint:** Divide the tasks into sub-tasks logically.

---

### **Question 3: Understanding Flowcharts**

A flowchart is designed for a program that checks if a number is positive, negative, or zero. It has these steps:

1. **Input the number.**
2. **Check if it’s greater than zero.** If true, output “Positive”.
3. **Else, check if it’s less than zero.** If true, output “Negative”.
4. If neither, output “Zero”.
5. End.

Draw the flowchart to represent this process.

💡 **Hint:** Use symbols like parallelograms (for input/output), diamonds (for decisions), and rectangles (for processes).

---

### **Question 4: Decomposition Exercise**

Decompose the problem: **Create a library management system that allows users to borrow and return books.**  
Write down at least three sub-tasks for this problem.

💡 **Hint:** Think about what actions users can perform in a library.

---

# **7.3: Understanding Algorithms**

An **algorithm** is a **step-by-step set of instructions** used to solve a problem. It must be **clear, precise, and efficient** to produce the correct result.

### **Key Characteristics of a Good Algorithm:**

✅ **Correctness** – It should always give the correct output.

✅ **Efficiency** – It should solve the problem quickly without unnecessary steps.

✅ **Clarity** – It should be easy to understand and follow.

✅ **Definiteness** – Each step must be clearly defined.

✅ **Finiteness** – It should have a finite number of steps and must terminate.

---

## **7.3.1 Explain the Purpose of a Given Algorithm**

Every algorithm is designed for a **specific purpose**, such as sorting data, searching for an item, or performing calculations.

### **7.3.1.1 Stating the Purpose of an Algorithm**

When analyzing an algorithm, you need to determine **what it is doing**.

**Example 1:**  
Consider this pseudocode:

```
INPUT A, B

Sum ← A + B

OUTPUT "The sum is ", Sum
```

**Purpose:** This algorithm **takes two numbers, adds them together, and displays the sum**.

**Example 2:**

```
INPUT Number

IF Number MOD 2 = 0 THEN

OUTPUT "Even"

ELSE

OUTPUT "Odd"

END IF
```

**Purpose:** This algorithm **determines whether a number is even or odd**.

---

### **7.3.1.2 Describing the Processes in an Algorithm**

A process is any **action or calculation** performed in an algorithm.

🔹 **Input** – The data entered into the program.  
🔹 **Processing** – The calculations or decisions performed.  
🔹 **Output** – The result displayed to the user.

**Example:** Find the largest of three numbers.

```
INPUT A, B, C

IF A > B AND A > C THEN

OUTPUT "Largest number is ", A

ELSE IF B > C THEN

OUTPUT "Largest number is ", B

ELSE

OUTPUT "Largest number is ", C

END IF
```

**Processes:**

1. Takes three numbers as **input**.
2. Compares them using **conditions**.
3. Displays the **largest number as output**.

---

# **Task 7.3**

### **Question 1: Identifying an Algorithm’s Purpose**

Look at the following pseudocode:

```
INPUT N

Factorial ← 1

FOR i ← 1 TO N DO

Factorial ← Factorial * i

NEXT i

OUTPUT "Factorial is ", Factorial
```

What does this algorithm do?

**A) Finds the sum of numbers from 1 to N**

**B) Finds the product of numbers from 1 to N**

**C) Checks if N is even or odd**

**D) Prints numbers from 1 to N**

💡 **Hint:** The variable **Factorial** is repeatedly multiplied.

---

### **Question 2: Tracing an Algorithm**

What will be the output of the following pseudocode if **N = 4**?

```
Sum ← 0

FOR i ← 1 TO N DO

Sum ← Sum + i

NEXT i

OUTPUT "Sum is ", Sum
```

- **A) 4**
- **B) 10**
- **C) 6**
- **D) 15**

💡 **Hint:** The loop **adds numbers from 1 to N**.

---

### **Question 3: Debugging an Algorithm**

A student writes the following pseudocode to check if a number is positive:

```
INPUT Number

IF Number > 0 THEN

OUTPUT "Positive"

ELSE IF Number < 0 THEN

OUTPUT "Negative"

ELSE

OUTPUT "Zero"
```

However, the program **does not work correctly** when Number = 0.  
What should be corrected?

💡 **Hint:** The **“Zero” condition** should be correctly placed.

---

### **Question 4: Writing an Algorithm**

Write **pseudocode** for an algorithm that:

1. Takes a number as input.
2. Checks whether the number is a **multiple of 5**.
3. Outputs **“Multiple of 5”** or **“Not a multiple of 5”**.

💡 **Hint:** Use **MOD (modulus) operator** to check divisibility.

---

# **7.4: Standard Methods of Solution**

Standard methods of solution are **predefined techniques** used to solve common problems in programming. These methods help programmers avoid reinventing the wheel and ensure **efficient problem-solving**.

In **IGCSE/O Level Computer Science (0478/2210)**, you must understand the following standard methods:

1. **Linear search**
2. **Bubble sort**
3. **Totalling**
4. **Counting**
5. **Finding maximum, minimum, and average values**

---

## **7.4.1 Common Algorithmic Techniques**

### **1. Linear Search**

[Go to this page for a detailed tutorial on Linear Search](https://moshikur.com/pseudocode/6-pseudocode-array/6-2-pseudocode-linear-search/)

🔹 **Used for:** Finding an item in an **unordered** list.  
🔹 **How it works:** The algorithm **checks each item** one by one until it finds the target item or reaches the end of the list.

**Pseudocode Example:**

```
INPUT Target

List ← [12, 45, 67, 89, 23, 90]

Found ← FALSE

FOR i ← 1 TO Length of List DO

IF List[i] = Target THEN

OUTPUT "Item found at position ", i

Found ← TRUE

END IF

NEXT i

IF NOT Found THEN

OUTPUT "Item not found"

END IF
```

**Efficiency:** Slow for large lists but works well for small datasets.

---

### **2. Bubble Sort**

[Go to this page for a detailed tutorial on Bubble Sort](https://moshikur.com/pseudocode/6-pseudocode-array/7-pseudocode-bubble-sort/)

🔹 **Used for:** Sorting a list of numbers in **ascending or descending order**.  
🔹 **How it works:**

- Compares two adjacent numbers.
- If the first is greater than the second, swap them.
- Repeats this process until no swaps are needed.

**Pseudocode Example:**

```
List ← [12, 5, 8, 19, 1]

FOR i ← 1 TO Length of List - 1 DO

FOR j ← 1 TO Length of List - i DO

IF List[j] > List[j + 1] THEN

Temp ← List[j]

List[j] ← List[j + 1]

List[j + 1] ← Temp

END IF

NEXT j

NEXT i

OUTPUT List
```

**Efficiency:** **Inefficient for large lists** but easy to understand.

---

### **3. Totalling**

[Go to this page for a detailed tutorial on Totaling](https://moshikur.com/pseudocode/5-pseudocode-basic-operations/5-2-pseudocode-totaling/)

🔹 **Used for:** Adding all the values in a list.  
🔹 **How it works:** Uses a loop to sum all numbers.

**Pseudocode Example:**

```
List ← [10, 20, 30, 40]

Total ← 0

FOR i ← 1 TO Length of List DO

Total ← Total + List[i]

NEXT i

OUTPUT "Total is ", Total
```

**Example Use Case:** Calculating the **total sales of a store**.

---

### **4. Counting**

[Go to this page for a detailed tutorial on Counting](https://moshikur.com/pseudocode/5-pseudocode-basic-operations/5-1-pseudocode-counting/)

🔹 **Used for:** Counting how many times a specific value appears.  
🔹 **How it works:** Uses a loop and a counter variable.

**Pseudocode Example:**

```
List ← [3, 7, 3, 2, 3, 9, 3]

Target ← 3

Count ← 0

FOR i ← 1 TO Length of List DO

IF List[i] = Target THEN

Count ← Count + 1

END IF

NEXT i

OUTPUT "Target appears ", Count, " times"
```

**Example Use Case:** **Counting how many students scored above 90%**.

---

### **5. Finding Maximum, Minimum, and Average Values**

[Go to this page for a detailed tutorial on Finding Maximum/Minimul Values](https://moshikur.com/pseudocode/5-pseudocode-basic-operations/5-3-pseudocode-finding-highest-lowest-value/)

🔹 **Used for:** Finding the **highest, lowest, or average value** in a dataset.  
🔹 **How it works:** Uses a loop to compare values.

**Pseudocode Example (Finding Maximum):**

```
List ← [45, 12, 89, 55, 33]

Max ← List[1]

FOR i ← 2 TO Length of List DO

IF List[i] > Max THEN

Max ← List[i]

END IF

NEXT i

OUTPUT "Maximum value is ", Max
```

**Pseudocode Example (Finding Minimum):**

```
Min ← List[1]

FOR i ← 2 TO Length of List DO

IF List[i] < Min THEN

Min ← List[i]

END IF

NEXT i

OUTPUT "Minimum value is ", Min
```

**Pseudocode Example (Finding Average):**

```
Total ← 0

FOR i ← 1 TO Length of List DO

Total ← Total + List[i]

NEXT i

Average ← Total / Length of List

OUTPUT "Average value is ", Average
```

**Example Use Case:** Finding the **highest exam score** in a class.

---

# Task 7.4

### **Question 1: Understanding Bubble Sort**

A student runs a bubble sort algorithm on this list:  
`[5, 1, 4, 2]`  
How many swaps will be made in the first pass?

- **A) 1**
- **B) 2**
- **C) 3**
- **D) 4**

💡 **Hint:** Compare adjacent numbers.

---

### **Question 2: Linear Search**

A **linear search** is used on this list:  
`[4, 8, 15, 23, 42]`  
What is the worst-case scenario for searching for number **42**?

- **A) 1 comparison**
- **B) 2 comparisons**
- **C) 5 comparisons**
- **D) Not found**

💡 **Hint:** Worst-case means checking **every** element.

---

### **Question 3: Writing Pseudocode**

Write **pseudocode** for an algorithm that counts **how many even numbers** exist in a list.

💡 **Hint:** Use `MOD` operator to check divisibility by `2`.

---

### **Question 4: Debugging an Algorithm**

A student wrote this code to find the sum of a list, but it has an error:

```
List ← [3, 5, 8, 12]

Total ← 1

FOR i ← 1 TO Length of List DO

Total ← Total + List[i]

NEXT i

OUTPUT "Sum is ", Total
```

What mistake did they make?

- **A) Wrong loop range**
- **B) Total should start at 0**
- **C) Missing output statement**
- **D) Incorrect conditional statement**

💡 **Hint:** What should the initial sum be?

---

# **7.5 Validation and Verification**

[Go to this page for a detailed tutorial on Validation & Verification](https://moshikur.com/pseudocode/5-pseudocode-basic-operations/5-4-validation-verification/)

When data is entered into a computer system, errors can occur. To minimize these errors, we use **validation and verification techniques**.

**Validation** ensures that the input **is reasonable and meets specific rules**.

**Verification** checks that the **data entered matches the intended input**.

---

## **7.5.1 Validation Checks**

**Validation** is used to check **if data is valid but does not guarantee correctness**. It only ensures that the data **follows specific rules**.

### **Types of Validation Checks**

| Validation Check | Purpose | Example |
| --- | --- | --- |

| Validation Check | Purpose | Example |
| --- | --- | --- |
| Range Check | Ensures that a value falls within a specified range. | A student’s age must be between 5 and 18. |
| Length Check | Ensures that input data has the correct number of characters. | A password must be exactly 8 characters long. |
| Type Check | Ensures that input data is of the correct type (e.g., number, text). | A phone number should only contain digits. |
| Presence Check | Ensures that an input field is not left empty. | A user must enter their email before submitting a form. |
| Format Check | Ensures data follows a specified pattern. | A date must be entered in the format DD/MM/YYYY . |
| Check Digit | Uses a mathematical formula to detect errors in numbers. | Used in barcode numbers, credit card numbers. |

📝 **Example (Pseudocode for a Range Check):**

```
INPUT Age

IF Age < 5 OR Age > 18 THEN

OUTPUT "Invalid age"

ELSE

OUTPUT "Valid age"

END IF
```

**Why use validation?** It reduces errors but does **not** guarantee correctness. A person can enter a **valid but incorrect** age (e.g., entering **10 instead of 11**).

---

## **7.5.2 Verification Checks**

**Verification** ensures that the data entered **is accurate** and matches the intended input.

### **Types of Verification**

| Verification Method | Purpose | Example |
| --- | --- | --- |
| Double Entry Check | Requires the user to enter data twice to check for mismatches. | Entering a password twice when creating an account. |
| Visual Check | The user manually reviews the input for errors. | A user checks a printed form before submission. |

**Example (Pseudocode for Double Entry Check):**

```
INPUT Password1

INPUT Password2

IF Password1 = Password2 THEN

OUTPUT "Passwords match"

ELSE

OUTPUT "Passwords do not match. Try again."

END IF
```

**Why use verification?** It ensures the data entered is **exactly as intended**.

---

# **Task 7.5**

### **Question 1: Identifying the Validation Check**

A user is required to enter a **six-digit student ID**.  
Which type of validation check should be applied?

- **A) Range check**
- **B) Length check**
- **C) Format check**
- **D) Presence check**

💡 **Hint:** The number must have **exactly six digits**.

---

### **Question 2: Understanding Verification**

A banking system requires users to **enter their email twice** before submitting the form.  
Which type of verification is being used?

- **A) Visual check**
- **B) Double entry check**
- **C) Format check**
- **D) Type check**

💡 **Hint:** The system is checking if both inputs match.

---

### **Question 3: Writing Pseudocode**

Write **pseudocode** for a program that:

1. Asks the user to enter their age.
2. **Validates** that the age is between 18 and 65.
3. If the age is valid, displays **“Valid age”**; otherwise, shows **“Invalid age”**.

💡 **Hint:** Use a **range check**.

---

### **Question 4: Debugging an Algorithm**

A student wrote this pseudocode for a **presence check**, but it has an error:

```
INPUT Username

IF Username = "" THEN

OUTPUT "Valid username"

ELSE

OUTPUT "Username required"

END IF
```

What is wrong with this code?

- **A) The conditions are reversed**
- **B) The presence check is missing**
- **C) The output statements are incorrect**
- **D) The INPUT statement is incorrect**

💡 **Hint:** A blank username **should not** be considered valid.

---

# **7.6 Testing**

Testing is the process of checking if a program **works correctly** and **meets the requirements**. It helps find **errors (bugs)** before the program is used by real users.

There are **different types of test data** used to check how a program handles various inputs.

---

## **7.6.1 Types of Test Data**

To ensure a program works correctly, we use different types of test data:

| Type of Test Data | Purpose | Example (Checking Age 1-100) |
| --- | --- | --- |
| Normal Data | Typical, expected input that should be processed correctly. | 25, 50, 75 |
| Abnormal Data | Completely incorrect data that should be rejected. | “hello”, -5, 200 |
| Extreme Data | Data at the very edges of the acceptable range . | 1, 100 |
| Boundary Data | Data that is at or just outside the limit. | 0, 1, 100, 101 |

---

## **Example: Testing a Program That Accepts a Number Between 1 and 100**

A program asks the user to enter an age between **1 and 100**.

### **Test Plan Table**

| Test Data Type | Input Value | Expected Output |
| --- | --- | --- |
| Normal | 25 | “Valid age” |
| Abnormal | “hello” | “Invalid input, please enter a number” |
| Extreme | 1 | “Valid age” |
| Extreme | 100 | “Valid age” |
| Boundary | 0 | “Invalid age” |
| Boundary | 101 | “Invalid age” |

---

## **Pseudocode Example: Testing for a Valid Age**

```
INPUT Age

IF Age >= 1 AND Age <= 100 THEN

OUTPUT "Valid age"

ELSE

OUTPUT "Invalid age"

END IF
```

**This program should be tested using all types of test data** to ensure it works correctly.

---

## **Debugging and Fixing Errors**

Errors can occur in programs. Testing helps identify **three main types of errors**:

| Error Type | Description | Example |
| --- | --- | --- |
| Syntax Error | Mistakes in the code structure (e.g., missing brackets or incorrect keywords). | IF x = 10 THEN OUTPUT "Valid" (missing END IF ) |
| Logic Error | The program runs but gives the wrong output . | Total ← Number1 - Number2 instead of Total ← Number1 + Number2 |
| Runtime Error | Errors that cause the program to crash , like dividing by zero. | Total ← 10 / 0 (division by zero) |

---

# task 7.6

### **Question 1: Identifying Test Data**

A school grading system accepts marks between **0 and 100**.  
Which of the following is an example of **abnormal data**?

- **A) 50**
- **B) 100**
- **C) “Ninety”**
- **D) 0**

💡 **Hint:** Abnormal data is something **completely incorrect**.

---

### **Question 2: Understanding Extreme Data**

A login system only accepts **passwords with 8 to 12 characters**.  
Which of the following is an example of **extreme data**?

- **A) A password with 10 characters**
- **B) A password with 8 characters**
- **C) A password with 3 characters**
- **D) A password with 12 characters**

💡 **Hint:** Extreme data is **at the limits** of the allowed range.

---

### **Question 3: Writing Pseudocode for Testing**

Write **pseudocode** for a program that:

1. Asks the user to enter a **temperature between -50 and 50**.
2. Checks if the input is within range.
3. Displays **“Valid temperature”** or **“Invalid temperature”**.

💡 **Hint:** Use a **range check**.

---

### **Question 4: Debugging a Code**

A student wrote this program to check if a number is positive:

```
INPUT Number

IF Number > 0 THEN

OUTPUT "Positive"

ELSE

OUTPUT "Negative"
```

What mistake did they make?

- **A) No check for zero**
- **B) Syntax error in OUTPUT**
- **C) Missing ELSE statement**
- **D) Using the wrong variable name**

💡 **Hint:** Zero is **neither positive nor negative**.

---

# **7.7 Trace Tables and Debugging**

Trace tables are used to **manually check** how an algorithm processes data **step by step**.  
They help find **logic errors**, track **variable changes**, and understand how an algorithm works.

Debugging is the process of **identifying and fixing errors** in a program.

---

## **7.7.1 Completing a Trace Table**

A **trace table** records the values of **variables** at each step of an algorithm.

### **Example Algorithm (Finding Sum of First 3 Numbers)**

```
Sum ← 0

FOR i ← 1 TO 3 DO

Sum ← Sum + i

NEXT i

OUTPUT Sum
```

### **Trace Table**

| Step | i | Sum | Output |
| --- | --- | --- | --- |
| 1 | 1 | 1 (0+1) | – |
| 2 | 2 | 3 (1+2) | – |
| 3 | 3 | 6 (3+3) | – |
| 4 | – | – | 6 |

💡 **Final Output:** 6  
💡 **Purpose of Trace Table:** Helps us **verify** that the logic works correctly.

---

## **7.7.1.1 Tracking Variables, Outputs, and User Prompts**

### **Example Algorithm (Checking Even or Odd)**

```
INPUT Num

IF Num MOD 2 = 0 THEN

OUTPUT "Even"

ELSE

OUTPUT "Odd"

END IF
```

#### **Trace Table Example**

| Step | Num | Condition (Num MOD 2 = 0) | Output |
| --- | --- | --- | --- |
| 1 | 4 | TRUE | “Even” |
| 2 | 5 | FALSE | “Odd” |

💡 **Why use a trace table?** To **verify each step** and check for **errors**.

---

## **7.7.2 Identifying and Fixing Errors in Algorithms**

Errors in a program can be:

1. **Syntax Errors** – Grammar mistakes in the code (e.g., missing `END IF`).
2. **Logic Errors** – Wrong calculations or conditions (e.g., `x - y` instead of `x + y`).
3. **Runtime Errors** – Errors that crash the program (e.g., dividing by zero).

### **Example: Debugging an Algorithm**

A student wrote this algorithm to find the largest of two numbers:

```
INPUT A, B

IF A > B THEN

OUTPUT "Largest is ", A

ELSE

OUTPUT "Largest is ", A

END IF
```

💡 **Error:** The second `OUTPUT` should print **B**, not **A**.  
**Fixed Version:**

```
IF A > B THEN

OUTPUT "Largest is ", A

ELSE

OUTPUT "Largest is ", B

END IF
```

---

# task 7.7

### **Question 1: Understanding Trace Tables**

What will be the **final value of Sum** after this algorithm runs?

```
Sum ← 0

FOR i ← 1 TO 4 DO

Sum ← Sum + i

NEXT i

OUTPUT Sum
```

| Step | i | Sum |
| --- | --- | --- |
| 1 | 1 | 1 |
| 2 | 2 | 3 |
| 3 | 3 | 6 |
| 4 | 4 | ? |

- **A) 6**
- **B) 10**
- **C) 7**
- **D) 4**

💡 **Hint:** Keep adding `i` to `Sum`.

---

### **Question 2: Identifying Errors**

A student wrote this program:

```
INPUT Number

IF Number > 0 THEN

OUTPUT "Positive"

ELSE

OUTPUT "Negative"
```

What mistake did they make?

- **A) No check for zero**
- **B) Syntax error in OUTPUT**
- **C) Missing ELSE statement**
- **D) Using the wrong variable name**

💡 **Hint:** Zero is **neither positive nor negative**.

---

### **Question 3: Completing a Trace Table**

Given this algorithm:

```
Num ← 10

WHILE Num > 0 DO

Num ← Num - 2

OUTPUT Num

END WHILE
```

Fill in the missing values in the trace table.

| Step | Num (Before) | Num – 2 | Num (After) | Output |
| --- | --- | --- | --- | --- |
| 1 | 10 | 8 | ? | ? |
| 2 | 8 | ? | ? | ? |
| 3 | 6 | ? | ? | ? |

💡 **Hint:** Subtract 2 each time.

---

### **Question 4: Writing Pseudocode for Debugging**

Write **pseudocode** for an algorithm that:

1. Accepts a number.
2. Checks if the number is a **multiple of 5**.
3. Outputs **“Multiple of 5”** or **“Not a multiple of 5”**.

💡 **Hint:** Use `MOD` operator to check divisibility.

---

# **7.8 Writing and Modifying Algorithms**

An **algorithm** is a **step-by-step set of instructions** designed to solve a problem. Writing and modifying algorithms requires understanding how to **structure logic**, use **loops**, **conditional statements**, and handle **data correctly**.

### **7.8.1 Writing and Amending Algorithms**

Algorithms can be represented using:

**Pseudocode** – A structured, language-independent way to write logic.

**Program Code** – The actual implementation in a programming language.

**Flowcharts** – A visual representation of the logic.

---

## **7.8.1.1 Writing Algorithms Using Pseudocode**

Pseudocode uses simple English-like statements to describe the steps of an algorithm.

### **Example: Find the Largest of Two Numbers**

```
INPUT A, B

IF A > B THEN

OUTPUT "Largest is ", A

ELSE

OUTPUT "Largest is ", B

END IF
```

**Why use pseudocode?** It **doesn’t depend on a specific programming language** and helps plan the solution.

---

## **7.8.1.2 Writing Algorithms Using Program Code**

Once an algorithm is written in **pseudocode**, it can be converted into an actual programming language.

### **Example (Python Code for Finding the Largest of Two Numbers)**

```
A = int(input("Enter first number: "))

B = int(input("Enter second number: "))

if A > B:

print("Largest is", A)

else:

print("Largest is", B)
```

**Why convert to code?** The **computer can execute the instructions** to give the desired output.

---

## **7.8.1.3 Writing Algorithms Using Flowcharts**

Flowcharts use symbols to **visually represent an algorithm**.

### **Example: Flowchart for Checking Even or Odd Numbers**

[![Flowchart depicting a simple algorithm to determine if a number is positive or negative, including steps for input and output.](images/topic7_algorithm_design/ch_07_algorithm_design_and_problem_solving/img_001.png)](https://i0.wp.com/moshikur.com/wp-content/uploads/2026/01/ChatGPT-Image-Jan-16-2026-11_54_32-PM-1.png?ssl=1)

**Why use flowcharts?** They help **visualize** how the program flows.

---

# **Modifying Algorithms**

Sometimes, an existing algorithm needs **improvement or modification** to:

- **Optimize performance**
- **Add new features**
- **Fix errors (debugging)**

### **Example: Modifying an Algorithm**

A student wrote this algorithm to add **two numbers**, but now wants it to **add three numbers**.

```
INPUT A, B

Sum ← A + B

OUTPUT "Sum is ", Sum
```

**Modified Version (Adding Three Numbers):**

```
INPUT A, B, C

Sum ← A + B + C

OUTPUT "Sum is ", Sum
```

**Modification:** Added a third input **C** and updated the sum calculation.

---

# **task 7.8**

### **Question 1: Understanding Pseudocode**

What will be the output of the following pseudocode if the user enters `A = 8` and `B = 12`?

```
INPUT A, B

IF A > B THEN

OUTPUT "A is greater"

ELSE

OUTPUT "B is greater"

END IF
```

- **A) A is greater**
- **B) B is greater**
- **C) No output**
- **D) Error in code**

💡 **Hint:** Compare `A` and `B` values.

---

### **Question 2: Identifying Errors in an Algorithm**

A student wrote this pseudocode:

```
INPUT Num

IF Num MOD 2 = 0 THEN

OUTPUT "Odd"

ELSE

OUTPUT "Even"

END IF
```

What mistake did they make?

- **A) Condition is reversed**
- **B) Syntax error in OUTPUT**
- **C) Missing ELSE statement**
- **D) Loop is needed**

💡 **Hint:** Even numbers are divisible by `2`.

---

### **Question 3: Writing Pseudocode**

Write **pseudocode** for an algorithm that:

1. Takes a number as input.
2. Checks whether the number is **positive, negative, or zero**.
3. Outputs **“Positive”**, **“Negative”**, or **“Zero”**.

💡 **Hint:** Use **IF-ELSE conditions**.

---

### **Question 4: Modifying an Algorithm**

A student wrote an algorithm that calculates the **average of two numbers**:

```
INPUT A, B

Average ← (A + B) / 2

OUTPUT "Average is ", Average
```

Modify it to **calculate the average of four numbers**.

💡 **Hint:** Add **two more inputs** and adjust the formula.

---

### Leave a Reply[Cancel reply](/igcse-o-level-cs/ch-07-algorithm-design-and-problem-solving/#respond)