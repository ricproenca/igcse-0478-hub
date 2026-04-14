# CH 09 Databases

> Source: https://moshikur.com/igcse-o-level-cs/ch-09-databases/

# CH 09 Databases

---

# 9.1

---

# [Introduction](#9.1)

# 9.2

---

# [Data Types](#9.2)

# 9.3

---

# [Primary Keys](#9.3)

## 9.4

---

# [Structured Query Language (SQL)](#9.4)

## 9.5

---

# [SQL Query Outputs](#9.5)

**>**>Syllabus

9.1 Introduction to Databases  
 • 9.1.1 Define a single-table database  
 • 9.1.2 Understand key database components: fields, records, and validation  
9.2 Data Types in Databases  
 • 9.2.1 Identify and describe basic data types:  
 ○ 9.2.1.1 Text/Alphanumeric  
 ○ 9.2.1.2 Character  
 ○ 9.2.1.3 Boolean  
 ○ 9.2.1.4 Integer  
 ○ 9.2.1.5 Real  
 ○ 9.2.1.6 Date/Time  
9.3 Primary Keys and Database Structure  
 • 9.3.1 Understand the purpose of a primary key  
 • 9.3.2 Identify a suitable primary key for a database table  
9.4 Structured Query Language (SQL)  
 • 9.4.1 Read and understand SQL scripts  
 • 9.4.2 Write and complete SQL queries for a single-table database  
 • 9.4.3 SQL commands covered:  
 ○ 9.4.3.1 SELECT  
 ○ 9.4.3.2 FROM  
 ○ 9.4.3.3 WHERE  
 ○ 9.4.3.4 ORDER BY ASCENDING  
 ○ 9.4.3.5 ORDER BY DESCENDING  
 ○ 9.4.3.6 SUM  
 ○ 9.4.3.7 COUNT  
 ○ 9.4.3.8 AND  
 ○ 9.4.3.9 OR  
9.5 SQL Query Outputs  
9.5.1 Identify and interpret outputs from SQL queries

---

# **9.1**

# **Introduction to Databases**

[![An infographic illustrating the concept of databases, featuring a central database icon with arrows pointing to user input, reports and files, and live data feeds, alongside the title 'Introduction to Databases' and a description of 'Organized Collection of Data'.](images/topic9_databases/ch_09_databases/img_001.png)](https://i0.wp.com/moshikur.com/wp-content/uploads/2025/11/image-6.png?ssl=1)

### **9.1.1 – What is a Single-Table Database?**

A **database** is a place where data is stored in an organised way so it can be easily searched and managed.

A **single-table database** means:

- All the data is stored in **one table**
- Each row stores **one record**
- Each column stores **one field**

### Example:

Imagine a **school database** that stores student information. It might look like this:

| StudentID | FirstName | LastName | Age | Gender |
| --- | --- | --- | --- | --- |
| 1001 | Amina | Khan | 15 | F |
| 1002 | Joseph | Lee | 16 | M |
| 1003 | Sara | Ali | 14 | F |

This is a **single-table** because everything is in **one table only**.

---

### **9.1.2 – Key Database Components**

Let’s break down the three important parts:

# 1. **Field**

- A **field** is a **column** in the table.
- Each field stores **one type** of data (e.g., Name, Age).
- Example: `FirstName`, `Age` are fields.

# 2. **Record**

- A **record** is a **row** in the table.
- It contains **all the information** about one person or item.
- Example: `1002 | Joseph | Lee | 16 | M` is one record.

### **Why Use Databases?**

**Easy to search** for information (e.g., find all students aged 16)

**Organised** and clean format

**Quick to update** and manage data

Helps avoid **mistakes** with validation

---

# Activity 9.1

---

### **1. Define what is meant by a database.** [2]

---

### **2. State what is meant by a single-table database and give an example.** [3]

---

### **3. A school uses a single-table database to store student information.**

**(a)** State what is meant by a **field** and give one example from a school database. [2]  
**(b)** State what is meant by a **record** and give one example from a school database. [2]

---

### **4. Identify the most suitable validation check for each of the following fields:**

**(a)** Student Age  
**(b)** Email Address  
**(c)** Name  
**(d)** Student ID [4]

---

### **5. Explain the purpose of validation when entering data into a database. Include one example.** [3]

---

# **9.2**

# **Data Types in Databases**

[![Infographic depicting the process of classifying data types in databases, featuring sections labeled 'Raw Information,' 'Classification/Storage,' and 'Structured Data.' Includes examples of data types like text, numbers, and dates, with a focus on ensuring correct handling and integrity.](images/topic9_databases/ch_09_databases/img_002.png)](https://i0.wp.com/moshikur.com/wp-content/uploads/2025/11/image-7.png?ssl=1)

---

### **What is a Data Type?**

When you create a database, each **field** must have a **data type**.

A **data type** tells the computer **what kind of data** will be stored in that field — is it a number, text, date, etc.?

This helps the database:

- Store the right kind of data
- Use the right validation rules
- Avoid errors

---

### **Common Data Types You Need to Know**

Here are the **six data types** in the syllabus, explained with examples:

---

### **1. Text / Alphanumeric**

Used for **words**, **letters**, **numbers that are not used for calculations**.

Can include letters, numbers, and symbols.

✅ Examples:  
`"Apple"`, `"A1B2C3"`, `"Postcode123"`

### **2. Character**

Used for **a single letter, number, or symbol**.

Only **one character** is stored.

✅ Examples:  
`'A'`, `'7'`, `'%'`

### **3. Boolean**

Only stores **TRUE** or **FALSE** values.

Sometimes shown as **Yes/No** or **1/0**.

✅ Examples:  
`TRUE`, `FALSE`, `Yes`, `No`

### **4. Integer**

Whole numbers only (no decimal point).

✅ Examples:  
`12`, `0`, `-5`, `1000`

### **5. Real**

Numbers that **can have decimals** (also called floating point numbers).

✅ Examples:  
`12.5`, `3.14`, `0.0`, `-9.99`

### **6. Date/Time**

Stores **dates**, **times**, or both.

Usually in a standard format like `DD/MM/YYYY` or `HH:MM`.

✅ Examples:  
`21/06/2025`, `14:30`, `01/01/2000 08:00`

---

# Activity 9.2

### **1. Data Type Detective**

**Task:**  
You are given a list of field names from different databases. Your job is to become a **Data Type Detective** and match each field to the correct data type.

**Field Names:**

- StudentName
- Age
- IsVaccinated
- Height
- ExamDate
- GenderInitial

**Instructions:**

- Write the **data type** for each field.
- Explain **why** you chose that data type.

---

### **2. Make a Mini Database Table**

**Task:**  
Create your own **5-row mini database table** about a topic you enjoy (e.g., pets, video games, books, sports, or food).

**Instructions:**

- Create at least **5 fields**, each using a different **data type**.
- Fill in **5 records**.
- Label each field with its **data type**.

**Example Topic: Pets**

| PetID (Integer) | PetName (Text) | PetType (Text) | Age (Integer) | IsVaccinated (Boolean) | BirthDate (Date) |
| --- | --- | --- | --- | --- | --- |
| 1 | Rocky | Dog | 3 | TRUE | 14/03/2021 |

---

### **3. Role-Play: Be the Field**

**Task:**  
Work in pairs or small groups. Each student **pretends to be a field** in a database.

**Instructions:**

- Choose a database theme (e.g., Library, School, Online Store).
- Each student picks a **field name** and **data type**.
- Act out what kind of data you accept and what you reject.

**Example:**  
“I’m the `Price` field. I’m a **REAL** data type. I allow decimal numbers like 12.99, but I reject words like ‘free’!”

---

### **4. Data Type Sorting Game**

**Task:**  
Cut out or prepare small cards with different **data values** (e.g., “John”, `TRUE`, `18.5`, `'A'`, `31/12/2024`).

**Instructions:**

- Create 6 boxes or sections for each data type.
- Sort the cards into the correct category.
- Time the class and turn it into a race!

---

### **5. Quiz Maker Challenge**

**Task:**  
Create a **multiple-choice quiz** with 6 questions (1 per data type). Each question should test understanding of when to use a specific data type.

**Instructions:**

- Write the question.
- Provide 4 answer choices.
- Mark the correct answer.

You can swap quizzes with a friend and test each other!

---

# **9.3**

## **Primary Keys and Database Structure**

### **9.3.1 – What is a Primary Key?**

A **primary key** is a **special field** in a database table that **uniquely identifies each record**.

Think of it like a **fingerprint** — it’s different for every person.

---

### Why is a Primary Key Important?

- It makes sure that **no two records are the same**.
- It helps to **search and find data quickly**.
- It prevents **duplicate data**.

---

### Example Table: Students

| StudentID | Name | Age | Class |
| --- | --- | --- | --- |
| 1001 | Amina | 15 | 9A |
| 1002 | Joseph | 16 | 10B |
| 1003 | Sara | 14 | 9B |

- Here, **StudentID** is the **primary key**.
- Each student has a **different ID**, even if they have the same name or age.

---

### ❌ Can a Primary Key Have Repeated Values?

**No!**  
A primary key must always be:

1. **Unique** (no two records can have the same value)
2. **Not empty** (you must enter something in it)

---

### **9.3.2 – How to Choose a Suitable Primary Key**

A good primary key should:

- Always be **unique** for each record
- Not change over time
- Be **simple** and **easy to use**

---

### ✅ Examples of Good Primary Keys

| Table | Field to Use as Primary Key |
| --- | --- |
| Students | StudentID |
| Library Books | BookID |
| Employees | EmployeeNumber |
| Products | ProductCode |
> ❗ Avoid using names, addresses, or anything that **can repeat or change**.

---

### 🔄 What if There’s No Natural Unique Field?

If no field is naturally unique, create an **ID number** just for that purpose. This is called a **surrogate key**.

Example:

- CustomerID: `C001`, `C002`, `C003`…

---

# Activity 9.3

---

### **1. Design Your Own Database**

**Task:**  
Choose a topic you like (e.g., Movies, Pets, Students, Books, Cars) and create a database table with at least **5 fields** and **5 records**.

**Instructions:**

- Include one field that will be the **primary key**
- Highlight or mark that field clearly
- Explain **why** you chose that field as the primary key

*Bonus*: Add a fake duplicate record and explain why it would cause a problem if the primary key wasn’t unique.

---

### **2. Primary Key Investigator**

**Task:**  
Your teacher gives you **a table with a problem**: two records have the same values in all fields!

**Instructions:**

- Identify why this is a problem
- Suggest a **new field** that could be used as a **primary key**
- Explain how it solves the issue

---

### **3. Role-Play: Find Your Match**

**Task:**  
Give each student a “record card” with different details (e.g., Name, Age, Favourite Colour, ID Number). Make two students have the same name or age.

**Instructions:**

- Ask students to walk around and **find someone with the same field** (e.g., same name)
- Show how this can cause confusion in a database
- Discuss how the **unique ID** helps prevent this confusion

---

### **4. Match the Table to the Key**

**Task:**  
Give students **sets of tables** and a **list of possible primary keys**.

**Instructions:**

- Match each table to its most suitable primary key
- Explain your choices

Example tables:

- Library books
- Hospital patients
- Exam results
- Vehicles

---

### **5. Primary Key Challenge**

**Task:**  
Challenge students to come up with the **worst possible field** to use as a primary key for different tables.

**Instructions:**

- Give reasons why that field would cause problems
- Then suggest a better alternative

Example:

- Table: Employees
- Bad key: LastName ❌
- Why? Many employees might have the same surname
- Good key: EmployeeID ✅

---

# **9.4**

# **Structured Query Language (SQL)**

[![Diagram illustrating the Structured Query Language (SQL) process, showing how a user or application sends a query to a database and receives results or data in return.](images/topic9_databases/ch_09_databases/img_003.png)](https://i0.wp.com/moshikur.com/wp-content/uploads/2025/11/image-8.png?ssl=1)

---

### **What is SQL?**

SQL (Structured Query Language) is a special language used to **talk to databases**.

You use SQL to:

- **Find data**
- **Filter data**
- **Sort data**
- **Do calculations on data**

You don’t need to draw tables — you write **commands**, and the computer gives you the results.

---

### **A Simple Table: Students**

| StudentID | FirstName | Age | Class |
| --- | --- | --- | --- |
| 1001 | Amina | 15 | 9A |
| 1002 | Joseph | 16 | 10B |
| 1003 | Sara | 14 | 9B |

This table is called **Students**.

---

### **Basic SQL Keywords**

You must know how to read and understand these commands:

---

### **1. SELECT**

Used to **choose which fields/columns** to show.

```
SELECT FirstName

FROM Students
```

> *This shows only the “FirstName” of every student.*

```
SELECT FirstName

FROM Students
```

> *This shows all fields of every student.*

---

### **2. FROM**

Used to **name the table** you are taking data from.

```
SELECT Age

FROM Students
```

*This means: Show me the Age column from the Students table.*

---

### **3. WHERE**

Used to **filter the rows** — only show the records that match a condition.

```
SELECT FirstName

FROM Students

WHERE Age = 15
```

*This shows the names of students who are 15 years old.*

---

### **4. AND / OR**

Used to add **more conditions**.

```
SELECT FirstName

FROM Students

WHERE Age > 14 AND Class = '9B'
```

*This shows names of students who are older than 14 AND in class 9B.*

```
SELECT FirstName

FROM Students

WHERE Class = '9A' OR Class = '9B'
```

💡 *This shows names of students who are in class 9A OR 9B.*

---

### **5. ORDER BY ASC / DESC**

Used to **sort** the output in **ascending (ASC)** or **descending (DESC)** order.

```
SELECT FirstName, Age

FROM Students

ORDER BY Age ASC
```

*This shows the names and ages of students, sorted from youngest to oldest.*

```
SELECT FirstName, Age

FROM Students

ORDER BY Age DESC
```

*This shows them from oldest to youngest.*

---

## **SQL Functions: SUM and COUNT**

---

### **6. COUNT**

Used to **count how many records** match a condition.

```
SELECT COUNT(*)

FROM Students
```

*This counts how many students are in the table.*

```
SELECT COUNT(*)

FROM Students

WHERE Age > 14
```

*This counts how many students are older than 14.*

---

### **7. SUM**

Used to **add up all values** in a numeric field.

```
SELECT SUM(Age)

FROM Students
```

*This adds up the ages of all students.*

---

```
SELECT SUM(Age)

FROM Students

WHERE Class = '9B'
```

*This adds up the ages of only the students in class 9B.*

**8. AVG**

Used to calculate the **average** value of a numeric column for all records that match a condition.

```
SELECT AVG(Marks)

FROM Students;
```

*This calculates the **average marks** of all students in the table.*

---

## **Writing Complete SQL Queries**

Here’s a step-by-step guide:

---

### Example Task:

Write a query to show the names of students in Class 10B.

**Solution:**

```
SELECT FirstName

FROM Students

WHERE Class = '10B'
```

---

### Example Task:

Count how many students are 15 years old.

**Solution:**

```
SELECT COUNT(*)

FROM Students

WHERE Age = 15
```

---

### Example Task:

Show names and ages of students, ordered from youngest to oldest.

**Solution:**

```
SELECT FirstName, Age

FROM Students

ORDER BY Age ASC
```

---

### **Understanding SQL Query Outputs**

Once you write a query, the computer gives you a **table of results**.

Example Query:

```
SELECT FirstName, Age

FROM Students

WHERE Class = '9A'
```

Output:

| FirstName | Age |
| --- | --- |
| Amina | 15 |
| Daniel | 14 |

This means:

- Only students from class 9A are shown.
- Only their **FirstName** and **Age** fields appear.
- It matches the exact condition you gave.

---

# Activity 9.4

## **SQL Commands – Tasks**

---

### **Students Table**

| StudentID | FirstName | Age | Class |
| --- | --- | --- | --- |
| 1001 | Amina | 15 | 9A |
| 1002 | Joseph | 16 | 10B |
| 1003 | Sara | 14 | 9B |
| 1004 | Daniel | 15 | 9A |
| 1005 | Laila | 17 | 10A |
| 1006 | Ethan | 16 | 10B |
| 1007 | Fatima | 14 | 9A |
| 1008 | Zain | 15 | 9B |
| 1009 | Priya | 15 | 10C |
| 1010 | Ali | 16 | 10A |

---

### **1. SELECT / FROM**

**Example Task:** Show the **FirstName** of all students in the **Students** table.

```
SELECT FirstName

FROM Students
```

✍️ **Student Task:**  
Show the **Age** of all students in the **Students** table.

---

### **2. WHERE**

**Example Task:** Show all students who are **15 years old**.

```
SELECT *

FROM Students

WHERE Age = 15
```

✍️ **Student Task:**  
Show all students who are in **Class ’10B’**.

---

### **3. AND**

**Example Task:** Show students who are **older than 14 AND in Class ‘9B’**.

```
SELECT *

FROM Students

WHERE Age > 14 AND Class = '9B'
```

✍️ **Student Task:**  
Show students who are **younger than 16 AND in Class ’10A’**.

---

### **4. OR**

**Example Task:** Show students who are in **Class ‘9A’ OR Class ‘9B’**.

```
SELECT *

FROM Students

WHERE Class = '9A' OR Class = '9B'
```

✍️ **Student Task:**  
Show students who are in **Class ’10B’ OR Class ’10C’**.

---

### **5. ORDER BY ASC**

**Example Task:** Show **FirstName** and **Age** of all students, sorted from **youngest to oldest**.

```
SELECT FirstName, Age

FROM Students

ORDER BY Age ASC
```

✍️ **Student Task:**  
Show **FirstName** and **Age** of all students, sorted from **oldest to youngest**.

---

### **6. ORDER BY DESC**

**Example Task:** Show **FirstName** and **Age**, sorted from **oldest to youngest**.

```
SELECT FirstName, Age

FROM Students

ORDER BY Age DESC
```

✍️ **Student Task:**  
Show **FirstName** and **StudentID**, sorted from **highest to lowest StudentID**.

---

### **7. COUNT**

**Example Task:** Count how many students are **15 years old**.

```
SELECT COUNT(*)

FROM Students

WHERE Age = 15
```

✍️ **Student Task:**  
Count how many students are in **Class ‘9B’**.

---

### **8. SUM**

**Example Task:** Find the **total of all students’ ages**.

```
SELECT SUM(Age)

FROM Students
```

✍️ **Student Task:**  
Find the **total of ages** of students in **Class ’10B’**.

---

### **9. SELECT + WHERE + ORDER BY**

**Example Task:** Show the **FirstName** and **Age** of students in **Class ‘9A’**, ordered from **youngest to oldest**.

```
SELECT FirstName, Age

FROM Students

WHERE Class = '9A'

ORDER BY Age ASC
```

✍️ **Student Task:**  
Show the **FirstName** and **Age** of students in **Class ’10B’**, ordered from **oldest to youngest**.

---

### **10. SELECT + WHERE + COUNT**

**Example Task:** Count how many students are **younger than 16**.

```
SELECT COUNT(*)

FROM Students

WHERE Age < 16
```

✍️ **Student Task:**  
Count how many students are **older than 14 AND in Class ‘9B’**.

---

### **11. SELECT + WHERE + SUM**

**Example Task:** Find the **total age** of students who are in **Class ’10A’**.

```
SELECT SUM(Age)

FROM Students

WHERE Class = '10A'
```

✍️ **Student Task:**  
Find the **total age** of students who are **older than 14 AND in Class ‘9A’**.

---

# **9.5**

# **SQL Query Outputs**

### **What does SQL output mean?**

When you write an SQL query, the database **processes your request** and shows the **result as a table**.

Understanding the output is just as important as writing the correct query.

---

### **Let’s Use the Students Table Again**

| StudentID | FirstName | Age | Class |
| --- | --- | --- | --- |
| 1001 | Amina | 15 | 9A |
| 1002 | Joseph | 16 | 10B |
| 1003 | Sara | 14 | 9B |
| 1004 | Daniel | 15 | 9A |
| 1005 | Laila | 17 | 10A |
| 1006 | Ethan | 16 | 10B |
| 1007 | Fatima | 14 | 9A |
| 1008 | Zain | 15 | 9B |
| 1009 | Priya | 15 | 10C |
| 1010 | Ali | 16 | 10A |

---

### **1. Viewing Specific Columns**

```
SELECT FirstName, Age

FROM Students
```

💡 *Only the selected fields (columns) appear in the output.*

**Output:**

| FirstName | Age |
| --- | --- |
| Amina | 15 |
| Joseph | 16 |
| Sara | 14 |
| Daniel | 15 |
| … | … |

---

### **2. Filtering Rows with WHERE**

```
SELECT FirstName

FROM Students

WHERE Age = 16
```

💡 *Only students aged 16 are shown.*

**Output:**

| FirstName |
| --- |
| Joseph |
| Ethan |
| Ali |

---

### **3. Using COUNT to Get a Total**

```
SELECT COUNT(*)

FROM Students

WHERE Class = '10B'
```

**Output:**

| COUNT(\*) |
| --- |
| 2 |

💡 *There are 2 students in Class 10B.*

---

### **4. Using SUM to Add Values**

```
SELECT SUM(Age)

FROM Students

WHERE Class = '10A'
```

**Output:**

| SUM(Age) |
| --- |
| 33 |

💡 *The total of ages for students in Class 10A is 33 (Laila: 17 + Ali: 16).*

---

### **5. Sorting Output with ORDER BY**

```
SELECT FirstName, Age

FROM Students

ORDER BY Age ASC
```

*Rows are sorted from youngest to oldest.*

**Output:**

| FirstName | Age |
| --- | --- |
| Sara | 14 |
| Fatima | 14 |
| Amina | 15 |
| Daniel | 15 |
| … | … |

---

### Leave a Reply[Cancel reply](/igcse-o-level-cs/ch-09-databases/#respond)