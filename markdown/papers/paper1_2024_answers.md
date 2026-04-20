# Paper 1 Marking Scheme (2024)

This document contains the expected answers and key points from the 2024 Paper 1 marking schemes, organized by syllabus topics.

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

#### Data Storage Measurement
**State how many bits there are in a byte** (1 mark)
- 8 bits = 1 byte

**State how many bits there are in a kibibyte** (1 mark)
- 8192 bits (1024 × 8)

**State how many kibibytes there are in 2 mebibytes** (1 mark)
- 2048 KiB (2 × 1024)

**Identify the unit of data that is equal to 4 bits** (1 mark)
- Nibble

**Give the name of the data storage measurement equal to 1024 gibibytes** (1 mark)
- Tebibyte (TiB)

#### Conversions
**Convert denary numbers to hexadecimal** (3 marks)
- Divide by 16, record remainders
- Example: 20 → 14, 32 → 20, 165 → A5

**Convert three denary numbers to binary** (3 marks)
- Divide by 2, record remainders
- Example: 10 → 1010, 50 → 110010, 201 → 11001001

**Convert denary number to binary** (2 marks)
- 128 + 32 + 8 + 4 + 2 + 1 = 175 → 10101111

**Convert hexadecimal address to binary** (3 marks)
- Each hexadecimal digit = 4 binary digits
- A2F → 1010 0010 1111

**Convert hexadecimal address to denary** (1 mark)
- A2F = (10 × 256) + (2 × 16) + 15 = 2607

**Convert binary number to hexadecimal** (3 marks)
- Group into nibbles (4 bits)
- 000110011011 → 19B

**Convert binary number to denary** (1 mark)
- 000110011011 = 411

**Convert denary to hexadecimal** (3 marks)
- Divide by 16, record remainders
- 14 → E, 100 → 64, 250 → FA

**Convert denary ASCII numbers to binary** (2 marks)
- 65 → 01000001, 109 → 01101101

**Convert denary ASCII numbers to hexadecimal** (2 marks)
- 65 → 41, 109 → 6D

**Convert binary ASCII number to denary** (1 mark)
- 01111001 = 121

**Convert binary ASCII number to hexadecimal** (1 mark)
- 01111001 = 79

**Convert binary to hexadecimal for given numbers** (3 marks)
- 15 → 0001, 2D → 0010 1101, 091 → 0000 1001 0001

#### Binary Addition
**Add two binary integers using binary addition** (3 marks)
- Add bits from right to left
- Carry values when sum exceeds 1
- Example: 00110000 + 01100110 = 10010110

**Add two binary ASCII numbers** (3 marks)
- 01010100 + 01110100 = 11001000
- Show all carries

**Add two binary integers and show overflow** (4 marks)
- 11100011 + 11001100 = 11001111
- Overflow occurs (carry out of MSB)

#### Logical Shifts
**Perform a logical left shift of three places** (1 mark)
- 10100011 → 00011000 (multiply by 2³ = 8)

**Identify which statement about logical left shift of two places is correct** (1 mark)
- Multiplies the binary number by 4

**Describe the process of a logical left shift** (2 marks)
- Each digit shifted left one place
- Leftmost bit lost
- 0 added as rightmost bit

**State the effect of a logical left shift** (1 mark)
- Multiplies the binary number by 2

**Perform a logical right shift of two places** (1 mark)
- 01111001 → 00011110

#### Two's Complement
**Convert two's complement integer to denary** (2 marks)
- 10100011 = -93 (flip bits, add 1)

**Calculate the two's complement integer for a negative number** (2 marks)
- 00100000 → flip → 11011111 → add 1 → 11100000 = -32

**Calculate the two's complement 8-bit integer for -25** (2 marks)
- 25 = 00011001, flip → 11100110, add 1 → 11100111

**Calculate the denary number for two's complement 10001110** (2 marks)
- Flip → 01110001, add 1 → 01110010 = 114, so original = -114

#### Number Systems
**Identify which statement about hexadecimal is incorrect** (1 mark)
- "It is a base 10 system" is incorrect

**Give the name of the number system that is base 16** (1 mark)
- Hexadecimal

**Give one similarity between hexadecimal and binary** (1 mark)
- Both are positional number systems
- Both can represent the same values

**Give two differences between hexadecimal and binary** (2 marks)
- Hexadecimal is base 16, binary is base 2
- Hexadecimal uses letters A-F, binary uses only 0 and 1

**Explain why data is converted to binary** (2 marks)
- Computers use logic gates/switches
- Only process values 0 and 1

#### Hexadecimal Uses
**Give one reason why addresses are displayed in hexadecimal** (1 mark)
- Easier to read/understand/debug
- Shorter representation of binary
- Takes up less screen space

**Identify two other ways hexadecimal is used** (2 marks)
- HTML colour codes
- URL addresses
- Memory dump
- IP addresses
- MAC addresses
- Assembly language
- Error codes/messages
- ASCII/Unicode representation

### 1.2 Text, Sound and Images

#### Image Representation
**State what is meant by a 16-bit colour depth** (1 mark)
- 16 bits used to represent each colour in the image

**Give the effect of changing image resolution on file size** (1 mark)
- File size will decrease (fewer pixels)

**Calculate the file size of a 16-bit colour image** (3 marks)
- 512 × 512 × 16 = 4,194,304 bits
- ÷ 8 = 524,288 bytes
- ÷ 1024 = 512 KiB

#### Text Representation
**Identify one other character set** (1 mark)
- Unicode

**State what Unicode is an example of** (1 mark)
- Character set

**Give two advantages of Unicode over ASCII** (2 marks)
- Can represent more characters
- Can represent emojis/symbols
- Can represent more languages

**Give one disadvantage of Unicode over ASCII** (1 mark)
- Each character requires more storage space

#### Sound Representation
**Calculate the file size of a sound effect** (3 marks)
- Sample rate × duration × sample resolution
- 22,016 × 10 × 8 = 1,761,280 bits
- ÷ 8 = 220,160 bytes
- ÷ 1024 = 215 KiB

### 1.3 Data Storage and Compression

#### Data Compression
**Identify which is not a unit of measurement for a file** (1 mark)
- Bot

**Give two types of compression** (2 marks)
- Lossy and Lossless

**Give three benefits of reducing file size** (3 marks)
- File requires less storage space
- Takes less time to transmit
- Lower bandwidth required
- Less data usage
- Meets file size limits

**State the effect of compression on the report file** (1 mark)
- File size will be reduced

**Give two benefits of compressing the report file** (2 marks)
- Faster upload/download/transmission
- Takes less storage space
- Requires less bandwidth
- Less data allowance used

**State what is meant by file compression** (1 mark)
- Reducing the size of a file

**Give one benefit of compressing the file** (1 mark)
- Takes up less storage space

**Explain why lossy compression is not suitable** (3 marks)
- Data will be permanently removed
- Could be important data
- Not suitable for text files (damages/corrupts)
- Quality of images will be reduced

---

## Topic 2: Data Transmission

### 2.1 Types and Methods of Data Transmission

#### Data Transmission Methods
**Identify which is not a method for transmitting data** (1 mark)
- Parity

**Give one other method of data transmission** (1 mark)
- Serial simplex/half-duplex/full-duplex
- Parallel simplex/half-duplex

#### Packet Switching
**Describe the structure of a data packet** (4 marks)
- Header: destination address, source address, packet number
- Payload: main data
- Trailer: error detection system used

**Give the name of the unit data is broken down into** (1 mark)
- Packet

**Identify the device that controls packet paths** (1 mark)
- Router

**Identify the method of sending packets along different paths** (1 mark)
- Packet switching

**Circle three items in packet header** (3 marks)
- Originator's address, destination address, packet number

#### Serial Transmission
**Explain why serial data transmission is used** (3 marks)
- Network may be spread over long distance
- More reliable, bits arrive in sequence
- Less crosstalk/interference
- Less likely to have errors
- Serial cables only needed

#### Serial Half-Duplex
**Draw and annotate serial half-duplex diagram** (4 marks)
- Bits sent one at a time over single wire
- Data sent to and from, but not simultaneously

**Give two benefits of serial half-duplex** (2 marks)
- Bits will not be skewed, sent in order
- Less chance of error/crosstalk
- Can send over long distances
- Higher bandwidth than full duplex

**Give one drawback of serial half-duplex** (1 mark)
- Relatively slow transmission
- Cannot send and receive at same time
- May be more data collisions

#### Parallel Full-Duplex
**Explain reasons for choosing parallel full-duplex** (4 marks)
- Sends multiple bits at same time, fast transmission
- Devices in single room, no long distance
- Sends data in both directions simultaneously, no delay

**Give two drawbacks of parallel full-duplex** (2 marks)
- More interference/crosstalk
- Data may be skewed, arrive out of order
- More data collisions
- More chance of error

### 2.2 Methods of Error Detection

#### Error Detection Methods
**Complete table with error detection methods** (5 marks)
- Parity check: odd or even process
- Checksum: value calculated before/after transmission
- Echo check: copy sent back by receiver
- ARQ: acknowledgement and timeout
- Check digit: value appended and checked on entry

**Give two other error detection methods** (2 marks)
- Echo check
- Checksum
- Even parity check
- Negative ARQ

**Give two error detection methods** (2 marks)
- Parity check, checksum, echo check, ARQ

#### Parity Check
**Describe odd parity check and ARQ operation** (8 marks)
- Count 1s in each byte, parity bit added
- Data sent with timer started
- Receiver counts 1s, sends acknowledgement
- If odd parity and 1s are odd, data is error-free
- If no acknowledgement before timeout, data resent
- Process continues until acknowledgement received

#### Check Digit
**Explain how barcode check digit operates** (4 marks)
- Check digit calculated using barcode data
- Algorithm (e.g., Modulo 11) applied
- Check digit added to barcode
- After scan, check digit recalculated
- If values don't match, error detected

#### Echo Check
**Explain how echo check detects errors** (3 marks)
- Copy of data sent back to sender
- Sender compares original to received copy
- If values don't match, error detected

**Explain why non-matching checksum indicates error** (2 marks)
- Checksum calculated from data using same algorithm
- Different values mean data has changed

### 2.3 Encryption

#### Symmetric Encryption
**Explain how symmetric encryption works** (4 marks)
- Same key used to encrypt and decrypt
- Plain text encrypted into cipher text
- Algorithm uses a key to encrypt
- Key transmitted to receiver

**Give the purpose of encryption** (1 mark)
- Keep data secure
- Make data meaningless

#### Asymmetric Encryption
**Complete asymmetric encryption paragraph** (4 marks)
- Plain text encrypted into cipher text using public key
- Encrypted data transmitted
- Decrypted using private key

#### Symmetric vs Asymmetric
**Give one similarity between symmetric and asymmetric encryption** (1 mark)
- Both use a key
- Both scramble data
- Both turn plain text into cipher text

**Give two differences between symmetric and asymmetric** (2 marks)
- Symmetric uses one key, asymmetric uses two (public and private)
- Symmetric can send key with data, asymmetric does not
- Symmetric decrypts with same key, asymmetric with different key
- Symmetric is less secure than asymmetric

---

## Topic 3: Hardware

### 3.1 Computer Architecture

#### CPU Role
**Describe the role of the CPU** (2 marks)
- To process instructions/data
- To run the fetch-decode-execute cycle

#### Registers
**State the purpose of a register** (1 mark)
- Temporarily store data/instruction/address
- Allow immediate access during FDE cycle

**Give three registers in the CPU** (3 marks)
- MAR (Memory Address Register)
- MDR (Memory Data Register)
- ACC (Accumulator)
- PC (Program Counter)
- CIR (Current Instruction Register)

**Give name of two registers used in fetch stage** (2 marks)
- PC and MAR (also MDR, CIR)

**Give one register used in execute stage** (1 mark)
- Accumulator, MAR, or MDR

**Complete table with CPU component names and descriptions** (6 marks)
- Control unit/CU: sends signals to manage data flow
- Program counter: stores address of next instruction
- MAR: stores address of data to be fetched
- Data bus: transmits data between RAM and CPU
- Accumulator: stores interim calculation results
- CIR: stores instruction when being decoded

**Identify two other registers used in fetch stage** (2 marks)
- PC and MAR (or CIR)

#### Buses
**Circle three buses used in CPU** (3 marks)
- Address, data, control

#### Fetch-Decode-Execute Cycle
**Complete paragraph about fetching instruction** (7 marks)
- PC contains address of next instruction
- Sent to MAR using address bus
- Address sent to RAM
- Instruction sent to MDR using data bus
- MDR sends to CIR using data bus
- CIR sends to control unit (CU)

**Describe what happens at decode stage** (3 marks)
- Instruction sent from MDR to CIR/CU using data bus
- Instruction separated into opcode and operand
- CU decodes using instruction set

**Draw and annotate fetch stage diagram** (4 marks)
- PC sends address to MAR, increments
- Address sent via address bus to RAM
- Data/instruction sent to MDR via data bus
- MDR sends to CIR to be decoded
- Control unit sends signals via control bus

**Complete and annotate decode stage diagram** (4 marks)
- MDR sends to CIR/CU via data bus
- CIR built into CU
- Instruction separated into operand and opcode
- CU decodes using instruction set

#### Instruction Sets
**State what is meant by an instruction set** (1 mark)
- List of machine code commands processed by CPU

#### ALU
**Describe the purpose of the ALU** (3 marks)
- Execute instructions
- Perform calculations (e.g., add, subtract)
- Perform logical operations (e.g., AND, OR)
- Store interim results
- Read/write to accumulator

#### CPU Performance Factors
**Explain why a different CPU increases performance** (4 marks)
- More cores: more FDE cycles simultaneously
- Higher clock speed: more FDE cycles per second
- Greater cache: frequently used data accessed faster

**Explain effect of changing clock speed on CPU performance** (2 marks)
- More instructions/FDE per second
- Increases CPU performance

### 3.2 Input and Output Devices

#### Input Devices
**Identify two input devices built into tablet/smartphone/smartwatch** (2 marks)
- Touch screen, microphone, button, camera, accelerometer, biometric device, sensor

**Circle three other input devices** (3 marks)
- Touch screen, microphone, keyboard

**Identify two input devices built into smartwatch** (2 marks)
- Touch screen, microphone, button, camera, sensor, biometric device

#### Output Devices
**Identify one output device built into tablet** (1 mark)
- Screen, speaker, LED

**Identify two output devices built into smartphone** (2 marks)
- Screen, speaker, LED, actuator

**Identify one output device built into smartwatch** (1 mark)
- Screen, speaker, LED, actuator

#### Sensors
**Give two benefits of using sensors in automated systems** (2 marks)
- Data collected without human intervention
- Gathers data faster
- Accurate readings
- Continuous monitoring (24/7)
- Works in dangerous environments

**Complete table with sensor uses** (4 marks)
- Acoustic: detecting water pipe leaks
- Temperature: kettle boiling, climate control
- Humidity: spray-painting garage, greenhouse
- Infra-red: security motion, automatic doors
- Magnetic field: counting vehicles, monitoring parking

**Identify most suitable sensor for robot vacuum navigation** (1 mark)
- Proximity sensor

### 3.3 Data Storage

#### Primary Storage
**State the purpose of secondary storage** (1 mark)
- Store data/files/software permanently

**Explain why computer needs RAM** (3 marks)
- Store data temporarily
- Store data currently in use
- Store software currently in use
- Faster access than secondary storage
- Speeds up fetch stage

**Identify which statement about RAM is correct** (1 mark)
- RAM stores data currently in use

**State characteristic of ROM that makes it primary storage** (1 mark)
- Directly accessible by CPU

**Give example of primary storage and explain its purpose** (3 marks)
- RAM: stores data/instructions in use, volatile
- ROM: stores BIOS/bootstrap, non-volatile
- Cache: stores frequently used data, fast access

**Explain why smartwatch needs ROM** (2 marks)
- Store BIOS/bootstrap/bootloader/start-up instructions
- Store firmware
- Non-volatile storage
- Stores instructions that shouldn't change

#### Secondary Storage
**Identify three examples of optical storage** (3 marks)
- CD, DVD, Blu-ray disk

**Complete table with types of secondary storage** (6 marks)
- Optical: pits and lands on reflective surface, laser read/write
- Solid-state: NAND/NOR technology, transistors as gates
- Magnetic: spinning platters with tracks/sectors, electromagnets

**Describe three differences between solid-state and optical** (6 marks)
- Solid-state: no moving parts; optical: has moving parts
- Solid-state: faster access; optical: slower
- Solid-state: uses less power; optical: uses more
- Solid-state: quieter; optical: noisier
- Solid-state: more durable; optical: less durable
- Solid-state: larger capacity; optical: smaller capacity
- Solid-state: more expensive per GB; optical: cheaper per GB
- Solid-state: stores on silicon chips; optical: burns pits/lands

**Explain why computer needs secondary storage** (2 marks)
- Store data/files permanently
- Otherwise data would need re-downloading each time
- Allows software installation
- For creating virtual memory

**Identify most suitable secondary storage for smartphone (SSD)** (4 marks)
- Small/thin for device, lightweight, durable (no moving parts)
- Fast read/write, cool operation, quiet
- Low power consumption, large capacity possible

#### Cloud Storage
**Describe what is meant by cloud storage** (2 marks)
- Collection of servers
- Access data remotely
- Third party manages hardware
- Data stored/accessed using internet

**Explain two benefits of cloud storage** (4 marks)
- No hardware maintenance needed
- Resources can be increased/decreased on demand
- No need to worry about running out of storage
- Less storage space needed on device
- Can access from any device
- Data available if device breaks/is lost

### 3.4 Network Hardware

#### MAC Address
**Identify which statement about MAC address is correct** (1 mark)
- Assigned by manufacturer

#### IP Address
**Give example of IPv4 address** (1 mark)
- 10.245.3.99 or similar format

**Give two characteristics of IPv6 format** (2 marks)
- 128-bit, 16 bytes
- Hexadecimal characters
- Separated by colons
- 8 groups of 4 characters
- Double colons for consecutive zeros

---

## Topic 4: Software

### 4.1 Types of Software and Interrupts

#### System vs Application Software
**Give one example of system software** (1 mark)
- Operating system, utility software

**Give two examples of application software** (2 marks)
- Word processor, spreadsheet, database, web browser, email client, game

**Describe difference between system and application software** (2 marks)
- System software manages/maintains hardware/software
- Application software allows user to perform tasks

#### Operating System Functions
**Identify which is not a function of operating system** (1 mark)
- Loading the bootstrap (it's a purpose, not a function)

**Identify one function of operating system and describe it** (2 marks)
- Memory management: managing what gets allocated where
- Managing peripherals and drivers
- Multitasking: switching between tasks
- Platform for running applications
- System security: username and password
- User accounts: multiple accounts

**Give two functions of operating system relating to memory** (2 marks)
- Memory management
- Virtual memory creation

#### Interrupts
**Complete paragraph about interrupts** (7 marks)
- Printer sends interrupt to computer
- Interrupt given priority level
- Processor completes current fetch-decode-execute cycle
- Checks interrupt queue
- If higher priority than current task, stores current task
- Calls interrupt service routine (ISR)
- ISR handles interrupt, generates message

### 4.2 Types of Programming Language, Translators and IDEs

#### Assembly Language
**Give name of translator for assembly language** (1 mark)
- Assembler

**Give one benefit of using assembly language** (1 mark)
- More control over manipulating hardware
- Faster execution than high-level for testing
- Can use machine-specific instructions

#### IDE Functions
**Describe three ways IDE helps programmer** (6 marks)
- Code editor: enter and amend code
- Run-time environment: run program and see outputs
- Error-diagnostic: show where errors are
- Auto-completion: suggest commands
- Auto-correction: correct minor misspellings
- Prettyprint: colour key commands

**Explain purpose of IDE** (4 marks)
- Software to write/develop/edit code
- Test and debug code
- Features like auto-completion
- Translate code to machine code

#### Software Definition
**State what is meant by software** (1 mark)
- Instructions/programs used to operate computer/hardware

#### Utility Software
**Identify which is utility software** (1 mark)
- Anti-virus

#### System Software
**Identify type of software that manages inputs and outputs** (1 mark)
- Operating system/system software

---

## Topic 5: The Internet and its Uses

### 5.1 The Internet and the World Wide Web

#### Internet vs WWW
**Describe difference between internet and WWW** (2 marks)
- Internet is the infrastructure
- WWW is a collection of web pages

#### URL
**Identify three parts of URL** (3 marks)
- Protocol, domain name, file name/path

**Identify two different parts of a URL** (2 marks)
- Protocol, domain name, file name

**State what is meant by a URL** (1 mark)
- Text-based address for website/web page

#### Web Browser Functions
**Give three other functions of web browser** (3 marks)
- Display web pages
- Store bookmarks/favourites
- Record user history
- Allow multiple tabs
- Store cookies
- Provide navigation tools
- Set home page

**Describe how web pages are located, retrieved and displayed** (6 marks)
1. User types URL into address bar
2. Browser sends URL to DNS
3. DNS searches for matching IP address
4. DNS returns IP address to browser
5. If not found, URL sent to next DNS
6. Browser sends request to IP address/web server
7. Server sends HTML data to browser
8. Browser renders HTML to display page

**Draw and annotate diagram of web page retrieval** (5 marks)
- URL sent from browser to DNS
- DNS finds matching IP address
- If not found, sent to next DNS
- IP address returned to browser
- Request sent to web server
- Web page/HTML sent back
- Browser renders HTML

#### Cookies
**Complete statements about cookies** (7 marks)
- Cookies stored by web browser
- Session cookies are temporary text files deleted when browser closed
- Persistent cookies are permanent text files stored until manually deleted or expire

**Give three examples of cookie uses** (3 marks)
- User preferences
- Login details
- Payment details
- Personal details
- Shopping cart contents
- Targeted advertising

### 5.2 Digital Currency

#### Blockchain
**Draw and annotate blockchain payment diagram** (4 marks)
- Digital ledger used
- Device encrypts payment data
- Payment data sent to digital ledger
- Transaction recorded including digital signature/time/date
- Stored in block in multiples
- Each block has hash/unique identifier
- When block executed or full, added to blockchain on all devices

### 5.3 Cyber Security

#### DDoS Attack
**Draw and annotate DDoS attack diagram** (5 marks)
- Perpetrator sends malware to computers
- Malware turns computers into bots
- Bots form botnet
- Third party initiates attack
- All bots send requests to web server simultaneously
- Web server crashes from overload

**Identify solution to prevent DDoS attack** (1 mark)
- Proxy server

#### Firewalls
**Explain how firewall operates to protect network** (5 marks)
- Criteria can be set (blacklist/whitelist of IP addresses)
- Examines incoming traffic
- Checks traffic meets criteria
- Rejects traffic that doesn't meet criteria
- Certain ports used by hackers can be blocked/closed

#### Proxy Server
**Give three cyber security threats proxy server protects against** (3 marks)
- DDoS/DoS
- Hacking
- Malware
- Brute-force attack

**Identify two functions of proxy server** (2 marks)
- Limit requests to web server
- Process common requests without entering network
- Act as firewall
- Examine incoming data
- Have rules/criteria for data
- Block traffic that doesn't meet criteria
- Close certain ports

#### Malware
**Give two examples of malware firewall protects against** (2 marks)
- Virus, worm, trojan horse, spyware, adware, ransomware

#### SSL Protocol
**Complete SSL paragraph** (5 marks)
- Web browser asks web server to identify itself
- Web server sends back digital certificate
- Web browser authenticates the certificate
- If authentic, encrypted data transmission begins

---

## Topic 6: Automated and Emerging Technologies

### 6.1 Automated Systems

#### Automated Systems
**State what is meant by automated system** (1 mark)
- System that performs actions without human intervention

**Describe role of microprocessor in automated plough** (3 marks)
- Receives data from sensor
- Analyses data
- Checks if data within/out of range
- Sends signals to trigger actions

**Give two benefits of using automated system** (2 marks)
- Farmer free to do other jobs
- Doesn't need to take breaks, works 24/7
- Performs boring repetitive tasks
- Saves labour costs
- More accurate/efficient
- Safer in dangerous environments

### 6.2 Robotics

#### Robot Characteristics
**State what is meant by robot being automated** (1 mark)
- Performs actions without human intervention

**Give three characteristics of a robot** (3 marks)
- Mechanical structure/framework
- Electrical components
- Programmable
- Can move

**Give two advantages of automated robot** (2 marks)
- More accurate when planting
- Doesn't need breaks, works 24/7
- Won't get bored of repetitive tasks
- Farmer can do other tasks
- Faster/more efficient
- Works in dangerous environments
- No labour costs

**Give two disadvantages of automated robot** (2 marks)
- Expensive to purchase
- Maintenance costs
- Takes away jobs
- Workers may be deskilled
- Training needed
- If breaks, must manually plant
- If faulty, may cause damage
- Cannot adapt to unexpected events

#### Sensors and Actuators
**Explain how robot uses sensors and microprocessor to detect fence** (6 marks)
- Proximity sensor continuously sends data to microprocessor
- Microprocessor compares data to stored value/range
- If value within range/matches, robot continues
- If value above/below/outside range, signal sent to turn/stop
- Actuator turns/stops robot
- Process repeats until turned off

### 6.3 Artificial Intelligence

#### AI Definition
**Describe what is meant by AI** (2 marks)
- Simulation of intelligent behaviours by computers
- Collection of data and rules for using data
- Ability to reason
- Ability to learn/adapt

#### Expert Systems
**Complete expert system paragraph** (7 marks)
- Expert system is type of artificial intelligence
- Doctor types symptoms into interface
- Inference engine decides which questions to ask
- Using facts in knowledge base
- Linked to rule base
- Inference engine decides diagnosis
- Output on interface

**Explain how expert system diagnoses car problems** (5 marks)
- User enters data via interface/plugs car in
- Inference engine decides questions to ask based on previous answers
- Compares data/answers to knowledge base and rule base
- Calculates most likely option if multiple
- Outputs diagnosis
- Explanation system shows how diagnosis reached

**Circle three components of expert system** (3 marks)
- Knowledge base, rule base, inference engine

#### Machine Learning
**Give name of ability to automatically adapt processes and data** (1 mark)
- Machine learning

**Explain how machine learning improves robot** (2 marks)
- Robot adapts by changing own rules/data/processes
- Becomes more efficient with greater knowledge of surroundings
- Remembers fences, routes, obstacles
- Makes fewer errors

**Explain how robot vacuum uses machine learning** (3 marks)
- Gathers data during vacuuming
- Adapts own processes based on data
- Learns obstacle locations, dirtier areas, room shape
- Develops efficient cleaning routes
- Knows areas to avoid/concentrate on

**Explain how plough uses AI** (4 marks)
- Makes use of machine learning
- Gathers ploughing data and adapts processes
- Makes fewer mistakes
- Learns field dimensions, landscape, obstacle locations
- Creates map of field
- Develops most efficient route

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
