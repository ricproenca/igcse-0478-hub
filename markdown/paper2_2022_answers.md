# Paper 2 Marking Scheme (2022)

This document organises the 2022 Paper 2 marking scheme content by syllabus structure.

---

## 7. Algorithm Design and Problem-Solving

### 7.3 Algorithm Design Methods

#### Complete a flowchart to classify scores as pass/fail and count each category [6] *(S22 V1 Q4a)*
- Input Score
- IS Score >= 50? Yes → Pass[PassCount] ← Score, PassCount ← PassCount + 1; No → Fail[FailCount] ← Score, FailCount ← FailCount + 1
- Count ← Count + 1
- IS Count = 60? (loop control)
- All branches and connectors correct

#### Complete a flowchart to calculate the total and average of 100 numbers [6] *(S22 V3 Q5)*
- Total ← 0; Counter ← 0
- INPUT Number
- Total ← Total + Number
- Counter ← Counter + 1
- IS Counter = 100? No → loop back; Yes → Average ← Total / Counter
- OUTPUT Total; OUTPUT Average; END

#### Redesign a sorting algorithm to use a WHILE loop with a suitable end condition [4] *(W22 V2 Q5b)*
- Set condition to end input (correct placement)
- Set up test (correct placement)
- Remove MarksEntry counter
- WHILE / ENDWHILE structure correct

#### Modify an algorithm to count backwards using a different loop structure [3] *(W22 V3 Q2b)*
- Set Count ← 50
- Subtract 1 from Count each iteration
- UNTIL Count = 34 / Count < 35; OR FOR Count ← 50 TO 35 STEP -1 / NEXT Count

---

### 7.4 Standard Methods of Solution

#### Describe what the number-finding algorithm does [2] *(S22 V1 Q5b)*
- Finds 3-digit numbers where the first digit equals the last digit
- Outputs these numbers (palindromic 3-digit numbers)

#### Describe what the prime number finding algorithm does [2] *(S22 V3 Q4b)*
- Finds prime numbers from the input
- Stores prime numbers in an array

---

### 7.5 Validation and Verification

#### Identify three different validation checks for a four-digit PIN number [6] *(W22 V1 Q3a)*
- Type check: must be integer (not letters or special characters)
- Length check: must be exactly 4 characters/digits
- Range check: must be between 1000 and 9999 (inclusive)
- Two marks per check: name of check + description of what it does

#### Describe a verification method used when changing a PIN number [3] *(W22 V1 Q3b, W22 V2 Q3)*
- Input new PIN; input again / visual check
- Check both inputs are the same
- Check new PIN is not the same as old PIN
- **Verification** ensures data has not changed from the original when entered; double entry involves comparing two inputs of the same data

#### Modify an algorithm to output only non-zero readings [3] *(W22 V1 Q2b)*
- IF Reading[Count] <> 0 THEN OUTPUT … ENDIF
- Conditional placed correctly between the output statements (between statements 17 and 18)

#### Write code to validate the day number input for a car park booking [3] *(W22 V2 Q1b)*
- Range check: 1–14
- Type check: integer
- IF conditional with error message
- WHILE / REPEAT loop for re-entry

#### Write conditional code to store valid floor number choice with error for invalid [3] *(W22 V3 Q1b)*
- Conditional statement checking input value
- Only store True for 3-floors if 2-floors is not already True
- Error message displayed for invalid input

#### Calculate the check digit for a given barcode number [1] *(W22 V3 Q3a(i))*
- Check digit = 1

#### Identify which barcodes have incorrect check digits [2] *(W22 V3 Q3a(ii))*
- Codes C and D have incorrect check digits

#### Identify a type of error that check digits cannot detect [2] *(W22 V3 Q3b(i))*
- Two or more digits transposed (swapped) — check digit systems cannot detect transposition errors

#### Describe how a weighted check digit is calculated [2] *(W22 V3 Q3b(ii))*
- Multiply each digit by a different number / place value
- Add together and divide (modulo check)

#### State two other types of validation check [2] *(W22 V3 Q3c)*
- Length check
- Type check
- Presence check
- Format check
(Any two of the above)

#### Write validation code for area of interest input [3] *(S22 V1 Q1c)*
- Presence check: not empty
- Type check: valid inputs Y/N or from an area list
- Error message if invalid; continue if valid

#### Write validation code to ensure score input is within range 0–100 [4] *(S22 V1 Q4b)*
- WHILE Score < 0 OR Score > 100 DO; error message; INPUT Score; ENDWHILE
- OR REPEAT … UNTIL Score >= 0 AND Score <= 100

#### Identify the validation check and verification method in the password algorithm [4] *(S22 V2 Q2b)*
- Validation: length check — checks number of characters in password
- Verification: double entry — comparison of two inputs being the same

#### Add input validation to a prime number algorithm to reject values less than 3 [3] *(S22 V3 Q4c)*
- Insert WHILE loop after Input Number with Number < 3 condition
- Error message within loop
- ENDWHILE to close; OR REPEAT … UNTIL Number >= 3

---

### 7.6 Testing

#### Identify two types of test data with descriptions [2] *(W22 V2 Q4)*
- Normal: valid data that should be accepted (e.g. 7 for a 1–14 range)
- Boundary/Extreme: data on the acceptable limits (e.g. 1 or 14)
- (One mark per type: name + description)

#### Write two sets of test data for an email address validation algorithm [4] *(S22 V1 Q3)*
- Normal: computerscience@cambridge.org.uk (valid — contains @, accepted)
- Erroneous: computerscienceisgreat (no @, rejected)
- Two marks per set: data value + expected outcome

#### Write two sets of test data for a password validation algorithm [4] *(S22 V2 Q2c)*
- Set 1 erroneous: e.g. "small" (rejected — too short)
- Set 2 normal: "password" and "password" (accepted — both match and correct length)

#### Describe normal and erroneous test data for room type validation [2] *(S22 V3 Q1b)*
- Normal: accepted room type from the valid menu (e.g. Large, Small1, Small2)
- Erroneous: any value not on the menu (rejected)

#### Match test data types to their descriptions [4] *(S22 V3 Q2)*
- Extreme: data always on the limit of the acceptable range
- Boundary: data on or just outside the limit of the acceptable range
- Erroneous/Abnormal: data that should always be rejected
- Normal: data within the limits of acceptability

---

### 7.7 Trace Tables

#### Complete a partially-written reading-counter algorithm — W22 V1 [6] *(W22 V1 Q2a)*
- Line 1 = 100
- Line 7 = Value > 100
- Line 11 = Reading[Value] + 1
- Line 14 = INPUT Value
- Line 18 = Reading[Count]
- Line 19 = Count – 1

#### Complete a partially-written reading-counter algorithm — W22 V3 [6] *(W22 V3 Q2a)*
- Line 01 = 50
- Line 08 = Value > 50
- Line 12 = Reading[Value] + 1
- Line 18 = INPUT Value
- Line 23 = Reading[Count]
- Line 24 = Count + 1

#### Complete a trace table for a stock management algorithm [4] *(W22 V1 Q4a)*
Trace (Sold / Stock / Total / OUTPUT):
- 50 / 0
- 24 / 26 / 24
- 12 / 14 / – / Add new stock
- 64 / 36
- 6 / 58 / 42
- 30 / 28 / 72
- 12 / 16 / – / Add new stock
- 66 / 84
- 18 / 48 / 102
- –1 / – / – / 102

#### Complete a trace table for a stock and sales tracking algorithm [4] *(W22 V3 Q4a)*
Trace (Stock / Total / Sale / OUTPUT):
- 10 / 0
- 9 / 1 / Y
- 8 / 2 / Y
- 7 / 3 / Y
- 6 / 4 / Y
- 5 / 5 / Y
- 4 / 6 / Y
- 14 / –
- – / – / N / Add new stock
- – / – / – / 6

#### Complete a trace table for a digit decomposition algorithm [5] *(W22 V2 Q6)*
Trace (Counter / Number / Hundreds / Temp / Tens / Units / OUTPUT):
- 876 → 8, 76, 7, 6
- 606 → 6, 6, 0, 6
- 124 → 1, 24, 2, 4

#### Complete a trace table for an algorithm finding numbers where first = last digit [5] *(S22 V1 Q5a)*
Inputs: 8, 66, 606, 6226, 8448, 642, 747, 77, 121; Limit = 9
Trace (Counter / Value / First / Last / Limit / OUTPUT):
- – / – / 0 / 0 / 8
- 1 / 66
- 2 / 606 / 6 / 6 / – / 606
- 3 / 6226
- 4 / 8448
- 5 / 642 / 6 / 2
- 6 / 747 / 7 / 7 / – / 747
- 7 / 77
- 8 / 121 / 1 / 1 / – / 121

#### Complete a trace table for a temperature monitoring algorithm [7] *(S22 V2 Q4a)*
Inputs: 75, 78, 84, 87, 91, 80, 75, 70, 65, 62, –1, 20
Trace (Counter / Hot / Cold / Serve / Temp / Error / OUTPUT):
- 0 / 0 / 0 / 0
- 1 / – / – / 1 / 75
- 2 / – / – / 2 / 78
- 3 / – / – / 3 / 84
- 4 / 1 / – / – / 87 / – / Too Hot
- 5 / 2 / – / – / 91 / – / Too Hot
- 6 / – / – / 4 / 80
- 7 / – / – / 5 / 75
- 8 / – / – / 6 / 70
- 9 / – / – / 7 / 65
- 10 / – / 1 / – / 62 / – / Too Cold
- – / – / – / – / –1 / 30 / 30

#### Complete a trace table for a prime number finding algorithm [7] *(S22 V3 Q4a)*
Inputs: 5, 9, 8, 10, 7; Limit = 5
Trace (In / Logic / Test / Number / Store[Count] / Count / Limit / Out / OUTPUT):
- – / – / – / – / – / 0 / 5
- 1 / TRUE / 2 / 9
- – / – / 3
- – / FALSE
- 2 / TRUE / 2 / 5
- – / – / 3 / 5 / 1
- 3 / TRUE / 2 / 8
- – / FALSE
- 4 / TRUE / 2 / 10
- – / FALSE
- 5 / TRUE / 2 / 7
- – / – / 3 / 7 / 2 / – / 0 / 5
- – / – / – / – / – / – / – / 1 / 7

---

### 7.8 Error Identification

#### Identify and describe a problem in the stock management algorithm [3] *(W22 V1 Q4b)*
- Stock falls below zero (goes negative)
- Before subtracting, test if Stock > Sold
- Provide an error message / re-input if not enough stock

#### Identify and correct four errors in an array-sorting algorithm [4] *(W22 V2 Q5a)*
- Line 09: `Higher[HighList] ← MarksEntry` → should be `Higher[HighList] ← Mark`
- Line 15: `MidList ← MidList` → should be `MidList ← MidList + 1`
- Line 17: `Lower[HighList] ← Mark` → should be `Lower[LowList] ← Mark`
- Line 22: `NEXT MarksEntry = 500` → should be `UNTIL MarksEntry = 500`

#### Identify three errors in a password validation algorithm [3] *(S22 V2 Q2a)*
- Line 8: `PassCheck ← TRUE` → should be `PassCheck ← FALSE`
- Line 12: `IF Password <> Password` → should be `IF Password2 <> Password`
- Line 18: `UNTIL PassCheck OR Attempt <> 3` → should be `UNTIL PassCheck OR Attempt = 3`

#### Identify an unnecessary statement in the temperature algorithm [1] *(S22 V2 Q4c)*
- Updating Serve variable (`Serve ← Serve + 1`) is not required / redundant

---

## 8. Programming

### 8.1 Programming Concepts

#### Identify an appropriate constant for a car park booking program [2] *(W22 V2 Q1a(i))*
- Name: NumberDays (or similar)
- Value: 14
- Constants store values that do not change during program execution

#### Identify an appropriate constant for a window cleaning program [3] *(W22 V3 Q1a(i))*
- Name: BasicClean (or similar)
- Value: 10.00
- Reason: the base cleaning cost doesn't change during program execution

#### Identify an appropriate constant for a wildlife park program [3] *(S22 V2 Q1a(i))*
- Name: AdultCostOneDay (or similar)
- Value: 20.00
- Purpose: storing the cost of an adult ticket for one day (fixed, does not change)

#### Identify appropriate variables and arrays for meeting room program [4] *(S22 V3 Q1a)*
- Variable: ClientName — storing the name of the person making a booking
- Array: BookingsLarge[] — storing bookings for the large meeting room
- Other appropriate names, data types and uses accepted

#### Identify an appropriate variable for a wildlife park program [3] *(S22 V2 Q1a(ii))*
- Name: NumberOfTickets
- Data type: Integer
- Purpose: inputting the number of tickets / adult tickets purchased

#### Match programming terms to descriptions [4] *(W22 V2 Q2)*
- Counting: tracking the number of iterations in a loop
- Repetition: carrying out an action multiple times
- Selection: branching based on a condition
- Sequence: a set of statements executed in order
- Totalling: adding numbers together to find a sum

#### Match data types to descriptions [4] *(S22 V1 Q2)*
- Char: a single character from the keyboard
- String: multiple characters
- Boolean: only one of two values (True/False)
- Integer: only whole numbers
- Real: any number including decimals

#### Explain the difference between variables and constants with examples [4] *(S22 V3 Q3)*
- Variables represent values that change during execution (can store results, count, total, or hold user input); example: any variable used in a program
- Constants represent values that must stay the same throughout execution; example: Pi, tax rate, fixed fee
- (Two marks each: explanation + example)

#### Describe how to improve the output of the temperature monitoring algorithm [1] *(S22 V2 Q4b)*
- Include a message to explain the value being output
- Outputting labels for Hot count, Cold count and Serve count

---

### 8.2 Arrays

#### Identify appropriate arrays with names, data types and sample data for a membership club program [5] *(W22 V1 Q1a(i))*
- Possible array names: Name, Age, Gender, Type, TeamMember, AnnualFee, Paid
- Data types: String (Name), Integer (Age), Char (Gender/Type), Boolean (TeamMember/Paid), Real (AnnualFee)
- Sample data provided for each array
- At least two complete array descriptions for full marks

#### Write code using a loop to input values into an array [2] *(W22 V1 Q1a(ii))*
- Use a FOR / REPEAT / WHILE loop to input values
- Append / store each input in the correct array index

#### Identify an appropriate array for a car park booking program [2] *(W22 V2 Q1a(ii))*
- Name: LicenceNumbers (or similar)
- Purpose: storing car licence numbers for each booked space

#### Identify an appropriate array for a window cleaning program [3] *(W22 V3 Q1a(ii))*
- Name: NameAddress (or similar)
- Data type: String
- Sample data: e.g. Mrs Singh / Park View

#### Identify appropriate arrays, variables and constants for the pier program [5] *(S22 V1 Q1a)*
- MP1: arrays identified
- MP2: variables / constants identified
- MP3: names given
- MP4: sample data provided
- MP5: uses described
- MP6: two fully described examples (name + sample data + use)

#### Describe a 1D array including structure, index and example declaration [3] *(S22 V2 Q3a)*
- A list / one column of data of the same data type
- Stored under a single identifier with a single index
- Example: `DECLARE MyArray[1:10] OF INTEGER`

#### Explain why a loop is needed to search all elements of an array [2] *(S22 V2 Q3b)*
- Use a counter to index each array element
- The same code is used repeatedly to check every element (loop avoids repetition)

---

## 9. Databases

### 9.1 Database Design

#### Identify the primary key field in a warehouse stock database table [2] *(W22 V1 Q5a, W22 V3 Q5a)*
- Primary key: ItemCode
- Reason: uniquely identifies each item in the database

#### Identify the data type of the SubjectCode field [1] *(W22 V2 Q7a(i))*
- SubjectCode: Text

#### Explain why the Candidates field cannot be Boolean [1] *(W22 V2 Q7a(ii))*
- Boolean only has two possible values (True/False); Candidates can hold many different numeric values

#### State the number of fields in the games database table [1] *(S22 V1 Q6a)*
- 8 fields

#### Explain why a primary key field must contain a unique value for each record [1] *(S22 V1 Q6b)*
- The primary key must be unique / different for each record so that each record can be individually identified

#### Explain why a specific field in the nursing database is redundant [1] *(S22 V2 Q5b)*
- The field Uses already shows this information; storing it again duplicates data

#### Identify a Boolean field from the PLANETS database table [1] *(S22 V3 Q6a)*
- Larger (only two values: Yes/No — whether the planet is larger than Earth)

---

### 9.2 SQL Queries

#### Write a QBE query to find items with stock level below 10 [3] *(W22 V1 Q5b)*
- Fields: ItemCode / Manufacturer / Level
- Table: WAREHOUSE (all three)
- Show: ✓ ✓ ✗
- Criteria: Level < 10

#### Write a SQL SELECT query for subjects sorted ascending with Practicals less than 1 [3] *(W22 V2 Q7b)*
- Output: Geography 200, Geology 80, History 250, Mathematics 350 (sorted ascending)
- Criteria: Practicals < 1
- Correct SELECT / FROM / WHERE / ORDER BY structure

#### Write a QBE query for subjects with fewer than 150 candidates sorted descending [3] *(W22 V2 Q7c)*
- Fields: SubjectCode / SubjectName / Candidates
- Sort: Descending on Candidates
- Criteria: Candidates < 150

#### Write a QBE query to find items not in store from a specific country [3] *(W22 V3 Q5b)*
- Fields: Description / Country / InStore
- Show: ✓ ✓ ✗
- Criteria: InStore = N

#### Write a QBE query to find out-of-stock games on order sorted by name [3] *(S22 V1 Q6c)*
- Fields: GameID / GameName / GamePrice
- Sort: Ascending on GameName
- Show: ✓ ✓ ✓ ✗ ✗
- Criteria: NumberStock = 0 AND OnOrder = "Y"

#### Write a QBE query to find single-use items with stock below reorder level [4] *(S22 V2 Q5a)*
- Table: NURSE
- Fields: ItemNumber / Description / SingleUse / StockLevel
- Show: ✓ ✓ ✗ ✗
- Criteria: SingleUse = True AND StockLevel < [ReorderLevel]

#### Write a QBE query to find planets larger than Earth with year length over 365 days [3] *(S22 V3 Q6b)*
- Field: PlanetName (Sort = Ascending, Show ✓)
- Field: Larger (Show ✗, Criteria = Yes)
- Field: YearLength (Show ✗, Criteria = > 365)

---

## 11. Scenario-Based Algorithm

### 11.1 Writing Pseudocode for Context Scenario

#### Write code to filter out unpaid members and transfer paid members to new arrays [2] *(W22 V1 Q1b)*
- Loop through all members
- IF Paid = False: transfer those with Paid = True to new arrays (or delete unpaid entries)

#### Write algorithm to calculate annual membership fees based on age and team membership [6] *(W22 V1 Q1c)*
- Loop through all members
- CASE age OF: 18 → Adult rate; 50 → Senior rate; 80 → Golden rate
- IF TeamMember THEN fee × 0.9 (10% discount) ELSE full fee
- Correct conditional nesting and fee assignment

#### Write algorithm to calculate unpaid fee running totals and display percentages [5] *(W22 V1 Q1d)*
- Loop all members
- Identify unpaid via condition (Paid = False)
- Running totals by each of the three fee types
- Calculate percentage of total for each category
- Display all three totals with appropriate messages

#### Write algorithm to book the first available parking space for a given day [6] *(W22 V2 Q1c)*
- Input day number and accessible choice
- Conditional check for accessible requirement
- Initialise variable to find first available
- Loop through array elements for the given day
- Find first available space; store licence number and client name
- Output space number or "no space available" message

#### Describe changes needed to extend car park booking system to 4 weeks [3] *(W22 V2 Q1d)*
- Change constant to 560 / 28 (days × spaces)
- Update validation message range to 1–28
- Resize arrays to match new capacity
- Update loops to cover the full new range

#### Write algorithm to count and display total accessible and general bookings [4] *(W22 V2 Q1e)*
- Initialise counters for accessible and general separately
- Increment the correct counter for each booking type
- Maintain counts for the full 2-week cycle
- Output totals for both types with appropriate messages

#### Write algorithm to calculate total cleaning cost with multipliers and additions [6] *(W22 V3 Q1c)*
- Total ← 10.00 (base cost)
- Add extra windows cost if applicable
- CASE floors: 2 → × 1.1; 3 → × 1.15 (in correct order)
- IF inside → × 1.25
- IF polish → × 1.05 (correct order of operations)
- IF solar panels → + 20.00

#### Write algorithm to count customers per service and identify most/least popular [5] *(W22 V3 Q1d)*
- Count customers per service type (all services, excluding basic + additional windows)
- Identify the most popular service
- Identify the least popular service
- Calculate percentage of total bills for each service
- Display results with appropriate messages

#### Write algorithm to extend stock purchase with quantity and stock validation [3] *(W22 V3 Q4b)*
- Input number / quantity to purchase
- Check quantity ≤ current stock
- After checking: update Stock ← Stock – Number; update Total ← Total + Number

#### Write code to calculate and display total membership fee for paid members [3] *(S22 V1 Q1b)*
- Add / use a variable to total membership fee
- Initialise total to 0
- Check Paid field using conditional; add 75 to running total
- OR count paid members and multiply by 75

#### Write algorithm to input sponsor name and message with confirmation and storage [5] *(S22 V1 Q1d)*
- Input sponsor name and message
- Output both for confirmation
- Method to confirm (Y/N input)
- Allow re-entry if errors detected
- Charge $200; store name + message in arrays; increment array index

#### Write algorithm to display a menu and output the selected membership list [4] *(S22 V1 Q1e)*
- Menu provided to user; input code
- Validate input
- CASE / IF to match chosen option
- Output chosen list using loop through arrays
- Handle empty list case

#### Write code to display today's date and following booking dates [3] *(S22 V2 Q1b)*
- Input today's date
- Use a loop (FOR / REPEAT / WHILE)
- Output today's date with suitable message and 6 or 7 following dates
- OR use an array / variables with all days and display available dates

#### Describe how to generate a unique booking number [2] *(S22 V2 Q1c)*
- Initialise variable / counter for booking number
- Each booking number is one larger than the previous
- OR check existing bookings to ensure uniqueness before assigning

#### Write algorithm to calculate total cost of tickets and attraction add-ons [6] *(S22 V2 Q1d)*
- Initialise running total to 0
- Input number of tickets with prompt; identify ticket type; add cost to running total
- Ability to book several different ticket types
- Check children ≤ 2 × adults
- Identify attraction type; input number with prompt
- Check attraction count ≤ total tickets; add attraction cost to running total

#### Describe how to calculate and compare family ticket price against individual prices [3] *(S22 V2 Q1e)*
- Use selection to identify 2+ adults/seniors and 2+ children
- Calculate new price including family tickets
- Compare family ticket price vs ordinary / group price
- Identify the best value / lowest cost option

#### Write algorithm to calculate discounted cost for multi-day room bookings [4] *(S22 V3 Q1c)*
- Introduce variable / array for number of days
- IF / CASE to check 2–6 days inclusive
- Get daily rate for selected room type
- Multiply days by room rate; multiply total cost by 70% (reduce by 30%)

#### Write algorithm to confirm booking, generate unique code and store booking data [6] *(S22 V3 Q1d)*
- Output all relevant data (client name, room, day, cost) with messages
- Input confirmation from user
- Conditional to check for positive confirmation (WHILE loop)
- Attempt to generate a unique booking code; fully unique code generated
- Identify room using CASE / IF
- Store code in both room array and booking code array; store client name and cost in arrays

#### Write algorithm to search a selected room's bookings for available days [4] *(S22 V3 Q1e)*
- Select room to search
- Use a suitable loop through the room's booking array
- IF / conditional to check if element has a booking
- If not booked, output the day index
- Check all elements until end of array
