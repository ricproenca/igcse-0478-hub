# IGCSE Computer Science Paper 1 - Master Consolidated Answers

This document consolidates all question types and answers from 2021-2025 papers, organized by syllabus topics 1.1 through 6.3.

---

## Topic 1: Data Representation

### 1.1 Number Systems

#### Binary Conversions
**Convert denary to binary** (X marks)
- Divide by 2, record remainders
- Example: 175 → 10101111

**Convert binary to denary** (X marks)
- Multiply each bit by place value and sum
- Example: 10110011 = 179

**Convert hexadecimal to binary** (X marks)
- Each hex digit = 4 binary digits
- Example: A2F → 10100010 1111

**Convert binary to hexadecimal** (X marks)
- Group into nibbles (4 bits), convert each to hex
- Example: 000110011011 → 19B

**Convert hexadecimal to denary** (X marks)
- Multiply each digit by place value (16^n)
- Example: A2F = (10×256) + (2×16) + 15 = 2607

**Convert denary to hexadecimal** (X marks)
- Divide by 16, record remainders
- Example: 175 → AF

**Convert binary to denary with multiple bytes** (X marks)
- Example: 00000000 01000111 → 71
- Example: 00000001 00000001 → 257

#### Binary Representation
**Explain why computer can only process binary data** (X marks)
- Computers use logic gates/switches
- Logic gates have two states (on/off)
- Binary represents these two states (0/1)

**Give characteristics of binary number system** (X marks)
- Base 2, only uses values 0 and 1
- Contains logic gates/switches with two states

**Explain why data is converted to binary** (X marks)
- Computers use logic gates/switches
- Only process values 0 and 1

#### Hexadecimal Uses
**Give two benefits of converting binary to hexadecimal** (X marks)
- Easier/quicker to read/write/understand
- Easier/quicker to identify errors/debug
- Takes up less screen/display space
- Less chance of making an error

**Identify three other uses of hexadecimal** (X marks)
- MAC address
- URL addresses
- Assembly language
- Error codes/messages
- IP addresses
- Memory dumps
- HTML colour codes
- ASCII/Unicode representation

**Give one reason why addresses are displayed in hexadecimal** (X marks)
- Easier to read/understand/debug
- Shorter representation of binary
- Takes up less screen space

#### Number Systems
**Identify base of binary number system** (X marks)
- Base-2

**Identify base of denary number system** (X marks)
- Base-10

**Give the name of the number system that is base 16** (X marks)
- Hexadecimal

**Give one similarity between hexadecimal and binary** (X marks)
- Both are positional number systems
- Both can represent the same values

**Give two differences between hexadecimal and binary** (X marks)
- Hexadecimal is base 16, binary is base 2
- Hexadecimal uses letters A-F, binary uses only 0 and 1

#### Logical Shifts
**Perform a logical left shift on a binary number** (X marks)
- Each digit shifted left one place
- Leftmost bit lost, 0 added as rightmost bit
- Multiplies the binary number by 2

**Perform a logical right shift on a binary number** (X marks)
- Each digit shifted right one place
- Rightmost bit lost, 0 added as leftmost bit
- Divides the binary number by 2

**State the effect of logical left shift** (X marks)
- Multiplies the binary number by 2 (for each shift)

**State the effect of logical right shift** (X marks)
- Value becomes incorrect/inaccurate as rightmost bits lost
- Value is divided by 2 (for each shift)

#### Two's Complement
**Calculate two's complement integer for a negative number** (X marks)
- Convert positive number to binary
- Flip all bits (0→1, 1→0)
- Add 1
- Example: -25 → 11100111

**Convert two's complement integer to denary** (X marks)
- Check MSB: if 0, convert normally
- If 1, flip bits, add 1, then negate
- Example: 10100011 = -93

**Calculate negative denary from two's complement** (X marks)
- Check MSB: if 0, convert normally
- If 1, flip bits, add 1, then negate
- Example: 10011101 → -98

#### Binary Addition
**Add two binary integers** (X marks)
- Add bits from right to left
- Carry values when sum exceeds 1
- Show all carries in working
- Example: 00110000 + 01100110 = 10010110

**Add two binary numbers showing overflow** (X marks)
- Perform binary addition
- Overflow occurs when result requires more than 8 bits
- Example: 11100011 + 11001100 = overflow

#### Parity Check
**Identify whether odd or even parity for each binary value** (X marks)
- Count the 1s in each byte
- If count is odd (odd parity), if count is even (even parity)

**Identify why parity check may not detect error** (X marks)
- There is a transposition of bits
- It does not check the order of the bits (just the sum of 1s/0s)
- Even number of bits change
- Incorrect bits still add up to correct parity

**State why parity check does not identify error** (X marks)
- There is a transposition of bits
- Bits still add up to correct parity

---

### 1.2 Text, Sound and Images

#### Sound Representation
**Calculate the file size of a sound recording** (X marks)
- File size = sample rate × duration × sample resolution × number of channels
- Sample rate: number of samples per second
- Sample resolution: number of bits per sample

**State what is meant by sample rate and sample resolution** (X marks)
- Sample rate: number of samples taken per second
- Sample resolution: number of bits per sample

**Describe how sound files are compressed using lossless compression** (X marks)
- (Compression) algorithm is used
- No data will be removed // original file can be restored
- Example of type of algorithm that would be used e.g. RLE
- Repeated patterns in the music are identified and indexed

**Give reason for using lossless compression** (X marks)
- Maintains quality // quality better than lossy
- Original file is retained // Data is not permanently lost
- A significant reduction in file size is not required
- To provide highest quality of music file

**Give two reasons for using lossy compression** (X marks)
- Lossy decreases the file size more
- Takes up less storage space on webserver/users' computer
- Quicker to upload/download
- May not need to be high quality
- Website will load faster for users
- Less lag/buffering when watching
- Takes up less bandwidth to download/upload

#### Image Representation
**Calculate the file size of an image** (X marks)
- File size = resolution × colour depth
- Resolution = width × height in pixels
- Colour depth = bits per pixel

**State what is meant by colour depth** (X marks)
- Number of bits used to represent each colour in the image

**State what is meant by resolution** (X marks)
- Number of pixels wide × number of pixels high

**Give reason for higher colour depth** (X marks)
- Greater range of colours
- Image closer to real life
- More detail in image

**Give effect of changing image resolution on file size** (X marks)
- File size will decrease (fewer pixels)

#### Text Representation
**Describe how text is converted to binary** (X marks)
- Character set used (e.g., ASCII/Unicode)
- Each character has unique binary value
- Text converted using character set

**Explain differences between ASCII and Unicode** (X marks)
- ASCII: limited characters (128/256), fewer languages
- Unicode: more characters (65,536+), covers many languages/emojis
- ASCII: 7-8 bits per character
- Unicode: up to 16-32 bits per character
- Unicode can represent more symbols and international characters

**Give two advantages of Unicode over ASCII** (X marks)
- Can represent more characters
- Can represent emojis/symbols
- Can represent more languages

**Give one disadvantage of Unicode over ASCII** (X marks)
- Each character requires more storage space

---

### 1.3 Data Storage and Compression

#### Compression Types
**Explain the difference between lossy and lossless compression** (X marks)
- Lossless compression: original data can be fully reconstructed (e.g., ZIP, PNG)
- Lossy compression: some data is discarded, original cannot be fully reconstructed (e.g., JPEG, MP3)
- Lossy achieves greater compression but loses quality

**Describe how lossy compression reduces video file size** (X marks)
- A compression algorithm is used
- Redundant data is removed
- Reduce colour depth
- Reduce image resolution
- Reduce sample rate
- Reduce sample resolution
- Reduce frame rate
- Use perceptual music shaping
- Data is permanently removed

**Describe how lossless compression reduces file size** (X marks)
- Compression algorithm used
- Repeating frames/pixels are identified and collated/indexed
- No data is permanently removed
- It just records the changes between frames/pixels

**State reason for using lossless compression** (X marks)
- Maintains quality // quality better than lossy
- Original file is retained // Data is not permanently lost

**Explain why lossy compression is not suitable** (X marks)
- Data will be permanently removed
- Could be important data
- Not suitable for text files (damages/corrupts)

#### File Size
**Give three benefits of reducing file size** (X marks)
- File requires less storage space
- Takes less time to transmit
- Lower bandwidth required
- Less data usage
- Meets file size limits

**State the effect of compression on the report file** (X marks)
- File size will be reduced

#### Data Storage Measurement
**State number of bits in a byte** (X marks)
- 8 bits

**State number of bytes in a kibibyte** (X marks)
- 1024 bytes

**Identify the unit of data that is equal to 4 bits** (X marks)
- Nibble

**Give the name of the data storage measurement equal to 1024 gibibytes** (X marks)
- Tebibyte (TiB)

---

## Topic 2: Data Transmission

### 2.1 Types and Methods of Data Transmission

#### Serial vs Parallel Transmission
**Describe how data is sent using serial transmission** (X marks)
- Data is sent one bit at a time
- Data is sent using a single wire

**Describe how data is sent using serial half-duplex** (X marks)
- Bits sent one at a time down a single wire
- Data sent in both directions but only one direction at a time

**Describe how data is sent using serial duplex** (X marks)
- Data is sent one bit at a time
- Data is sent using a single wire
- Data is sent in both directions at the same time

**Describe how data is sent using parallel half-duplex** (X marks)
- Multiple bits are sent at the same time
- Uses multiple wires
- Data is sent in both directions but only one direction at a time

**State drawback of serial transmission** (X marks)
- Data transmission can be slower (than parallel)
- Additional data may need to be sent

**State two drawbacks of parallel transmission** (X marks)
- Bits may arrive skewed
- More expensive to setup/manufacture/purchase cable
- Limited distance
- More prone to interference/error

**Give benefits of serial transmission** (X marks)
- Data won't be skewed
- Less chance of interference/crosstalk/error
- Transmission speed adequate
- Suitable for long distances
- Less crosstalk

**Give one benefit of parallel transmission** (X marks)
- Data may be transmitted quicker

#### USB
**State two benefits of USB connection** (X marks)
- It cannot be inserted incorrectly
- Supports different transmission speeds
- High speed transmission
- Automatically detected (not connected)
- Powers the device (for data transfer)
- Backward compatible

**Identify type of data transmission in USB** (X marks)
- Serial

**Describe the features of USB that make it suitable for connecting devices** (X marks)
- Hot-swappable: devices can be connected/disconnected without restarting computer
- Plug and play: operating system automatically detects and configures devices
- Multiple device types supported: keyboards, mice, storage, printers
- Power delivery: can charge devices without external power supply

#### Packet Switching
**State two features of packet switching** (X marks)
- Data split into packets
- Each packet has header with address
- Packets can take different routes
- Reassembled at destination

**Identify pieces of data in packet header** (X marks)
- Destination/receiver IP address
- Packet number
- Originator/sender's IP address

**Describe the structure of a data packet** (X marks)
- Header: destination address, source address, packet number
- Payload: main data
- Trailer: error detection system used

**Explain packet switching** (X marks)
- Data is split into packets
- Each packet can take different route
- Router controls path/route
- Selecting shortest/fastest available route
- Packets may arrive out of order
- Reordered when last packet arrives
- Missing/corrupted packets are requested again

---

### 2.2 Methods of Error Detection

#### Parity Check
**Describe how odd parity check detects errors** (X marks)
- Number of 1s/0s counted in each byte
- Parity bit added to make sum odd
- After transmission, if number is odd, no error detected
- If number is even, error is detected

**Explain how parity check detects errors** (X marks)
- Count 1s in received byte
- Compare with parity bit
- If mismatch, error detected
- Cannot detect multiple bit errors

#### Checksum
**State what checksum is used for** (X marks)
- Detect errors after data transmission
- Sum of data values compared before/after

**Explain how checksum detects errors** (X marks)
- Sum of all data values is calculated and sent with data
- Receiver recalculates sum and compares
- If sums don't match, error detected

#### ARQ
**Describe how ARQ handles errors** (X marks)
- Sender transmits data, starts timer
- Receiver checks for errors, sends acknowledgement
- If no ACK before timeout, data resent
- Continues until successful transmission

**Describe how Automatic Repeat Query (ARQ) handles transmission errors** (X marks)
- Sender transmits data and waits for acknowledgement (ACK) or negative acknowledgement (NAK)
- If NAK received or timeout occurs, data is resent
- Process continues until ACK received
- Uses sequence numbers to identify missing packets

#### Check Digit
**State what check digit is used for** (X marks)
- Detect errors in data entry/transmission
- Calculated using algorithm (e.g., Modulo 11)

**Explain how barcode check digit operates** (X marks)
- Check digit calculated using barcode data
- Algorithm (e.g., Modulo 11) applied
- Check digit added to barcode
- After scan, check digit recalculated
- If values don't match, error detected

#### Echo Check
**State name of error detection method** (X marks)
- Echo check

**Explain how echo check detects errors** (X marks)
- Copy of data sent back by receiver
- Sender compares original to received copy
- If values don't match, error detected

---

### 2.3 Encryption

#### Symmetric Encryption
**Explain how symmetric encryption works** (X marks)
- Same key used to encrypt and decrypt
- Plain text encrypted into cipher text
- Algorithm uses a key to encrypt
- Key transmitted to receiver

**Explain how symmetric encryption works and give one advantage** (X marks)
- Same key used for encryption and decryption
- Advantage: faster than asymmetric encryption

#### Asymmetric Encryption
**Explain how asymmetric encryption uses public and private keys** (X marks)
- Public key: used to encrypt, freely available
- Private key: used to decrypt, kept secret
- Sender encrypts with recipient's public key
- Only recipient's private key can decrypt

**Explain how SSL protocol secures data transmission** (X marks)
- Enables an encrypted link (between the browser and the web server)
- Based on the authentication of an (SSL) certificate
- Will only send data if the certificate is authentic

**Identify alternative to SSL protocol** (X marks)
- Transport Layer Security // TLS

**Give two ways to identify if website uses secure transmission** (X marks)
- URL begins with HTTPS
- Padlock symbol is locked
- Check the certificate is valid

**Explain difference between HTTP and HTTPS** (X marks)
- HTTPS uses encryption (SSL/TLS)
- HTTPS authenticates website identity
- HTTPS protects data in transit

**Give one similarity between symmetric and asymmetric encryption** (X marks)
- Both use a key
- Both scramble data
- Both turn plain text into cipher text

**Give two differences between symmetric and asymmetric** (X marks)
- Symmetric uses one key, asymmetric uses two (public and private)
- Symmetric can send key with data, asymmetric does not
- Symmetric decrypts with same key, asymmetric with different key

---

## Topic 3: Hardware

### 3.1 Computer Architecture

#### Von Neumann Model
**Complete table about Von Neumann components** (X marks)
- Memory Address Register (MAR): holds address of data/instruction to be fetched
- Program Counter (PC): holds address of next instruction to be processed
- Accumulator: temporarily holds result of calculation
- Memory Data Register (MDR): holds data or instruction fetched from memory
- Control Unit (CU): sends signals to control flow of data
- Address bus: carries addresses around CPU

**State the purpose of the accumulator in the ALU** (X marks)
- Stores intermediate results of calculations performed by ALU

**Identify component that carries out calculations** (X marks)
- Arithmetic Logic Unit // ALU

**Describe three types of buses in CPU** (X marks)
- Address bus: carries memory addresses between CPU components
- Data bus: carries data between CPU components
- Control bus: carries control signals from CU to other components

**Identify two other registers in Von Neumann model** (X marks)
- MAR, MDR // MBR, PC, CIR // IR

#### Fetch-Decode-Execute Cycle
**Describe the three stages of FDE cycle** (X marks)
- Fetch: instruction copied from memory to MAR, then MDR, then CIR; PC incremented
- Decode: CU interprets instruction, determines operation
- Execute: ALU performs calculation OR data transferred

**Describe role of PC in FDE cycle** (X marks)
- Holds address of next instruction
- Incremented after each fetch

**Describe role of MAR in FDE cycle** (X marks)
- Stores addresses of next instruction/data to be fetched
- Stores where data is to be written

**Describe role of MDR in FDE cycle** (X marks)
- Stores data that has been fetched
- Stores data to be written to memory

#### CPU Performance Factors
**Explain effect of clock speed on CPU performance** (X marks)
- Higher clock speed = more cycles per second
- More instructions processed per second
- Faster execution

**Explain how cache memory improves CPU performance** (X marks)
- Fast memory close to CPU
- Stores frequently accessed data/instructions
- Reduces time to fetch from main memory

**Explain how cache memory improves performance** (X marks)
- Stores frequently accessed data/instructions
- Reduces time to fetch from main memory

**Explain why multiple cores increase performance** (X marks)
- More instructions processed simultaneously
- More FDE cycles can happen at same time

#### Interrupt
**Give name of signal that stops music for call** (X marks)
- interrupt

**State what happens without interrupt signals** (X marks)
- Computer would only start a new task when finished processing current task
- Computer will not be able to multitask
- Errors may not be dealt with
- Computer would become impossible to use

**Describe role of interrupt in generating paper jam message** (X marks)
- Printer generates interrupt
- Interrupt is given a priority
- Interrupt is queued
- Interrupt stops CPU from processing current task
- CPU will service interrupt
- Generating output message to state there is a paper jam

**Give three examples of when interrupt signal generated** (X marks)
- Error that might occur
- Peripheral is connected/disconnected
- A key on a keyboard is pressed
- A mouse button click
- A phone/video call is received
- Buffer requires more data
- Printer has paper jam
- Printer runs out of paper
- Printer runs out of ink
- When switching from one application to another

#### Embedded Systems
**State what is meant by embedded system** (X marks)
- Computer system designed for specific purpose
- Built into larger device
- Contains microprocessor/dedicated hardware

---

### 3.2 Input and Output Devices

#### Input Devices
**Identify three devices to input personal data** (X marks)
- Keyboard, Mouse, Microphone
- Keypad, Touchscreen, Touchpad

**Identify two input devices** (X marks)
- Keyboard, Mouse, Touchscreen, Microphone, Camera, Scanner, Sensor

**Identify input device for ticket machine** (X marks)
- Touchscreen, Trackpad/touchpad, Microphone, QR code reader, Barcode reader, Magnetic strip reader, RFID reader

**Identify input device for mobile phone** (X marks)
- Microphone

#### Output Devices
**Identify output device for ticket machine** (X marks)
- Printer, Speaker, Light/LED, Actuator

**Identify two output devices** (X marks)
- Screen, Speaker, Printer, Actuator, LED

#### Touchscreen
**State touchscreen technology type** (X marks)
- capacitive

**Complete paragraph about capacitive and resistive touchscreens** (X marks)
- Capacitive: uses conductive touch, detects change in capacitance
- Capacitive: uses conductive touch, detects coordinates
- Resistive: uses pressure, circuit completes when layers touch

#### Keyboard and Mouse
**Complete paragraph about keyboard operation** (X marks)
- Switch activated by key press
- Circuit completed, current flows
- Character code calculated
- Converted to binary
- Sent to computer

**Complete paragraph about optical mouse operation** (X marks)
- LED emits light
- Photoelectric sensor detects surface
- Lens magnifies light
- Microswitch detects movement
- Data sent via USB

#### Sensors
**Identify most appropriate sensor for automated system** (X marks)
- Temperature sensor, Light sensor, Proximity sensor, Pressure sensor

**Give two benefits of using sensors in automated systems** (X marks)
- Data collected without human intervention
- Gathers data faster
- Accurate readings
- Continuous monitoring (24/7)
- Works in dangerous environments

#### Actuators
**Explain how an actuator converts electrical signals into physical movement** (X marks)
- Converts electrical signals from computer into physical movement
- Types: motors (rotary), solenoids (linear), servos (controlled position)
- Examples: robot arm movement, motor driving wheels, valve control

---

### 3.3 Data Storage

#### Storage Types
**Complete table about HDD, SSD, USB characteristics** (X marks)
- HDD: uses magnetic properties, has moving parts, slower read/write
- SSD: uses NAND gates, no moving parts, faster, non-volatile
- USB flash memory: no moving parts, uses NAND technology, small physical size

**Complete table about magnetic, solid-state, optical storage** (X marks)
- Magnetic: data stored on platters, uses electromagnets, has moving parts
- Solid-state: uses flash memory, no moving parts
- Optical: pits and lands used, uses laser to read/write

**Describe two characteristics of magnetic secondary storage** (X marks)
- Uses magnetised platters, read/write heads, high capacity, relatively slow

**Describe three differences between solid-state and optical** (X marks)
- Solid-state: no moving parts; Optical: has moving parts
- Solid-state: faster access; Optical: slower
- Solid-state: uses less power; Optical: uses more

**Give three features of solid-state storage** (X marks)
- Flashes data onto chips
- Uses NAND/NOR transistors
- Uses control gates and floating gates
- Controls electron flow

**Give three features of magnetic storage** (X marks)
- Data stored on platters divided into tracks/sectors
- Components spun, read/write arm used
- Electromagnets read/write data, magnetic field determines binary value

#### Primary Storage
**State differences between RAM and ROM** (X marks)
- RAM: volatile, read/write, temporary storage
- ROM: non-volatile, read-only, permanent storage

**State what is meant by volatile memory** (X marks)
- Contents lost when power is removed

**Explain why computer needs RAM** (X marks)
- Store data temporarily
- Store data currently in use
- Store software currently in use
- Faster access than secondary storage
- Speeds up fetch stage

**Explain why smartwatch needs ROM** (X marks)
- Store BIOS/bootstrap/bootloader/start-up instructions
- Store firmware
- Non-volatile storage
- Stores instructions that shouldn't change

**Identify which is type of primary storage** (X marks)
- RAM: directly accessible by CPU

#### Secondary Storage
**Identify three examples of optical storage** (X marks)
- CD, DVD, Blu-ray disk

**Give example of magnetic storage** (X marks)
- Hard disk drive // HDD, Magnetic tape

**Give example of optical storage** (X marks)
- CD, DVD, Blu-ray disk

**Explain why computer needs secondary storage** (X marks)
- Store data/files permanently
- Otherwise data would need re-downloading each time
- Allows software installation
- For creating virtual memory

**Identify most suitable secondary storage for smartphone** (X marks)
- SSD: small/thin, lightweight, durable (no moving parts), fast read/write, cool operation, quiet, low power consumption, large capacity possible

#### Virtual Memory
**Explain how virtual memory allows a computer to run programs larger than RAM** (X marks)
- Portion of secondary storage used as additional RAM
- When RAM is full, inactive data moved to virtual memory (swap file/page file)
- Allows programs larger than physical RAM to run
- Slower than actual RAM due to secondary storage access time

**Complete paragraph about virtual memory** (X marks)
- RAM used when program running
- If RAM full, pages moved to hard disk drive
- Pages swapped between RAM and HDD
- Virtual memory is HDD space used as additional RAM
- Allows larger programs to run

#### Cloud Storage
**State what cloud storage is** (X marks)
- Data stored on remote servers
- Accessed via internet
- Third party manages hardware

**Describe what is meant by cloud storage** (X marks)
- Collection of servers, stores data in remote location
- Accessed using internet connection
- Third party manages hardware

**Explain two benefits of cloud storage** (X marks)
- No hardware maintenance needed
- Resources can be increased/decreased on demand
- No need to worry about running out of storage
- Less storage space needed on device
- Can access from any device
- Data available if device breaks/is lost

**Explain two drawbacks of cloud storage** (X marks)
- Requires internet connection
- Security concerns
- Ongoing subscription costs

---

### 3.4 Network Hardware

#### MAC Address
**Identify who assigns MAC address** (X marks)
- Manufacturer

**Give three features of MAC address** (X marks)
- Assigned by manufacturer
- Unique to each device
- 48-bit address (12 hex digits)
- Cannot be changed

#### IP Address
**Describe what is meant by dynamic IP address** (X marks)
- Can be used to uniquely identify device on network
- Changes each time device connects to network

**Explain characteristics of IPv4 address format** (X marks)
- Denary based, numbers 0-255
- 32 bits, 4 sets separated by dots
- Unique address, can be static or dynamic
- Contains network prefix and host number

**Explain the difference between IPv4 and IPv6 addresses** (X marks)
- IPv4: 32-bit address; four decimal numbers (0-255) separated by dots
- IPv6: 128-bit address; eight hexadecimal groups
- IPv6 provides larger address space, better security, auto-configuration

**Identify similarity between IP and MAC address** (X marks)
- Both addresses can be used to identify a computer/device

**Identify two differences between IP and MAC address** (X marks)
- IP address is assigned by network/router/ISP, MAC address is assigned by manufacturer
- IP address can be changed (if dynamic), MAC address cannot be changed
- IP address has 4 groups of values, MAC address has 6 groups of values
- IP address is 32-bit/128-bit, MAC address is 48-bit

**Give example of IPv4 address** (X marks)
- 10.245.3.99 or similar format

**Give two characteristics of IPv6 format** (X marks)
- 128-bit, hexadecimal characters
- Separated by colons, 8 groups of 4 characters

---

## Topic 4: Software

### 4.1 Types of Software

#### Operating System
**State two other functions of operating system** (X marks)
- Interrupt/error-handling
- Peripheral management
- Providing user interface
- Platform for running applications
- Managing security/access rights
- Managing time slicing/multitasking

**Identify one function of operating system and describe it** (X marks)
- Memory management: managing what gets allocated where
- Managing peripherals and drivers
- Multitasking: switching between tasks
- Platform for running applications
- System security: username and password
- User accounts: multiple accounts

**Describe two functions of an operating system** (X marks)
- Memory management: tracks what is stored in RAM; allocates memory to programs; handles swapping
- File management: organises files in folders/directories; handles reading/writing; controls access
- Device management: communicates with peripherals via drivers; manages printer queues; handles input/output

**Explain difference between system and application software** (X marks)
- System software manages computer resources
- Application software allows user to perform tasks
- System software runs in background
- Application software is user-facing

#### Software Licensing
**Describe freeware and free software** (X marks)

**Freeware:**
- User does not have access to the source code
- Has copyright
- User does not have the right to edit the software
- Normally distributed for free

**Free software:**
- User has access to the source code
- Still has copyright // Is copyleft
- User has the right to edit and share the software
- Normally has a fee to buy

**Identify type of software for trial version** (X marks)
- Distribute as shareware

#### Interrupts
**Explain what happens when an interrupt is generated** (X marks)
- Signal to CPU indicating device needs attention
- Generated by hardware when action required
- CPU suspends current task, handles interrupt, resumes execution

**Explain how interrupts are handled by the operating system** (X marks)
- Interrupt generated when device needs CPU attention
- CPU completes current instruction, saves state
- Interrupt Service Routine (ISR) executed to handle interrupt
- CPU returns to interrupted program
- Allows efficient use of CPU

---

### 4.2 Translators and IDEs

#### Programming Languages
**Complete table about programming language types** (X marks)
- High-level language: requires translator, English-like, portable
- Assembly language: requires translator, uses mnemonics, low-level
- Machine code: binary, directly executed by CPU, low-level

**State type of programming language used** (X marks)
- High-level

**Describe what is meant by high-level language** (X marks)
- English-like statements
- Portable across different hardware
- Requires translator to execute

**Describe what is meant by low-level language** (X marks)
- Close to language processed by computers
- May use mnemonics
- Example: assembly language, machine code

#### Translators
**Give one similarity between compiler and interpreter** (X marks)
- Both translate high-level language into machine code
- Both check for errors
- Both report errors

**Describe two differences between compiler and interpreter** (X marks)
- Interpreter translates and executes code line by line
- Compiler translates entire code before execution
- Interpreter stops when it finds an error
- Compiler produces error report after full translation
- Interpreter does not produce executable file
- Compiler produces executable file

**Identify translator during development and benefits** (X marks)
- Interpreter: easier to debug, errors immediately reported
- Compiler: all errors reported in single report, can all be fixed at same time

**Identify translator for final program and benefits** (X marks)
- Compiler: creates executable file, source code cannot be stolen

**Explain why compiler used instead of interpreter** (X marks)
- Creates an executable file
- Source code not released
- Translator not required each time
- Making it machine independent

**Explain purpose of assembler** (X marks)
- Translates assembly language to machine code
- One-to-one translation
- Produces object code

#### IDE Functions
**Identify three IDE features** (X marks)
- Code editor with syntax highlighting
- Debugger with breakpoints
- Compiler/interpreter
- Auto-completion
- Error diagnostics

**Describe three ways IDE helps programmer** (X marks)
- Code editor: enter and amend code
- Run-time environment: run program and see outputs
- Error-diagnostic: show where errors are
- Auto-completion: suggest commands

---

## Topic 5: The Internet and its Uses

### 5.1 The Internet and the World Wide Web

#### Internet Terms
**Complete table with web page and Internet terms** (X marks)
- HTML: the language used to create a web page
- Browser: the software application used to display a web page
- IP address: an address given to a computer to allow unique identification
- Cookie: a text file sent by web server to collect data about browsing habits
- ISP: the company that provides connection to the Internet

#### Web Browser
**Describe how web pages are requested and displayed** (X marks)
- Browser sends URL to DNS
- Uses HTTP/HTTPS
- IP address found on DNS
- DNS returns IP address to browser
- Browser sends request to web server
- Web server sends web page back to browser
- Browser interprets/renders the HTML

**Describe how a web browser retrieves and displays a web page** (X marks)
- User enters URL or clicks link
- Browser sends HTTP/HTTPS request to web server
- Server responds with HTML, CSS, JavaScript
- Browser renders and displays content

**Give two functions of web browser** (X marks)
- Display/render web pages
- Store cookies
- Store bookmarks/favourites

#### Cookies
**Describe how cookies store and auto-enter payment details** (X marks)
- Webserver sends cookie file to user's browser
- User's payment details stored in encrypted text file
- Cookie file stored by browser on HDD/SSD
- When user revisits website, webserver requests cookie file
- Browser sends cookie file back to webserver

**Explain why users may be concerned about cookies** (X marks)
- User does not see what information is stored
- A profile could be built about the user
- Sensitive information stored could be intercepted
- Other websites could gain access to cookies
- Payment information could be stolen

**State what a cookie is** (X marks)
- Small text file stored by website
- Contains user data/preferences

**Explain purpose of cookies** (X marks)
- Remember user preferences
- Track browsing habits
- Store login information
- Enable targeted advertising

**Explain difference between session and persistent cookies** (X marks)
- Session: stored in RAM, deleted when browser closes
- Persistent: stored on hard disk, remains until deleted/expiry

**Give three examples of cookie uses** (X marks)
- User preferences, Login details, Payment details
- Personal details, Shopping cart contents
- Targeted advertising

---

### 5.2 Digital Currency

#### Bitcoin
**Identify characteristics of Bitcoin** (X marks)
- Digital cryptocurrency, Decentralized
- Uses blockchain technology
- Encrypted transactions

#### Blockchain
**Describe how blockchain records transactions** (X marks)
- Transaction added to block
- Block contains hash of previous block
- Distributed across network
- Verified by multiple computers
- Immutable once added

**Give name of technology behind cryptocurrency** (X marks)
- Blockchain

---

### 5.3 Cyber Security

#### Firewall
**Complete paragraph about firewall operation** (X marks)
- Software or network-based
- Criteria set for acceptable traffic
- Accept or reject traffic
- Reject or accept based on criteria

**Explain how firewall keeps mobile device secure** (X marks)
- Monitors incoming/outgoing traffic
- Sets criteria for acceptable traffic
- Blocks traffic not meeting criteria
- Prevents unauthorized access

**Explain how firewall operates to protect network** (X marks)
- Criteria can be set (blacklist/whitelist of IP addresses)
- Examines incoming traffic
- Checks traffic meets criteria
- Rejects traffic that doesn't meet criteria

#### Security Methods
**Identify three methods to keep data secure** (X marks)
- Password
- Biometrics (device)
- Encryption
- Physical methods (locks)
- Two-factor authentication
- Anti-viruses

**Identify two software security methods** (X marks)
- Encryption, Biometric device, Firewall
- Anti-spyware, Two-factor authentication

**Identify three methods to prevent data viewing** (X marks)
- Password
- Biometric device
- Two-step verification/Two-factor authentication
- Physically lock the laptop away

**Describe two security measures that protect data on a computer system** (X marks)
- Access levels: different permissions for different users
- Firewalls: monitors network traffic
- Anti-malware: scans for malicious software
- Authentication: passwords, biometrics

#### Email Attacks
**Describe what is meant by phishing and pharming** (X marks)

**Phishing:**
- Legitimate looking email sent to user
- Encourages user to click link to fake website
- User encouraged to enter personal details

**Pharming:**
- Malicious code/malware downloaded without users' knowledge
- Re-directs user to fake website when legitimate URL entered
- User encouraged to enter personal details

**State purpose of phishing and pharming** (X marks)
- To obtain user's personal data

#### Malware
**Complete table about virus, spyware, DoS attack** (X marks)
- Virus: self-replicating, damages files, installed on web server
- Spyware: captures keyboard data, installed on web server
- Denial of service: prevents access to website

**Identify three types of malware** (X marks)
- Virus, Worm, Trojan horse, Spyware, Ransomware, Adware

**Identify three cyber security threats** (X marks)
- Phishing, Pharming, Malware, DDoS, Hacking

**Identify three other Internet security risks** (X marks)
- Hacking/cracking
- Virus, Spyware
- Malware

**State purpose of denial of service attack** (X marks)
- To disrupt the operation of a web server/network

**Explain why DoS attack prevents website access** (X marks)
- Web server has been flooded with traffic
- Server is brought to a halt/crashes

**Describe how brute-force attack works** (X marks)
- Trial and error to guess password
- Combinations repeatedly entered
- Until correct password found

**Draw and annotate DDoS attack diagram** (X marks)
- Malware downloaded to computers
- Turns them into bots/zombies
- Creates botnet
- Third party initiates attack
- Bots send requests to web server simultaneously
- Web server fails from overload

#### Security Solutions
**Give security solutions to prevent brute-force attacks** (X marks)
- Two-step verification, Two-factor authentication
- Biometrics, Firewall
- Strong/complex password
- Limit login attempts, Drop-down boxes

**Give ways to prevent DDoS attack** (X marks)
- Proxy server, Firewall
- Users scanning computers with anti-malware

**Identify two security methods against online attacks** (X marks)
- Firewall, Encryption, Antivirus, Authentication

---

### 5.4 Data Backup

**State three ways data could be accidentally damaged** (X marks)
- Human error
- Power failure/surge
- Hardware failure
- Software failure
- Fire, Flood

**Identify two ways data can be accidentally damaged** (X marks)
- Hardware failure, Software failure
- Power failure/surge
- Fire, Flood, Natural disaster

**Give two ways to prevent accidental data damage** (X marks)
- Use verification methods before deleting files
- Keep data in fireproof box
- Use surge protection/UPS
- Correct shutdown procedures
- Access rights, Back up data

---

## Topic 6: Automated and Emerging Technologies

### 6.1 Automated Systems

#### Sensors
**Identify two sensors for security light system** (X marks)
- Light sensor, Motion sensor/infra-red sensor

**Identify two sensors for counting people** (X marks)
- Pressure sensor, Motion sensor

**Identify suitable sensor for each task** (X marks)
- Temperature sensor: checking temperature
- pH sensor: checking acidity level
- Pressure sensor: checking weight

**Complete table with suitable sensors for each task** (X marks)
- Infrared/light: Check if vehicle is too high
- Magnetic field/pressure: Count vehicles entering car park
- Pressure/magnetic field/infrared: Check if vehicle parked

#### Sensor and Microprocessor Control
**Describe how temperature sensor and microprocessor maintain temperature** (X marks)
- Sensor sends data to microprocessor
- Data is converted from analogue to digital (using ADC)
- Microprocessor compares data to stored values/range
- If data greater than range, sends signal to adjust
- If data below range, sends signal to adjust
- If data within range, no action taken
- Actuator is used to operate system
- Whole process is continuous

**Describe how sensors and microprocessor control system** (X marks)
- Sensor detects physical condition
- Converts to electrical/digital signal
- Microprocessor receives and processes data
- Compares to stored threshold values
- If condition met, sends signal to actuator
- Actuator produces physical response
- Feedback loop maintains desired state

**Describe how sensors and actuators work together in an automated system** (X marks)
- Sensor detects physical change in environment
- Converts to electrical signal (analog or digital)
- Processed by microprocessor/controller
- Actuator receives command and produces physical output
- Feedback loop maintains desired conditions

**State what is meant by automated system** (X marks)
- System that performs actions without human intervention

**State what is meant by a sensor in an automated system** (X marks)
- Device that detects changes in physical conditions
- Converts physical input to electrical signals

**Give two benefits of using automated system** (X marks)
- Farmer/worker free to do other jobs
- Doesn't need to take breaks, works 24/7
- Performs boring repetitive tasks
- Saves labour costs
- More accurate/efficient
- Safer in dangerous environments

**State two drawbacks of automated monitoring** (X marks)
- High set-up/installation costs
- Utility/maintenance/repair costs
- Deskilling of workforce

---

### 6.2 Robotics

#### Robot Characteristics
**Identify three characteristics of a robot** (X marks)
- Mechanical structure/framework
- Electrical components
- Programmable
- Can move/perform actions

**Describe three components of a robot and their functions** (X marks)
- Sensors: collect data from environment (cameras, proximity sensors)
- Microprocessor/controller: processes sensor data, makes decisions
- Actuators: motors that produce physical movement

**Give two advantages of automated robot** (X marks)
- More accurate when performing tasks
- Doesn't need breaks, works 24/7
- Won't get bored of repetitive tasks
- Can do other tasks
- Faster/more efficient
- Works in dangerous environments
- No labour costs

**Give two disadvantages of automated robot** (X marks)
- Expensive to purchase
- Maintenance costs
- Takes away jobs
- Workers may be deskilled
- Training needed
- If breaks, must manually perform task
- If faulty, may cause damage
- Cannot adapt to unexpected events

**Give advantages to employees of using robots** (X marks)
- Protected from dangerous tasks
- Don't need to lift heavy items
- Can use skills in other tasks
- Don't need to perform repetitive/mundane tasks

**Explain advantages of robots in manufacturing** (X marks)
- Work 24/7, no breaks needed
- More accurate/precise
- Don't get bored with repetitive tasks
- No health and safety concerns
- Consistent quality

---

### 6.3 Artificial Intelligence

#### Logic Circuits
**Draw logic circuit for given logic statement** (X marks)
- One mark per each correct logic gate with correct input

**Complete truth table for logic statement** (4 marks)
- 4 marks per 8 correct outputs

| A | B | C | X |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 0 |
| 0 | 1 | 0 | 0 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 0 |
| 1 | 0 | 1 | 1 |
| 1 | 1 | 0 | 0 |
| 1 | 1 | 1 | 1 |

**Identify four errors in truth table** (X marks)
- Specific rows identified based on logic statement

**Identify three logic gates used in circuit** (X marks)
- AND, OR, NOT, XOR, NAND, NOR

**State name and draw symbol of gate not in statement** (X marks)
- NAND, NOR, XOR

#### AI Definition
**Give characteristic of AI** (X marks)
- Ability to learn/adapt
- Collection of data and rules
- Ability to reason
- Simulates intelligent behaviour

**Explain what is meant by AI** (X marks)
- Simulation of intelligent behaviours by computers
- Collection of data and rules for using data
- Ability to reason, Ability to learn/adapt

#### Expert Systems
**Give three components of expert system** (X marks)
- Rule base, Knowledge base, Interface

**Describe expert system components** (X marks)
- Knowledge base: stores facts from experts
- Rule base: stores IF-THEN rules
- Inference engine: reasoning mechanism
- Interface: user interaction

**Explain how expert system makes decisions** (X marks)
- Expert system uses knowledge base (facts and rules) and inference engine
- Applies rules to facts using reasoning
- Provides advice/diagnosis based on stored knowledge

**Explain how expert system diagnoses problems** (X marks)
- User enters data via interface
- Inference engine decides questions to ask based on previous answers
- Compares answers to knowledge base and rule base
- Outputs diagnosis/explanation of how diagnosis reached

**Explain difference between AI and expert systems** (X marks)
- AI: simulates human intelligence, learns
- Expert system: applies predefined rules

#### Machine Learning
**Give name of ability to automatically adapt processes and data** (X marks)
- Machine learning

**Explain how machine learning improves system** (X marks)
- System adapts by changing own rules/data/processes
- Becomes more efficient with greater knowledge
- Learns patterns, routes, obstacles
- Makes fewer errors

**Explain the difference between traditional programming and machine learning** (X marks)
- Traditional programming: programmer writes explicit rules
- Machine learning: computer learns patterns from data, creates its own rules
- Uses training data, improves with more data

**Explain how plough uses AI** (X marks)
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
- Confusing similar concepts
- Giving vague descriptions instead of specific details

### Answer Presentation
- Use bullet points for multiple points
- Numbered steps for processes
- Diagrams where appropriate
- Clear, concise language