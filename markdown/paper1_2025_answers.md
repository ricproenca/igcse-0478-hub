# Paper 1 Marking Scheme (2025)

This document contains the expected answers and key points from the 2025 Paper 1 marking schemes, organized by syllabus topics.

## Marking Principles
- Award marks for correct information only
- Alternative wording may be acceptable if meaning is conveyed
- Unless stated otherwise, acceptanswers that are factually correct
- Do not penalize spelling or grammatical errors unless specified
- Use the "OR" convention for alternative acceptable answers
- Use the "e.g." convention for examples that gain credit

---

## Topic 1: Data Representation

### 1.1 Number Systems

#### Binary, Hexadecimal, Denary Conversions
**Q1a (S25 V1) - 2 marks**
- A nibble contains 4 bits
- Conversion of hexadecimal digit to denary: multiply each digit by its place value

**Q1b (S25 V1) - 2 marks**
- Convert binary to hexadecimal by grouping bits into nibbles (4 bits each)
- Starting from the right, pad with leading zeros if necessary
- Convert each nibble to its hexadecimal equivalent

**Q1a (S25 V2) - 2 marks**
- Denary to binary: divide by 2, record remainders
- Denary to hexadecimal: divide by 16, record remainders OR convert via binary

#### Binary Addition
**Q1c (S25 V1) - 3 marks**
- Add bits from right to left
- Carry over values when sum exceeds 1
- Show all carries in working
- State final result

**Q1b (S25 V2) - 3 marks**
- Perform binary addition with overflow detection
- Overflow occurs when result requires more bits than allocated
- State whether overflow has occurred

#### Two's Complement
**Q1c (S25 V2) - 2 marks**
- Invert all bits (change 0s to 1s and 1s to 0s)
- Add 1 to the result
- Discard any overflow bit

#### Logical Shifts
**Q1d (S25 V2) - 3 marks**
- Logical left shift: multiply by 2 (each shift left)
- Logical right shift: divide by 2 (each shift right)
- Fill vacated positions with zeros

### 1.2 Text, Sound and Images

#### Image Representation
**Q1a (S25 V3) - 2 marks**
- File size = resolution × colour depth
- Resolution = width × height in pixels
- Colour depth = bits per pixel

**Q1b (S25 V3) - 2 marks**
- Number of colours = 2^n where n = colour depth (bits per pixel)
- To find colour depth needed: use logarithm or trial and error

#### Sound Representation
**Q1c (S25 V3) - 3 marks**
- File size = sample rate × duration × sample resolution × number of channels
- Sample rate measured in Hz (samples per second)
- Sample resolution = bits per sample

### 1.3 Data Storage and Compression

#### Data Compression
**Q1d (S25 V3) - 3 marks**
- Lossless compression: original data can be fully reconstructed (e.g., ZIP, PNG)
- Lossy compression: some data is discarded, original cannot be fully reconstructed (e.g., JPEG, MP3)
- Lossy achieves greater compression but loses quality

---

## Topic 2: Data Transmission

### 2.1 Types and Methods of Data Transmission

#### Packet Switching
**Q2a (S25 V1) - 2 marks (1+1)**
- Header: contains source/destination addresses, sequence numbers, error control information
- Trailer: contains error-checking data (e.g., checksum) to detect transmission errors

#### Data Transmission Methods
**Q2b (S25 V1) - 4 marks**
- Serial: data sent one bit at a time over a single channel
- Parallel: multiple bits sent simultaneously over multiple channels
- Identify method based on: number of channels, distance capability, cost, interference susceptibility

#### USB Interface
**Q2c (S25 V1) - 3 marks**
- Hot-swappable (can connect/disconnect without restarting)
- Single connector type for multiple devices
- Supports plug and play
- High data transfer rates
- Power can be supplied to devices

#### Serial vs Parallel
**Q2a (S25 V3) - 2 marks**
- Advantage of serial: suitable for long distances, less interference, fewer wires/cables
- Parallel: faster for short distances but suffers from crosstalk over long distances

### 2.2 Methods of Error Detection

#### Parity Check
**Q2a (S25 V2) - 3 marks**
- Even parity: number of 1-bits should be even
- Odd parity: number of 1-bits should be odd
- If parity doesn't match, an error has occurred
- Cannot detect multiple bit errors

#### Checksum
**Q2b (S25 V2) - 2 marks**
- Sum of all data values is calculated and sent with data
- Receiver recalculates sum and compares
- If sums don't match, error detected

#### ARQ (Automatic Repeat Query)
**Q2c (S25 V2) - 3 marks**
- Sender transmits data and waits for acknowledgement (ACK) or negative acknowledgement (NAK)
- If NAK received or timeout occurs, data is resent
- Process continues until ACK received
- Uses sequence numbers to identify missing packets

#### Check Digit
**Q2d (S25 V2) - 4 marks**
- For ISBN: multiply digits by positional weights, sum, divide by 11, find remainder
- Check digit = 11 minus remainder (or 0 if remainder is 0, or X if remainder is 10)

### 2.3 Encryption

#### Symmetric Encryption
**Q5d (S25 V2) - 3 marks**
- Same key used for encryption and decryption
- Advantage: faster than asymmetric encryption
- Disadvantage: key must be shared securely between sender and receiver

#### Asymmetric Encryption
**Q2d (S25 V3) - 3 marks**
- Public key: used to encrypt, freely available
- Private key: used to decrypt, kept secret
- Sender encrypts with recipient's public key
- Only recipient's private key can decrypt

---

## Topic 3: Hardware

### 3.1 Computer Architecture

#### Von Neumann Components
**Q3a (S25 V1) - 3 marks (2+1)**
- Components: ALU (Arithmetic Logic Unit), CU (Control Unit), registers, main memory, buses
- Accumulator: stores intermediate results of calculations performed by ALU

**Q3a (S25 V3) - 2 marks**
- MAR (Memory Address Register): holds address of memory location to be accessed
- MDR (Memory Data Register): holds data being read from or written to memory
- PC (Program Counter): holds address of next instruction to be fetched
- CIR (Current Instruction Register): holds the current instruction being executed

#### Fetch-Decode-Execute Cycle
**Q3b (S25 V1) - 4 marks**
1. Fetch: instruction copied from memory to MAR, then to MDR, then to CIR; PC incremented
2. Decode: CU interprets the instruction and determines required operations
3. Execute: ALU performs calculation or data transferred between registers/memory

**Q3b (S25 V3) - 4 marks**
- Stage 1 (Fetch): Copy instruction from memory address in PC to CIR; increment PC
- Stage 2 (Decode): CU decodes instruction in CIR; determines operation needed
- Stage 3 (Execute): ALU carries out operation OR data moved between registers/memory

#### CPU Performance Factors
**Q3c (S25 V1) - 4 marks**
- Cache: fast memory close to CPU; stores frequently accessed instructions/data; reduces time to fetch from main memory
- Cores: multiple cores allow parallel processing; each core can execute instructions independently
- Clock speed: rate at which CPU processes instructions (Hz); higher speed = faster processing

**Q3c (S25 V3) - 4 marks**
- Cores: more cores = more instructions processed simultaneously = better multitasking
- Cache: larger cache = more data/instructions held close to CPU = faster access
- Clock speed: higher frequency = more fetch-decode-execute cycles per second

#### Embedded Systems
**Q3d (S25 V3) - 2 marks**
- Computer system built into another device
- Designed for a specific purpose rather than general use
- Examples: washing machine, car engine management, microwave

### 3.2 Input and Output Devices

#### Input Devices
**Q6a (S25 V2) - 2 marks**
- Barcode scanner: uses light sensor to read reflected light pattern; decodes into numerical data

#### Sensors
**Q6b (S25 V2) - 3 marks**
- Temperature sensor: converts temperature to electrical signal (analog or digital)
- Uses thermistor or thermocouple principles
- Analog: continuous voltage that varies with temperature
- Digital: discrete values output to computer

**Q6b (S25 V3) - 4 marks**
- Light sensor: uses photodiode/phototransistor; resistance changes with light intensity
- Temperature sensor: uses thermistor; resistance changes with temperature
- Motion sensor: uses PIR (passive infrared); detects changes in infrared radiation

#### Output Devices
**Q6c (S25 V2) - 4 marks**
- Inkjet: sprays tiny droplets of ink onto paper; droplets directed by electrostatic plates
- Laser: uses toner powder and heat; laser creates image on photoconductive drum
- Inkjet: better for photo printing, slower, ink can smudge
- Laser: faster, higher quality text, more expensive initially

#### Actuators
**Q6d (S25 V2) - 4 marks**
- Actuator: converts electrical signals from computer into physical movement
- Types: motors (rotary), solenoids (linear), servos (controlled position)
- Examples: robot arm movement, motor driving wheels, valve control

### 3.3 Data Storage

#### Primary Storage
**Q3a (S25 V2) - 3 marks (2+1)**
- RAM: random access memory; volatile; read and write; stores programs and data currently in use
- ROM: read-only memory; non-volatile; permanently stored instructions; bootstrap program
- Volatile: contents lost when power is removed

#### Secondary Storage
**Q3b (S25 V2) - 3 marks**
- Magnetic storage (hard drive): uses magnetised platters; read/write heads; high capacity; relatively slow
- Optical storage (CD/DVD): uses laser to read reflective surface; portable; lower capacity
- Solid-state storage (SSD): uses flash memory; no moving parts; fast; expensive per GB

#### Virtual Memory
**Q3c (S25 V2) - 4 marks**
- Portion of secondary storage used as additional RAM
- When RAM is full, inactive data moved to virtual memory (swap file/page file)
- Allows programs larger than physical RAM to run
- Slower than actual RAM due to secondary storage access time

### 3.4 Network Hardware

#### IP Address
**Q3d (S25 V2) - 4 marks**
- IPv4: 32-bit address; four decimal numbers (0-255) separated by dots (e.g., 192.168.1.1)
- IPv6: 128-bit address; eight hexadecimal groups (e.g., 2001:0db8:85a3::8a2e:0370:7334)
- IPv6 provides larger address space, better security, auto-configuration

---

## Topic 4: Software

### 4.1 Types of Software and Interrupts

#### System vs Application Software
**Q4a (S25 V1) - 2 marks**
- Application software: programs that perform specific tasks for users
- Examples: word processor, web browser, spreadsheet, games

#### Operating System Functions
**Q4b (S25 V1) - 4 marks**
- Memory management: tracks what is stored in RAM; allocates memory to programs; handles swapping
- File management: organises files in folders/directories; handles reading/writing; controls access
- Device management: communicates with peripherals via drivers; manages printer queues; handles input/output

**Q4a (S25 V3) - 2 marks**
- Examples: Windows, macOS, Linux (operating systems)
- Functions: user interface, memory management, file management, process management

**Q4b (S25 V3) - 4 marks**
- File management: creating, deleting, renaming, moving files and folders; maintaining directory structure
- Folder hierarchy: organised in tree structure; path names locate files; access permissions

#### Interrupts
**Q4c (S25 V1) - 2 marks**
- Interrupt: signal to CPU indicating device needs attention
- Generated by hardware when action required (e.g., keypress, data received)
- CPU suspends current task, handles interrupt, resumes execution

**Q4c (S25 V2) - 4 marks**
- Interrupt generated when device needs CPU attention
- CPU completes current instruction, saves state
- Interrupt Service Routine (ISR) executed to handle interrupt
- CPU returns to interrupted program
- Allows efficient use of CPU; non-polling approach

### 4.2 Types of Programming Language, Translators and IDEs

#### Compiler vs Interpreter
**Q4a (S25 V2) - 2 marks**
- Compiler: translates entire program before execution; produces separate executable file
- Interpreter: translates and executes line by line; no separate executable

**Q4d (S25 V1) - 4 marks**
- Compiler: entire source code translated to machine code/executable; errors shown after full translation; faster execution; no source code needed to run
- Interpreter: line-by-line translation; errors shown immediately; slower execution; source code needed to run

#### IDE Functions
**Q4b (S25 V2) - 4 marks**
- Code editor: syntax highlighting, line numbers, auto-indentation
- Debugger: step-through execution, watch variables, breakpoints
- Compiler/Interpreter: built-in translation of code
- Run/Build tools: one-click compilation and execution

#### Assembly Language
**Q4c (S25 V3) - 3 marks**
- Low-level language using mnemonics (e.g., ADD, MOV)
- One-to-one correspondence with machine code instructions
- Used for direct hardware control, embedded systems, performance-critical code

#### High-Level Languages
**Q4d (S25 V3) - 3 marks**
- Advantages: easier to read/write; portable across different hardware; abstraction from hardware details
- Examples: Python, Java, C++

---

## Topic 5: The Internet and its Uses

### 5.1 The Internet and the World Wide Web

#### HTTP and HTTPS
**Q5a (S25 V1) - 3 marks (1+2)**
- HTTPS: HyperText Transfer Protocol Secure
- Uses encryption (SSL/TLS) to secure data in transit
- Provides authentication of website identity
- Required for sensitive data (banking, passwords)

#### Cookies
**Q5b (S25 V1) - 3 marks**
- Small text file stored on user's computer by website
- Contains information about user preferences, login status, browsing history

**Q5c (S25 V1) - 3 marks**
- Session cookies: temporary; deleted when browser closes; used for login status
- Persistent cookies: stored until expiry date; remember preferences; tracking

**Q5c (S25 V3) - 3 marks**
- Cookies stored with: domain name, expiry date, unique ID, data
- Website reads cookie when user returns; retrieves saved preferences

#### URL
**Q5a (S25 V3) - 2 marks**
- Protocol: http:// or https://
- Domain name: identifies website server
- Path: location of specific page/file on server

#### Web Browser Functions
**Q5b (S25 V3) - 3 marks**
1. User enters URL or clicks link
2. Browser sends HTTP/HTTPS request to web server
3. Server responds with HTML, CSS, JavaScript
4. Browser renders and displays content

### 5.2 Digital Currency
*No questions in 2025 papers on this sub-topic*

### 5.3 Cyber Security

#### Cyber Security Threats
**Q5a (S25 V2) - 2 marks**
- Malware: software designed to damage or disrupt (viruses, worms, trojans, ransomware)
- Phishing: fraudulent emails/messages attempting to steal personal information

**Q5d (S25 V3) - 4 marks**
- Phishing: fake emails/websites imitating legitimate sources; tricks users into revealing passwords/financial details
- Malware: viruses, worms, trojans; spreads through downloads, attachments, infected websites
- Prevention: anti-malware software, user education, email filtering, two-factor authentication

#### Social Engineering
**Q5b (S25 V2) - 3 marks**
- Phishing: persuading victims to reveal confidential information
- Prevents: user education, verifying sender, not clicking unknown links, checking URLs carefully

#### Security Solutions
**Q5d (S25 V1) - 4 marks**
- Access levels: different permissions for different users; prevents unauthorized access to files
- Firewalls: monitors incoming/outgoing network traffic; blocks suspicious connections
- Anti-malware: scans for and removes malicious software; real-time protection
- Authentication: passwords, biometrics; verifies user identity before granting access

**Q5c (S25 V2) - 4 marks (AO3)**
- Effectiveness evaluation criteria: cost, ease of use, level of protection, maintenance required
- Compare solutions based on: protection level, false positives, system performance impact

---

## Topic 6: Automated and Emerging Technologies

### 6.1 Automated Systems

#### Sensors
**Q6a (S25 V1) - 2 marks**
- Sensor: device that detects changes in physical conditions (temperature, light, sound)
- Converts physical input to electrical signals for computer processing

**Q6b (S25 V1) - 4 marks**
- Sensor detects physical change in environment
- Converts to electrical signal (analog or digital)
- Processed by microprocessor/controller
- Actuator receives command and produces physical output
- Feedback loop maintains desired conditions

#### Automated System Definition
**Q6a (S25 V3) - 2 marks**
- System that operates automatically without continuous human intervention
- Uses sensors, processors, and actuators to monitor and control processes

**Q6b (S25 V3) - 4 marks**
- Light sensor: detects light intensity; used in street lamps, camera exposure
- Temperature sensor: measures heat; used in HVAC, weather stations
- Motion sensor: detects movement; used in security systems, automatic doors

### 6.2 Robotics

#### Robot Components
**Q6c (S25 V1) - 4 marks**
- Sensors: collect data from environment (cameras, proximity sensors, pressure sensors)
- Microprocessor/controller: processes sensor data; makes decisions; controls actuators
- Actuators: motors that produce physical movement (arms, wheels, grippers)
- Program/instructions: software that defines robot behavior and responses

### 6.3 Artificial Intelligence

#### AI Characteristics
**Q6d (S25 V1) - 3 marks**
- Expert system: uses knowledge base (facts and rules) and inference engine
- Reasoning: applies rules to facts using backward/forward chaining
- Provides advice/diagnosis based on stored knowledge

#### Machine Learning
**Q6c (S25 V3) - 3 marks**
- Traditional programming: programmer writes explicit rules; computer follows them
- Machine learning: computer learns patterns from data; creates its own rules
- Uses training data; improves with more data; can handle complex/vague patterns

#### Expert Systems
**Q6d (S25 V3) - 4 marks (AO3)**
- Advantages: consistent, available 24/7, can process large amounts of data, no human fatigue
- Disadvantages: lacks common sense, cannot handle novel situations, depends on knowledge base quality
- Compare to human experts: humans have intuition, creativity, emotional intelligence

---

## General Marking Notes

### Command Words
| Command | Meaning |
|---------|---------|
| State | Give factual answer without explanation |
| Describe | Give detailed account |
| Explain | Give reasons or causes |
| Compare | Show similarities and differences |
| Evaluate | Make judgement based on evidence |

### Common Errors to Avoid
- Not showing working for calculations
- Forgetting to include units
- Confusing similar concepts (e.g., RAM vs ROM, compiler vs interpreter)
- Giving vague descriptions instead of specific details

### Answer Presentation
- Use bullet points for multiple points
- Numbered steps for processes
- Diagrams where appropriate (not required but helpful)
- Clear, concise language
