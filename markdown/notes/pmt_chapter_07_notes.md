# CAIE Computer Science IGCSE — Chapter 7: Algorithm Design and Problem-Solving
### Advanced Notes

---

### Program Development Life Cycle

The program development life cycle describes the main stages involved in creating a program. The four stages are: analysis, design, coding, and testing.

| Stage | Purpose | Tasks |
|-------|---------|-------|
| Analysis | Understand the problem and what the solution needs to achieve. | **Abstraction**: Removing unnecessary details to focus only on what is important. **Decomposition**: Breaking the overall problem into smaller, more manageable sub-problems. **Identification of the problem**: Clearly state what the problem is. **Identification of requirements**: Work out what inputs, processes, and outputs are required. |
| Design | Plan the solution before writing code. | **Decomposition**: Continue breaking down sub-problems into smaller steps if needed. **Design the solution**: The solution to a problem can be represented in several ways, including structure diagrams, flowcharts, and pseudocode, to provide a plan for the coding stage. |
| Coding | Translate the design into a working program. | **Writing program code**: Use a programming language to implement the design. **Iterative testing**: Test the code repeatedly as it is written, fixing errors as they occur. |
| Testing | Check that the program works correctly and meets requirements. | **Test program code**: Run the program code, using test data to make sure that it produces the correct output. |

---

### System Decomposition

Every computer system is made up of sub-systems. Each sub-system is made up of further sub-systems. Breaking a system into sub-systems makes it easier to design, understand, and test.

Decomposition is the process of breaking a problem into smaller, more manageable parts. Each smaller part can then be solved separately. Each part will usually involve:

- **Inputs:** Data that goes into the system
- **Processes:** Actions or calculations performed on the data
- **Outputs:** Information produced by the system
- **Storage:** Data saved for later use

---

### Methods to Design and Construct a Solution to a Problem

In the design stage, the solution to a problem can be represented in the following forms.

#### Structure Diagrams

Structure diagrams can be used to visually represent the process of decomposing a problem. Each level, further down the structure diagram, shows tasks further broken down.

When coding the solution for the problem, each sub-system can be developed independently, allowing work to be made on the system in parallel (by spreading the workload across a team) and making testing and debugging easier.

![Diagram: hierarchical structure diagram showing a "System" box at the top, branching down to three boxes: "Sub-system 1", "Sub-system 2", and "Sub-system 3"; Sub-system 1 branches further down to "Sub-system 1.1"; Sub-system 3 branches down to "Sub-system 3.1" and "Sub-system 3.2"]

---

#### Pseudocode

Pseudocode is a text-based way of describing a solution in structured steps. It uses programming-like keywords but is language-independent. There is a specific set of pseudocode keywords available online for the Cambridge IGCSE Computer Science exam.

Here's an example of some pseudocode to ask the user to enter a number repeatedly until the number they enter is less than or equal to 100.

```
INPUT Number
WHILE Number > 100 DO
    OUTPUT "The number is too large"
    INPUT Number
ENDWHILE
OUTPUT "The number is acceptable"
```

---

#### Flowcharts

Flowcharts are diagrams that show the step-by-step flow of a process. You should be aware of the following flowchart symbols:

![Diagram: reference table of flowchart symbols showing six shapes each paired with a name and description — (1) arrow/flow line: "An arrow represents control passing between the connected shapes"; (2) rectangle/process: "This shape represents something being performed or done"; (3) rectangle with double vertical lines/subroutine: "This shape represents a subroutine call that will relate to a separate, non-linked flowchart"; (4) parallelogram/input-output: "This shape represents the input or output of something into or out of the flowchart"; (5) diamond/decision: "This shape represents a decision (Yes/No or True/False) that results in two lines representing the different possible outcomes"; (6) rounded rectangle/terminator: "This shape represents the 'Start' and 'Stop' of the process"]

Here is a typical flowchart to outline a process for inputting a value and checking if it falls within a specific range (0 to 100 inclusive):

![Diagram: flowchart showing — START terminator → PRINT "Input a value between 0 and 100 inclusive" process box → INPUT Value parallelogram → IS Value < 0 OR IS Value > 100? diamond; "Yes" branch goes right to PRINT "Invalid value, try again" parallelogram, which loops back up to INPUT Value; "No" branch goes down to PRINT "Accepted: ", Value parallelogram → END terminator]

---

### Standard Methods of Solution

The following methods of solution can be used to solve many different problems.

#### Linear Search

Linear search is a searching algorithm, used to find items in a list. You can think of it as going along a bookshelf one by one until you come across the book you're looking for. Sometimes the algorithm gets lucky and finds the desired element almost immediately, while in other situations, if the desired element is towards the end of a list or the list is incredibly long, the algorithm is incredibly inefficient.

**Example:** Find the position of Apple in the data.

![Diagram: step-by-step colour-coded table walkthrough of a linear search for "Apple" in an array [Banana, Orange, Apple, Kiwi, Mango] at indices 0–4 — first, index 0 (Banana) is highlighted in red/blue as the current position; then index 1 (Orange) is highlighted; then index 2 (Apple) is highlighted in green indicating a match found; the algorithm returns index 2 and terminates]

*Note: if the item was not found, a suitable error message should be output.*

---

#### Bubble Sort

Sorting algorithms are designed to take a number of elements in any order and output them in a logical order. Bubble sort is a common form of sorting algorithm that makes comparisons and swaps between adjacent elements. The largest element in the unsorted part of the input is said to "bubble" to the top of the data with each iteration of the algorithm.

The algorithm starts at the first element in an array and compares it to the second. If they are in the wrong order, the algorithm swaps the pair. Otherwise, the algorithm moves on. The process is then repeated for every adjacent pair of elements in the array until the end of the array is reached (at which point the largest element is in the last position of the array).

This is referred to as one pass of the algorithm. For an array with n elements, the algorithm will perform a maximum of n passes through the data, at which point the input is sorted and can be returned.

**Example:** Use bubble sort to arrange the elements in the array into ascending order.

![Diagram: multi-step colour-coded walkthrough of bubble sort on array [4, 9, 1, 6, 7] — Pass 1: (1) 4 and 9 highlighted green (correct order, no swap); (2) 9 and 1 highlighted red then swapped to show [4, 1, 9, 6, 7]; (3) 9 and 6 highlighted red then swapped to show [4, 1, 6, 9, 7]; (4) 9 and 7 highlighted red then swapped to show [4, 1, 6, 7, 9] — end of first pass. Pass 2: (1) 4 and 1 highlighted red then swapped to show [1, 4, 6, 7, 9]; (2) 4 and 6 highlighted green (correct order); (3) 6 and 7 highlighted green (correct order); (4) 7 and 9 highlighted green (correct order) — end of second pass, data is sorted. A final third pass confirms no swaps are made before the algorithm terminates]

This is the end of the second pass, and we can see that the data is sorted. However, the algorithm wouldn't terminate here. It would carry out another final pass before terminating, to confirm that the data is sorted by checking that no swaps are made.

---

#### Totalling

Totalling is used to work out the sum of a set of values. There are lots of scenarios where totalling can be used, such as adding up a player's score in each round of a game to find their total score.

To find the total, create a variable that is initialised as 0, and then add each value to the total using a loop.

#### Counting

Counting is used to count how many times something occurs.

To count the number of times something occurs, create a variable that is initialised as 0, and increase the counter by 1 each time the condition is met. This is often used within WHILE loops to control the number of repetitions.

#### Finding Minimum and Maximum Values

To identify the largest or smallest value in a set:

- Start with the first value as the current maximum or minimum.
- Compare each new value with the current maximum/minimum and update if needed.

#### Finding the Average Value

To calculate the mean value in a set of numbers, use totalling to find the sum of all numbers. Then divide the total by the count of numbers.

To find the median, select the item at the middle index (which can be found by dividing the maximum index by 2).

---

### Validation

Validation is the process of checking that input data is reasonable and sensible before it is accepted by the system. It prevents errors caused by incorrect or unrealistic data being entered. There are several different types of validation check.

#### Range check

Ensures data is within a specified range.

*Example: Age must be between 0 and 120.*

#### Length check

Ensures data has the correct number of characters.

*Example: A UK postcode should not exceed 8 characters.*

#### Type check

Ensures data is of the correct data type.

*Example: An age field must be numeric, not text.*

#### Presence check

Ensures data is actually entered (not left blank).

*Example: A name field must not be empty.*

#### Format check

Ensures data is in the correct format or pattern.

*Example: An email address must contain "@".*

#### Check digit

Extra digit calculated from the other digits, used to detect errors in entry.

*Example: Commonly used in ISBN numbers and barcodes.*

---

*This work by PMT Education is licensed under CC BY-NC-ND 4.0*
