# CH 10 Boolean Logic

> Source: https://moshikur.com/igcse-o-level-cs/ch-10-boolean-logic/

# CH 10 Boolean Logic

---

## **10.1 Logic Gates**

- **10.1.1** Identify and use the standard symbols for logic gates
  - NOT gate
  - AND gate
  - OR gate
  - NAND gate
  - NOR gate
  - XOR (EOR) gate
- **10.1.2** Define and understand the functions of logic gates
  - Behavior of each gate
  - Single input (NOT) and two inputs (others)

## **10.2 Logic Circuits**

- **10.2.1** Use logic gates to create logic circuits from:
  - **10.2.1.1** A problem statement
  - **10.2.1.2** A logic expression
  - **10.2.1.3** A truth table
- **10.2.2** Circuits must be drawn for the statement given without simplification
- **10.2.3** Circuits limited to a maximum of three inputs and one output

## **10.3 Truth Tables**

- **10.3.1** Complete a truth table from:
  - **10.3.1.1** A problem statement
  - **10.3.1.2** A logic expression
  - **10.3.1.3** A logic circuit
- **10.3.2** Example format:  
  Columns for each input and the corresponding output.

## **10.4 Logic Expressions**

- **10.4.1** Write a logic expression from:
  - **10.4.1.1** A problem statement
  - **10.4.1.2** A logic circuit
  - **10.4.1.3** A truth table

---

# 10.1 **Logic Gates**

---

## What are Logic Gates?

- Computers **make decisions** using **logic gates**.
- A **logic gate** takes **input signals** (0 or 1) and **produces an output** (0 or 1).
- 0 means **OFF** (no electricity), and 1 means **ON** (electricity flows).

Think of logic gates like **small machines** that follow simple rules!

---

## Standard Logic Gates You Need to Know:

There are **6 gates** you must learn:

- **NOT**
- **AND**
- **OR**
- **NAND**
- **NOR**
- **XOR** (also called EOR)

Let’s go through them one by one!

---

# 1. NOT Gate 🔄

[![](images/topic10_boolean_logic/ch_10_boolean_logic/img_001.png)](https://i0.wp.com/moshikur.com/wp-content/uploads/2025/04/image-16.png?ssl=1)

**NOT** means **opposite**.

- If you input a 0, output is 1.
- If you input a 1, output is 0.

| Input | Output |
| --- | --- |
| 0 | 1 |
| 1 | 0 |

---

# 2. AND Gate

[![](images/topic10_boolean_logic/ch_10_boolean_logic/img_002.png)](https://i0.wp.com/moshikur.com/wp-content/uploads/2025/04/image-17.png?ssl=1)

**AND** needs **both inputs** to be 1 to give 1.

Otherwise, it gives 0.

| A | B | Output |
| --- | --- | --- |
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

**Symbol:**

---

# 3. OR Gate ➕

[![](images/topic10_boolean_logic/ch_10_boolean_logic/img_003.png)](https://i0.wp.com/moshikur.com/wp-content/uploads/2025/04/image-18.png?ssl=1)

**OR** gives 1 if **either** input is 1.

| A | B | Output |
| --- | --- | --- |
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 1 |

Shaped like a spaceship 🚀.

---

# 4. NAND Gate 🚫

[![](images/topic10_boolean_logic/ch_10_boolean_logic/img_004.png)](https://i0.wp.com/moshikur.com/wp-content/uploads/2025/04/image-19.png?ssl=1)

**NAND** is **AND** followed by **NOT**.

So, **reverse** the AND output.

| A | B | Output |
| --- | --- | --- |
| 0 | 0 | 1 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

**Symbol:**  
AND gate shape + small circle.

---

# 5. NOR Gate 🚫➡️

[![](images/topic10_boolean_logic/ch_10_boolean_logic/img_005.png)](https://i0.wp.com/moshikur.com/wp-content/uploads/2025/04/image-20.png?ssl=1)

- **NOR** is **OR** followed by **NOT**.
- So, **reverse** the OR output.

| A | B | Output |
| --- | --- | --- |
| 0 | 0 | 1 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 0 |

**Symbol:**  
OR gate shape + small circle.

---

# 6. XOR Gate

- **XOR** means **only one input must be 1**.
- If both inputs are the same, output is 0.

| A | B | Output |
| --- | --- | --- |
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

**Symbol:**  
OR gate but with **extra curved line**.

---

# 🎯 Important Tips:

- **NOT** only has **1 input**. All others have **2 inputs**.
- Learn the **symbols carefully** — drawing the wrong one loses marks!
- **Practice truth tables** — they come a lot in the exam.
- **Don’t simplify** expressions unless the question asks!

---

# 📋 Quick Summary Table

| Gate | Rule | Symbol Shape |
| --- | --- | --- |
| NOT | Opposite | Triangle + small circle |
| AND | Both must be 1 | D-shape |
| OR | Either 1 or both | Curved spaceship |
| NAND | AND then NOT | D-shape + circle |
| NOR | OR then NOT | Curved spaceship + circle |
| XOR | Only one input 1 | Curved spaceship + extra line |

# 10.2 – Logic Circuits

---

## What are Logic Circuits?

- **Logic circuits** are made by **connecting multiple logic gates** together.
- They take **inputs** (0 or 1), process them using gates (NOT, AND, OR, etc.), and produce an **output**.
- Logic circuits are used **inside computers**, **phones**, and **other devices** to control how they behave.

---

## What You Must Be Able to Do in Exams:

✅ **Draw** a logic circuit from:

- a **problem statement**
- a **logic expression**
- a **truth table**

✅ **Create** a logic expression from:

- a **logic circuit diagram**.

✅ **Complete** a truth table for a given:

- **logic circuit** or **logic expression**.

✅ **Important rules**:

- **Do NOT simplify** unless the question says so.
- Maximum of **three inputs** (A, B, C).
- Maximum of **one output** (usually X or Z).
- **Each logic gate** should have **only two inputs** at most (except NOT, which has one).

---

## How to Read and Draw Logic Circuits:

### Step 1: Inputs

- Inputs are usually **A**, **B**, and **C**.
- Inputs flow from **left to right** across the circuit.

---

### Step 2: Gates

- Each gate **processes** the signals according to its rule:
  - AND → both inputs must be 1 to give 1.
  - OR → either input must be 1 to give 1.
  - NOT → flips the signal.
  - NAND → AND then flip.
  - NOR → OR then flip.
  - XOR → only one input 1 gives output 1.

---

### Step 3: Output

- The final gate produces the **output** (X or Z).

---

# 🎯 Important Techniques

### 1. Reading from a logic circuit

- Start from the **inputs** and follow the wires.
- Find what each small section does.
- Combine the small parts step-by-step.
- Write the **logic expression**:
  - Example:
    - If a NOT gate is used on A → becomes NOT A
    - If an AND gate combines (NOT A) and B → becomes (NOT A AND B)
    - If an OR gate combines two outputs → (…OR…)

---

### 2. Drawing a circuit from a logic expression

- Break down the expression into **small parts**.
- Start with NOT gates first if needed.
- Use two-input gates (AND, OR) properly.
- Connect the outputs carefully.
- Example:
  - Expression: (NOT A AND B) OR NOT C
  - Draw NOT gate for A.
  - Draw AND gate for (NOT A and B).
  - Draw NOT gate for C.
  - Then use an OR gate to combine the two outputs.

---

# 🛠 Working Example (Simple)

### Expression:

X=(A OR B) AND (NOT B AND C)X = (A \text{ OR } B) \text{ AND } (\text{NOT } B \text{ AND } C)

### Steps:

- Draw OR gate between A and B.
- Draw NOT gate for B.
- Draw AND gate between (NOT B) and C.
- Finally, AND the two results together to get X.

---

# 📋 Common Mistakes to Avoid:

- ❌ Connecting three wires into one gate (only 2 inputs allowed!).
- ❌ Missing out NOT gates when needed.
- ❌ Drawing wrong symbols for gates.
- ❌ Simplifying expressions when you were not asked.

---

# 🌟 Quick Checklist Before Submitting Logic Circuits:

| Check | Why important? |
| --- | --- |
| Two inputs per gate maximum? | Otherwise wrong drawing |
| NOT gates placed correctly? | Otherwise wrong outputs |
| Correct symbols for each gate? | Mark lost if wrong symbol |
| Final output labeled (X or Z)? | Otherwise mark lost |

# 10.3 – Truth Tables

---

## What is a Truth Table?

- A **truth table** shows **all possible combinations of inputs** and the **resulting output**.
- It helps you understand how a **logic gate**, a **logic expression**, or a **logic circuit** behaves.
- It **lists every possibility**:  
  Example:  
  If there are 3 inputs (A, B, C), there are 23=82^3 = 8 rows.

---

## When Do We Use Truth Tables?

✅ To find the output of a **logic expression**.  
✅ To find the output of a **logic circuit**.  
✅ To check how a **problem description** behaves.

---

## How to Build a Truth Table:

### Step 1: List all input combinations

If there are:

- 1 input → 2 rows (0, 1)
- 2 inputs → 4 rows (00, 01, 10, 11)
- 3 inputs → 8 rows

| A | B | C |
| --- | --- | --- |
| 0 | 0 | 0 |
| 0 | 0 | 1 |
| 0 | 1 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 0 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |
| 1 | 1 | 1 |

---

### Step 2: Follow the logic step-by-step

Use the gates or expression rules for each row:

- Work out the outputs of small parts first (e.g., NOT A, A AND B).
- Then combine them step-by-step.

---

### Step 3: Fill in the final output

After calculating all parts, write the **final output (X or Z)** for each input combination.

---

# ✏️ Example:

Given: X=(A OR B) AND (NOT C)

| A | B | C | A OR B | NOT C | (A OR B) AND (NOT C) → X |
| --- | --- | --- | --- | --- | --- |
| 0 | 0 | 0 | 0 | 1 | 0 |
| 0 | 0 | 1 | 0 | 0 | 0 |
| 0 | 1 | 0 | 1 | 1 | 1 |
| 0 | 1 | 1 | 1 | 0 | 0 |
| 1 | 0 | 0 | 1 | 1 | 1 |
| 1 | 0 | 1 | 1 | 0 | 0 |
| 1 | 1 | 0 | 1 | 1 | 1 |
| 1 | 1 | 1 | 1 | 0 | 0 |

---

# 🎯 How to Tackle Truth Table Questions:

### 1. Identify small steps

- Break the big expression into smaller parts.
- Solve step-by-step: NOT first, then AND/OR/NAND etc.

### 2. Build helping columns

- Use extra columns like “NOT A” or “A AND B” if needed.
- Cambridge expects neat working space!

### 3. Double-check

- Some errors happen if you forget brackets or NOT operations.
- Always check parentheses first!

---

# 📋 Common Mistakes To Avoid:

| Mistake | Why it matters |
| --- | --- |
| Missing a row | Truth table incomplete |
| Wrong NOT application | Opposite result |
| Wrong number of rows | Wrong number of combinations |
| Ignoring brackets | Wrong logic order |

---

# ✨ Quick Tips:

- **NOT** first, **AND** second, **OR** last (if multiple operations).
- If unsure, quickly draw a mini circuit to help yourself.
- Practice solving truth tables **fast** because in exam you get 4–5 marks easily here!

---

# TASKS

---

## **Question 1**

The logic expression for a circuit is:

## X=(A AND (NOTB)) OR (B AND (NOTC))

Complete the truth table for the expression.

| A | B | C | NOT B | NOT C | A AND NOT B | B AND NOT C | X |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 0 | 0 | | | | | |
| 0 | 0 | 1 | | | | | |
| 0 | 1 | 0 | | | | | |
| 0 | 1 | 1 | | | | | |
| 1 | 0 | 0 | | | | | |
| 1 | 0 | 1 | | | | | |
| 1 | 1 | 0 | | | | | |
| 1 | 1 | 1 | | | | | |

[6]

---

## **Question 2**

Draw a logic circuit that matches the following problem description:

> “An alarm system turns ON (output 1) if either:
>
> - Door sensor (D) is open, OR
> - Window sensor (W) is open,  
>   but only if the system is not disarmed (Disarmed = 0).”

Use standard logic gate symbols. [5]

---

## **Question 3**

Here is a description of a logic circuit:

- Input A passes through a NOT gate.
- Inputs B and C go into an AND gate.
- The outputs from the NOT gate and the AND gate go into an OR gate to produce X.

Write the logic expression for X. [3]

---

## **Question 4**

Which logic gate has an output of 1 **only when exactly one input is 1**?  
Tick (✓) the correct answer.

- AND
- OR
- XOR
- NAND

[1]

---

## **Question 5**

State the names of the following gates based on their behavior:

(a) Produces 0 when both inputs are 1, otherwise produces 1. [1]

(b) Produces 1 when at least one input is 1. [1]

(c) Produces 1 only when both inputs are 1. [1]

---

### Leave a Reply[Cancel reply](/igcse-o-level-cs/ch-10-boolean-logic/#respond)