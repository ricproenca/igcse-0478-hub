# Paper 1 Analysis Plan

## Objective
Analyze all Paper 1 exam questions and map them to the syllabus structure. Create one pair of files (questions + answers) for each year.

## Files to Process

### Input Files (Paper 1 - Computer Systems)
| Type | Files |
|------|-------|
| Question Papers | `docs/papers_p1/0478_[series]_qp_[variant].pdf` |
| Marking Schemes | `docs/papers_p1/0478_[series]_ms_[variant].pdf` |

### Output Files (Per Year)
| File | Description |
|------|-------------|
| `markdown/paper1_[year]_questions.md` | Question mapping table |
| `markdown/paper1_[year]_answers.md` | Marking scheme content by syllabus |

## Output File Structure

### Questions File (`markdown/paper1_[year]_questions.md`)
Question mapping table with columns:
- Paper (e.g., S25 V1)
- Question (e.g., Q1)
- Alinea (e.g., a, b, c)
- Sub-alinea (e.g., i, ii, iii)
- Marks
- Topic
- Sub-topic
- Sub-sub-topic
- Difficulty (AO1, AO2, AO3)
- Description (one-sentence summary)

### Answers File (`markdown/paper1_[year]_answers.md`)
Marking scheme content organized by syllabus structure:
- Topic → Sub-topic → Sub-sub-topic
- Contains key answers, expected responses, and mark allocations
- **Question headers use the description from the questions file** (e.g., "State the number of bits in a nibble...") instead of question references (e.g., "Q1a (S25 V1)")
- **Deduplication**: When multiple questions have similar/identical answers, consolidate into a single entry with all relevant bullet points (avoid repeating the same answer multiple times)

## Syllabus Coverage (Paper 1 - Topics 1-6)

### 1. Data Representation
- 1.1 Number Systems
- 1.2 Text, Sound and Images
- 1.3 Data Storage and Compression

### 2. Data Transmission
- 2.1 Types and Methods of Data Transmission
- 2.2 Methods of Error Detection
- 2.3 Encryption

### 3. Hardware
- 3.1 Computer Architecture
- 3.2 Input and Output Devices
- 3.3 Data Storage
- 3.4 Network Hardware

### 4. Software
- 4.1 Types of Software and Interrupts
- 4.2 Types of Programming Language, Translators and IDEs

### 5. The Internet and its Uses
- 5.1 The Internet and the World Wide Web
- 5.2 Digital Currency
- 5.3 Cyber Security

### 6. Automated and Emerging Technologies
- 6.1 Automated Systems
- 6.2 Robotics
- 6.3 Artificial Intelligence

## Assessment Objectives
| Code | Description | Weighting |
|------|-------------|-----------|
| AO1 | Demonstrate knowledge and understanding of the principles and concepts | 40% |
| AO2 | Apply knowledge and understanding to given contexts | 40% |
| AO3 | Evaluate, make reasoned judgements, present conclusions | 20% |

## Processing Steps (Per Year)
1. Read QP PDFs for the year → Extract question structure (Q#, alineas, sub-alineas, marks)
2. Read MS PDFs for the year → Extract answer content
3. Map each sub-question to syllabus topics
4. Assess AO1/AO2/AO3 difficulty
5. Generate one-sentence description
6. **Deduplicate answers**: Merge questions with similar/identical answers into single entries
7. Create `paper1_[year]_questions.md` table
8. Create `paper1_[year]_answers.md` with MS content organized by syllabus (using descriptions as headers)

## Years to Process
- [x] 2025 (S25)
- [x] 2024 (W24, S24)
- [x] 2023 (W23, S23)
- [x] 2022 (W22, S22)
- [x] 2021 (W21, S21)

## Completed Files
| Year | Questions File | Answers File |
|------|---------------|--------------|
| 2025 | `markdown/paper1_2025_questions.md` | `markdown/paper1_2025_answers.md` |
| 2024 | `markdown/paper1_2024_questions.md` | `markdown/paper1_2024_answers.md` |
| 2023 | `markdown/paper1_2023_questions.md` | `markdown/paper1_2023_answers.md` |
| 2022 | `markdown/paper1_2022_questions.md` | `markdown/paper1_2022_answers.md` |
| 2021 | `markdown/paper1_2021_questions.md` | `markdown/paper1_2021_answers.md` |

## Master Consolidated Files
| File | Description | Lines |
|------|-------------|-------|
| `markdown/paper1_master_questions.md` | All questions aggregated by topic/sub-topic/sub-sub-topic (2021-2025) | ~1635 |
| `markdown/paper1_master_answers.md` | All answers deduplicated and consolidated by topic (2021-2025) | ~1414 |
