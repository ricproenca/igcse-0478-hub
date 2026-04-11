# Paper 2 Analysis Plan

## Objective
Analyze all Paper 2 exam questions and map them to the syllabus structure. Create one pair of files (questions + answers) for each year.

## Files to Process

### Input Files (Paper 2 - Algorithms, Programming and Logic)
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
- Paper (e.g., S25 V1)
- Question (e.g., Q7)
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
- **Question headers use the description from the questions file** (e.g., "Write pseudocode to calculate the average of...") instead of question references (e.g., "Q7a (S25 V1)")
- **Deduplication**: When multiple questions have similar/identical answers, consolidate into a single entry with all relevant bullet points (avoid repeating the same answer multiple times)

## Syllabus Coverage (Paper 2 - Topics 7-11)

### 7. Algorithm Design and Problem-Solving
- 7.1 Program Development Life Cycle
- 7.2 Problem Decomposition
- 7.3 Algorithm Design Methods
- 7.4 Standard Methods of Solution
- 7.5 Validation and Verification
- 7.6 Testing
- 7.7 Trace Tables
- 7.8 Error Identification

### 8. Programming
- 8.1 Programming Concepts
- 8.2 Arrays
- 8.3 File Handling

### 9. Databases
- 9.1 Database Design
- 9.2 SQL Queries

### 10. Boolean Logic
- 10.1 Logic Gates
- 10.2 Logic Circuits

### 11. Scenario-Based Algorithm
- 11.1 Writing Pseudocode for Context Scenario

## Assessment Objectives
| Code | Description | Weighting |
|------|-------------|-----------|
| AO1 | Demonstrate knowledge and understanding of the principles and concepts | 40% |
| AO2 | Apply knowledge and understanding to given contexts | 40% |
| AO3 | Evaluate, make reasoned judgements, present conclusions | 20% |

## Paper Structure (75 marks total)
| Question(s) | Topic | Marks |
|-------------|-------|-------|
| Q1-Q5 | Topics 7-10 (various) | ~60 marks |
| Q6/Q7 | Topic 11: Scenario-Based Algorithm | 15 marks |

**Note:** Topic 11 (Scenario-Based Algorithm) appears as the final question on each paper, worth 15 marks, requiring students to design pseudocode for a given real-world scenario.

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

### 2024 ✅ (Winter 2024 + Summer 2024)
| Variant | Question Paper | Marking Scheme |
|---------|---------------|---------------|
| V1 | `0478_w24_qp_21.pdf` | `0478_w24_ms_21.pdf` |
| V2 | `0478_w24_qp_22.pdf` | `0478_w24_ms_22.pdf` |
| V3 | `0478_w24_qp_23.pdf` | `0478_w24_ms_23.pdf` |
| V4 | `0478_s24_qp_21.pdf` | `0478_s24_ms_21.pdf` |
| V5 | `0478_s24_qp_22.pdf` | `0478_s24_ms_22.pdf` |
| V6 | `0478_s24_qp_23.pdf` | `0478_s24_ms_23.pdf` |

### 2023 ✅ (Winter 2023 + Summer 2023)
| Variant | Question Paper | Marking Scheme |
|---------|---------------|---------------|
| V1 | `0478_w23_qp_21.pdf` | `0478_w23_ms_21.pdf` |
| V2 | `0478_w23_qp_22.pdf` | `0478_w23_ms_22.pdf` |
| V3 | `0478_w23_qp_23.pdf` | `0478_w23_ms_23.pdf` |
| V4 | `0478_s23_qp_21.pdf` | `0478_s23_ms_21.pdf` |
| V5 | `0478_s23_qp_22.pdf` | `0478_s23_ms_22.pdf` |
| V6 | `0478_s23_qp_23.pdf` | `0478_s23_ms_23.pdf` |

### 2022 (Winter 2022 + Summer 2022)
| Variant | Question Paper | Marking Scheme |
|---------|---------------|---------------|
| V1 | `0478_w22_qp_21.pdf` | `0478_w22_ms_21.pdf` |
| V2 | `0478_w22_qp_22.pdf` | `0478_w22_ms_22.pdf` |
| V3 | `0478_w22_qp_23.pdf` | `0478_w22_ms_23.pdf` |
| V4 | `0478_s22_qp_21.pdf` | `0478_s22_ms_21.pdf` |
| V5 | `0478_s22_qp_22.pdf` | `0478_s22_ms_22.pdf` |
| V6 | `0478_s22_qp_23.pdf` | `0478_s22_ms_23.pdf` |

### 2021 (Winter 2021 + Summer 2021)
| Variant | Question Paper | Marking Scheme |
|---------|---------------|---------------|
| V1 | `0478_w21_qp_21.pdf` | `0478_w21_ms_21.pdf` |
| V2 | `0478_w21_qp_22.pdf` | `0478_w21_ms_22.pdf` |
| V3 | `0478_w21_qp_23.pdf` | `0478_w21_ms_23.pdf` |
| V4 | `0478_s21_qp_21.pdf` | `0478_s21_ms_21.pdf` |
| V5 | `0478_s21_qp_22.pdf` | `0478_s21_ms_22.pdf` |
| V6 | `0478_s21_qp_23.pdf` | `0478_s21_ms_23.pdf` |

**Note:** 2025 papers may not be available yet.

## Output Files Overview
| Year | Questions File | Answers File |
|------|---------------|--------------|
| 2024 | `markdown/paper2_2024_questions.md` | `markdown/paper2_2024_answers.md` |
| 2023 | `markdown/paper2_2023_questions.md` | `markdown/paper2_2023_answers.md` |
| 2022 | `markdown/paper2_2022_questions.md` | `markdown/paper2_2022_answers.md` |
| 2021 | `markdown/paper2_2021_questions.md` | `markdown/paper2_2021_answers.md` |

## Master Consolidated Files (Future)
| File | Description |
|------|-------------|
| `markdown/paper2_master_questions.md` | All questions aggregated by topic/sub-topic/sub-sub-topic (2021-2024) |
| `markdown/paper2_master_answers.md` | All answers deduplicated and consolidated by topic (2021-2024) |