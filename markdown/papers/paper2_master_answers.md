# IGCSE Computer Science Paper 2 - Master Consolidated Answers

This document consolidates all question types and answers from 2021-2024 papers, organized by syllabus topics 7 through 11.

---

## Topic 7: Algorithm Design and Problem-Solving

### 7.1 Program Development Life Cycle

#### Identify or match stages of the PDLC
- Analysis → understand the problem, define requirements, identify inputs/outputs/processes
- Design → create algorithm (pseudocode / flowchart / structure diagram), plan data structures
- Coding → translate design into a programming language
- Testing → run the program with test data, check correctness, find and fix errors
- Maintenance → update or modify the program after release

**State the purpose of the analysis stage**
- Understand and define the problem fully
- Identify what data is input, what processing is needed, and what output is required
- Define success criteria and requirements

**Describe the analysis stage tasks**
- Identify inputs, outputs and processes required
- Research the current system / interview stakeholders
- Write a requirements specification
- Decompose the problem into manageable parts

---

### 7.2 Problem Decomposition

**Describe abstraction**
- Abstraction means removing unnecessary detail from a problem
- Only the relevant information is kept and modelled
- Simplifies the problem so it is easier to solve

**Identify three component parts when decomposing a problem**
- Inputs
- Outputs
- Processes (or: storage / sequence / decision / repetition)

**Describe what a grades algorithm does**
- Reads student marks / scores
- Compares each mark to grade boundaries
- Assigns a grade (e.g., Distinction, Pass, Fail) and stores it in an array

---

### 7.3 Algorithm Design Methods

**Name three methods used to design an algorithm**
- Pseudocode
- Flowchart
- Structure diagram

**Describe the three design methods**
- Pseudocode: uses English-like statements to describe program logic; easy to convert to code
- Flowchart: uses standard symbols connected by arrows to show flow of execution; visual representation
- Structure diagram: shows decomposition of a problem into modules/sub-tasks; top-down hierarchy

**Match flowchart symbols**
- Oval / rounded rectangle → start / end (terminator)
- Rectangle → process / statement
- Diamond → decision / condition
- Parallelogram → input / output
- Rectangle with double lines / striped sides → subroutine call

**Complete or draw a flowchart**
- Start with a terminator (Start/Stop)
- Use parallelogram for all INPUT and OUTPUT statements
- Use rectangle for all assignment and process statements
- Use diamond for all conditions (IF / WHILE / REPEAT)
- Flow arrows must connect all symbols; YES/NO (or TRUE/FALSE) paths must be labelled on decision symbols

---

### 7.4 Standard Methods of Solution

**Bubble sort — how it works**
- Compare adjacent elements in the array
- If the left element is greater than the right, swap them
- Repeat for each pair along the array (one pass)
- Repeat passes until no swaps occur in a full pass (array is sorted)

**Bubble sort — how to make it more efficient**
- Add a Boolean flag (swapped) that is set to TRUE whenever a swap occurs
- If a full pass completes with swapped = FALSE, the array is already sorted → exit loop early
- This avoids unnecessary comparisons on already-sorted data

**Find largest and smallest value in a list**
- Set Large and Small to the first input value before the loop
- Loop through all remaining values
- If current value > Large, update Large
- If current value < Small, update Small
- After loop: calculate range = Large − Small and output all three

**Sentinel value algorithm**
- Input a value
- Use a WHILE or REPEAT loop that continues until the sentinel value is entered
- Inside loop: process the value (accumulate total, increment count, etc.)
- After loop: output result (total, average, count)

**Linear search**
- Start from the first element
- Compare each element to the target value
- If found, record position and stop (or set Found flag to TRUE)
- If end of array is reached without a match, report not found

---

### 7.5 Validation and Verification

**Types of validation check**
- Range check: ensures the value falls within an acceptable minimum and maximum (e.g., 1 to 100)
- Length check: ensures the input has the correct number of characters (e.g., exactly 8 characters)
- Type check: ensures the input is the correct data type (e.g., integer, not text)
- Format check: ensures the input follows a required pattern (e.g., DD/MM/YYYY)
- Presence check: ensures a required field is not left empty
- Check digit: a calculated digit appended to a code that validates the entire sequence

**Write validation pseudocode (range check with re-entry loop)**
```
INPUT Value
WHILE Value < Min OR Value > Max DO
    OUTPUT "Invalid input, please re-enter"
    INPUT Value
ENDWHILE
```
Or using REPEAT...UNTIL:
```
REPEAT
    INPUT Value
    IF Value < Min OR Value > Max THEN
        OUTPUT "Invalid input"
    ENDIF
UNTIL Value >= Min AND Value <= Max
```

**Write validation pseudocode (length / format check)**
```
INPUT Code
WHILE LENGTH(Code) <> RequiredLength DO
    OUTPUT "Invalid length, please re-enter"
    INPUT Code
ENDWHILE
```

**Check digit — how it is calculated (weighted)**
- Multiply each digit in the number by its positional weight
- Sum all the products
- Calculate check digit = sum MOD 10 (or another modulus)
- Append the check digit to form the complete code

**Verification — double entry**
- User enters the same data twice
- Program compares both entries
- If they match: data is accepted
- If they do not match: user is prompted to re-enter

**Verification — proofreading**
- Data entered is displayed back to the user on screen
- User reads it carefully and checks for accuracy
- User confirms if correct or corrects if wrong

**Classifying checks as validation or verification**
- Validation: program checks automatically that data is reasonable / correct type / correct format / in range
- Verification: checks that data has been entered correctly / matches an original source (double entry or proofreading)
- Neither: a process that is neither validation nor verification

---

### 7.6 Testing

**Types of test data**
- Normal (valid): data within the expected range that should be accepted
- Boundary (extreme): data at the exact edge of the valid range (should be accepted); just outside the boundary (should be rejected)
- Erroneous (abnormal / invalid): data outside the valid range or wrong type that should be rejected

**Give test data for a range check (e.g., 1 to 100)**

| Type | Example | Expected Outcome |
|------|---------|-----------------|
| Normal | 50 | Accepted |
| Boundary (lower) | 1 | Accepted |
| Boundary (upper) | 100 | Accepted |
| Boundary (just outside) | 0 or 101 | Rejected |
| Erroneous | −5, 200, "abc" | Rejected |

**Why extreme/boundary test data is used**
- Values at the exact boundary are most likely to expose off-by-one errors in conditions (e.g., > vs >=)

---

### 7.7 Trace Tables

**How to complete a trace table**
- List all variables in the algorithm as column headings
- Read the algorithm line by line
- Each time a variable changes value, record the new value in its column on the current row
- Record OUTPUT values when an output statement is reached
- Complete one row per significant state change or per iteration

**Purpose of trace tables**
- Used to dry-run (manually execute) an algorithm without running it on a computer
- Allows errors to be identified by checking actual variable values against expected values

**Algorithm purpose — describe what the algorithm does**
- State what inputs it takes
- Describe the process (e.g., sorts, finds max/min, calculates, filters)
- State what it outputs

---

### 7.8 Error Identification

**Types of errors**
- Syntax error: code that does not follow the rules of the language (e.g., missing keyword, wrong operator)
- Logic error: code that runs but produces incorrect results (e.g., wrong condition, wrong variable used, off-by-one error)
- Runtime error: code that causes the program to crash during execution (e.g., division by zero, accessing beyond array bounds)

**Common algorithm errors to look for**
- Wrong variable name used
- Wrong comparison operator (e.g., > instead of >=, = instead of <>)
- Missing or incorrect loop condition
- Incorrect counter initialisation (e.g., starting at 1 instead of 0)
- Wrong accumulation (overwriting instead of adding)
- Missing or extra quotation marks around string literals
- Incorrect assignment direction (e.g., 0 ← Counter instead of Counter ← 0)

---

## Topic 8: Programming

### 8.1 Programming Concepts

#### Operators
**Types of operators**
- Arithmetic: +, −, *, /, MOD (remainder), DIV (integer division), ^ (power)
- Comparison: =, <>, <, >, <=, >=
- Boolean (logical): AND, OR, NOT
- String: & (concatenation)

**DIV and MOD**
- DIV: integer division, returns the whole-number quotient (e.g., 17 DIV 5 = 3)
- MOD: returns the remainder of integer division (e.g., 17 MOD 5 = 2)
- Use MOD to test divisibility (e.g., Number MOD 2 = 0 → even number)

**RANDOM**
- RANDOM(a, b) generates a random integer between a and b inclusive

**ROUND**
- ROUND(value, decimal_places) rounds a number to the specified number of decimal places
- Example: ROUND(3.7654, 2) → 3.77

#### Data Types
**Integer** — whole numbers, no decimal part (e.g., 42, −7, 0)

**Real** — numbers with a decimal/fractional part (e.g., 3.14, −0.5)

**Boolean** — only two values: TRUE or FALSE

**String** — sequence of characters (text), e.g., "Hello", "AB123"

**Char** — a single character, e.g., 'A', '5'

#### Constants and Variables
**Variable** — a named location in memory whose value can change during program execution

**Constant** — a named location in memory whose value is set once and cannot change during execution

**When to use a constant**
- When a value does not change (e.g., VAT rate, maximum array size, PI)
- Makes code more readable and easier to update (change in one place only)

**Declare a constant**
```
CONSTANT Name ← Value
```

#### Control Structures
**IF selection**
```
IF condition THEN
    statements
ELSE
    statements
ENDIF
```

**CASE selection**
```
CASE OF variable
    value1: statement
    value2: statement
    OTHERWISE: statement
ENDCASE
```

**WHILE loop (pre-condition)**
```
WHILE condition DO
    statements
ENDWHILE
```
- Condition checked before the loop body executes
- May execute zero times if condition is initially FALSE

**REPEAT...UNTIL loop (post-condition)**
```
REPEAT
    statements
UNTIL condition
```
- Condition checked after the loop body executes
- Always executes at least once

**FOR loop (count-controlled)**
```
FOR variable ← start TO end
    statements
NEXT variable
```
- Use when number of iterations is known in advance

#### Subroutines
**Procedure** — a named block of code that performs a task; does not return a value; called by name

**Function** — a named block of code that performs a task and returns a value to the calling program

**Parameter** — a value passed into a procedure or function when it is called

**Local variable** — a variable declared inside a subroutine; only accessible within that subroutine

**Global variable** — a variable declared outside all subroutines; accessible throughout the program

**Why use procedures**
- Avoids repeating the same code in multiple places (code reuse)
- Makes programs easier to read, test and maintain
- Each procedure can be developed and tested independently
- Reduces program length

#### String Manipulation Functions
**LENGTH(string)** — returns the number of characters in the string

**SUBSTRING(string, start, length)** — returns a portion of the string starting at position *start* for *length* characters

**UCASE(string)** — converts all characters in the string to uppercase

**LCASE(string)** — converts all characters in the string to lowercase

**String concatenation** — joining strings together using & (e.g., "Hello" & " " & "World")

#### Identifier Naming
**Why meaningful identifiers are important**
- Makes the program easier to read and understand
- Makes it easier to maintain and update
- Reduces the chance of errors when modifying code
- Other programmers can understand the purpose of each variable/constant without additional comments

**Features that improve maintainability**
- Meaningful identifiers (variable/constant names that describe their purpose)
- Comments explaining complex logic
- Constants instead of magic numbers (e.g., use MaxStudents instead of 30)
- Consistent indentation and formatting
- Modular design (use of procedures/functions)

---

### 8.2 Arrays

**What is a 1D array**
- A data structure that stores multiple values of the same data type
- Each value is accessed using a single index (e.g., Array[3])
- Size is fixed at the time of declaration
- All elements have the same data type

**Declare a 1D array**
```
DECLARE ArrayName : ARRAY[1:N] OF DataType
```
Example: `DECLARE Scores : ARRAY[1:30] OF INTEGER`

**Why a loop is needed to search an array**
- Each element must be checked individually
- A loop allows every element to be visited in sequence without repeating the same code N times

**Initialise an array using a FOR loop**
```
FOR Index ← 1 TO ArraySize
    Array[Index] ← 0
NEXT Index
```
- Advantage over manual assignment: requires fewer lines; works for any array size

**Traverse and output an array**
```
FOR Index ← 1 TO ArraySize
    OUTPUT Array[Index]
NEXT Index
```

**Find minimum value in an array**
```
Min ← Array[1]
FOR Index ← 2 TO ArraySize
    IF Array[Index] < Min THEN
        Min ← Array[Index]
    ENDIF
NEXT Index
OUTPUT Min
```

**What is a 2D array**
- A data structure that stores values in rows and columns
- Each element is accessed using two indices (e.g., Grid[row][col])
- Used for grids, tables, matrices

**Declare a 2D array**
```
DECLARE Grid : ARRAY[1:Rows, 1:Cols] OF DataType
```

**Output all elements of a 2D array**
```
FOR Row ← 1 TO NumRows
    FOR Col ← 1 TO NumCols
        OUTPUT Grid[Row][Col]
    NEXT Col
NEXT Row
```

---

### 8.3 File Handling

**Why store data in a file (instead of a variable)**
- Variables lose their values when the program ends; files persist between program runs
- Files allow large amounts of data to be stored permanently
- Data can be shared between different programs

**File handling keywords**
- OPENFILE: opens a file for reading or writing
- CLOSEFILE: closes the file after use (saves data and releases resources)
- READFILE: reads the next line/value from an open file
- WRITEFILE: writes a value or line to an open file

**Write pseudocode to write data to a file**
```
OPENFILE "filename.txt" FOR WRITE
WRITEFILE "filename.txt", DataValue
CLOSEFILE "filename.txt"
```

**Write pseudocode to read data from a file**
```
OPENFILE "filename.txt" FOR READ
READFILE "filename.txt", Variable
CLOSEFILE "filename.txt"
```

---

## Topic 9: Databases

### 9.1 Database Design

**What is a primary key**
- A field (or combination of fields) whose value uniquely identifies each record in a table
- No two records can have the same primary key value
- The primary key cannot be empty (null)

**Why the primary key must be unique**
- Each record must be individually identifiable
- Without uniqueness, it would be impossible to reliably locate, update or delete a specific record

**Choose a suitable primary key**
- Select a field whose value is unique for every record and will not change (e.g., ID number, code, serial number)
- A field like Name or Type is NOT suitable because values can repeat

**Common field data types**

| Data Type | Use |
|-----------|-----|
| Integer / Number | Whole numbers (counts, IDs, quantities) |
| Real / Currency | Decimal numbers, prices |
| Text / String | Names, codes, descriptions |
| Boolean | True/False flags (e.g., InStock, Active) |
| Date | Dates in standard format |
| Char | Single character |

---

### 9.2 SQL Queries

**Basic SQL SELECT structure**
```sql
SELECT field1, field2
FROM TableName
WHERE condition
ORDER BY field ASC/DESC
```

**Aggregate functions**
- `COUNT(field)` — counts the number of records matching the condition
- `SUM(field)` — totals all values in the specified field
- `MAX(field)` / `MIN(field)` — returns the highest / lowest value

**WHERE clause operators**
- `=`, `<>`, `<`, `>`, `<=`, `>=` — comparison operators
- `AND`, `OR`, `NOT` — combine multiple conditions
- `LIKE "pattern"` — pattern matching (% = wildcard)

**QBE (Query by Example) structure**

| Field | Table | Sort | Show | Criteria |
|-------|-------|------|------|----------|
| FieldName | TableName | ASC / DESC | ✓ (tick = show) | condition |

- Tick Show to include the field in results
- Leave Show blank to use the field for filtering only
- Enter criterion directly in the Criteria row (e.g., "A", <10, True, >0)
- Use Sort row for ASC (ascending) or DESC (descending)

---

## Topic 10: Boolean Logic

### 10.1 Logic Gates

**Standard logic gates**

| Gate | Symbol description | Output |
|------|--------------------|--------|
| AND | Flat input side, curved output | 1 only when ALL inputs are 1 |
| OR | Curved input and output | 1 when ANY input is 1 |
| NOT | Triangle with circle (inverter) | Inverts the input (0→1, 1→0) |
| NAND | AND gate with circle on output | Opposite of AND; 0 only when all inputs are 1 |
| NOR | OR gate with circle on output | Opposite of OR; 1 only when all inputs are 0 |
| XOR | OR gate with extra curved line | 1 only when inputs are DIFFERENT |

**Complete a truth table for common gates**

| A | B | AND | OR | NAND | NOR | XOR |
|---|---|-----|----|------|-----|-----|
| 0 | 0 | 0 | 0 | 1 | 1 | 0 |
| 0 | 1 | 0 | 1 | 1 | 0 | 1 |
| 1 | 0 | 0 | 1 | 1 | 0 | 1 |
| 1 | 1 | 1 | 1 | 0 | 0 | 0 |

---

### 10.2 Logic Circuits

**Write a Boolean expression from a circuit**
- Trace each gate from inputs to output
- Write the expression for each gate output step by step
- Combine into a single expression for the final output
- Example: NOT gate on A → NOT A; then AND with B → (NOT A) AND B

**Draw a logic circuit from a Boolean expression**
- Identify all individual gate operations in the expression
- Draw gates in the correct order (innermost brackets first)
- Connect outputs of earlier gates as inputs to later gates
- Label inputs (A, B, C) and final output (X or Z)

**Complete a truth table for a Boolean expression**
- List all combinations of inputs (for 3 variables: 8 rows; for 2 variables: 4 rows)
- Calculate intermediate values for each sub-expression
- Calculate the final output for each row

**Three-input truth table template**

| A | B | C | [sub-expression 1] | [sub-expression 2] | Output |
|---|---|---|--------------------|--------------------|--------|
| 0 | 0 | 0 | | | |
| 0 | 0 | 1 | | | |
| 0 | 1 | 0 | | | |
| 0 | 1 | 1 | | | |
| 1 | 0 | 0 | | | |
| 1 | 0 | 1 | | | |
| 1 | 1 | 0 | | | |
| 1 | 1 | 1 | | | |

---

## Topic 11: Scenario-Based Algorithm

### 11.1 Writing Pseudocode for Context Scenario

#### Declare a constant
```
CONSTANT Name ← Value
```
- Use CONSTANT keyword; assign a fixed value appropriate to the scenario
- A constant should be used when a value does not change (e.g., max players, number of courts, number of options)

#### Declare a variable
```
DECLARE Name : DataType
```
- Choose an appropriate data type: INTEGER, REAL, STRING, BOOLEAN, CHAR

#### Declare a 1D array
```
DECLARE ArrayName : ARRAY[1:Size] OF DataType
```
- Size should match the scenario requirement (e.g., number of courts, candidates, tables)
- Use a constant as the size where possible (e.g., ARRAY[1:MaxCandidates])

#### Generate a unique code
```
REPEAT
    Code ← RANDOM(1000, 9999)
    Unique ← TRUE
    FOR i ← 1 TO ArraySize
        IF CodeArray[i] = Code THEN
            Unique ← FALSE
        ENDIF
    NEXT i
UNTIL Unique = TRUE
```

#### Check availability and book a slot
```
INPUT SlotNumber
IF Available[SlotNumber] = TRUE THEN
    INPUT Name
    INPUT ContactDetail
    NameArray[SlotNumber] ← Name
    ContactArray[SlotNumber] ← ContactDetail
    Available[SlotNumber] ← FALSE
    OUTPUT "Booking confirmed"
ELSE
    OUTPUT "Not available"
ENDIF
```

#### Input validation (re-entry loop)
```
INPUT Value
WHILE Value < Min OR Value > Max DO
    OUTPUT "Invalid, please re-enter"
    INPUT Value
ENDWHILE
```

#### Count and display totals
```
Total ← 0
FOR i ← 1 TO N
    Total ← Total + Array[i]
NEXT i
OUTPUT "Total: ", Total
OUTPUT "Average: ", Total / N
```

#### Find maximum value and its position
```
MaxValue ← Array[1]
MaxPos ← 1
FOR i ← 2 TO N
    IF Array[i] > MaxValue THEN
        MaxValue ← Array[i]
        MaxPos ← i
    ENDIF
NEXT i
OUTPUT "Maximum: ", MaxValue, " at position ", MaxPos
```

#### Sort an array (bubble sort)
```
Swapped ← TRUE
WHILE Swapped = TRUE DO
    Swapped ← FALSE
    FOR i ← 1 TO N - 1
        IF Array[i] > Array[i+1] THEN
            Temp ← Array[i]
            Array[i] ← Array[i+1]
            Array[i+1] ← Temp
            Swapped ← TRUE
        ENDIF
    NEXT i
ENDWHILE
```

#### Assign rank from sorted position
```
FOR i ← 1 TO N
    Rank[i] ← i
NEXT i
```
(After sorting, position 1 = rank 1, position 2 = rank 2, etc.)

#### Modify a program to handle a variable number of items (instead of fixed constant)
- Replace the constant with a variable
- Input the number of items at the start of the program
- Use this variable as the array size bound and loop limit throughout

#### Modify a program to extend functionality (add counter, percentage, extra output)
- Add a new counter variable initialised to 0 before any loops
- Increment the counter inside the loop based on the relevant condition
- After the loop, calculate and output the required value (e.g., percentage = count / total × 100)

#### Program to count votes and display results per group
```
FOR i ← 1 TO TotalVoters
    INPUT VoterGroup    // e.g., "student" or "staff"
    INPUT VoteOption    // e.g., 1 to NumberOfOptions
    IF VoterGroup = "student" THEN
        StudentVotes[VoteOption] ← StudentVotes[VoteOption] + 1
    ELSE
        StaffVotes[VoteOption] ← StaffVotes[VoteOption] + 1
    ENDIF
NEXT i

FOR opt ← 1 TO NumberOfOptions
    OUTPUT "Option ", opt, " - Students: ", StudentVotes[opt]
    OUTPUT "Option ", opt, " - Staff: ", StaffVotes[opt]
    OUTPUT "Option ", opt, " - Total: ", StudentVotes[opt] + StaffVotes[opt]
NEXT opt
```

#### Write data to and read data from a file
```
// Write
OPENFILE "data.txt" FOR WRITE
WRITEFILE "data.txt", DataValue
CLOSEFILE "data.txt"

// Read
OPENFILE "data.txt" FOR READ
READFILE "data.txt", Variable
CLOSEFILE "data.txt"
```

#### Manage league standings (record, sort and display)
```
// Input results
FOR i ← 1 TO NumberOfTeams
    INPUT TeamName[i]
    INPUT Points[i]
NEXT i

// Bubble sort by Points descending
// (bubble sort with > replaced by < to sort descending)

// Display rankings
FOR i ← 1 TO NumberOfTeams
    OUTPUT i, " - ", TeamName[i], " - Points: ", Points[i]
NEXT i
```

#### 2D grid / board game pseudocode
```
// Initialise grid
FOR row ← 1 TO Rows
    FOR col ← 1 TO Cols
        Grid[row][col] ← 0
    NEXT col
NEXT row

// Validate move
INPUT Row
INPUT Col
WHILE Row < 1 OR Row > Rows OR Col < 1 OR Col > Cols DO
    OUTPUT "Invalid move"
    INPUT Row
    INPUT Col
ENDWHILE

// Make move
Grid[Row][Col] ← PlayerSymbol
```
