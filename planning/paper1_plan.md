# Paper 1 Analysis Plan

## Objective
Analyze all 2025 Paper 1 exam questions and map them to the syllabus structure.

## Files to Process

### Input Files (Paper 1 - Computer Systems)
| Type | Files |
|------|-------|
| Question Papers | `docs/papers_p1/0478_s25_qp_11.pdf`, `0478_s25_qp_12.pdf`, `0478_s25_qp_13.pdf` |
| Marking Schemes | `docs/papers_p1/0478_s25_ms_11.pdf`, `0478_s25_ms_12.pdf`, `0478_s25_ms_13.pdf` |

## Output Files

### 1. `markdown/paper1_questions.md`
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

### 2. `markdown/paper1_answers.md`
Marking scheme content organized by syllabus structure:
- Topic → Sub-topic → Sub-sub-topic
- Contains key answers, expected responses, and mark allocations

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

## Processing Steps
1. Read QP PDFs → Extract question structure (Q#, alineas, sub-alineas, marks)
2. Read MS PDFs → Extract answer content
3. Map each sub-question to syllabus topics
4. Assess AO1/AO2/AO3 difficulty
5. Generate one-sentence description
6. Create `paper1_questions.md` table
7. Create `paper1_answers.md` with MS content organized by syllabus
