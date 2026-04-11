# Paper 2 Marking Scheme (2021)

This document contains marking scheme content for the 2021 Paper 2 exams, organized by syllabus structure.

---

## 7. Algorithm Design and Problem-Solving

### 7.2 Problem Decomposition

#### Algorithm Analysis

**Describe what a given algorithm does when processing student marks and assigning grades** *(3 marks — S21 V1 Q4a)*

- The algorithm reads marks for each student [1]
- Compares each mark against grade boundaries (e.g., Distinction / Pass / Fail) and assigns a grade [1]
- Stores each student's score and grade in arrays Score[] and Grade[] [1]

---

### 7.3 Algorithm Design Methods

#### Flowcharts

**Match pseudocode statements to their corresponding flowchart symbols** *(3 marks — S21 V2 Q3a)*

- INPUT / OUTPUT statement → parallelogram [1]
- IF / ELSE (selection / decision) → diamond [1]
- Assignment or process statement → rectangle [1]

---

### 7.4 Standard Methods of Solution

#### Finding Maximum and Minimum

**Write an algorithm to find the largest value, smallest value and the range from 500 numbers entered by the user** *(6 marks — S21 V2 Q2a)*

- Input first number and set both Large and Small to this value [1]
- Loop 499 more times (500 total) to input each remaining number [1]
- Inside loop: if current number > Large, update Large [1]
- Inside loop: if current number < Small, update Small [1]
- After loop, calculate range = Large − Small [1]
- Output Large, Small and range [1]

Example structure:
```
INPUT Number
Large ← Number
Small ← Number
FOR Count ← 2 TO 500
    INPUT Number
    IF Number > Large THEN
        Large ← Number
    ENDIF
    IF Number < Small THEN
        Small ← Number
    ENDIF
NEXT Count
Range ← Large - Small
OUTPUT Large, Small, Range
```

#### Algorithm Efficiency

**Describe how the algorithm for finding largest/smallest values could be modified to produce the answer more quickly** *(2 marks — S21 V2 Q2b)*

- Sort the data into ascending order first [1]
- The smallest value is then the first element and the largest is the last, so no comparison loop is needed [1]

OR

- Store all 500 numbers in an array first, then sort the array [1]
- Read the first and last elements for Small and Large directly [1]

---

### 7.5 Validation and Verification

#### Validation

**Write pseudocode to validate that the passenger's start stage number is within the valid range** *(3 marks — W21 V2 Q1b)*

- Use a WHILE or REPEAT loop to repeatedly prompt for input [1]
- Check whether input is within the valid range [1]
- Re-prompt / display error message if input is invalid; exit loop when valid [1]

Example:
```
INPUT StartStage
WHILE StartStage < 1 OR StartStage > MaxStage DO
    OUTPUT "Invalid input, please re-enter"
    INPUT StartStage
ENDWHILE
```

**Write two validation checks with appropriate test data for the mountain railway ticket booking system** *(6 marks — S21 V2 Q1b)*

- First validation check: range check on train number (must be between 1 and number of trains) [1]
  - Test data: train number = 0 or negative / greater than maximum [1]
  - Expected outcome: rejected / error displayed [1]
- Second validation check: range check on ticket quantity (must be a positive integer, not exceed available seats) [1]
  - Test data: quantity = 0, negative, or greater than seats available [1]
  - Expected outcome: rejected / error displayed [1]

**Identify appropriate validation checks (length, range, type) for three given data inputs** *(6 marks — S21 V3 Q3)*

- One mark for each correct validation check type [1] and one mark for justification/example [1]:
  - Length check: for a text/string field that must not exceed a specified number of characters
  - Range check: for a numeric field that must fall within a minimum and maximum value
  - Type check: to verify the value matches the expected data type (e.g., integer rather than text)

**Extend a calculator algorithm to validate that the operator entered is one of the four valid operations** *(5 marks — W21 V2 Q4b)*

- Input the operator from the user [1]
- Use a WHILE or REPEAT loop [1]
- Condition checks that operator is NOT one of "+", "−", "*", "/" [1]
- Display an error message if invalid [1]
- Loop exits when a valid operator is entered [1]

Example:
```
INPUT Operator
WHILE Operator <> "+" AND Operator <> "-" AND Operator <> "*" AND Operator <> "/" DO
    OUTPUT "Invalid operator, please re-enter"
    INPUT Operator
ENDWHILE
```

#### Verification Methods

**Describe one method of verification suitable for data entered into the squash court booking program** *(3 marks — W21 V1 Q3b)*

**Double entry:**
- The user is asked to enter the same data twice [1]
- The program compares both entries [1]
- If the entries match, the data is accepted; if not, the user is prompted to re-enter [1]

OR

**Proofreading:**
- The entered data is displayed back to the user on screen [1]
- The user reads the data carefully and checks it for errors [1]
- The user confirms the data is correct or makes corrections [1]

**Describe two different methods of verification suitable for data entered into the program** *(4 marks — W21 V3 Q3b)*

- Method 1 — Double entry: data is entered twice; the program compares both entries; if they differ, the user is prompted to re-enter [2]
- Method 2 — Proofreading: the data is displayed on screen; the user reads it and checks for accuracy before confirming or correcting [2]

#### Classifying Checks

**Classify three given checks as validation, verification, or neither / both** *(3 marks — W21 V2 Q2, S21 V1 Q2)*

- One mark for each correct classification [1] each
- **Validation**: the program automatically checks data is sensible (correct type, within range, correct length, correct format)
- **Verification**: checking that data has been entered correctly (double-entry comparison or proofreading by user)
- **Both**: a check that simultaneously verifies correct entry and validates correctness
- **Neither**: a check that is neither a validation nor verification process

---

### 7.6 Testing

#### Normal Test Data

**Give four sets of normal test data for a function that validates a number with three decimal places greater than zero** *(4 marks — W21 V1 Q3a(i))*

- Any four valid positive numbers with exactly three decimal places [1] each
- Examples: 0.001, 1.500, 7.123, 99.999
- Must be greater than 0.000; must have exactly three decimal places

**Give four sets of test data for a password validation function that checks length and character requirements** *(4 marks — W21 V3 Q3a(i))*

- Any four passwords that fully satisfy the validation criteria (correct length, required character types) [1] each
- All four must be valid test data (normal / expected-to-pass)

#### Boundary Test Data

**Give three sets of boundary test data for a number validation function** *(3 marks — W21 V1 Q3a(ii), W21 V3 Q3a(ii))*

- The smallest valid value (lower boundary) [1]
- A value just below the lower boundary (invalid) [1]
- The largest valid value (upper boundary, if applicable) [1]

Accept: "just above the lower boundary" as an alternative boundary point for one mark.

#### Test Data Categories

**Give normal, extreme and erroneous test data with expected outcomes for a program accepting inputs in the range 1 to 100** *(6 marks — W21 V2 Q3)*

| Type | Example Test Data | Expected Outcome |
|------|------------------|-----------------|
| Normal | Any value 2–99 (e.g., 50) [1] | Accepted [1] |
| Extreme | 1 or 100 [1] | Accepted [1] |
| Erroneous | 0, −1, 101, or non-numeric (e.g., "abc") [1] | Rejected / error [1] |

---

### 7.7 Trace Tables

#### Trace Table Completion

**Complete a trace table tracking Counter, Distinction, Mark, Award and OUTPUT for a grade-counting algorithm** *(5 marks — W21 V1 Q4)*

*Column headings: Counter | Distinction | Mark | Award | OUTPUT*

- Trace each iteration of the loop using the given input values [1 per correct row/column set, up to 5]
- Counter increments with each iteration
- Mark is read each iteration; Award is assigned based on the mark value (e.g., "Distinction" if Mark ≥ threshold)
- Distinction counter increments when Award = "Distinction"
- OUTPUT shows final count or summary after loop ends

**Complete a trace table tracking List, Value, List1, List2 and OUTPUT for a list-sorting algorithm** *(5 marks — W21 V2 Q5)*

*Column headings: List | Value | List1 | List2 | OUTPUT*

- Trace the algorithm as it separates or sorts values into List1 and List2 [1 per correct row/column set, up to 5]
- List and Value update with each iteration; List1 / List2 grow based on conditions
- OUTPUT shows result after algorithm completes

**Complete a trace table tracking Counter, Pass, Mark, Help and OUTPUT for a student score analysis algorithm** *(5 marks — W21 V3 Q4)*

*Column headings: Counter | Pass | Mark | Help | OUTPUT*

- Trace each loop iteration with the given input values [1 per correct row/column set, up to 5]
- Counter increments each iteration; Mark is read; Pass and Help are updated based on mark thresholds
- OUTPUT displays summary values after loop ends

**Complete a trace table tracking Value, Diff1, Diff2 and OUTPUT for an algorithm that finds the closest value** *(4 marks — S21 V1 Q5a)*

*Column headings: Value | Diff1 | Diff2 | OUTPUT*

- Trace each step as the algorithm computes differences [1 per correct row/column set, up to 4]
- Diff1 and Diff2 hold absolute differences; the algorithm selects the value with the smallest difference
- OUTPUT shows the closest matching value

**Complete a trace table tracking Password, PasswordRepeat and OUTPUT for a password-matching algorithm** *(3 marks — S21 V2 Q4a)*

*Column headings: Password | PasswordRepeat | OUTPUT*

- Trace each input combination [1 per correct row/column set, up to 3]
- When Password = PasswordRepeat, OUTPUT confirms match; otherwise prompts re-entry or shows mismatch

**Complete a trace table tracking Op, Value1, Value2, Ans and OUTPUT for a calculator algorithm** *(5 marks — S21 V3 Q5a)*

*Column headings: Op | Value1 | Value2 | Ans | OUTPUT*

- Trace each calculation step [1 per correct row/column set, up to 5]
- Op holds the operator; Value1 and Value2 hold the operands; Ans holds the result
- OUTPUT displays Ans after each operation

#### Algorithm Analysis

**Describe what the traced algorithm does in terms of its overall purpose** *(2 marks — S21 V1 Q5b, S21 V3 Q5b)*

- State the overall purpose of the algorithm (e.g., it performs arithmetic calculations / finds the closest value) [1]
- Describe what the output represents (e.g., the result of the calculation / the value closest to a target) [1]

---

### 7.8 Error Identification

#### Error Correction

**Identify and correct four errors in a membership-checking algorithm** *(4 marks — W21 V1 Q2a)*

- One mark for each error correctly identified and corrected [1] each (4 errors total)
- Common error types: wrong variable name used; wrong comparison operator (e.g., = instead of <>); missing or wrong loop condition; incorrect assignment statement

**Identify and correct five errors in a calculator algorithm that performs arithmetic operations** *(5 marks — W21 V2 Q4a)*

- One mark for each error correctly identified and corrected [1] each (5 errors total)
- Common error types: wrong arithmetic operator; missing or mismatched quotation marks; incorrect variable assignment; wrong conditional operator; wrong variable referenced in output

**Identify and correct four errors in a score-calculation algorithm** *(4 marks — S21 V3 Q4a)*

- One mark for each error correctly identified and corrected [1] each (4 errors total)
- Common error types: off-by-one in loop bounds; incorrect accumulation (e.g., overwriting instead of adding); wrong condition for a comparison; missing output statement

---

## 8. Programming

### 8.1 Programming Concepts

#### Constants

**Declare a constant NoCourts with an appropriate value for a squash court booking system** *(3 marks — W21 V1 Q1a)*

- Keyword `CONSTANT` (or equivalent) [1]
- Identifier NoCourts [1]
- Appropriate value assigned (accept 8, 10, or 80 depending on interpretation of the scenario) [1]

```
CONSTANT NoCourts ← 8
```

**Declare a constant MaxNoTables with value 20 for a cruise ship restaurant booking system** *(3 marks — W21 V3 Q1a)*

- Keyword `CONSTANT` [1]
- Identifier MaxNoTables [1]
- Value 20 assigned [1]

```
CONSTANT MaxNoTables ← 20
```

**Declare a constant MaxCandidates with value 4 for an election voting system** *(3 marks — S21 V1 Q1a(i))*

- Keyword `CONSTANT` [1]
- Identifier MaxCandidates [1]
- Value 4 assigned [1]

```
CONSTANT MaxCandidates ← 4
```

**Declare a constant NumberofOptions with value 5 for a referendum voting system** *(3 marks — S21 V3 Q1a(i))*

- Keyword `CONSTANT` [1]
- Identifier NumberofOptions [1]
- Value 5 assigned [1]

```
CONSTANT NumberofOptions ← 5
```

#### Variables

**Identify two variables used in the rail journey booking program** *(2 marks — W21 V2 Q1a(i))*

- PassengerID (String or Integer) [1]
- StartStage (Integer) [1]

**Declare a variable UniqueNumber with an appropriate data type to store a unique voter identifier** *(2 marks — S21 V3 Q1a(ii))*

- Identifier UniqueNumber with correct declaration syntax [1]
- Appropriate data type (Integer or String) [1]

```
DECLARE UniqueNumber : INTEGER
```

#### Data Types

**Identify the data type for three given values with justification** *(6 marks — S21 V1 Q3)*

| Value | Data Type | Justification |
|-------|-----------|--------------|
| 37 | Integer [1] | Whole number with no decimal point [1] |
| Cambridge2021 | String [1] | Contains letters and digits / sequence of characters [1] |
| 47.86 | Real [1] | Number with a decimal point / not a whole number [1] |

**Match four data type names to their descriptions** *(3 marks — S21 V3 Q2)*

- Real → numbers with a decimal/fractional part [1]
- String → text / sequence of characters [1]
- Integer → whole numbers only [1]
- Boolean → True or False values [1]
- (Award 3 marks from 4 correct matchings)

#### Iteration

**State the name of the loop type where the condition is checked before the loop body executes** *(1 mark — W21 V1 Q2c)*

- WHILE loop [1] (also accept: pre-condition loop)

**Rewrite a given loop using a FOR...NEXT construct to iterate a fixed number of times** *(3 marks — W21 V1 Q2b, W21 V3 Q2b)*

- FOR statement with correct loop variable and range [1]
- Loop body transferred correctly from original [1]
- NEXT statement with loop variable [1]

Example:
```
FOR Counter ← 1 TO 10
    [loop body]
NEXT Counter
```

**Complete a partially written algorithm that checks a series of values using a loop** *(4 marks — W21 V3 Q2a)*

- Correct loop structure (FOR or WHILE) with appropriate range/condition [1]
- Correct conditional check inside the loop [1]
- Correct update/action within the loop body [1]
- Correct output or result after loop [1]

**Modify the algorithm to accept a variable number of students rather than a fixed class size** *(3 marks — S21 V1 Q4c)*

- Input the number of students at the start [1]
- Use this value as the upper bound of the loop [1]
- Declare arrays with this variable size (or ensure existing arrays are large enough) [1]

**Extend the password algorithm to allow the user three attempts to enter a matching password** *(4 marks — S21 V2 Q4b)*

- Initialize an attempt counter to 0 or 1 [1]
- Use a loop that runs while passwords do not match AND attempts < 3 [1]
- Increment the attempt counter inside the loop [1]
- Output a message if the maximum number of attempts is exceeded [1]

**Write pseudocode using a FOR loop to initialise all elements of an array to zero** *(3 marks — S21 V2 Q5a)*

- FOR statement with correct variable and range matching array size [1]
- Array element assigned to 0 inside the loop [1]
- NEXT statement [1]

```
FOR Index ← 1 TO ArraySize
    Array[Index] ← 0
NEXT Index
```

**Explain one advantage of using a FOR loop to initialise an array compared to assigning each element individually** *(1 mark — S21 V2 Q5b)*

- Requires less code / fewer lines to write [1]
- OR: automatically handles all elements regardless of array size [1]

**Describe the purpose of adding a loop to the calculator algorithm** *(1 mark — S21 V3 Q5c)*

- Allows the program to perform multiple calculations without restarting [1]
- OR: repeats the calculation process until the user chooses to quit [1]

#### Programming Constructs

**Identify the programming concept demonstrated by three given pseudocode statements** *(3 marks — S21 V2 Q3b)*

- IF / ELSE statement → Selection [1]
- PRINT / OUTPUT statement → Output [1]
- Counter ← Counter + 1 (incrementing a variable) → Counting [1]

---

### 8.2 Arrays

#### Array Declaration

**Declare four 1D arrays for storing court booking data for one session** *(4 marks — W21 V1 Q1b)*

- Availability1 declared as Boolean array with appropriate size [1]
- Guest1 declared as String array [1]
- Mobile1 declared as String array [1]
- Code1 declared as String array [1]
- All arrays must have the same size matching NoCourts

```
DECLARE Availability1 : ARRAY[1:8] OF Boolean
DECLARE Guest1 : ARRAY[1:8] OF String
DECLARE Mobile1 : ARRAY[1:8] OF String
DECLARE Code1 : ARRAY[1:8] OF String
```

**Declare two arrays to store stage names and prices for a rail journey booking system** *(5 marks — W21 V2 Q1a(ii))*

- JourneyStage1 declared as String array [1]
- Correct size for JourneyStage1 [1]
- PriceStage1 declared as Real array [1]
- Correct size for PriceStage1 [1]
- Correct declaration syntax for both [1]

```
DECLARE JourneyStage1 : ARRAY[1:N] OF String
DECLARE PriceStage1 : ARRAY[1:N] OF Real
```

**Declare four 1D arrays for lunch session bookings on a cruise ship** *(4 marks — W21 V3 Q1b)*

- TableLunch declared as Boolean array with appropriate size [1]
- PassengerLunch declared as String array [1]
- CabinLunch declared as String array [1]
- DietReqLunch declared as String array [1]

```
DECLARE TableLunch : ARRAY[1:20] OF Boolean
DECLARE PassengerLunch : ARRAY[1:20] OF String
DECLARE CabinLunch : ARRAY[1:20] OF String
DECLARE DietReqLunch : ARRAY[1:20] OF String
```

**Declare a variable NumberCandidates and an array CandidateNames** *(4 marks — S21 V1 Q1a(ii))*

- NumberCandidates declared as Integer [1]
- CandidateNames declared as String array [1]
- Array size references MaxCandidates (or a suitable constant value) [1]
- Correct declaration syntax [1]

```
DECLARE NumberCandidates : INTEGER
DECLARE CandidateNames : ARRAY[1:MaxCandidates] OF String
```

**Declare a 1D array TrainUpPassengers of Integer type to store passenger counts per journey** *(3 marks — S21 V2 Q1a)*

- Array name TrainUpPassengers [1]
- Integer type [1]
- Appropriate size (number of trains / journeys in the scenario) [1]

```
DECLARE TrainUpPassengers : ARRAY[1:N] OF INTEGER
```

**Declare a 1D array IdNumber of Integer type with 170 elements to store all voter IDs** *(4 marks — S21 V3 Q1a(iii))*

- Array name IdNumber [1]
- Integer type [1]
- Size 170 (or bounds 1 to 170) [1]
- Correct declaration syntax [1]

```
DECLARE IdNumber : ARRAY[1:170] OF INTEGER
```

#### Array Traversal

**Write pseudocode to display the contents of Score[] and Grade[] arrays for all students** *(3 marks — S21 V1 Q4b)*

- FOR loop with correct range (1 to NumberStudents or 0 to NumberStudents−1) [1]
- OUTPUT Score[Index] inside loop [1]
- OUTPUT Grade[Index] inside loop [1]

```
FOR Index ← 1 TO NumberStudents
    OUTPUT Score[Index]
    OUTPUT Grade[Index]
NEXT Index
```

#### Array Manipulation

**Extend the score algorithm to store results in an array and calculate the average score** *(4 marks — S21 V3 Q4b)*

- Declare an array of appropriate type and size to store scores [1]
- Inside the loop, store each score in the array at the correct index [1]
- Accumulate a running total (or sum the array after collection) [1]
- Calculate and output average = total / number of scores [1]

---

## 9. Databases

### 9.1 Database Design

#### Field Data Types

**State appropriate data types for CATEGORY, PRICE, CODE and STOCK fields in an electrical appliance database** *(4 marks — W21 V1 Q5a)*

| Field | Data Type |
|-------|-----------|
| CATEGORY | Text / String [1] |
| PRICE | Currency / Real [1] |
| CODE | Text / String [1] |
| STOCK | Number / Integer [1] |

**State appropriate data types for WEIGHT, PRICE, CODE and STOCK fields** *(4 marks — W21 V3 Q5a)*

| Field | Data Type |
|-------|-----------|
| WEIGHT | Number / Real [1] |
| PRICE | Currency / Real [1] |
| CODE | Text / String [1] |
| STOCK | Number / Integer [1] |

**State the data type for the InStock field in a pet supply stock database** *(1 mark — W21 V2 Q6a(i))*

- Boolean [1]

#### Primary Keys

**State which field should be used as the primary key in the STOCK database table** *(1 mark — W21 V2 Q6a(ii))*

- ProductID [1]

**Explain why the primary key must be unique in a database table** *(1 mark — S21 V1 Q6a)*

- Each record must be uniquely identifiable; no two records can have the same primary key value [1]

#### Database Structure

**State the number of records in the given database table** *(1 mark — S21 V1 Q6b)*

- 18 [1]

**State all field names present in the TREAD database table** *(2 marks — S21 V3 Q6a)*

- LicenceNo [1] and Mileage [1] (plus tyre-related field names as shown in the table)
- One mark per correct field name identified, up to 2

---

### 9.2 SQL Queries

#### QBE Queries

**Create a QBE query to display CATEGORY, MANUFACTURER and CODE from APPLIANCE where ECONOMYRATING is "A"** *(3 marks — W21 V1 Q5b)*

| Field | Table | Show | Criteria |
|-------|-------|------|----------|
| CATEGORY | APPLIANCE | ✓ | |
| MANUFACTURER | APPLIANCE | ✓ | |
| CODE | APPLIANCE | ✓ | |
| ECONOMYRATING | APPLIANCE | | "A" |

- Correct table name APPLIANCE [1]
- Correct fields ticked (CATEGORY, MANUFACTURER, CODE) [1]
- Correct criterion: ECONOMYRATING = "A" [1]

**Create a QBE query to show ProductID and ProductName from STOCK where Animal is "cat" and InStock is Yes, sorted ascending** *(4 marks — W21 V2 Q6b)*

| Field | Table | Sort | Show | Criteria |
|-------|-------|------|------|----------|
| ProductID | STOCK | Ascending | ✓ | |
| ProductName | STOCK | | ✓ | |
| Animal | STOCK | | | "cat" |
| InStock | STOCK | | | Yes |

- Correct table name STOCK [1]
- Correct fields shown (ProductID and ProductName ticked) [1]
- Animal = "cat" criterion [1]
- InStock = Yes criterion [1]
- (Sorted ascending on ProductID; award within marks above)

**Create a QBE query to show CATEGORY, MANUFACTURER, PRICE and CODE from COMPUTER where WEIGHT < 2.5** *(3 marks — W21 V3 Q5b)*

| Field | Table | Show | Criteria |
|-------|-------|------|----------|
| CATEGORY | COMPUTER | ✓ | |
| MANUFACTURER | COMPUTER | ✓ | |
| PRICE | COMPUTER | ✓ | |
| CODE | COMPUTER | ✓ | |
| WEIGHT | COMPUTER | | <2.5 |

- Correct table COMPUTER and four fields ticked [1]
- WEIGHT criterion < 2.5 [1]
- WEIGHT not ticked in Show row (not displayed) [1]

**Create a QBE query to show ID, GenreName and Overdue from GENRE where Overdue > 0, sorted descending** *(4 marks — S21 V1 Q6c)*

| Field | Table | Sort | Show | Criteria |
|-------|-------|------|------|----------|
| ID | GENRE | | ✓ | |
| GenreName | GENRE | | ✓ | |
| Overdue | GENRE | Descending | ✓ | >0 |

- Correct table GENRE [1]
- Correct fields shown (ID, GenreName, Overdue ticked) [1]
- Criterion Overdue > 0 [1]
- Sorted descending [1]

**Create a QBE query to show SIZE, PRICE, NUMBERSOLD and NAME from PLANT where SIZE is "small" and FLOWER is False** *(5 marks — S21 V2 Q6)*

| Field | Table | Show | Criteria |
|-------|-------|------|----------|
| SIZE | PLANT | ✓ | "small" |
| PRICE | PLANT | ✓ | |
| NUMBERSOLD | PLANT | ✓ | |
| NAME | PLANT | ✓ | |
| FLOWER | PLANT | | False |

- Correct table PLANT [1]
- Correct fields shown (SIZE, PRICE, NUMBERSOLD, NAME ticked) [1]
- SIZE = "small" criterion [1]
- FLOWER = False criterion [1]
- FLOWER not shown / not ticked [1]

**Create a QBE query to show LicenceNo, Mileage and all tyre fields from TREAD where all tyre values are less than 2, sorted ascending** *(4 marks — S21 V3 Q6b)*

| Field | Table | Sort | Show | Criteria |
|-------|-------|------|------|----------|
| LicenceNo | TREAD | Ascending | ✓ | |
| Mileage | TREAD | | ✓ | |
| [Tyre field 1] | TREAD | | ✓ | <2 |
| [Tyre field 2] | TREAD | | ✓ | <2 |
| [Tyre field 3] | TREAD | | ✓ | <2 |
| [Tyre field 4] | TREAD | | ✓ | <2 |

- Correct table TREAD [1]
- Correct fields shown (LicenceNo, Mileage, all tyre fields ticked) [1]
- All tyre fields with criterion < 2 [1]
- Sorted ascending (e.g., on LicenceNo) [1]

---

## 11. Scenario-Based Algorithm

### 11.1 Writing Pseudocode for Context Scenario

#### Algorithm Design

**Write pseudocode to generate a unique 4-digit booking code for each reservation** *(3 marks — W21 V1 Q1c)*

- Generate a random 4-digit number (e.g., RANDOM(1000, 9999)) [1]
- Check whether the generated code already exists in the Code1 array [1]
- Repeat generation until a unique code is found (loop until unique) [1]

```
REPEAT
    BookingCode ← RANDOM(1000, 9999)
    Unique ← TRUE
    FOR i ← 1 TO NoCourts
        IF Code1[i] = BookingCode THEN
            Unique ← FALSE
        ENDIF
    NEXT i
UNTIL Unique = TRUE
```

**Write pseudocode to book a squash court by checking availability and recording guest name, mobile number and code** *(6 marks — W21 V1 Q1d)*

- Input court number from user [1]
- Check if court is available: Availability1[CourtNo] = TRUE [1]
- If available: input guest name and mobile number [1]
- Generate or assign unique booking code [1]
- Store guest, mobile and code in respective arrays [1]
- Set Availability1[CourtNo] ← FALSE to mark as booked [1]

```
INPUT CourtNo
IF Availability1[CourtNo] = TRUE THEN
    INPUT GuestName
    INPUT MobileNo
    [generate unique code]
    Guest1[CourtNo] ← GuestName
    Mobile1[CourtNo] ← MobileNo
    Code1[CourtNo] ← BookingCode
    Availability1[CourtNo] ← FALSE
ELSE
    OUTPUT "Court not available"
ENDIF
```

**Write pseudocode to calculate a discounted fare and display a booking confirmation for a rail journey** *(6 marks — W21 V2 Q1c)*

- Input passenger ID and start stage number [1]
- Look up fare from PriceStage1 array using stage number [1]
- Determine applicable discount based on conditions (e.g., early booking, loyalty) [1]
- Calculate discounted total [1]
- Display passenger name / ID and journey details [1]
- Display original fare, discount amount and final fare [1]

**Write pseudocode to count bookings over a period and apply an extra discount when the total exceeds a threshold** *(4 marks — W21 V2 Q1d)*

- Maintain a booking counter initialized to 0 [1]
- Increment counter with each confirmed booking [1]
- After each booking, check if counter exceeds threshold [1]
- If threshold exceeded, apply an extra discount to the current / next booking [1]

**Write pseudocode to book a table for a restaurant session by checking availability and recording passenger details** *(6 marks — W21 V3 Q1d)*

- Input table number from user [1]
- Check if table is available: TableLunch[TableNo] = TRUE [1]
- If available: input passenger name [1]
- Input cabin number and dietary requirement [1]
- Store all details in respective arrays [1]
- Set TableLunch[TableNo] ← FALSE to mark as booked [1]

```
INPUT TableNo
IF TableLunch[TableNo] = TRUE THEN
    INPUT PassengerName
    INPUT CabinNo
    INPUT DietReq
    PassengerLunch[TableNo] ← PassengerName
    CabinLunch[TableNo] ← CabinNo
    DietReqLunch[TableNo] ← DietReq
    TableLunch[TableNo] ← FALSE
ELSE
    OUTPUT "Table not available"
ENDIF
```

**Write pseudocode to verify a voter's eligibility and record their vote in the election system** *(5 marks — S21 V1 Q1c)*

- Input voter's unique ID [1]
- Search the registered voter list to verify the ID exists [1]
- Check that the voter has not already voted [1]
- If eligible: accept the voter's candidate selection [1]
- Record the vote and mark the voter as having voted (to prevent double voting) [1]

**Write pseudocode for a ticket booking algorithm that checks availability, calculates price and updates passenger records** *(6 marks — S21 V2 Q1c)*

- Input train number and number of tickets required [1]
- Check that sufficient seats are available on the selected train [1]
- If available: calculate total price (tickets × price per ticket) [1]
- Update TrainUpPassengers array to add the number of passengers booked [1]
- Display booking confirmation with train, seats and price [1]
- Deduct booked seats from remaining availability [1]

**Write pseudocode to count votes for each option and display separate results for students, staff and combined totals** *(6 marks — S21 V3 Q1b)*

- Declare arrays for student vote counts, staff vote counts and combined counts [1]
- Loop through all voter records [1]
- Identify whether each voter is a student or staff member [1]
- Increment the appropriate option counter (student or staff array) [1]
- Display counts for each option for students and staff separately [1]
- Display combined totals for each option [1]

#### Program Modification

**Describe changes to allow the program to handle a variable number of tables rather than a fixed constant** *(3 marks — W21 V3 Q1c)*

- Remove / replace CONSTANT MaxNoTables with a variable [1]
- Input the actual number of tables at the start of each session [1]
- Use this variable as the array size bound and loop limit throughout the program [1]

**Describe how the program could be modified to display the total number of courts booked in a session** *(4 marks — W21 V1 Q1e)*

- Add a counter variable (e.g., TotalBooked) initialized to 0 before the session [1]
- Each time a court is successfully booked, increment TotalBooked by 1 [1]
- After all bookings in the session are complete, display TotalBooked [1]
- Pseudocode or clear description provided for each point [1]

**Explain what changes would be needed to count and display the number of vegetarian and vegan passengers** *(4 marks — W21 V3 Q1e)*

- Add two counter variables: VegetarianCount and VeganCount, both initialized to 0 [1]
- When storing each dietary requirement, check whether it is "vegetarian" or "vegan" [1]
- Increment the appropriate counter each time a matching dietary requirement is recorded [1]
- At the end of the session, output both VegetarianCount and VeganCount [1]

**Describe the changes needed to the program to accommodate 8 candidates instead of 4** *(4 marks — S21 V1 Q1b)*

- Change the value of CONSTANT MaxCandidates from 4 to 8 [1]
- Increase the size of the CandidateNames array (and any vote-count arrays) to match [1]
- Loops and conditions that reference MaxCandidates will automatically use the new value [1]
- Check for any hardcoded value of 4 that was not using the constant and replace with MaxCandidates [1]

**Explain how the program could be extended to display each candidate's vote as a percentage of total votes** *(4 marks — S21 V1 Q1d)*

- Calculate the total number of votes cast (sum of all candidates' votes) [1]
- For each candidate, compute: (candidate's votes / total votes) × 100 [1]
- Output each candidate's name alongside their percentage [1]
- Handle edge case: if total votes = 0, avoid division by zero (display 0% or a message) [1]

**Explain how the program could display total passengers and revenue per journey, overall totals and the most popular journey** *(5 marks — S21 V2 Q1d)*

- Loop through all train journeys, displaying passenger count and revenue for each [1]
- Accumulate a running total of all passengers across all journeys [1]
- Accumulate a running total of all revenue across all journeys [1]
- Track which journey has the highest passenger count (using a max-finding comparison) [1]
- Display the name/number of the most popular journey and the overall totals [1]

**Describe what changes would need to be made to the program if there were 6 options instead of 5** *(2 marks — S21 V3 Q1c)*

- Change the value of CONSTANT NumberofOptions from 5 to 6 [1]
- Arrays and loops that use NumberofOptions as their bound will automatically update [1]

**Explain how the program would identify and count only first-preference votes from students** *(3 marks — S21 V3 Q1d)*

- Filter voter records to identify only student voters [1]
- From each student's ballot, read only the first-preference entry [1]
- Increment the counter for the corresponding option [1]
