# Paper 2 Marking Scheme (2023)

This document organises the 2023 Paper 2 marking scheme answers by syllabus topic.

---

## 7. Algorithm Design and Problem-Solving

### 7.1 Program Development Life Cycle

#### **Match PDLC stage descriptions to their correct stage names** (4 marks — S23 V1 Q1a)
- develop an algorithm using structure diagrams, flowcharts or pseudocode → **design**
- detect and fix errors in the program → **testing**
- identify the problem and its requirements → **analysis**
- write and implement the instructions to solve the problem → **coding**

#### **Identify the four processes of the PDLC** (4 marks — W23 V1 Q6b)
- analysis
- design
- coding
- testing

#### **Identify the first stage of the Program Development Life Cycle** (1 mark — S23 V2 Q1)
- A — analysis

#### **Identify the PDLC stage where a solution algorithm is created** (2 marks — W23 V1 Q5c)
- design (stage where algorithm is developed using flowcharts, pseudocode or structure diagrams)

---

### 7.2 Problem Decomposition

#### **Describe the concept of abstraction in the PDLC** (2 marks — W23 V1 Q5a)
- abstraction is the process of removing unnecessary detail / focusing only on relevant information
- … to allow the problem to be represented in a simplified form that can be solved

#### **Name three component parts found when decomposing a problem** (3 marks — W23 V1 Q5b; S23 V1 Q1b)
- inputs // what is put into the system
- processes // actions taken to achieve a result
- outputs // what is taken out of the system
- storage // what needs to be kept for future use
*(any three for 3 marks)*

---

### 7.3 Algorithm Design Methods

#### **Name three methods used to present an algorithm design** (3 marks — S23 V2 Q3; W23 V1 Q5c context)
- structure diagram / chart
- flowchart
- pseudocode

---

### 7.4 Standard Methods of Solution

#### **Identify the type of search algorithm used in a phonetic look-up** (1 mark — S23 V1 Q7b)
- (linear) search

#### **Describe the purpose of a bubble sort algorithm** (2 marks — S23 V2 Q9b; W23 V1 Q6a)
- (bubble) sort data in array
- … in ascending order
*(also: sort names into alphabetical order)*

#### **Complete a trace table for a bubble sort on an array of five values** (5 marks — S23 V2 Q9a)
- One mark for each correct column: F, C, X[1] to X[5] all entries correct (2 marks), T
- Array X = [10, 1, 5, 7, 11]; after sorting produces [1, 5, 7, 10, 11]
- Trace shows F (flag), C (counter), swaps and T (total/temp variable)

---

### 7.5 Validation and Verification

#### **Define data validation and explain its purpose** (2 marks — S23 V1 Q3a)
- validation is an automated check carried out by a computer
- … to make sure the data entered is sensible / acceptable / reasonable

#### **Identify validation checks appropriate for given inputs** (various)

**Range check** (W23 V1 Q8a; S23 V1 Q3a context; S23 V2 Q4a):
- range check — checks value is within an acceptable range (e.g. greater than zero AND less than 1000)

**Format check** (W23 V2 Q2a):
- format check — checks that data matches a required pattern or format

**Length check** (W23 V2 Q2c; S23 V2 Q4a):
- length check — checks the number of characters entered is within expected limits
- … to ensure there are no more than the required digits/characters

**Presence check** (S23 V2 Q4a):
- presence check — ensures the field is not left empty, will not continue until a value has been entered

**Type/character check** (W23 V3 Q4a; S23 V2 Q4a):
- type check / character check — ensures data entered is the correct data type (e.g. a number)

#### **Match validation check descriptions to check names** (4 marks — S23 V3 Q5a)
- to check that the data entered is an integer → **type check**
- to check that some data has been entered → **presence check**
- to check that the data entered has an appropriate number of characters → **length check**
- to check that an identification number contains no errors → **check digit**

#### **Write pseudocode to validate input using a length check (15–35)** (3 marks — S23 V3 Q5b)
```
WHILE Loop:
OUTPUT "Enter a number between 15 and 35 inclusive"
INPUT Length
WHILE Length < 15 OR Length > 35 DO
    OUTPUT "Your number must be between 15 and 35 inclusive"
    INPUT Length
ENDWHILE

REPEAT Loop:
REPEAT
    OUTPUT "Enter a number between 15 and 35 inclusive"
    INPUT Length
UNTIL Length >= 15 AND Length <= 35
```

#### **Write pseudocode for double entry verification** (3 marks — S23 V2 Q4b ii)
- use of iteration
- use of two inputs
- check that two inputs are the same / different
```
REPEAT
    OUTPUT "Please enter measurement"
    INPUT Measurement
    OUTPUT "Please re-enter measurement"
    INPUT MeasurementCheck
UNTIL Measurement = MeasurementCheck
```

#### **Explain why verification is used when copying data** (2 marks — S23 V3 Q4a)
- to ensure that data has been accurately copied // to ensure that changes have not been made to values originally intended
- … from one source to another

#### **Describe two types of verification checks with their uses** (4 marks — S23 V3 Q4b)
- Verification check 1 — **Visual check**: the user looks through the data that has been entered and confirms that no changes have been made
- Verification check 2 — **Double data entry**: data is entered twice, the two entries are compared, and if they do not match, a re-entry is requested

#### **Explain why double entry is used as verification** (1 mark — S23 V2 Q4b i)
- to verify the data / for verification / as a verification check // to make sure that no changes are made to the data on entry

#### **Write pseudocode to validate a single-digit input** (4 marks — S23 V2 Q7c)
- one mark for place in algorithm (around lines 05 and 06 / line 07 / after input)
- three marks for pseudocode:
  - use of `REPEAT … UNTIL` // any working loop structure
  - check for `> 0` // `>= 0`
  - check for `< 10` // `> 9`
  - check for whole number / check for `-1` / check length of digit `<> 1`
```
REPEAT
    OUTPUT "Enter a digit"
    INPUT Number[Counter]
UNTIL Number[Counter] = Round(Number[Counter],0) AND ((Number[Counter] = -1) OR
      (Number[Counter] > 0 AND Number[Counter] < 10))
```

---

### 7.6 Testing

#### **Provide normal, abnormal, and extreme test data with reasons** (various)

**For range 30–200** (6 marks — S23 V1 Q3b):
- Normal — 75; reason: data lies within required range **and** should be accepted
- Abnormal — Sixty; reason: this is the wrong data type **and** should be rejected
- Extreme — 200; reason: highest value in the required range that should be accepted
*(also valid Extreme: 30)*

**General approach** (W23 V1 Q8c; W23 V2 Q2b; W23 V3 Q4c):
- Normal data: a value within the acceptable range + reason (lies within range, should be accepted)
- Abnormal data: a value outside range or wrong type + reason (outside range / wrong type, should be rejected)
- Extreme data: boundary value (lowest or highest acceptable) + reason (boundary value, should be accepted/rejected)

---

### 7.7 Trace Tables

#### **Complete a trace table for a phonetic alphabet look-up algorithm** (4 marks — S23 V1 Q7a)
- One mark per correct column: Pointer, Letter, Choice, OUTPUT
- Algorithm searches array for input letter and outputs phonetic name
- e.g. Letter F → Pointer reaches 6 → OUTPUT "Letter F is represented by Foxtrot"
- Then: "Another Letter? (Y or N)", Choice=Y → Letter D → Pointer reaches 4 → OUTPUT "Letter D is represented by Delta"
- Then: Choice=N → algorithm stops

#### **Complete a trace table for an algorithm identifying multiples of 5 and 10** (6 marks — S23 V3 Q7a)
- Columns: Total, Value, Five1, Five2, Ten1, Ten2, OUTPUT
- One mark per correct column (Total, Value, Five1, Five2, Ten1+Ten2, OUTPUT)
- Example values: Value=5 → Five1=1, Five2=1, Ten1=0, Ten2=0.5 → Rejected; Value=50 → Five1=10, Five2=10, Ten1=5, Ten2=5; eventually Total=550, OUTPUT=550

#### **Describe the purpose of an algorithm** (various)
- **Averaging algorithm** (W23 V2 Q6b): to calculate the average/mean of a set of numbers entered by the user (using a sentinel value to stop input)
- **Multiples algorithm** (S23 V3 Q7b): to find if an input is divisible by both 5 and 10 / add them together **and** output the total

#### **Explain the limitation of a linear search with an invalid character** (2 marks — S23 V1 Q7c)
- the algorithm would not stop
- … because it would not have found the item it was seeking
- **OR**: the array would run out of values after the pointer reached 13 / the algorithm will crash

#### **Suggest changes to modify an algorithm** (3 marks — W23 V3 Q8b)
- One mark per valid change that correctly alters the algorithm's behaviour
- Changes must be consistent with the algorithm structure (e.g. modifying loop conditions, changing output statements, updating counter logic)

---

### 7.8 Error Identification

#### **Identify and correct errors in a pseudocode algorithm** (various)

**Four errors — counting positive numbers** (4 marks — S23 V1 Q5a):
- Line 04: `IF Number < 0` should be `IF Number > 0`
- Line 10 / Line 01: `Exit ← 1` should be `Exit ← 0` **and** `WHILE Exit <> 0` should be `WHILE Exit = 0`
- Line 13: `ENDIF` should be `ENDWHILE`
- Line 14: `OUTPUT "The total value of your numbers is ", Number` should be `OUTPUT "The total value of your numbers is ", Total`

**Four errors — WHILE loop algorithm** (4 marks — S23 V3 Q6a):
- Line 01: `Counter ← 100` should be `Counter ← 0`
- Line 03: `While Counter > 100 DO` should be `While Counter < 100 DO`
- Line 07: `Total ← Total + Counter` should be `Total ← Total + Number`
- Line 09: `ENDCASE` should be `ENDIF`

**Four errors — general approach** (W23 V2 Q4a; W23 V3 Q5a; S23 V2 Q7a/b):
- One mark per error correctly identified with the corrected version
- Look for: wrong comparison operators, wrong variable names, wrong keywords (ENDCASE vs ENDIF, ENDIF vs ENDWHILE), wrong initialisation values, wrong array indexing (e.g. `Number * Counter` instead of `Number[Counter] * Counter`)

#### **Suggest an improvement to make an algorithm more efficient** (2 marks — W23 V1 Q8e)
- add a count/counter to limit the number of iterations
- … or use a sentinel/flag value to exit the loop early when condition is met

---

## 8. Programming

### 8.1 Programming Concepts

#### **Identify the correct operator** (1 mark — W23 V1 Q1)
- C — `<=` (less than or equal to)

#### **Identify the term for a value passed into a procedure** (1 mark — W23 V1 Q2)
- B — parameter

#### **Match data types to their descriptions** (4 marks — W23 V1 Q3)
- Integer — whole number (no decimal places)
- Real — number with decimal places
- Boolean — can only hold True or False
- Char — a single character

#### **Match storage places to their descriptions** (3 marks — W23 V1 Q4)
- Variable — a named storage location whose value can change during program execution
- Constant — a named storage location whose value cannot change during program execution
- Array — a data structure that stores multiple values of the same data type under one identifier

#### **Identify the correct constant declaration** (1 mark — S23 V3 Q1)
- B — e.g. `CONSTANT MaxSize = 100`

#### **Explain the purpose of DIV and ROUND operators** (4 marks — S23 V1 Q4)
- `DIV`, max two marks:
  - to perform integer division
  - meaning only the whole number part of the answer is retained
  - e.g. `DIV(9, 4) = 2`
- `ROUND`, max two marks:
  - to return a value rounded to a specified number of digits / decimal places
  - the result will either be rounded to the next highest or next lowest value depending on whether the preceding digit is >= 5 or < 5
  - e.g. `ROUND(4.56, 1) = 4.6`

#### **Explain the purpose of MOD and RANDOM operators** (4 marks — S23 V3 Q2; W23 V3 Q2)
- `MOD`, max two marks:
  - to perform (integer) division when one number is divided by another
  - … and find the remainder
  - e.g. `7 MOD 2 = 1`
- `RANDOM`, max two marks:
  - to generate (pseudo) random numbers
  - … (usually) within a specified range
  - e.g. `RANDOM() * 10` returns a random number between 0 and 10

#### **Identify the operator that returns the remainder of integer division** (1 mark — W23 V3 Q2)
- B — MOD

#### **Explain how a function is called and returns a value** (3 marks — S23 V3 Q3)
- a call statement is used in order to make use of a function // the function is called using its identifier
- parameters are / may be passed (from the main program) to the function
- the function performs its task …
- … and returns a value / values to the main program

#### **Write pseudocode using procedures with parameters** (4 marks — W23 V2 Q8)
- one mark for correct procedure call with parameter(s)
- one mark for correct procedure definition with parameter(s)
- one mark for correct use of parameter(s) inside the procedure
- one mark for correct overall structure

#### **Describe the difference between local and global variables** (4 marks — W23 V3 Q7)
- Local variable: declared inside a procedure / function
  - only accessible / can only be used within that procedure / function
  - created when procedure called, destroyed when procedure ends
- Global variable: declared in the main program
  - accessible throughout the entire program / in all procedures and functions
  - exists for the lifetime of the program

#### **Describe features that make a program maintainable** (various — W23 V1 Q6c/d; S23 V1 Q6; S23 V2 Q6)
- **Meaningful identifiers** — to enable the programmer (or future programmers) to easily recognise the purpose of a variable / array / constant // to enable easy tracking through the program
  - e.g. using `Total` to store a running total
- **Use of comments** — to annotate each section of a program so that a programmer can find specific sections / knows the purpose of that section of code
  - e.g. `// all values are zeroed before the next calculation`
- **Procedures and functions** — to make programs modular and easier to update / add functionality
  - e.g. `CalculateInterest(Deposit, Rate)`

#### **Describe the changes needed to convert a WHILE loop to a FOR loop** (5 marks — S23 V3 Q6b)
- replace line 03 with `FOR`
- … with limits 0 to 99 / 1 to 100
- replace line 05 to check if `Number` is not positive
- … (if `Number` is not positive) insert a validation and re-input routine between lines 06 and 07 …
- … that will repeat until a positive value is entered
- remove the counter update / line 08
- replace line 10 / `ENDWHILE` with `NEXT`

#### **Modify an algorithm to count and output the number of positive inputs** (4 marks — S23 V1 Q5b)
- initialise a new (counting) variable … `Count ← 0` // to count the acceptable numbers
- insert a counting statement between lines 05 and 07 … `Count ← Count + 1`
- add a new output after the loop / after line 13 / at the end of the program … `OUTPUT Count`

#### **Distinguish between variables and constants** (3 marks — W23 V2 Q5)
- A variable is a named location in memory whose value can change during execution
- A constant is a named location whose value is fixed at the start and cannot change during execution
- One mark for each correct identification with example from the program

#### **Write declarations for a string variable and character variable** (2 marks — S23 V2 Q11a)
```
DECLARE P : STRING
P ← "The world"
DECLARE Q : CHAR
Q ← 'W'
```
*(one mark for any two correct lines)*

#### **Write pseudocode using LENGTH and UCASE to process a string** (3 marks — S23 V1 Q8a)
- storing string in `Phrase`
- correct use of `LENGTH` function
- correct use of `UCASE` function
- correct outputs of `LENGTH` and `UCASE`
```
Phrase ← "The beginning is the most important part"
OUTPUT LENGTH(Phrase)
OUTPUT UCASE(Phrase)
```

#### **State the expected output of a string manipulation program** (2 marks — S23 V1 Q8b)
- `40`
- `THE BEGINNING IS THE MOST IMPORTANT PART`

#### **Write pseudocode using UCASE, LENGTH, SUBSTRING to find a character position** (4 marks — S23 V2 Q11b)
- converting `P` to upper case
- finding the length of `P`
- using a loop to check for position of `Q`
- using the string operation substring
- storing the loop counter in `Position` if the value is found
```
P ← UCASE(P)
Counter ← 1
Position ← 0
REPEAT
    IF SUBSTRING(P, Counter, 1) = Q
        THEN
            Position ← Counter
    ENDIF
    Counter ← Counter + 1
UNTIL Position <> 0 OR Counter = LENGTH(P)
```

#### **State the value in Position after executing the string algorithm** (1 mark — S23 V2 Q11c)
- 5

#### **Write pseudocode using SUBSTRING and LCASE to process strings** (5 marks — W23 V2 Q7)
- correct use of `SUBSTRING` function with appropriate parameters (string, start position, length)
- correct use of `LCASE` function
- one mark for the initial quote / start / number extraction
- one mark for `LCASE` conversion
- one mark for correct overall structure

---

### 8.2 Arrays

#### **Identify the correct declaration statement for a one-dimensional array** (1 mark — S23 V1 Q2)
- A — e.g. `DECLARE Names : ARRAY[1:10] OF STRING`

#### **Write pseudocode to find the minimum value in an array** (4 marks — W23 V2 Q3b)
- initialise minimum variable to first element of array
- use a loop to traverse the array
- compare each element with current minimum
- update minimum if a smaller value is found
```
Min ← Array[1]
FOR Index ← 2 TO Size
    IF Array[Index] < Min
        THEN
            Min ← Array[Index]
    ENDIF
NEXT Index
```

---

### 8.3 File Handling

#### **Match file handling keywords to their functions** (4 marks — W23 V3 Q3a)
- `OPENFILE` — opens a file ready for reading or writing
- `CLOSEFILE` — closes a file after use
- `READFILE` — reads data from an open file
- `WRITEFILE` — writes data to an open file

#### **Explain why files are used to store data** (2 marks — W23 V3 Q3b)
- data stored in variables is lost when the program ends
- files allow data to be stored permanently / persistently beyond program execution

#### **Write a declaration statement for a string variable** (1 mark — S23 V3 Q9a)
```
DECLARE Saying : STRING
```

#### **Write pseudocode to input a string and write it to a text file** (5 marks — S23 V3 Q9b)
- input a string into `Saying`
- correct use of `OPENFILE` to write data
- correct use of `WRITEFILE` to write `Saying`
- correct use of `CLOSEFILE`
- correct use of filename `Quotations.txt` throughout
```
INPUT Saying
OPENFILE "Quotations.txt" FOR WRITE
WRITEFILE "Quotations.txt", Saying
CLOSEFILE "Quotations.txt"
```

---

## 9. Databases

### 9.1 Database Design

#### **State the number of records and/or fields in a database table** (various)
- W23 V2 Q10a: 18 records
- W23 V3 Q9a: Records = 14, Fields = 5
- S23 V3 Q10a: Fields = 5, Records = 12

#### **Identify the primary key for a database table** (various)
- W23 V1 Q9b(i): `CatNo` — each entry is a unique identifier
- W23 V2 Q10b: `Code` — unique identifier for each record
- W23 V3 Q9b(i): the field that is always unique for each record (e.g. ID or code field)
- S23 V1 Q10a: `TVCode` — each entry in this field is a unique identifier
- S23 V2 Q10a: `SongNumber`
- S23 V3 Q10b: to **uniquely identify** a record

#### **Explain why a field is suitable / not suitable as primary key** (various)
- Suitable: each entry is a unique identifier // no two records will have the same value
- Not suitable (e.g. Species field — W23 V3 Q9b iii): the value could be duplicated across multiple records // different records may share the same species name

#### **Identify appropriate data types for database fields** (various)

| Field | Data Type |
|-------|-----------|
| TVCode | Text |
| ScreenSize | Integer |
| SmartTV | Boolean |
| Price$ | Real |
| SongNumber | Text / Alphanumeric |
| Title | Text / Alphanumeric |
| Recorded | Date/time |
| Minutes | Real |
| Type | Alphanumeric |
| Private | Boolean |
| Rate$ | Integer |
| NumberGuest | Integer |

---

### 9.2 SQL Queries

#### **Complete an SQL query with SELECT, FROM, WHERE** (various)

**Retrieve Smart TV data** (4 marks — S23 V1 Q10c):
```
SELECT TVCode, ScreenSize, Price$
FROM TVRange
WHERE SmartTV = YES;
```

**Retrieve horse breed data** (W23 V2 Q10d):
```
SELECT Code, Breed
FROM Horses
WHERE ...;
```

**General SQL query structure** (W23 V1 Q9c; W23 V3 Q9d):
```
SELECT [field names]
FROM [table name]
WHERE [condition]
ORDER BY [field] [ASC/DESC];
```

#### **Predict SQL query output rows** (various)
- W23 V3 Q9c: state how many rows an SQL query returns (count rows matching WHERE condition)
- S23 V3 Q10d: output rows from query:
  ```
  Bay Lodge 10 1000
  Coppice Lodge 12 1200
  West Lodge 12 1200
  ```

#### **Describe the purpose of SQL statements** (3 marks — S23 V2 Q10c)
- to find the total number of minutes of music
- to find the total number of songs
- available for the genre rock

---

## 10. Boolean Logic

### 10.1 Logic Gates

#### **Match logic gate names to their standard circuit symbols** (4 marks — S23 V2 Q2)
- AND → D-shape with flat back
- OR → curved shape with pointed output
- NAND → AND gate with bubble (circle) on output
- NOT → triangle with bubble (circle) on output

#### **State the output of logic gates for given inputs** (2 marks each — W23 V3 Q6a/b/c)
- AND gate: output is 1 only when ALL inputs are 1; otherwise 0
- XOR gate: output is 1 when inputs are DIFFERENT; 0 when inputs are the same
- NOR gate: output is 1 only when ALL inputs are 0; otherwise 0

---

### 10.2 Logic Circuits

#### **Write the Boolean expression for a logic circuit** (4 marks — W23 V1 Q7a)
- Expression: **(NOT A AND B) OR NOT C**

#### **Complete truth tables for logic expressions** (various)

**Truth table for (NOT A AND B) OR NOT C** (W23 V1 Q7b — Z values):

| A | B | C | Z |
|---|---|---|---|
| 0 | 0 | 0 | 1 |
| 0 | 0 | 1 | 0 |
| 0 | 1 | 0 | 1 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 1 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 1 |
| 1 | 1 | 1 | 0 |

**Truth table for W23 V2 Q9b logic circuit** (Z values: 1,1,1,1,1,1,0,1):

| A | B | C | Z |
|---|---|---|---|
| 0 | 0 | 0 | 1 |
| 0 | 0 | 1 | 1 |
| 0 | 1 | 0 | 1 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 1 |
| 1 | 0 | 1 | 1 |
| 1 | 1 | 0 | 0 |
| 1 | 1 | 1 | 1 |

**Truth table for Z = (NOT A OR B) AND (B XOR C)** (S23 V1 Q9b):

| A | B | C | Z |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 |
| 0 | 1 | 0 | 1 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 0 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 1 |
| 1 | 1 | 1 | 0 |

**Truth table for X = (A OR B) AND (NOT B AND C)** (S23 V2 Q8):

| A | B | C | X |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 0 |
| 0 | 1 | 0 | 0 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 0 | 0 |
| 1 | 0 | 1 | 1 |
| 1 | 1 | 0 | 0 |
| 1 | 1 | 1 | 0 |

**Truth table for Z = (A AND NOT C) AND (B NOR C)** (S23 V3 Q8b):

| A | B | C | Z |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 0 |
| 0 | 1 | 0 | 0 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 0 | 1 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 0 |
| 1 | 1 | 1 | 0 |

---

## 11. Scenario-Based Algorithm

### 11.1 Writing Pseudocode for Context Scenario

All scenario questions are worth 15 marks (AO2 max 9 marks + AO3 max 6 marks). Each scenario specifies required data structures and three technique requirements (R1–R3).

---

#### **Theatre seat booking and availability management** (15 marks — W23 V1 Q10)
**Data structures required:** arrays for seats, variables for booking counts
**Requirements:**
- R1: Check and update seat availability (iteration, selection, input/output)
- R2: Record bookings and manage seat assignment
- R3: Display seat status and summary information

---

#### **Calculate and record wood flooring area measurements** (15 marks — W23 V2 Q11)
**Data structures required:** arrays/lists for room measurements, variables for totals
**Requirements:**
- R1: Input and validate room dimensions (iteration, validation, input/output)
- R2: Calculate floor areas (arithmetic, totalling)
- R3: Output results and comparisons with prompts

---

#### **Weather station data collection and reporting** (15 marks — W23 V3 Q10)
**Data structures required:** arrays for readings and days, variables for averages
**Requirements:**
- R1: Input and store weather readings with validation
- R2: Calculate averages and statistics
- R3: Output reports in required format

---

#### **Record and report weekly temperatures using Days[], Readings[], AverageTemp[]** (15 marks — S23 V1 Q11)
**Data structures required:**
- Arrays: `Days[]`, `Readings[]` (2D array [1:7, 1:24]), `AverageTemp[]`
- Variables: `WeekLoop`, `DayLoop`, `InTemp`, `TotalDayTemp`, `TotalWeekTemp`, `AverageWeekTemp`

**Requirements:**
- R1: Input and store hourly temperatures for each day with validation (nested iteration, range check −20 to +50)
- R2: Calculate daily average (rounded to 1 decimal place) and weekly average temperature
- R3: Convert averages to Fahrenheit (to 1 decimal place) and output in both Celsius and Fahrenheit with appropriate messages

**Example pseudocode structure:**
```
DECLARE Days : ARRAY[1:7] OF STRING
DECLARE Readings : ARRAY[1:7, 1:24] OF REAL
DECLARE AverageTemp : ARRAY[1:7] OF REAL
// populate Days[] with day names
Days[1] ← "Sunday" ... Days[7] ← "Saturday"
FOR WeekLoop ← 1 TO 7
    TotalDayTemp ← 0
    FOR DayLoop ← 1 TO 24
        OUTPUT "Enter temperature ", DayLoop, " for ", Days[WeekLoop]
        INPUT InTemp
        WHILE InTemp < -20.0 OR InTemp > 50.0 DO
            OUTPUT "Your temperature must be between -20.0 and +50.0 inclusive. Please try again"
            INPUT InTemp
        ENDWHILE
        Readings[WeekLoop, DayLoop] ← InTemp
        TotalDayTemp ← TotalDayTemp + ROUND(InTemp, 1)
    NEXT DayLoop
    AverageTemp[WeekLoop] ← ROUND(TotalDayTemp / 24, 1)
NEXT WeekLoop
// calculate weekly average
TotalWeekTemp ← 0
FOR WeekLoop ← 1 TO 7
    TotalWeekTemp ← TotalWeekTemp + AverageTemp[WeekLoop]
NEXT WeekLoop
AverageWeekTemp ← ROUND(TotalWeekTemp / 7, 1)
// output results in Celsius and Fahrenheit
FOR WeekLoop ← 1 TO 7
    OUTPUT "The average temperature on ", Days[WeekLoop], " was ", AverageTemp[WeekLoop],
           " Celsius and ", ROUND(AverageWeekTemp * 9 / 5 + 32, 1), " Fahrenheit"
NEXT WeekLoop
OUTPUT "The average temperature for the week was ", AverageWeekTemp, " Celsius and ",
       ROUND(AverageWeekTemp * 9 / 5 + 32, 1), " Fahrenheit"
```

---

#### **Manage bank account operations with Account[] and AccDetails[]** (15 marks — S23 V2 Q12)
**Data structures required:**
- Arrays: `Account[]`, `AccDetails[]`
- Variables: `Size`, `AccountNumber`

**Requirements:**
- R1: Check account number and password (iteration and validation, selection, input, output)
- R2: Display menu and make a selection (output, input and selection)
- R3: Perform actions selected — balance check, withdrawal, deposit (use of arrays and procedures with parameters)

**Example pseudocode structure:**
```
PROCEDURE CheckDetails(AccID : INTEGER)
    // validate account number, check name and password
    IF AccID < 0 OR AccID > Size THEN
        OUTPUT "Invalid Account Number"
    ELSE
        OUTPUT "Please Enter Name" : INPUT Name
        OUTPUT "Please Enter Password" : INPUT Password
        IF Name <> Account[AccID, 1] OR Password <> Account[AccID, 2] THEN
            OUTPUT "Invalid name or password"
        ELSE
            Valid ← True
        ENDIF
    ENDIF
ENDPROCEDURE

PROCEDURE Balance(AccID : INTEGER)
    OUTPUT "Your balance is ", AccDetails[AccID, 1]
ENDPROCEDURE

PROCEDURE WithDrawal(AccID : INTEGER) / PROCEDURE Deposit(AccID : INTEGER)
    // REPEAT...UNTIL with validation and array update
ENDPROCEDURE
```

---

#### **Manage a contact book using Contacts[] 2D array** (15 marks — S23 V3 Q11)
**Data structures required:**
- Arrays: `Contacts[]` (2D array [1:100, 1:2] of STRING)
- Variables: `CurrentSize`, `Cont`, `Choice`, `NewContacts`, `Count`, `Count2`, `Flag`

**Requirements:**
- R1: Output menu and input choice with validation (range check 1–3, output with messages)
- R2: Input number of new entries within limits, update current size, input new data and sort array (range check, totalling, iteration and bubble sort)
- R3: Output array whole contents and delete contents of array (iteration, output with labelling, array initialisation)

**Example pseudocode structure:**
```
CurrentSize ← 0
Cont ← TRUE
WHILE Cont DO
    OUTPUT "Press 1 to enter new contacts"
    OUTPUT "Press 2 to display your contacts"
    OUTPUT "Press 3 to delete all contacts"
    INPUT Choice
    // validate choice
    WHILE Choice < 1 OR Choice > 3 DO
        OUTPUT "Incorrect entry – please enter 1, 2, or 3"
        INPUT Choice
    ENDWHILE
    IF Choice = 1 THEN
        // input number of new contacts (1 to 5), validate, input data, bubble sort
        FOR Count ← CurrentSize + 1 TO CurrentSize + NewContacts
            INPUT Contacts[Count, 1]  // last name, first name
            INPUT Contacts[Count, 2]  // telephone number
        NEXT Count
        // bubble sort on Contacts[, 1]
    ENDIF
    IF Choice = 2 THEN
        // output all contacts
        FOR Count ← 1 TO CurrentSize
            OUTPUT Contacts[Count, 1], "   ", Contacts[Count, 2]
        NEXT Count
    ENDIF
    IF Choice = 3 THEN
        // delete all contacts (set to empty string)
        FOR Count ← 1 TO 100
            FOR Count2 ← 1 TO 2
                Contacts[Count, Count2] ← ""
            NEXT Count2
        NEXT Count
    ENDIF
ENDWHILE
```
