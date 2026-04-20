# Paper 1 Marking Scheme (2022)

This document contains the expected answers and key points from the 2022 Paper 1 marking schemes, organized by syllabus topics.

## Marking Principles
- Award marks for correct information only
- Alternative wording may be acceptable if meaning is conveyed
- Unless stated otherwise, accept answers that are factually correct
- Do not penalize spelling or grammatical errors unless specified
- Use the "OR" convention for alternative acceptable answers
- Use the "e.g." convention for examples that gain credit

---

## Topic 1: Data Representation

### 1.1 Number Systems

#### Binary Conversions
**Convert three denary numbers to binary** (3 marks)
- Divide by 2, record remainders
- Example: 64 → 01000000, 101 → 01100101, 242 → 11110010

**Match denary values to binary values** (3 marks)
- 41 → 00101001, 174 → 10101110, 86 → 01010110

**Convert 12-bit binary to denary** (2 marks)
- Multiply each bit by place value and sum
- Example: 000101010111 = 343

**Convert hexadecimal values to binary** (4-6 marks)
- Each hex digit = 4 binary digits
- Example: 2F → 00101111, 15 → 00010101, D6 → 11010110

**Convert binary to denary** (2-3 marks)
- Example: 10110011 = 179

**Convert denary to hexadecimal** (3 marks)
- Divide by 16, record remainders
- Example: 167 → A7, 214 → D6

#### Binary Representation
**Explain why computer can only process binary data** (2 marks)
- Computers use logic gates/switches
- Logic gates have two states (on/off)
- Binary represents these two states (0/1)

#### Hexadecimal Uses
**Give two other uses of hexadecimal** (2 marks)
- HTML colour codes
- MAC addresses
- Memory dumps
- Assembly language
- IP addresses
- Error codes

#### Two's Complement
**Calculate two's complement negative number** (2 marks)
- Convert positive number to binary
- Flip all bits (0→1, 1→0)
- Add 1
- Example: -78 → 10110010

### 1.2 Text, Sound and Images

#### Sound Representation
**Identify type of data stored in MP3 file** (1 mark)
- Sound

**Identify compression type for WAV file** (1 mark)
- Not compressed / lossless

**Calculate file size of sound recording** (3-4 marks)
- Sample rate × duration × sample resolution × channels
- Convert bits to bytes, then to appropriate units

**Identify effect on file size of reducing sample rate** (1 mark)
- File size decreases

#### Image Representation
**Calculate file size of 16-bit colour image** (3 marks)
- Width × height × colour depth = total bits
- Convert to bytes
- Example: 150 × 100 × 16 = 240,000 bits = 30,000 bytes

### 1.3 Data Storage and Compression

#### Compression Types
**Identify if MP3 is lossy, lossless or not compressed** (1 mark)
- Lossy compressed file

**Calculate effect of compression on file size** (2 marks)
- File size is reduced by percentage given

---

## Topic 2: Data Transmission

### 2.1 Types and Methods of Data Transmission

#### Packet Switching
**State two features of packet switching** (2 marks)
- Data split into packets
- Each packet has header with address
- Packets can take different routes
- Reassembled at destination

#### Serial vs Parallel
**Identify transmission method from description** (2 marks)
- Serial: single wire, one bit at a time
- Parallel: multiple wires, multiple bits simultaneously

#### USB
**Explain benefits of USB connection** (3 marks)
- Hot-swappable
- Single connector type
- Plug and play
- High data transfer rates
- Can supply power to devices

### 2.2 Methods of Error Detection

#### Check Digit
**State what check digit is used for** (2 marks)
- Detect errors in data entry/transmission
- Calculated using algorithm (e.g., Modulo 11)

**Calculate check digit for barcode** (4 marks)
- Multiply digits by positional weights
- Sum the products
- Divide by modulus (e.g., 11)
- Check digit = modulus - remainder

#### Parity Check
**Complete parity table for 7-bit values** (4 marks)
- Count 1s in each byte
- Add parity bit to make odd/even
- Example: 1010101 → 11010101 (odd parity)

**Identify which value has correct parity** (2 marks)
- Count 1s, verify against given parity bit

**Explain how parity check detects errors** (3 marks)
- Count 1s in received byte
- Compare with parity bit
- If mismatch, error detected
- Cannot detect multiple bit errors

#### Checksum
**State what checksum is used for** (2 marks)
- Detect errors after data transmission
- Sum of data values compared before/after

#### ARQ
**Describe how ARQ handles errors** (2-3 marks)
- Sender transmits data, starts timer
- Receiver checks for errors, sends acknowledgement
- If no ACK before timeout, data resent
- Continues until successful transmission

### 2.3 Encryption

**State how encryption keeps data secure** (1 mark)
- Scrambles data so it cannot be read
- Only authorized recipients can decrypt

---

## Topic 3: Hardware

### 3.1 Computer Architecture

#### Von Neumann Model
**State the name of primary storage where data is fetched** (1 mark)
- RAM (Random Access Memory)

**State second and third stages of FDE cycle** (2 marks)
- Decode
- Execute

**Identify two components used in fetch stage** (2 marks)
- PC (Program Counter)
- MAR (Memory Address Register)
- MDR (Memory Data Register)
- CIR (Current Instruction Register)

#### Registers
**State purpose of MAR** (1 mark)
- Memory Address Register
- Stores address of memory location to be accessed

**State purpose of MDR** (1 mark)
- Memory Data Register
- Stores data being read from or written to memory

**Describe role of PC in FDE cycle** (2 marks)
- Program Counter
- Holds address of next instruction
- Incremented after each fetch

**Describe role of accumulator** (2 marks)
- Stores intermediate results of calculations
- Part of ALU

**Identify three registers** (2-3 marks)
- MAR, MDR, PC, CIR, Accumulator

#### Buses
**Identify three types of buses** (2 marks)
- Address bus
- Data bus
- Control bus

**Describe role of three types of buses** (2 marks)
- Address bus: carries memory addresses
- Data bus: carries data between components
- Control bus: carries control signals

#### Fetch-Decode-Execute Cycle
**Describe the three stages of FDE cycle** (4 marks)
- Fetch: instruction copied from memory to MAR, then MDR, then CIR; PC incremented
- Decode: CU interprets instruction, determines operation
- Execute: ALU performs calculation OR data transferred

#### CPU Performance
**Explain effect of clock speed on performance** (2 marks)
- Higher clock speed = more cycles per second
- More instructions processed per second
- Faster execution

**Describe how cache memory improves performance** (3 marks)
- Fast memory close to CPU
- Stores frequently accessed data/instructions
- Reduces time to fetch from main memory

#### Embedded Systems
**State what is meant by embedded system** (2 marks)
- Computer system designed for specific purpose
- Built into larger device
- Contains microprocessor/dedicated hardware

### 3.2 Input and Output Devices

#### Input Devices
**Identify two input devices** (2 marks)
- Keyboard, mouse, touchscreen, microphone, camera, scanner, sensor

**Identify sensor for automated system** (1 mark)
- Temperature sensor, light sensor, proximity sensor, pressure sensor

#### Output Devices
**Identify two output devices** (2 marks)
- Screen, speaker, printer, actuator, LED

#### Sensors and Actuators
**Describe how sensors work in automated system** (3 marks)
- Sensor detects physical condition (temperature, light, etc.)
- Converts to electrical signal
- Sends to microprocessor for processing

**Describe how sensor and actuator work in automated system** (4-5 marks)
- Sensor detects change in environment
- Converts to digital signal
- Microprocessor compares to stored value
- If outside range, sends signal to actuator
- Actuator produces physical response

#### Inkjet Printer
**Complete paragraph about inkjet printer operation** (5 marks)
- Data held in buffer (temporary storage)
- Print head moves nozzles side to side
- Spray liquid ink droplets onto page
- Droplets created using piezoelectric or thermal bubble technology
- Paper jam triggers interrupt to computer

### 3.3 Data Storage

#### Solid-State Storage
**Identify example of solid-state storage** (1 mark)
- SSD, USB flash drive, SD card

**Give three reasons why SSD is suitable for mobile device** (3 marks)
- Small/thin size
- Lightweight
- No moving parts (durable)
- Fast read/write speeds
- Low power consumption
- Quiet operation

#### Optical Storage
**Explain how laser stores and reads data from optical disk** (3 marks)
- Laser burns pits into reflective surface
- Pits represent binary data (1)
- Lands represent binary data (0)
- Reading: laser reflects off surface, reflected light detected

#### Primary Storage
**State differences between RAM and ROM** (2 marks)
- RAM: volatile, read/write, temporary storage
- ROM: non-volatile, read-only, permanent storage

#### Cloud Storage
**State what cloud storage is** (2 marks)
- Data stored on remote servers
- Accessed via internet
- Third party manages hardware

**Evaluate benefits of cloud storage** (3 marks)
- Accessible from anywhere
- No maintenance required
- Scalable storage
- Automatic backups

**Evaluate drawbacks of cloud storage** (2 marks)
- Requires internet connection
- Security concerns
- Ongoing subscription costs
- Dependent on third party

### 3.4 Network Hardware

#### MAC Address
**Give three features of MAC address** (3 marks)
- Assigned by manufacturer
- Unique to each device
- 48-bit address (12 hex digits)
- Cannot be changed

---

## Topic 4: Software

### 4.1 Types of Software

#### System vs Application
**Identify two examples of software for SSD** (2 marks)
- Operating system, application software

**Identify characteristics of system software** (3 marks)
- Manages hardware and software resources
- Provides platform for applications
- Examples: OS, utility software, firmware

**Identify two functions of operating system** (2 marks)
- File management, memory management, process management, device management, user interface

**Describe two operating system functions** (2 marks)
- File management: creates, deletes, organizes files
- Memory management: allocates RAM to programs
- Process management: handles multitasking
- Device management: communicates with peripherals

**Explain difference between system and application software** (3 marks)
- System software manages computer resources
- Application software allows user to perform tasks
- System software runs in background
- Application software is user-facing

#### Utility Software
**Identify two functions of utility software** (3 marks)
- Disk defragmentation
- Antivirus scanning
- File compression
- Backup software

### 4.2 Translators and IDEs

#### High-Level Language
**Describe what is meant by high-level language** (3 marks)
- English-like statements
- Portable across different hardware
- Requires translator to execute
- Examples: Python, Java, C++

**Identify characteristics of assembly language** (3 marks)
- Low-level language
- Uses mnemonics
- One-to-one with machine code
- Example: ADD, MOV

#### Compiler vs Interpreter
**Give one other similarity between compiler and interpreter** (1 mark)
- Both translate high-level to machine code

**Explain two differences between compiler and interpreter** (4 marks)
- Compiler: translates entire program, creates executable, errors shown after
- Interpreter: translates line by line, executes immediately, errors shown as found
- Compiler: faster execution after translation
- Interpreter: easier debugging during development

#### Translators
**Explain purpose of assembler** (3 marks)
- Translates assembly language to machine code
- One-to-one translation
- Produces object code

**Compare interpreter and compiler** (4 marks)
- Interpreter: translates and executes line by line
- Compiler: translates entire program before execution
- Interpreter: slower but easier debugging
- Compiler: faster execution, all errors shown at end

#### Freeware vs Free Software
**Explain one drawback of freeware distribution** (2 marks)
- Source code not available
- Cannot modify or distribute modified versions
- May include advertising

**Explain one benefit of free software distribution** (2 marks)
- Source code available
- Can modify and redistribute
- Freedom to use, study, modify, distribute

#### IDE Functions
**Identify three IDE features** (2 marks)
- Code editor with syntax highlighting
- Debugger with breakpoints
- Compiler/interpreter
- Auto-completion
- Error diagnostics

---

## Topic 5: The Internet and its Uses

### 5.1 The Internet and the World Wide Web

#### Internet Terms
**Complete table with browser, ISP, HTTP, URL, cookie definitions** (5 marks)
- Browser: software to display web pages
- ISP: company providing internet connection
- HTTP: protocol for sending web pages
- URL: text address of web page
- Cookie: text file stored by website

**Identify three parts of URL** (3 marks)
- Protocol (http://, https://)
- Domain name
- File/page path

**Complete table showing which terms match Browser, IP address, URL** (5 marks)
- Browser: software, displays HTML, stores cookies
- IP address: type of address, contains domain name
- URL: contains domain name, type of address, stores cookies

#### HTML
**State what is meant by HTML structure and presentation** (4 marks)
- Structure: content organization, headings, paragraphs
- Presentation: colours, fonts, layout (CSS)

**Explain why presentation is separated from structure** (2 marks)
- Easier to maintain
- Allows different styles for same content
- Better accessibility

#### Web Browser
**Describe how web browser retrieves web page** (3-4 marks)
- User enters URL or clicks link
- Browser sends request to DNS for IP address
- DNS returns IP address
- Browser sends request to web server
- Server sends HTML, browser renders page

#### Browser Functions
**Identify three browser functions** (2-3 marks)
- Display web pages
- Store bookmarks/favourites
- Record browsing history
- Manage cookies
- Handle multiple tabs

#### HTTP/HTTPS
**Describe SSL/TLS secure transmission** (4 marks)
- Browser requests secure connection
- Server sends digital certificate
- Browser verifies certificate
- Encrypted data transmission begins
- Uses public/private key encryption

**Explain difference between HTTP and HTTPS** (3 marks)
- HTTPS uses encryption (SSL/TLS)
- HTTPS authenticates website identity
- HTTPS protects data in transit

#### Cookies
**State what a cookie is** (1 mark)
- Small text file stored by website
- Contains user data/preferences

**Explain purpose of cookies** (2 marks)
- Remember user preferences
- Track browsing habits
- Store login information
- Enable targeted advertising

**Explain difference between session and persistent cookies** (3 marks)
- Session: stored in RAM, deleted when browser closes
- Persistent: stored on hard disk, remains until deleted/expiry

### 5.2 Digital Currency

#### Bitcoin
**Identify characteristics of Bitcoin** (2 marks)
- Digital cryptocurrency
- Decentralized
- Uses blockchain technology
- Encrypted transactions

#### Blockchain
**Describe how blockchain records transactions** (2-4 marks)
- Transaction added to block
- Block contains hash of previous block
- Distributed across network
- Verified by multiple computers
- Immutable once added

### 5.3 Cyber Security

#### Biometric Passwords
**State what is meant by biometric password** (1 mark)
- Uses physical characteristics for authentication
- Examples: fingerprint, iris, face recognition

**Give two reasons why biometric is more secure than PIN** (2 marks)
- Unique to individual
- Cannot be guessed or stolen
- Difficult to replicate

#### Firewalls
**Identify correct statement about firewalls** (1 mark)
- Can be hardware-based or software-based

**Explain how firewall keeps mobile device secure** (3 marks)
- Monitors incoming/outgoing traffic
- Sets criteria for acceptable traffic
- Blocks traffic not meeting criteria
- Prevents unauthorized access

**Explain how firewall limits websites user can access** (4 marks)
- Can create whitelist/blacklist
- Checks website addresses against list
- Blocks access to inappropriate sites
- Logs attempted access

#### Email Attacks
**Identify two email security attacks and describe them** (6 marks)
- Phishing: fake emails to steal information
- Malware: malicious attachments
- Spam: unsolicited bulk emails

#### Security Solutions
**Identify two security methods against online attacks** (2 marks)
- Firewall, encryption, antivirus, authentication

**Describe two security measures** (2-3 marks)
- Encryption: scrambles data
- Two-factor authentication: requires extra verification
- Antivirus: detects/removes malware

**Identify two methods to prevent phishing** (2 marks)
- User education
- Check sender's email address
- Don't click suspicious links

#### Malware
**Identify three types of malware** (3 marks)
- Virus, worm, trojan horse, spyware, ransomware, adware

**Describe how three methods prevent malware** (3 marks)
- Antivirus: scans for known patterns
- Firewall: blocks suspicious connections
- User education: avoid suspicious downloads

#### Cyber Security Threats
**Identify three cyber security threats** (3 marks)
- Phishing, pharming, malware, DDoS, hacking, SQL injection

#### Computer Ethics
**Identify and describe three ethical issues when using Internet** (6 marks)
- Privacy: personal data collection
- Copyright: illegal downloading
- Cyberbullying: harassment online
- Identity theft: stealing personal information

### 5.4 Data Backup

**Complete table with accidental damage examples** (3 marks)
- Power surge: use UPS
- Human error: regular backups
- Hardware failure:RAID, backups
- Natural disaster: off-site backups

---

## Topic 6: Automated and Emerging Technologies

### 6.1 Automated Systems

#### Automated Systems
**Describe automated system components** (3 marks)
- Sensors: collect data from environment
- Microprocessor: processes data, makes decisions
- Actuators: produce physical output

**Identify two sensors for automated system** (2 marks)
- Temperature, light, motion, pressure, proximity, humidity

**Describe how sensors and microprocessor control system** (5-8 marks)
- Sensor detects physical condition
- Converts to electrical/digital signal
- Microprocessor receives and processes data
- Compares to stored threshold values
- If condition met, sends signal to actuator
- Actuator produces physical response
- Feedback loop maintains desired state

#### Evaluation
**Evaluate benefits of automated system** (3 marks)
- Increased efficiency
- Reduced labor costs
- 24/7 operation
- Consistent quality
- Works in dangerous environments

### 6.2 Robotics

#### Robot Characteristics
**Identify three characteristics of a robot** (3 marks)
- Mechanical structure
- Electrical components
- Programmable
- Can move/perform actions
- Sensors for input
- Actuators for output

### 6.3 Artificial Intelligence

#### Logic Circuits
**Draw logic circuit for given statement** (5-6 marks)
- Identify required gates (AND, OR, NOT, XOR, NAND, NOR)
- Connect inputs through gates as per statement
- Maximum 2 inputs per gate

**Complete truth table for logic statement** (4 marks)
- Calculate output for all 8 input combinations
- Apply logic gates in correct order
- Verify each row

#### Expert Systems
**Describe expert system components and operation** (4 marks)
- Knowledge base: stores facts
- Rule base: stores rules for reasoning
- Inference engine: applies rules to facts
- Interface: allows user input/output

**Explain difference between AI and expert systems** (2 marks)
- AI: simulates human intelligence, learns
- Expert system: applies predefined rules

#### AI vs Expert Systems
**Describe expert system components** (4 marks)
- Knowledge base: facts from experts
- Rule base: IF-THEN rules
- Inference engine: reasoning mechanism
- Interface: user interaction

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
- Confusing similar concepts (e.g., RAM vs ROM)
- Giving vague descriptions instead of specific details

### Answer Presentation
- Use bullet points for multiple points
- Numbered steps for processes
- Diagrams where appropriate
- Clear, concise language
