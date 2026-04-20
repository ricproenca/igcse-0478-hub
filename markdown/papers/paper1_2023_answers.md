# Paper 1 Marking Scheme (2023)

This document contains the expected answers and key points from the 2023 Paper 1 marking schemes, organized by syllabus topics.

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
**Convert denary numbers to 8-bit binary** (3 marks)
- Divide by 2, record remainders
- Example: 50 → 00110010, 102 → 01100110, 221 → 11011101

**Convert binary to denary** (1 mark)
- Multiply each bit by its place value and sum
- Example: 10101110 = 174

**Calculate parking cost from binary registers** (2 marks)
- Convert each register's binary to denary
- Combine values for total cost

**Convert denary to binary for registers** (2 marks)
- Divide by 2, record remainders for each register value

#### Hexadecimal Conversions
**Convert binary numbers to hexadecimal** (4 marks)
- Group into nibbles (4 bits)
- Convert each nibble to hexadecimal digit
- Example: 10010011 → 93, 00001101 → 0D

**Convert hexadecimal to binary** (3 marks)
- Each hex digit = 4 binary digits
- Example: A → 1010, 2 → 0010, F → 1111

**Convert denary to hexadecimal** (2-3 marks)
- Divide by 16, record remainders
- Example: 301 → 12D

**Convert binary ticket number to hexadecimal** (4 marks)
- Group into nibbles
- Example: 1010000000111101 → A03D

**Identify correct hexadecimal conversions** (2 marks)
- A and E are correct hex digits

#### Logical Shifts
**Complete register after logical right shift** (1 mark)
- Each bit shifts right one position
- Rightmost bit lost, 0 added on left
- Example: 01110101 → 00001110 (÷8)

**Complete register after logical left shift** (1 mark)
- Each bit shifts left one position
- Leftmost bit lost, 0 added on right
- Example: 01110000 → 11000000 (×2)

**State one effect of logical right shift** (1 mark)
- Value becomes incorrect/inaccurate as rightmost bits lost
- Value is divided by 2 (for each shift)

**Identify effect of logical left shift** (1 mark)
- Value is multiplied by 2 (for each shift)

#### Two's Complement
**Complete binary register for negative denary using two's complement** (2 marks)
- Convert positive number to binary
- Flip all bits (0→1, 1→0)
- Add 1
- Example: -78 → 10110010

**Calculate negative denary from two's complement** (2 marks)
- Check MSB: if 0, convert normally
- If 1, flip bits, add 1, then negate
- Example: 10011101 → flip → 01100010 → +98 → -98

#### Binary Addition
**Add two 8-bit binary numbers using binary addition** (3-4 marks)
- Add bits from right to left
- Carry values when sum exceeds 1
- Show all carries
- Example: 00110011 + 01100001 = 10010100

**Add two binary numbers showing overflow** (4 marks)
- Perform binary addition
- Overflow occurs when result requires more than 8 bits
- Example: 10000011 + 01100001 = 11100100

**Add two binary numbers with carries shown** (3 marks)
- Show carries in working
- Example: 00011111 + 10000101 = 10100100

#### Binary Number System
**Identify which statement about binary is correct** (1 mark)
- Binary is a base 2 system (correct answer)

**Give characteristics of binary number system** (2 marks)
- Base 2, only uses values 0 and 1
- Contains logic gates/switches with two states

**Explain why data is converted to binary** (2 marks)
- Computers use logic gates/switches
- Only process values 0 and 1

**Explain why overflow error occurred in binary addition** (2 marks)
- Result is greater than 255
- Value generated is larger than can be stored in register
- Register has predetermined number of bits

#### Hexadecimal Uses
**Give reasons for using hexadecimal** (2 marks)
- Easier/quicker to understand/read/write
- Easier/quicker to debug
- Less likely to make mistakes
- Shorter representation, takes less screen space

### 1.2 Text, Sound and Images

#### Sound Representation
**State what is meant by sample rate and sample resolution** (2 marks)
- Sample rate: number of samples taken per second
- Sample resolution: number of bits per sample

**Explain how analogue sound is recorded and converted to digital** (5 marks)
- Recorded using a microphone
- Sound wave is sampled
- Measuring amplitude at each sample
- Each amplitude assigned unique binary value
- Sample rate set (samples per second)
- Sample resolution set (bits per sample)
- Each sample converted to binary

**State ways to increase recording accuracy** (2 marks)
- Increase sample rate
- Increase sample resolution

**Give benefit of higher sample rate** (1 mark)
- Recording more accurate/closer to original

**Give drawback of higher sample rate** (1 mark)
- File size increases
- Requires more storage space

**Describe what is meant by sample resolution** (2 marks)
- Number of bits used per sample
- Determines variation in amplitude that can be stored
- Defines how quiet/loud sounds can be recorded

#### Text Representation
**Describe how text is converted to binary** (3 marks)
- Character set used (e.g., ASCII/Unicode)
- Each character has unique binary value
- Text converted using character set

#### ASCII vs Unicode
**Explain differences between ASCII and Unicode** (4 marks)
- ASCII: limited characters (128/256), fewer languages
- Unicode: more characters (65,536+), covers many languages/emojis
- ASCII: 7-8 bits per character
- Unicode: up to 16-32 bits per character
- Unicode can represent more symbols and international characters

#### Image Representation
**State what resolution means** (1 mark)
- Number of pixels wide × number of pixels high

**State what colour depth means** (1 mark)
- Number of bits used to represent each colour

**Give reason for higher colour depth** (1 mark)
- Greater range of colours
- Image closer to real life
- More detail in image

### 1.3 Data Storage and Compression

#### Lossy Compression
**Identify which type of compression was used** (1 mark)
- Lossy compression (reduces sample rate and resolution)

**Identify compression method that removes data** (1 mark)
- Lossy compression

#### Lossless Compression
**State the effect of lossless compression on file size** (1 mark)
- File size is reduced

**Describe how lossless compression works** (4 marks)
- Compression algorithm used (e.g., RLE/run length encoding)
- Repeating characters/patterns identified
- Indexed with number of occurrences
- Position recorded
- Original data can be fully reconstructed

**Give reasons for compressing text files** (2 marks)
- Save storage space
- Quicker to transmit
- Small enough to attach to email
- Reduce bandwidth needed

**Explain why musician would choose lossless compression** (3 marks)
- Want to edit original sound file
- Want highest sound quality
- Lossy would reduce quality
- Lossless doesn't permanently remove data

**Calculate maximum possible compression ratio** (1 mark)
- Divide original by compressed size

**Identify effect of halving bit depth on file size** (1 mark)
- File size is halved

#### Data Storage Measurement
**State number of bits in a byte** (1 mark)
- 8 bits

**State number of bytes in a kibibyte** (1 mark)
- 1024 bytes

---

## Topic 2: Data Transmission

### 2.1 Types and Methods of Data Transmission

#### Serial Transmission
**Describe serial transmission** (2 marks)
- Data sent one bit at a time
- Single wire used

**Give benefits of serial transmission** (2 marks)
- Data won't be skewed
- Less chance of interference/crosstalk/error
- Transmission speed adequate

**State one benefit of parallel transmission** (1 mark)
- Data may be transmitted quicker

#### Data Transmission Methods
**Circle data transmission methods** (2 marks)
- Serial half-duplex and serial full-duplex (for bidirectional single wire)

**Complete table identifying transmission methods** (4 marks)
- Serial simplex: single wire, one bit at a time, one direction
- Parallel half-duplex: multiple wires, both directions, one at a time
- Serial full-duplex: single wire, one bit at a time, both directions simultaneously
- Parallel simplex: multiple wires, multiple bits, one direction

#### Packet Switching
**Identify pieces of data in packet header** (2 marks)
- Destination/receiver IP address
- Packet number
- Originator's/sender's IP address

**Explain packet switching** (5 marks)
- Data is split into packets
- Each packet can take different route
- Router controls path/route
- Selecting shortest/fastest available route
- Packets may arrive out of order
- Reordered when last packet arrives
- Missing/corrupted packets are requested again

**Complete statements about packet switching** (4 marks)
- Packet has header (contains packet number, destination address)
- Main data section called payload
- Routers control different paths
- Last packet received before reordering

**Draw and annotate packet switching diagram** (4 marks)
- Packets sent through several routers
- Taking different routes from A to B
- Packets arrive out of order
- Reordered when all arrive

#### Transmission Issues
**State issue with parallel transmission over long distances** (1 mark)
- Interference/crosstalk

**Identify transmission method for LAN** (1 mark)
- Parallel transmission

### 2.2 Methods of Error Detection

#### Parity Check
**Explain how odd parity check detects errors** (4 marks)
- Number of 1s/0s counted in each byte
- Parity bit added to make sum odd
- After transmission, if number is odd, no error detected
- If number is even, error is detected

#### Echo Check
**State name of error detection method** (1 mark)
- Echo check

#### ARQ
**Describe how ARQ handles errors** (5 marks)
- Timer started when sending device transmits packet
- Receiving device checks for errors
- Sends acknowledgement when packet is error-free
- If acknowledgement not received before timeout, packet resent
- Process continues until acknowledgement received

### 2.3 Encryption

#### Encryption
**Explain how encryption prevents data being understood** (2 marks)
- Data is encrypted
- If intercepted, it will be meaningless without decryption key

---

## Topic 3: Hardware

### 3.1 Computer Architecture

#### CPU Components
**State purpose of the CPU** (1 mark)
- To perform fetch-decode-execute cycle
- To process/execute instructions

**Name three components of the CPU** (3 marks)
- Accumulator (ACC)
- Control unit (CU)
- Program counter (PC)

**State what controls timing of operations** (1 mark)
- Clock

**State component that performs calculations** (1 mark)
- Arithmetic logic unit (ALU)

#### Control Unit
**State name of component that sends signals for FDE cycle** (1 mark)
- Control unit

#### Clock Speed
**Describe what is meant by 2.4 GHz clock speed** (2 marks)
- 2.4 billion cycles/clock pulses per second
- Maximum number of FDE cycles CPU can perform per second

**State what is meant by clock speed** (1 mark)
- Maximum number of FDE cycles/instructions CPU can perform per second

**Explain effect of changing CPU from 2GHz to 3GHz** (2 marks)
- Increases/improves performance
- More FDE cycles/instructions processed per second
- Tasks performed quicker/faster

#### CPU Performance Factors
**Explain why multiple cores increase performance** (2 marks)
- More instructions processed simultaneously
- More FDE cycles can happen at same time

#### Registers
**Describe purpose of registers** (2 marks)
- Store/hold data/address/instruction temporarily
- Allow immediate access during FDE cycle

**Describe role of MDR in FDE cycle** (2 marks)
- Stores data that has been fetched
- Stores data to be written to memory

**Describe role of MAR in FDE cycle** (2 marks)
- Stores addresses of next instruction/data to be fetched
- Stores where data is to be written

**Identify three other registers in CPU** (3 marks)
- Memory address register (MAR)
- Program counter (PC)
- Current instruction register (CIR)
- Accumulator (ACC)

#### Buses
**Describe three types of buses in CPU** (3 marks)
- Address bus: transmits/carries addresses between CPU components
- Data bus: transmits/carries data between CPU components
- Control bus: transmits control signals from CU to other components

#### Instruction Set
**State name of list of machine code commands** (1 mark)
- Instruction set

### 3.2 Input and Output Devices

#### Input/Output Devices
**Circle three output devices** (3 marks)
- Actuator, printer, speaker

**Give two input devices for automated system** (2 marks)
- Touchscreen, microphone, keyboard, keypad, digital camera, sensor, biometric device, button

**Give one output device for automated system** (1 mark)
- Screen, speaker, LED, actuator, motor

**Give three examples of input devices** (2 marks)
- Keyboard, mouse, touchscreen, digital camera, QR code scanner, barcode scanner, 2D scanner, microphone

**Give one example of output device** (1 mark)
- Speakers, headphones

#### Sensors
**Explain how microprocessor processes barcode scanner data** (3 marks)
- Receives data from barcode scanner
- Compares book data to stored database of stock
- If found, decrements stock by 1
- If not found, displays error message

### 3.3 Data Storage

#### Secondary Storage
**Circle three secondary storage devices** (3 marks)
- Compact disk (CD), solid-state drive (SSD), hard disk drive (HDD)

**Identify which statement about secondary storage is correct** (1 mark)
- It is used to permanently store software and data files

**Give two features of magnetic storage** (2 marks)
- Data stored on platters divided into tracks/sectors
- Components spun, read/write arm used
- Electromagnets read/write data
- Magnetic field determines binary value
- Non-volatile

**Give three features of solid-state storage** (3 marks)
- Flashes data onto chips
- Uses NAND/NOR transistors
- Uses control gates and floating gates
- Controls electron flow
- Can be volatile or non-volatile

**Give example of each storage type** (3 marks)
- Magnetic: HDD, magnetic tape, floppy disk
- Solid-state: SSD, USB drive, SD card
- Optical: CD, DVD, Blu-ray

#### Primary Storage
**Identify RAM and ROM** (2 marks)
- RAM: random access memory
- ROM: read only memory

**Identify which is type of primary storage** (1 mark)
- RAM

**Give characteristic of primary storage** (1 mark)
- Directly accessed by CPU
- Has both volatile and non-volatile storage

#### Cloud Storage
**Describe what is meant by cloud storage** (2 marks)
- Collection of servers
- Stores data in remote location
- Accessed using internet connection
- Third party manages hardware

**Give one disadvantage of cloud storage** (1 mark)
- Less secure
- Access lost if internet connection lost
- Third party maintains hardware (ongoing fees)
- Reliant on third party for maintenance

**Identify correct statement about cloud storage** (1 mark)
- (C) More than one user can access the same data simultaneously

#### Virtual Memory
**Complete paragraph about virtual memory** (5 marks)
- RAM used when program running
- If RAM full, pages moved to hard disk drive
- Pages swapped between RAM and HDD
- Virtual memory is HDD space used as additional RAM
- Allows larger programs to run

### 3.4 Network Hardware

#### Network Components
**Identify component needed to access network** (1 mark)
- Network interface card/controller (NIC)

**Identify type of address allocated by manufacturer** (1 mark)
- MAC (media access control) address

#### DHCP/Router
**Identify device that assigns IP addresses** (1 mark)
- Router

#### IP Address
**Describe what is meant by dynamic IP address** (3 marks)
- Can be used to uniquely identify device on network
- Changes each time device connects to network

**Explain characteristics of IPv4 address format** (4 marks)
- Denary based, numbers 0-255
- 32 bits, 4 sets separated by dots
- Unique address, can be static or dynamic
- Contains network prefix and host number

**Describe differences between IPv4 and IPv6** (3 marks)
- IPv4: 32-bit, decimal, dots
- IPv6: 128-bit, hexadecimal, colons
- IPv6 has larger address space

**Identify similarity between MAC and IP address** (1 mark)
- Both can identify a device on a network

#### Network Devices
**Complete table about network devices and addresses** (5 marks)
- Router: forwards packets to correct destinations
- IP address: assigned by network, identifies device on network
- NIC: enables device to connect to network
- MAC address: assigned by manufacturer, uniquely identifies device
- Firewall/proxy-server: filters incoming/outgoing traffic

---

## Topic 4: Software

### 4.1 Types of Software

#### Software Definitions
**Complete statements about software types** (4 marks)
- System software provides services computer requires (e.g., utility software)
- Application software runs on operating system
- Operating system runs on firmware
- Firmware runs on hardware

**Complete table with software terms and descriptions** (4 marks)
- Hardware: collective term for physical components
- Application software: provides services user requires, allows tasks
- Operating system: manages main functions, files, memory
- Firmware: stored in ROM, includes BIOS and bootloader

**Identify correct statement about high-level language** (1 mark)
- (C) The computer program is machine independent

**Describe three functions of operating system** (3 marks)
- Performs basic functions of computer
- Manages hardware
- Provides platform to run software
- Provides user interface
- Manages tasks (multitasking, memory, files)

#### System vs Application Software
**Explain differences between system and application software** (4 marks)
- System software provides services computer requires
- Application software provides services user requires
- System software: utility software, operating system
- Application software: word processor, web browser, video-editing software

**Give example of secondary storage** (1 mark)
- Hard disk drive (HDD), SSD

#### Interrupts
**State name of software that manages interrupts** (1 mark)
- Operating system, interrupt handler

**Describe how interrupts are used when key is pressed** (5 marks)
- Key press generates interrupt
- Interrupt given priority
- Interrupt sent to CPU
- Placed in queue
- CPU stops current task to check queue
- Uses interrupt service routine (ISR)
- If key press is highest priority, processed

**Give examples of hardware interrupts** (2 marks)
- Moving/clicking mouse
- Plugging in device
- Paper jam in printer
- Printer out of paper

**Give examples of software interrupts** (2 marks)
- Division by zero
- Two processes accessing same memory location
- Null value

### 4.2 Translators and IDEs

#### Low-Level Language
**Describe what is meant by low-level language** (2 marks)
- Close to language processed by computers
- May use mnemonics
- Example: assembly language, machine code

**Give reasons for choosing low-level language** (2 marks)
- Can directly manipulate hardware
- No requirement for portability
- More memory efficient
- No compiler/interpreter needed
- Quicker to execute
- Can use specialised hardware

#### Compiler
**Describe how compiler translates program** (3 marks)
- Translates high-level language to low-level/machine code
- Translates all code before execution
- Creates executable file

**Describe how compiler reports errors** (2 marks)
- Creates error report after compilation
- Displays all errors in code
- Requires correction before execution

**Identify what compiler does** (1 mark)
- Translates entire program before execution

#### Interpreter
**Identify what interpreter does** (1 mark)
- Translates line by line during execution

**Identify when interpreter translates code** (1 mark)
- During execution, line by line

**Identify what machine code is** (1 mark)
- Low-level language, object code

#### IDE Functions
**Give three other common functions of IDE** (3 marks)
- Code editors
- Run-time environment
- Built-in interpreter
- Error diagnostics
- Auto-completion
- Auto-correction
- Prettyprint

---

## Topic 5: The Internet and its Uses

### 5.1 The Internet and the World Wide Web

#### Web Browser
**Explain purpose of web browser** (2 marks)
- Displays web pages
- Renders HTML

**Give two functions of web browser** (2 marks)
- Display/render web pages
- Store cookies
- Store bookmarks/favourites

**State purpose of storing cookies** (1 mark)
- Store user's personal data

**Give one reason for storing bookmarks** (1 mark)
- Save/find websites quickly
- Quick access to favourite sites

**Explain why HTTPS connection is secure** (1 mark)
- Data is encrypted
- Uses digital certificates

### 5.2 Digital Currency

#### Digital Currency
**Give characteristics of digital currency** (2 marks)
- Only exists electronically
- Can be decentralised or centralised
- Usually encrypted

#### Blockchain
**Give name of technology behind cryptocurrency** (1 mark)
- Blockchain

### 5.3 Cyber Security

#### Brute-Force Attack
**Describe how brute-force attack works** (3 marks)
- Trial and error to guess password
- Combinations repeatedly entered
- Until correct password found
- Can be carried out manually or automatically

**Give other aims of brute-force attack** (2 marks)
- Steal/view/access data
- Delete data
- Change data
- Lock account, encrypt data
- Damage business reputation

#### Malware
**Identify three types of malware** (3 marks)
- Virus, worm, trojan horse, spyware, ransomware, keylogger, adware

**Identify which is not a type of malware** (1 mark)
- Phishing

**Identify one other example of malware** (1 mark)
- Spyware, keylogger, ransomware, trojan horse

**Identify type of software that removes malware** (1 mark)
- Anti-malware

#### DDoS Attack
**Draw and annotate DDoS attack diagram** (6 marks)
- Malware downloaded to computers
- Turns them into bots/zombies
- Creates botnet
- Third party initiates attack
- Bots send requests to web server simultaneously
- Web server fails from overload
- Legitimate requests cannot reach server

**Give aims for carrying out DDoS attack** (2 marks)
- Revenge
- Affect company reputation
- Entertainment
- Demand ransom to stop
- Test system resilience

#### Pharming
**State aim of pharming** (1 mark)
- Obtain personal data/details

**Draw and annotate pharming diagram** (4 marks)
- User clicks attachment/link, downloads malware
- User enters website address
- Redirected to fake website
- Data stolen from fake site

#### Security Solutions
**Give security solutions to prevent brute-force attacks** (2 marks)
- Two-step verification, two-factor authentication
- Biometrics
- Firewall, proxy server
- Strong/complex password
- Limit login attempts
- Drop-down boxes
- Request partial password entry

**Give ways to prevent DDoS attack** (2 marks)
- Proxy server
- Firewall
- Users scanning computers with anti-malware

**Draw and annotate firewall diagram** (4 marks)
- Traffic passing through firewall
- Criteria set for firewall
- Traffic compared to criteria
- Rejected if doesn't meet criteria
- Accepted if meets criteria

#### Phishing
**Give ways to check if website is genuine** (3 marks)
- Check spelling and tone of email/website
- Check URL attached to link
- Scan download with anti-malware
- Download from trusted sources only
- Never provide personal details online
- Install firewall to validate website

#### Social Engineering
**Define social engineering** (3 marks)
- Manipulating/deceiving/tricking people
- To obtain data or force them to make an error
- Example: phishing, vishing, tailgating

#### Access Levels
**Describe access levels and permissions** (3 marks)
- Users given different permissions for data
- Limiting access to reading data
- Limiting access to editing/deleting data
- Normally linked to username

#### Packet Sniffing
**Draw and annotate packet sniffing diagram** (4 marks)
- Data sent between devices
- Examined during transmission
- Packet sniffer used
- Intercepted data reported to third party
- Analysed for useful information
- Connection hacked to spoof destination

#### Cyber Security Terms
**Complete paragraph about malware and botnets** (5 marks)
- Malware downloaded to computers
- Turns computers into bots
- Creates botnet
- Bots send requests to web server
- Website crashes

---

## Topic 6: Automated and Emerging Technologies

### 6.1 Automated Systems

#### Sensors
**Identify most appropriate sensor for automated water bowl** (1 mark)
- Level/pressure/moisture sensor

**Describe how sensor and microprocessor automatically refill water bowl** (6 marks)
- Sensor continually sends digitised data to microprocessor
- Microprocessor compares data to stored values
- If value outside range, signal sent to release water
- Bowl filled by set amount/time
- Actuator used to release water
- Process repeats until stopped

**Explain how sensor and microprocessor check if door can close** (6 marks)
- Proximity/infrared/pressure sensor used
- Sensor sends digitised data to microprocessor
- When button pushed, microprocessor compares data to stored values
- If in range/matches, signal sent to close door
- Actuator closes door
- If not in range, door won't close
- Process repeats until door can close

**State what flow rate sensor measures** (1 mark)
- Amount of liquid/gas/steam flowing through environment

#### Automated Systems
**State two benefits of automated monitoring** (2 marks)
- Increases safety (workers don't enter dangerous areas)
- Can increase jobs/skills (maintain equipment)
- No need for repetitive tasks

**State two drawbacks of automated monitoring** (2 marks)
- High set-up/installation costs
- Utility/maintenance/repair costs
- Deskilling of workforce

### 6.2 Robotics

#### Robot Characteristics
**State other characteristics of robot** (2 marks)
- Mechanical structure/framework
- Electrical components

#### Robot Advantages
**Give advantages to employees of using robots** (2 marks)
- Don't need to lift heavy furniture
- Protected from dangerous tasks
- Can use skills in other tasks
- Don't need to perform repetitive/mundane tasks

**Explain advantages of robots in manufacturing** (3 marks)
- Work 24/7, no breaks needed
- More accurate/precise
- Don't get bored with repetitive tasks
- No health and safety concerns
- Consistent quality

#### Robot Disadvantages
**Give disadvantage to company owners of using robots** (1 mark)
- Expensive to install/purchase
- High ongoing costs/maintenance
- May deskill workforce
- If malfunction, production may stop

### 6.3 Artificial Intelligence

#### AI Definition
**Give characteristic of AI** (1 mark)
- Ability to learn/adapt
- Collection of data and rules
- Ability to reason
- Simulates intelligent behaviour
- Analyses patterns

#### Expert Systems
**Give three components of expert system** (3 marks)
- Rule base
- Knowledge base
- Interface

**Identify interface and knowledge base** (2 marks)
- Interface: allows input/output
- Knowledge base: stores facts

**Describe role of rule base** (2 marks)
- Stores rules for the system
- Used by inference engine
- Links facts in knowledge base

**Explain how expert system makes decisions** (2 marks)
- Makes decisions by applying rules/logic to facts
- Provides result/diagnosis

**Describe how expert system works** (6 marks)
- Interface allows input/output
- Knowledge base stores facts
- Rule base stores rules
- Inference engine applies rules to knowledge base
- Outputs diagnosis/result/solution/decision
- Decides what to ask next based on input

**Explain how expert systems are developed and used** (3 marks)
- Knowledge base built from expert knowledge
- Rules created by experts
- Used to diagnose problems/make decisions
- Interface allows users to input symptoms
- Inference engine provides solutions

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
