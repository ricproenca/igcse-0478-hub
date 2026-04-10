# Paper 2 Analysis Plan

## Objective
Analyze all Paper 2 exam questions and map them to the syllabus structure. Create one pair of files (questions + answers) for each year.

## Files to Process

### Input Files (Paper 2 - Algorithms, Programming, Databases)
| Type | Files |
|------|-------|
| Question Papers | `docs/papers_p2/0478_[series]_qp_[variant].pdf` |
| Marking Schemes | `docs/papers_p2/0478_[series]_ms_[variant].pdf` |

### Output Files (Per Year)
| File | Description |
|------|-------------|
| `markdown/paper2_[year]_questions.md` | Question mapping table |
| `markdown/paper2_[year]_answers.md` | Marking scheme content by syllabus |

## Output File Structure

### Questions File (`markdown/paper2_[year]_questions.md`)
Question mapping table with columns:
- Paper (e.g., S24 V1)
- Question (e.g., Q1)
- Alinea (e.g., a, b, c)
- Sub-alinea (e.g., i, ii, iii)
- Marks
- Topic
- Sub-topic
- Sub-sub-topic
- Difficulty (AO1, AO2, AO3)
- Description (one-sentence summary)

### Answers File (`markdown/paper2_[year]_answers.md`)
Marking scheme content organized by syllabus structure:
- Topic → Sub-topic → Sub-sub-topic
- Contains key answers, expected responses, and mark allocations
- **Question headers use the description from the questions file** instead of question references
- **Deduplication**: When multiple questions have similar/identical answers, consolidate into a single entry

## Syllabus Coverage (Paper 2 - Topics 7-11)

### 7. Algorithm Design and Problem-Solving
- 7.1 Program Development Life Cycle
- 7.2 Problem Decomposition
- 7.3 Algorithm Design Methods (structure diagrams, flowcharts, pseudocode)
- 7.4 Standard Methods of Solution (linear search, bubble sort, totalling, counting, max/min/avg)
- 7.5 Validation and Verification
- 7.6 Testing (normal, abnormal, extreme, boundary test data)
- 7.7 Trace Tables
- 7.8 Error Identification

### 8. Programming
- 8.1 Programming Concepts (variables, data types, input/output, sequence, selection, iteration, string handling)
- 8.2 Arrays (1D and 2D arrays)
- 8.3 File Handling (open, close, read, write)

### 9. Databases
- 9.1 Database Design (fields, records, data types, primary key)
- 9.2 SQL Queries (SELECT, FROM, WHERE, ORDER BY, SUM, COUNT)

### 10. Boolean Logic
- 10.1 Logic Gates (NOT, AND, OR, NAND, NOR, XOR)
- 10.2 Logic Circuits (circuits from statements/truth tables, truth tables, logic expressions)

### 11. Scenario Based Algorithm
- Last question from every paper variant (may be Q8, Q9, Q10, Q11, Q12 or Q13 depending on paper)
- 15-mark unseen scenario question requiring **pseudocode/programming code**
- Scenario-based algorithm writing with arrays, loops, and calculations

## Assessment Objectives
| Code | Description | Weighting |
|------|-------------|-----------|
| AO1 | Demonstrate knowledge and understanding of the principles and concepts | 30% |
| AO2 | Apply knowledge and understanding to given contexts | 30% |
| AO3 | Evaluate, make reasoned judgements, present conclusions | 40% |

## Processing Steps (Per Year)
1. Read QP PDFs for the year → Extract question structure (Q#, alineas, sub-alineas, marks)
2. Read MS PDFs for the year → Extract answer content
3. Map each sub-question to syllabus topics
4. Assess AO1/AO2/AO3 difficulty
5. Generate one-sentence description
6. **Deduplicate answers**: Merge questions with similar/identical answers into single entries
7. Create `paper2_[year]_questions.md` table
8. Create `paper2_[year]_answers.md` with MS content organized by syllabus (using descriptions as headers)

## Years to Process
- [ ] 2024 (W24, S24, M24)
- [ ] 2023 (W23, S23, M23)
- [ ] 2022 (W22, S22, M22)
- [ ] 2021 (W21, S21, M21)

Note: 2025 papers not available in dataset

## Completed Files
| Year | Questions File | Answers File |
|------|---------------|--------------|
| 2024 | `markdown/paper2_2024_questions.md` | `markdown/paper2_2024_answers.md` |
| 2023 | | |
| 2022 | | |
| 2021 | | |

## Master Consolidated Files (After Processing)
| File | Description |
|------|-------------|
| `markdown/paper2_master_questions.md` | All questions aggregated by topic/sub-topic/sub-sub-topic (2021-2024) |
| `markdown/paper2_master_answers.md` | All answers deduplicated and consolidated by topic (2021-2024) |