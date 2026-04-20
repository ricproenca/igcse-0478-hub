# Paper 2 Marking Scheme (2024)

This document organises the marking scheme content for the 2024 Paper 2 exams by syllabus structure. Question headers use the description from the questions file. Similar answers across variants are consolidated into single entries.

---

## 7. Algorithm Design and Problem-Solving

### 7.1 Program Development Life Cycle

#### PDLC stages

**Identify three stages of the Program Development Life Cycle [3]** *(W24 V1 Q4)*
- Any three from: Analysis / Design / Coding / Testing / Maintenance [1 each]

**Identify which program development method uses a particular technique [1]** *(W24 V2 Q1 — structure diagrams; S24 V2 Q1 — flowchart; W24 V3 Q2; S24 V3 Q1)*
- Structure diagrams (W24 V2 Q1) [1]
- Flowchart (S24 V2 Q1) [1]
- Structure diagram (W24 V3 Q2) [1]
- Subroutine rectangle with two vertical lines at sides (S24 V3 Q1) [1]

**Identify and describe two stages of the Program Development Life Cycle [6]** *(W24 V3 Q5)*
- Any two stages, 1 mark for identification + 1 mark for description each [2 each]:
  - Design — create solution methods (flowchart, pseudocode, structure diagram) [1+1]
  - Coding — write program code based on the design [1+1]
  - Testing — use test data to verify program works correctly [1+1]
  - (Others accepted with valid descriptions)

#### Analysis stage

**Identify one other stage of the PDLC / Describe three tasks in the analysis stage [1+3]** *(W24 V2 Q5a, Q5b)*
- One other stage: any valid stage not already stated, e.g. Coding / Testing / Maintenance [1]
- Three analysis tasks (any three from):
  - Abstraction [1]
  - Decomposition [1]
  - Identification of the problem [1]
  - Identification of requirements [1]
  - Research / data collection [1]

**Identify three tasks carried out during the analysis stage [3]** *(S24 V2 Q3)*
- Any three from: Abstraction / Decomposition / Identification of problem / Identification of requirements / Research or data collection [1 each]

---

### 7.3 Algorithm Design Methods

#### Flowcharts

**Match flowchart symbols to their names [4]** *(W24 V2 Q3a)*
- Subroutine symbol (rectangle with lines) → Subroutine [1]
- Oval → Terminator [1]
- Diamond → Decision [1]
- Rectangle → Process [1]

**Draw a flowchart to input 50 numbers and output their total [6]** *(W24 V2 Q3b)*
- START / STOP terminator [1]
- Total ← 0 initialisation [1]
- Count ← 1 initialisation [1]
- INPUT Number [1]
- Total ← Total + Number [1]
- IS Count > 50? / UNTIL Count > 50 decision with correct loop structure and OUTPUT Total [1]

**Complete a flowchart for a program that validates and stores a new password [6]** *(W24 V1 Q8a)*
- INPUT Password [1]
- Decision: IS LENGTH(Password) >= 8? [1]
- Decision: IS Password <> OldPassword? [1]
- "Password accepted" / "Password rejected" output paths [1]
- Correct flow for both YES and NO paths [1]
- Correct loop structure to re-prompt on rejection [1]

**Describe three methods used to design and construct a solution to a problem [6]** *(W24 V1 Q5)*
- Structure diagram — description of how it represents decomposition [1+1]
- Flowchart — description of how it shows flow of logic [1+1]
- Pseudocode — description of how it uses structured language steps [1+1]

---

### 7.4 Standard Methods of Solution

#### Sorting algorithms

**Explain how the bubble sort algorithm can be made more efficient [3]** *(W24 V2 Q4b)*
- Use a flag variable (set to FALSE) to detect if a swap was made [1]
- Stop the outer loop early if no swaps were made (already sorted) [1]
- Reduce the inner loop limit by one each pass (last element already in place) [1]

**Outline the three main processes shown in the bubble sort flowchart [3]** *(S24 V1 Q6b)*
- Numbers are input and stored in an array [1]
- Array is sorted in ascending order using bubble sort [1]
- Middle/median value is found and output [1]

**Describe what the bubble sort algorithm does to the array [2]** *(S24 V2 Q9b)*
- Sorts array elements in descending order [1]
- By repeatedly comparing adjacent pairs and swapping if necessary [1]

#### Algorithm purpose and standard algorithms

**State the purpose of the factorial algorithm [1]** *(W24 V2 Q7b)*
- Multiplies an input number by each decreasing integer until value equals 1 / calculates the factorial [1]

**Outline the purpose of the algorithm that processes L, S, T, and A variables [2]** *(S24 V3 Q5b)*
- Finds / outputs the largest value, smallest value, total, and average of a set of inputs [1 each, max 2]

**Write an algorithm using a sentinel value (9999.9) to input and total a series of numbers [4]** *(S24 V2 Q6a)*
- WHILE Value <> 9999.9 / REPEAT…UNTIL Value = 9999.9 [1]
- Total ← 0 initialisation before loop [1]
- INPUT Value inside loop; Total ← Total + Value [1]
- OUTPUT Total after loop ends [1]

**Extend the algorithm to count how many input values are greater than 100 [4]** *(S24 V2 Q6b)*
- Counter ← 0 initialisation [1]
- IF Value > 100 THEN Counter ← Counter + 1 inside loop [1]
- OUTPUT Counter after loop [1]
- Correct overall structure integrated with sentinel loop [1]

---

### 7.5 Validation and Verification

#### Verification checks

**Identify which statement describes a visual check as a verification method [1]** *(W24 V1 Q1)*
- D — A person looks at the original data and then at the data that has been entered, checking they are the same [1]

**Outline one verification check and explain how it is carried out [2]** *(W24 V2 Q6)*
- Visual check — a person looks at the original data and the entered data to confirm they match [1+1]
- Double entry check — data is entered twice and the two versions are compared automatically [1+1]
(either accepted for full marks)

#### Validation checks

**Identify which statement describes a type check / format check / validation method [1]** *(W24 V3 Q1; S24 V1 Q1)*
- Type check — checks data entered is the correct data type (W24 V3 Q1) [1]
- Format check — checks data matches a required pattern/format (S24 V1 Q1) [1]

**State the rules a password must follow according to the algorithm [3]** *(W24 V3 Q10b)*
- Maximum 20 characters [1]
- Minimum 8 characters [1]
- Must contain at least one uppercase and one lowercase letter AND must contain the character '!' [1]

**Identify three validation checks applicable to a product code (PD + 4 digits) [6]** *(S24 V2 Q4a)*
- Length check — code must be exactly 6 characters [1+1]
- Format check — first two characters must be "PD" [1+1]
- Range check — last four characters (digits) must be between 1000 and 9999 [1+1]

#### Validation conditions and pseudocode

**Identify the range condition used to validate temperature input [2]** *(W24 V1 Q9b)*
- >= 35 AND <= 38 [2] (both conditions required)

**Explain how to add input validation for values in the range 1 to 500 [4]** *(S24 V1 Q4c)*
- Add a WHILE or REPEAT loop after the INPUT statement [1]
- Check if value is between 1 and 500 inclusive (>= 1 AND <= 500) [1]
- Re-prompt INPUT inside the loop if invalid [1]
- UNTIL / end condition that exits when valid [1]

**Write pseudocode to validate a product code using a LENGTH check [2]** *(S24 V2 Q4b(i))*
```
REPEAT
    INPUT Product
UNTIL LENGTH(Product) = 6
```
- REPEAT…UNTIL structure or WHILE equivalent [1]
- LENGTH(Product) = 6 as the condition [1]

**Write pseudocode to validate a product code using a SUBSTRING check [2]** *(S24 V2 Q4b(ii))*
```
REPEAT
    INPUT Product
UNTIL SUBSTRING(Product, 1, 2) = "PD"
```
- REPEAT…UNTIL / WHILE structure [1]
- SUBSTRING(Product, 1, 2) = "PD" as the condition [1]

---

### 7.6 Testing

#### Test data

**Identify two test data items (with types) for a program accepting values up to 80 [4]** *(W24 V2 Q8)*
- 80 — largest accepted / extreme/boundary value [1+1]
- 81 — smallest rejected / abnormal value [1+1]

**Identify three types of test data (type, example, expected outcome) for range 1–100 [9]** *(W24 V3 Q7)*
- Normal: e.g. 25 → Accepted [1+1+1]
- Extreme: 1 or 100 → Accepted (boundary) [1+1+1]
- Abnormal: e.g. 125 → Rejected [1+1+1]
- (Boundary: 0 or 101 → Rejected, accepted as alternative to extreme)

**Give normal, abnormal, and extreme test data for a program accepting values from 1 to 80 [3]** *(S24 V3 Q6a)*
- Normal: e.g. 75 [1]
- Abnormal: e.g. 101 [1]
- Extreme: 1 or 80 (boundary of accepted range) [1]

**Describe what extreme test data is and why it is used [2]** *(S24 V3 Q6b)*
- Test data at the limits (boundaries) of acceptable input [1]
- Used to test that the program correctly accepts/rejects the largest and smallest valid values [1]

---

### 7.7 Trace Tables

#### Trace table completion

**Complete the trace table for the temperature-monitoring algorithm [2]** *(W24 V1 Q9c)*
- Temperature column showing values that pass the >= 35 AND <= 38 validation [1]
- OUTPUT column showing corresponding valid temperature outputs [1]

**Complete the trace table for a factorial calculation algorithm [5]** *(W24 V2 Q7a)*
- Value = 5: Count traces 4, 3, 2, 1 → Answer = 120 → OUTPUT 120 [2]
- Value = 6: Count traces 5, 4, 3, 2, 1 → Answer = 720 → OUTPUT 720 [2]
- Value = -1: No iterations, immediate output [1]

**Complete three trace tables for a password-validation algorithm [6]** *(W24 V3 Q10a)*
- MYWORD: Accept goes TRUE then FALSE → Output: Rejected [2]
- M!word: Accepted goes TRUE then FALSE (missing uppercase) → Output: Rejected [2]
- My!Hidden: All conditions met → Output: Accepted [2]

**Complete the trace table for a bubble sort algorithm on seven numbers [7]** *(S24 V1 Q6a)*
- Input array: 47, 50, 52, 60, 80, 63, 70 [1]
- Limit, Count columns correct [1]
- Flag, Swap columns correct for each pass [2]
- Array state correct after each pass [2]
- Result / OUTPUT correct [1]

**Complete the trace table for a bubble sort algorithm sorting values in descending order [5]** *(S24 V2 Q9a)*
- List[1:5] = {15, 17, 20, 5, 9} traced through descending sort [2]
- Correct pass-by-pass values [2]
- Final sorted order: 20, 17, 15, 9, 5 [1]

**Complete the trace table for an algorithm that finds the largest, smallest, total and average [6]** *(S24 V3 Q5a)*
- L (Largest), S (Smallest), T (Total), A (Average) columns populated correctly [2 each, max 6]
- Sample: L=50, S=2, T=182, A=18.2

---

### 7.8 Error Identification

#### Code debugging

**Identify four errors in a pseudocode temperature-monitoring program [4]** *(W24 V1 Q9a)*
- Line 03: `Temp` should be `Temperature` [1]
- Line 04: `=` should be `<>` [1]
- Line 14: `OR` should be `AND` [1]
- Line 19: `WHILE` should be `UNTIL` [1]

**Identify five errors in a bubble sort pseudocode program [5]** *(W24 V2 Q4a)*
- Line 02: STRING → INTEGER (wrong data type) [1]
- Line 09: `Temp` should be `Swapped` (← TRUE) [1]
- Line 10: OR → AND [1]
- Line 17: `ItemList[Counter] ← Temp` should be `ItemList[Counter+1] ← Temp` [1]
- Line 19: ENDCASE → ENDIF [1]

**Identify four errors in a given flowchart [4]** *(W24 V3 Q9)*
- Yes/No labels on first decision box are swapped [1]
- Second decision box uses OR instead of AND [1]
- Flow line direction for A ← B is wrong [1]
- Symbol for A ← C should be a process rectangle, not a different shape [1]

**Identify four errors in a pseudocode program that inputs and totals numbers [4]** *(S24 V1 Q4a)*
- Line 01: STRING → INTEGER [1]
- Line 07: IF → FOR [1]
- Line 09: INPUT Loop → INPUT Value [1]
- Line 10: Total ← Total * Value → Total ← Total + Value [1]

**Describe the problem that occurs when the factorial algorithm receives values of 1, 0, or less than -1 [2]** *(W24 V2 Q7c)*
- For value = 1: Program enters FOR loop but Count would never reach 1 (already at limit) / endless loop risk [1]
- For value = 0 or below: Count starts below 1 and the loop condition is never satisfied → endless loop [1]

**Identify three errors in a pseudocode program to find maximum and minimum values [3]** *(S24 V2 Q7b)*
- Line 04: < → > [1]
- Line 08: Count → Counter [1]
- Line 11: ENDWHILE → ENDIF [1]

**Identify four errors in a pseudocode program using a 2D array [4]** *(S24 V3 Q4a)*
- Line 01: REAL → STRING [1]
- Line 10: Count ← 100 → Count ← 1 [1]
- Line 12: CASE OF → REPEAT [1]
- Line 27: UNTIL NOT Count → UNTIL NOT Continue [1]

---

## 8. Programming

### 8.1 Programming Concepts

#### Data types

**State the definition and give an example of Integer and Real data types [4]** *(S24 V1 Q3)*
- Integer: whole number (no fractional part), e.g. 27 [1+1]
- Real: number with a fractional part (decimal), e.g. 18.75 [1+1]

**Describe the String and Char data types with an example of each [4]** *(S24 V3 Q3)*
- String: a group of characters (letters, numbers, special characters), e.g. "Cambridge2024" [1+1]
- Char: a single character, e.g. 'X' [1+1]

#### Operator types

**Match operators to their operator types (Boolean, Logical, Arithmetic) [4]** *(W24 V1 Q3)*
- >= → Boolean [1]
- AND → Logical [1]
- DIV → Arithmetic [1]
- + → Arithmetic [1]

**State arithmetic, Boolean, and logical operators with an example of each [6]** *(S24 V2 Q5)*
- Arithmetic: used for calculations, e.g. A ← B + C [1+1]
- Boolean: true/false result, e.g. IF B AND C [1+1]
- Logical: comparisons, e.g. IF B > C [1+1]

#### Identifier naming

**Suggest more meaningful identifier names for variables in an array program [3]** *(W24 V1 Q6c; W24 V3 Q6c)*
- W24 V1: A → MyArray; T → Counter; C → Index; I → Total [1 each, any 3]
- W24 V3: A → Values; C → Index; X → Average; W → Total [1 each, any 3]

**Explain why L, S, T, and A may not be appropriate identifier names [3]** *(S24 V3 Q5c)*
- Identifiers are single letters [1]
- They do not indicate the values they hold [1]
- Identifiers should be meaningful / self-documenting [1]

**State more appropriate identifier names for L, S, T, and A [2]** *(S24 V3 Q5d)*
- L → Largest / Maximum [1]
- S → Smallest / Minimum; T → Total / Sum; A → Average / Mean [1 for any remaining two]

#### Subroutines

**Match programming terms to their definitions [4]** *(S24 V1 Q2a)*
- Function: always returns a value [1]
- Procedure: may not return a value [1]
- Parameter: value a procedure/function expects to receive [1]
- Local variable: variable declared within a specific procedure [1]

**Write the correct pseudocode to call the Average procedure with two arguments [2]** *(S24 V1 Q2b)*
```
CALL Average(25, 50)
```
- CALL keyword [1]
- Average(25, 50) with correct arguments [1]

**Outline three reasons why procedures are used in program development [3]** *(S24 V1 Q2c)*
- Divide code into smaller segments — easier to read and debug [1]
- Reusable — can be called multiple times without rewriting [1]
- Eliminates repeated code [1]

#### Control structures

**Identify the correct pseudocode example of an IF selection statement [1]** *(W24 V2 Q2)*
- C — `IF X = 7 THEN Y ← 21 ENDIF` [1]

**Write a CASE statement to output a message based on an input number from 1 to 4 [5]** *(S24 V1 Q5)*
```
INPUT Number
CASE OF Number
    1: OUTPUT "..."
    2: OUTPUT "..."
    3: OUTPUT "..."
    4: OUTPUT "..."
    OTHERWISE OUTPUT "ERROR"
ENDCASE
```
- INPUT Number [1]
- CASE OF Number structure [1]
- 1–4 branches with output [1]
- OTHERWISE "ERROR" [1]
- ENDCASE [1]

**Identify the line numbers for assignment, selection, and iteration statements [3]** *(S24 V2 Q7a)*
- Assignment: lines 01, 02, 06, 10 [1]
- Selection: lines 04 (07) and/or 08 [1]
- Iteration: lines 03 (12) [1]

#### Built-in functions and string manipulation

**Write the expression to calculate the average using the ROUND function [2]** *(S24 V1 Q4b)*
```
ROUND(Total / Limit, 1)
```
- ROUND function [1]
- Total / Limit with 1 decimal place as second argument [1]

**Write pseudocode using SUBSTRING to extract and output a section of a text string [4]** *(S24 V3 Q7a)*
```
FullText ← "IGCSE Computer Science at Cambridge"
PartText ← SUBSTRING(FullText, 7, 16)
OUTPUT PartText
OUTPUT UCASE(FullText)
```
- FullText assignment [1]
- SUBSTRING(FullText, 7, 16) [1]
- OUTPUT PartText [1]
- OUTPUT UCASE(FullText) [1]

---

### 8.2 Arrays

#### Array traversal and completion

**Complete pseudocode to count zero values and accumulate non-zero values in an array [3]** *(W24 V1 Q6a)*
- Line 06: `C ← 1` (initialise counter/index) [1]
- Line 08: `IF A[C] = 0` (check for zero) [1]
- Line 14: `NEXT C` (increment loop variable) [1]

**Complete pseudocode to count items in an array and calculate their average [3]** *(W24 V3 Q6a)*
- Line 06: `C ← 1` [1]
- Line 08: `W ← W + A[C]` (accumulate total) [1]
- Line 11: `X ← W / (C - 1)` (calculate average) [1]

**Write pseudocode to output the total and item count with suitable messages [3]** *(W24 V1 Q6b; W24 V3 Q6b)*
- OUTPUT T / Total with a suitable message [1]
- OUTPUT I / Count with a suitable message [1]
- Correct variable names matching the program [1]

#### 2D arrays

**Write pseudocode to output all elements of a 2D array in rows [4]** *(S24 V3 Q4b)*
- Use appropriate nested loop structure [1]
- Check array maximum not exceeded [1]
- Check current element is not empty [1]
- Output all three elements per row [1]

**Explain how to prevent the program from exceeding the 50-element array limit [4]** *(S24 V3 Q4c)*
- Declare a maximum size variable at the start [1]
- Check that counting variable does not exceed maximum [1]
- If limit reached, set Response ← 'N' or add UNTIL condition [1]
- Correct integration with existing loop structure [1]

---

### 8.3 File Handling

#### File storage purpose

**Explain why a new password needs to be stored in a file rather than in a variable [2]** *(W24 V1 Q8c)*
- Data in a variable is lost when the program ends (not persistent) [1]
- Data in a file provides a permanent/non-volatile copy that can be retrieved when needed [1]

**Outline two reasons why it is useful to store data in a file [2]** *(S24 V1 Q7a)*
- Creates a permanent copy of data that persists after the program ends [1]
- Can be retrieved and used again by the program / can be transferred to other systems [1]

#### Writing to files

**Write pseudocode to open a file, write the new password, and close the file [3]** *(W24 V1 Q8b)*
```
OPENFILE "passwords.txt" FOR WRITE
WRITEFILE "passwords.txt", Password
CLOSEFILE "passwords.txt"
```
- OPENFILE … FOR WRITE [1]
- WRITEFILE … Password [1]
- CLOSEFILE [1]

**Write pseudocode to open a file, write the extracted string, and close the file [3]** *(S24 V3 Q7b)*
```
OPENFILE "Subjects.txt" FOR WRITE
WRITEFILE "Subjects.txt", PartText
CLOSEFILE "Subjects.txt"
```
- OPENFILE "Subjects.txt" FOR WRITE [1]
- WRITEFILE "Subjects.txt", PartText [1]
- CLOSEFILE "Subjects.txt" [1]

#### Reading from files

**Write pseudocode to read a string from a file and output it in uppercase with its length [4]** *(S24 V1 Q7b)*
```
DECLARE Words : STRING
OPENFILE "Quotation.txt" FOR READ
READFILE "Quotation.txt", Words
OUTPUT UCASE(Words), LENGTH(Words)
CLOSEFILE "Quotation.txt"
```
- DECLARE string variable [1]
- OPENFILE … FOR READ [1]
- READFILE and store to variable [1]
- OUTPUT UCASE(Words) and LENGTH(Words) [1]

**Write pseudocode to read a string from input, convert to lowercase, and write to a file [6]** *(W24 V2 Q10)*
- DECLARE string variable [1]
- INPUT the string [1]
- OPENFILE Main.txt FOR WRITE, WRITEFILE original, CLOSEFILE [1]
- LowercaseText ← LCASE(string) [1]
- OUTPUT LowercaseText and LENGTH [1]
- OPENFILE Lowercase.txt FOR WRITE, WRITEFILE, CLOSEFILE [1]

---

## 9. Databases

### 9.1 Database Design

#### Records and fields

**State the number of records in the CheeseStock database table [1]** *(W24 V1 Q10a)*
- 19 [1]

**State the number of fields and records in the hotel database table [2]** *(W24 V2 Q11a)*
- Fields = 11 [1]
- Records = 15 [1]

**Complete a paragraph about databases using terms (rows, columns, SQL, primary key) [6]** *(W24 V3 Q4)*
- Rows = records [1]
- Columns = fields [1]
- SQL = Structured Query Language [1]
- Primary key = uniquely identifies a record [1]
- Plus two further correct database facts [1+1]

**State the number of fields and records in the Hangar1 database table [2]** *(S24 V3 Q8a)*
- Fields = 6 [1]
- Records = 11 [1]

#### Primary key

**Identify the most suitable field to use as the primary key [1]** *(W24 V1 Q10b(i); S24 V2 Q10a)*
- W24 V1: ChNo [1]
- S24 V2: ContractNumber [1]

**Explain why the chosen field is suitable as the primary key [1]** *(W24 V1 Q10b(ii))*
- It uniquely identifies each record in the table [1]

**Explain why the Type field is not suitable as the primary key [1]** *(W24 V2 Q11b)*
- Type contains repeating / non-unique data (multiple rooms share the same type) [1]

**State whether any field in the SoftDrinks table is suitable as a primary key [1]** *(S24 V1 Q9a)*
- None of the fields are likely to contain unique data [1]

#### Data types

**State the data type for each field in the hotel database table [2]** *(W24 V2 Q11c)*
- RoomNo / Type = alphanumeric / text [1]
- Mon–Sun = Boolean; Rate$ = real; Guests = integer [1]

**State the data type for each field in the subscriptions database table [2]** *(S24 V2 Q10b)*
- ContractNumber = text / alphanumeric [1]
- Months = integer; EndDate = date/time; Sport = Boolean [1]

---

### 9.2 SQL Queries

#### SELECT queries and output

**State the output of a given SQL query on the CheeseStock table [2]** *(W24 V1 Q10c)*
- CH04  0.0 [1]
- CH05  50.0 [1]

**State the output of a given SQL query on the hotel booking table [3]** *(W24 V2 Q11d)*
- 104S  Single  1  72.50 [1]
- 105S  Single  1  72.50; 201F  Family  4  160.00 [1]
- 301D  Double  2  200.00; 304P  Suite  6  700.00 [1]

**State the output of a given SQL query on the BuildStock database table [3]** *(W24 V3 Q11a)*
- MT12  Pebbles  large [1]
- MT06  Cobbles [1]
- (Correct rows selected and formatted) [1]

**State the output of a given SQL query on the Hangar1 aircraft database table [4]** *(S24 V3 Q8b)*
- 314  Clipper  1936  4 [1]
- C-47  Dakota  1942  2 [1]
- Nimrod  1966  4; DC-10  1970  3 [1]
- Concorde  1973  4 [1]

#### WHERE clause

**Complete the SQL query to select names of cheeses/items not currently in stock [3+2]** *(W24 V1 Q10d(i); W24 V3 Q11b(i))*
```sql
SELECT Name FROM CheeseStock WHERE NOT InStock
-- or
SELECT Name FROM CheeseStock WHERE WeightKg = 0.0
```
- SELECT Name [1]
- FROM CheeseStock / BuildStock [1]
- WHERE NOT InStock OR WHERE WeightKg = 0.0 / NumberBags = 0 [1]

**Explain an alternative way to write the WHERE clause for out-of-stock items [2]** *(W24 V1 Q10d(ii); W24 V3 Q11b(ii))*
- WHERE clause can check the InStock field for FALSE/No [1]
- OR the numeric weight/bag field for 0 (equivalent to NOT InStock) [1]

**Complete the SQL WHERE clause to filter records where both News and Sport are subscribed [2]** *(S24 V2 Q10d)*
```sql
WHERE News AND Sport
-- or
WHERE News = TRUE AND Sport = TRUE
```
- WHERE News AND Sport / News = TRUE AND Sport = TRUE [2]

**Complete the SQL query to select ID and Model for all airworthy aircraft [4]** *(S24 V3 Q8c)*
```sql
SELECT ID, Model FROM Hangar1 WHERE Airworthy = 'Y'
-- or
WHERE Airworthy
```
- SELECT [1]
- ID, Model [1]
- FROM Hangar1 [1]
- WHERE Airworthy = 'Y' / Airworthy = TRUE [1]

#### SQL aggregate functions

**Complete the SQL query to calculate the total number of canned soft drinks in stock [5]** *(S24 V1 Q9b)*
```sql
SELECT SUM(NumberInStock) FROM SoftDrinks WHERE Container = 'Can'
```
- SELECT [1]
- SUM(NumberInStock) [1]
- FROM SoftDrinks [1]
- WHERE Container [1]
- = 'Can' [1]

**Explain what the SUM and COUNT functions return in SQL queries [3]** *(S24 V2 Q10c)*
- SUM = returns the total/sum of all values in a specified column [1]
- COUNT = returns the number of records that match the specified condition [1]
- Both used with SELECT and FROM/WHERE [1]

---

## 10. Boolean Logic

### 10.1 Logic Gates

#### Gate symbols and matching

**Identify which statement correctly describes a truth table [1]** *(W24 V1 Q2)*
- C — a truth table shows all possible input combinations and their corresponding outputs [1]

**Match logic gate names to their symbols [4]** *(W24 V3 Q3; S24 V2 Q2; S24 V3 Q2a)*
- W24 V3: AND, NAND, NOR, XOR matched to correct gate symbols [4]
- S24 V2: AND, XOR, NAND, OR matched to standard symbols [4]
- S24 V3: NAND, OR, NOT, XOR matched to symbols [4]

#### Boolean expressions

**Write the Boolean logic expression for a combination lock that opens when A AND B AND NOT C [3]** *(S24 V2 Q8a)*
- X = (A AND B) AND NOT C [3]
- X = A AND B AND NOT C [1+1+1]

---

### 10.2 Logic Circuits

#### Circuit drawing

**Draw the logic circuit for the expression X = (NOT P OR Q) NAND (Q XOR R) [4]** *(W24 V2 Q9a)*
- NOT P gate [1]
- OR gate with NOT P and Q inputs [1]
- XOR gate with Q and R inputs [1]
- NAND gate combining both sub-expressions [1]

**Draw the logic circuit for Z = (R OR NOT T) XOR (NOT S AND T) [5]** *(S24 V1 Q8a)*
- NOT T gate [1]
- OR gate with R and NOT T inputs [1]
- NOT S gate [1]
- AND gate with NOT S and T inputs [1]
- XOR gate combining both sub-expressions [1]

#### Truth tables for circuits

**Complete the truth table for the logic circuit NOT X OR (Y XOR Z) [4]** *(W24 V1 Q7b)*
- 8-row truth table for X, Y, Z → W = NOT X OR (Y XOR Z) [2]
- Correct W values: 1, 1, 1, 1, 0, 1, 1, 0 [2]

**Write the Boolean logic expression for a given logic circuit [3]** *(W24 V1 Q7a)*
- NOT X [1]
- Y XOR Z [1]
- NOT X OR (Y XOR Z) [1]

**Complete the truth table for X = (NOT P OR Q) NAND (Q XOR R) [4]** *(W24 V2 Q9b)*
- 8-row truth table for P, Q, R → X [2]
- Correct X values: 1, 0, 0, 1, 1, 1, 0, 1 [2]

**Complete the truth table for a window-control logic circuit [4]** *(W24 V3 Q8)*
- Window opens (W=1) only when A=0 (alarm off), T=1 (high temp), H=0 (heating off) [2]
- All 8 rows of A, T, H, W correct [2]

**Complete the truth table for Z = (R OR NOT T) XOR (NOT S AND T) [4]** *(S24 V1 Q8b)*
- R, S, T, Z: 0,0,0,1; 0,0,1,1; 0,1,0,1; 0,1,1,0; 1,0,0,1; 1,0,1,0; 1,1,0,1; 1,1,1,1 [4]

**Complete the truth table for the combination lock logic expression X = A AND B AND NOT C [4]** *(S24 V2 Q8b)*
- 8-row truth table: all X = 0 except when A=1, B=1, C=0 → X=1 [4]

**Complete the truth table for a logic circuit combining NAND and NOR gates [4]** *(S24 V3 Q2b)*
- A, B, C, Z: 0,0,0,0; 0,0,1,1; 0,1,0,0; 0,1,1,0; 1,0,0,1; 1,0,1,0; 1,1,0,0; 1,1,1,0 [4]

---

## 11. Scenario-Based Algorithm

### 11.1 Writing Pseudocode for Context Scenario

**Write pseudocode for a running club program managing member times, rankings and certificates [15]** *(W24 V1 Q11)*

*AO2 — max 9 marks (correct pseudocode structure and logic):*
- Declare arrays: MemberName[], MemberTime[], MemberCertificate[] [1]
- R1: Input member names and times with validation loop [2]
- R2: Sort times in ascending order; output top 3 names/times [3]
- R3: Loop through members; award certificate if time < 240; count and store [3]

*AO3 — max 6 marks (quality, robustness, efficiency):*
- Correct use of loops and conditions [2]
- Appropriate use of arrays and indexing [2]
- Efficient and well-structured algorithm overall [2]

---

**Write pseudocode for a program that inputs room names and dimensions, calculates areas and finds the largest and smallest [15]** *(W24 V2 Q12)*

*AO2 — max 9 marks:*
- Declare arrays: Rooms[], Dimensions[][] [1]
- R1: Input number of rooms (validate 3–20), input name and dimensions for each [3]
- R2: Calculate area for each room; calculate total area and average; find largest and smallest [3]
- R3: Output all results (all areas, total, average, largest, smallest) [2]

*AO3 — max 6 marks:*
- Correct loop structure with appropriate start/end conditions [2]
- Correct use of 2D array for dimensions [2]
- Efficient algorithm with correct logic for finding maximum and minimum [2]

---

**Write pseudocode for a fruit-picking program managing picker weights, rankings and certificates [15]** *(W24 V3 Q12)*

*AO2 — max 9 marks:*
- Declare arrays: PickerName[], PickedWeight[], PickerCertificate[] [1]
- R1: Input and validate weights for each picker [3]
- R2: Sort weights in descending order; output top 2 picker names/weights [3]
- R3: Award certificate to pickers with weight > 3 kg; count and store [2]

*AO3 — max 6 marks:*
- Correct sort direction (descending) [2]
- Correct certificate logic and counting [2]
- Well-structured pseudocode overall [2]

---

**Write pseudocode for a cricket league program managing clubs, match results and standings [15]** *(S24 V1 Q10)*

*AO2 — max 9 marks:*
- Declare arrays: Clubs[], Statistics[][], Points[], TieIndex[] [1]
- R1: Input number of matches/clubs and W/D/L results with validation [3]
- R2: Calculate points (W×12 + D×5); find maximum points [3]
- R3: Identify ties (clubs with equal maximum points); output winners [2]

*AO3 — max 6 marks:*
- Correct points calculation formula [2]
- Correct tie-detection logic [2]
- Overall structure and efficiency [2]

---

**Write pseudocode for a 2D grid treasure-hunt game with move validation and win/lose conditions [15]** *(S24 V2 Q11)*

*AO2 — max 9 marks:*
- Set up grid: Grid[1:5, 1:5], place X in random cell, clear rest [2]
- R2: Input and validate moves (L/R/U/D); update player position [3]
- R3: Check if player found X (win); check if 10 moves reached (lose); output outcome [4]

*AO3 — max 6 marks:*
- Correct boundary checking for grid edges [2]
- Correct win/lose condition logic [2]
- Well-structured loops and conditions [2]

---

**Write pseudocode for a football league program managing teams, match results, points and rankings [15]** *(S24 V3 Q9)*

*AO2 — max 9 marks:*
- Declare arrays: Teams[], Results[][] [1]
- R1: Input number of games and teams; input W/D/L results with validation [3]
- R2: Calculate points (W×3 + D); sort teams in descending order by points [3]
- R3: Find and output top team(s); check for ties at the top [2]

*AO3 — max 6 marks:*
- Correct points formula [2]
- Correct tie-detection at top position [2]
- Efficient and well-structured algorithm [2]
