# Paper 1 Marking Scheme (2021)

This document contains the expected answers and key points from the 2021 Paper 1 marking schemes, organized by syllabus topics.

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
**Convert denary values from IP address to binary** (S21 V1)
```
1     0    1     0     0    1        1        1

1     1    0     1     0    1        1        0
```

**Convert hexadecimal values to binary** (S21 V3)
- 00010100
- 10100000
- 11001001

**Convert hexadecimal values to denary** (S21 V3)
- 41
- 200

**Convert binary to denary** (S21 V1)
- 179

**Convert hexadecimal to binary** (S21 V2)
| Denary | Hexadecimal | 8-bit binary |
|--------|-------------|--------------|
| 49 | 31 | 00110001 |
| 123 | 7B | 01111011 |
| 200 | C8 | 11001000 |

**Convert hexadecimal to denary** (W21 V1)
- 9, 16, 40, 161

**Convert hexadecimal to denary** (W21 V2)
- 5, 32, 26, 171

**Convert hexadecimal to binary** (W21 V2)
- 25 → 00100101
- 1B → 00011011

**Convert binary to denary** (W21 V3)
- 00000000 01000111 → 71
- 00000001 00000001 → 257

**Convert denary to binary** (W21 V3)
- 00000000 01000111
- 00000001 00000001

**Identify base of binary number system** (W21 V1)
- Base-2

**Identify base of denary number system** (W21 V2)
- Base-10

#### Binary Representation
**Explain why computer can only process binary data** (S21 V1)
- Computers use logic gates/switches
- Logic gates have two states (on/off)
- Binary represents these two states (0/1)

#### Hexadecimal Uses
**Give two benefits of converting binary to hexadecimal** (S21 V2)
- Easier/quicker to read/write/understand
- Easier/quicker to identify errors/debug
- Takes up less screen/display space
- Less chance of making an error

**Identify three other uses of hexadecimal** (S21 V2)
- MAC address
- URL
- Assembly language
- Error codes // error messages
- IP addresses
- Locations in memory
- Memory dumps

**Give use of hexadecimal in website development** (W21 V2)
- To represent HTML colour codes
- In error messages

**Give use of hexadecimal in low-level programming** (W21 V2)
- Assembly code/language
- Memory address locations
- In error messages
- Memory dump

#### Parity Check
**Identify whether odd or even parity for each binary value** (S21 V1)
- Odd
- Odd
- Even
- Even

**Identify whether odd or even parity for each binary value** (S21 V3)
- Odd
- Even
- Even
- Odd

**Identify whether odd or even parity for each binary value** (W21 V3)
- Even
- Even
- Odd
- Even

**Identify why parity check may not detect error** (S21 V1)
Any one from:
- There is a transposition of bits
- It does not check the order of the bits (just the sum of 1s/0s)
- Even number of bits change
- Incorrect bits still add up to correct parity

**State why parity check does not identify error** (S21 V3)
Any one from:
- There is a transposition of bits
- Bits still add up to correct parity

---

### 1.2 Text, Sound and Images

#### Sound Representation
**Calculate total file size of photographs** (W21 V1)
Working:
- 100 × 50 = 5000 bits
- 5000 × 8 = 40,000 bits
- 40,000 / 8 = 5,000 bytes
- 5,000 × 10 = 50,000 bytes
- 50,000 / 1024

Answer: 48.83 kB // 49 kB

**Describe how sound files are compressed using lossless compression** (S21 V1)
Four from:
- (Compression) algorithm is used
- No data will be removed // original file can be restored
- Example of type of algorithm that would be used e.g. RLE
- Repeated patterns in the music are identified
- … and indexed

#### Image Representation
**Complete paragraph about digital camera operation** (W21 V1)
- Light
- Lens
- Charge-coupled
- Analogue-to-digital
- Pixel

**Complete paragraph about MP3, MP4, MIDI files** (W21 V3)
- MP4
- MP3
- Microphone
- Compressed
- MIDI
- Notes
- Can

---

### 1.3 Data Storage and Compression

#### Compression Types
**State compression type and justify choice** (W21 V1)
- Lossless
- Lossy would remove data permanently // lossless would not remove any data permanently // File could be restored to original …
- … that could affect the quality (lossy) // … to maintain the quality (lossless)

**Describe how lossy compression reduces video file size** (S21 V3)
Any three from:
- A compression algorithm is used
- Redundant data is removed
- Reduce colour depth
- Reduce image resolution
- Reduce sample rate
- Reduce sample resolution
- Reduce frame rate
- Use perceptual music shaping
- Data is permanently removed

**Give three ways lossy compression reduces video size** (W21 V2)
Any three from:
- A compression algorithm is used
- The resolution could be reduced
- Colour depth could be reduced // bits per pixel reduced
- Sounds not heard by human ear could be removed // Perceptual music shaping can be used
- Repeating frames could be removed

**Give two reasons for using lossy compression** (S21 V3)
Any two from:
- Lossy decreases the file size more
- Take up less storage space on webserver/users' computer
- Quicker to upload/download
- May not need to be high quality
- Website will load faster for users
- Less lag/buffering when watching
- Takes up less bandwidth to download/upload
- Uses less data allowance

**State reason for using lossless compression** (S21 V1)
Any one from:
- To provide the highest quality of music file (that compression will allow)
- The user is able to listen to the original sound file
- No loss of quality for the sound file provided

**State reason for using lossless compression** (W21 V3)
Any one from:
- Maintains quality // quality better than lossy
- Original file is retained // Data is not permanently lost
- A significant reduction in file size is not required

**Give reason for using lossless compression** (W21 V2)
Any one from:
- Maintains quality // quality better than lossy
- Original file is retained // Data is not permanently lost
- A significant reduction in file size is not required

**Give benefit of compressing sound files** (S21 V1)
Any one from:
- Allow for quicker streaming speed
- Would not require as much bandwidth (to stream)
- Does not need as much RAM
- Smoother listening experience // less lag
- Will not use as much of data allowance

**Give drawback of lossless vs lossy compression** (S21 V1)
Two from:
- Streaming speed may be slower
- … and may affect listening experience // buffering may occur
- User may need more bandwidth to stream
- … that could be more expensive
- It would be a larger file size
- … so may take longer to upload
- … so will take up more storage space …
- … on webserver

**Give drawback of using lossy compression** (W21 V2)
Any one from:
- Quality may be reduced
- Data is lost // original file cannot be reconstructed

**Give two disadvantages of lossless compression** (W21 V2)
Any two from:
- Takes more time to transmit file // Takes more time to upload to web server // Takes more time to download to customer // Web page will load slower
- Takes up more storage space
- Data usage would be increased
- Uses more bandwidth

**Describe how lossless compression reduces file size** (W21 V3)
Any three from:
- Compression algorithm used
- …, e.g. RLE
- Repeating frames/pixels are identified
- … and are collated/indexed
- No data is permanently removed
- It just records the changes between frames/pixels

#### File Size
**Identify largest file size** (W21 V3)
| File Size | Tick (✓) |
|-----------|----------|
| 999 kB | |
| 1 MB | ✓ |
| 850 000 bytes | |

**Identify smallest file size** (W21 V3)
| File Size | Tick (✓) |
|-----------|----------|
| 4000 MB | |
| 2 GB | ✓ |
| 2 500 000 kB | |

---

## Topic 2: Data Transmission

### 2.1 Types and Methods of Data Transmission

#### Serial vs Parallel
**Describe how data is sent using parallel half-duplex** (S21 V1)
Four from:
- Multiple bits are sent at the same time
- Uses multiple wires
- Data is sent in both directions …
- … but only one direction at a time

**Describe how data is sent using serial duplex** (S21 V3)
- Data is sent one bit at a time
- Data is sent using a single wire
- Data is sent in both direction …
- … at the same time

**Describe how data is sent using serial half-duplex** (W21 V3)
Four from:
- Bits sent one at a time
- … down a single wire
- Data sent in both directions …
- … but only one direction at a time

**State drawback of serial transmission** (S21 V3)
Any one from:
- Data transmission can be slower (than parallel)
- Additional data may need to be sent

**Explain why half-duplex needed instead of simplex** (W21 V3)
Any two from:
- Simplex only sends data in one direction
- … so, printer may not be able to tell computer an error has occurred, and computer may not be able to send printer the document to be printed

**State two drawbacks of parallel transmission** (S21 V1)
Any two from:
- Bits may arrive skewed
- More expensive to setup/manufacture/purchase cable
- Limited distance
- More prone to interference/error

**Complete table about serial/parallel transmission** (W21 V2)
| Statement | Serial simplex (✓) | Parallel simplex (✓) | Parallel half-duplex (✓) | Serial duplex (✓) |
|-----------|-------------------|---------------------|------------------------|------------------|
| bits are transmitted along a single wire | ✓ | | | ✓ |
| data is transmitted in both directions | | | ✓ | ✓ |
| it is only suitable for distances less than 5 metres | | ✓ | ✓ | |
| Bits from the same byte are transmitted one after the other | ✓ | | | ✓ |
| data may not arrive in the correct sequence | | ✓ | ✓ | |
| data is transmitted in both directions, but only one direction at a time | | | ✓ | |

#### USB
**State two benefits of USB connection** (S21 V1)
Any two from:
- It cannot be inserted incorrectly
- Supports different transmission speeds
- High speed transmission
- Automatically detected (not connected) // automatically downloads drivers
- Powers the device (for data transfer)
- Backward compatible

**Identify type of data transmission in USB** (S21 V1)
- Serial

**Give three benefits of USB connection** (W21 V2)
Any three from:
- Can charge/power the mobile device (at the same time)
- (Uses serial transmission so) data less likely to be skewed / corrupted
- Universal / industry standard / connection
- Cable can only be plugged in one way // Cannot be inserted incorrectly
- Fast transmission speed
- Backward compatible
- Supports different transmission speeds
- Automatically detects device // Automatically downloads drivers

---

### 2.2 Methods of Error Detection

#### Error-Checking Methods
**Complete table about checksum, check digit, parity** (W21 V1)
| Statement | Checksum (✓) | Check digit (✓) | Parity check (✓) |
|-----------|-------------|-----------------|------------------|
| uses an additional bit to create an odd or even number of 1s | | | ✓ |
| checks for errors on data entry | | ✓ | |
| compares two calculated values to see if an error has occurred | ✓ | ✓ | |
| will not detect transposition errors | | | ✓ |
| sends additional values when data is transmitted from one computer to another | ✓ | | ✓ |

**Complete table about ARQ, check digit, checksum** (W21 V3)
| Statement | ARQ (✓) | Check digit (✓) | Checksum (✓) |
|-----------|---------|-----------------|--------------|
| checks for errors on data entry | | ✓ | |
| uses a process of acknowledgement and timeout | ✓ | | |
| compares two calculated values to see if an error has occurred | | ✓ | ✓ |
| may resend data until it is confirmed as received | ✓ | | |
| checks for errors in data after transmission from a computer to another | | | ✓ |

**Identify one other error-checking method** (W21 V1)
- ARQ

**Identify one other error-checking method** (W21 V3)
- Parity check

---

### 2.3 Encryption

**Explain how SSL protocol secures data transmission** (W21 V2)
- Enables an encrypted link (between the browser and the web server) // It encrypts the data
- … based on the authentication of an (SSL) certificate // and will only send it if the certificate is authentic

**Identify alternative to SSL protocol** (W21 V2)
- Transport Layer Security // TLS

**Give two ways to identify if website uses secure transmission** (W21 V2)
Any two from:
- URL begins with HTTPS
- Padlock symbol is locked
- Check the certificate is valid

**Give two ways to identify if website uses secure transmission** (W21 V3)
Any two from:
- URL begins with HTTPS
- Padlock symbol is locked

---

## Topic 3: Hardware

### 3.1 Computer Architecture

#### Von Neumann Model
**Complete table about MAR, MDR, PC registers** (W21 V1)
| Statement | MAR (✓) | MDR (✓) | PC (✓) |
|-----------|---------|---------|--------|
| it is a register in the CPU | ✓ | ✓ | ✓ |
| it holds the address of the next instruction to be processed | ✓ | | ✓ |
| it holds the address of the data that is about to be fetched from memory | ✓ | | ✓ |
| it holds the data that has been fetched from memory | | ✓ | |
| it receives signals from the control unit | ✓ | ✓ | ✓ |
| it uses the address bus to send an address to another component | ✓ | | ✓ |

**Complete table about Von Neumann components** (W21 V3)
| Component name | Description |
|----------------|-------------|
| Memory Address Register (MAR) | (A register that) holds the address of the data/instruction that needs to be fetched/processed // holds the address of where the data needs to be stored. |
| Program Counter (PC) | (A register that) holds the address of the next / current instruction to be processed. |
| Accumulator // ACC | This is a register that is built into the arithmetic logic unit. It temporary holds the result of a calculation. |
| Memory Data Register // MDR | This is a register that holds data or an instruction that has been fetched from memory. |
| Control Unit (CU) | Sends control signals to control the flow of data through the CPU // manages the execution of instructions in the CPU |
| Address bus | This carries addresses around the CPU. |

**Complete table about ALU, CU, RAM components** (S21 V3)
| Statement | ALU (✓) | CU (✓) | RAM (✓) |
|-----------|---------|--------|---------|
| Stores data and instructions before they enter the central processing unit (CPU) | | | ✓ |
| Contains a register called the accumulator | ✓ | | |
| Manages the transmission of data and instructions to the correct components | | ✓ | |
| Contained within the CPU | ✓ | ✓ | |
| Uses the data bus to send data into or out of the CPU | ✓ | | ✓ |
| Carries out calculations on data | ✓ | | |

**Give two other registers in Von Neumann model** (S21 V3)
Any two from:
- MAR
- MDR // MBR
- PC
- CIR // IR

**Identify component that carries out calculations** (W21 V1)
- Arithmetic Logic Unit // ALU

#### Interrupt
**Give name of signal that stops music for call** (W21 V1)
- interrupt

**State what happens without interrupt signals** (W21 V2)
Any one from:
- The computer would only start a new task when it had finished processing the current task // by example
- Computer will not be able to multitask
- Errors may not be dealt with
- Computer would become impossible to use

**Describe role of interrupt in generating paper jam message** (W21 V3)
Any four from:
- Printer generates interrupt
- Interrupt is given a priority
- Interrupt is queued
- Interrupt stops CPU from processing current task
- CPU will service interrupt // Interrupt handler services interrupt …
- … generating an output message to state there is a paper jam

**Give three examples of when interrupt signal generated** (W21 V2)
Any three from:
- A suitable description of any error that might occur
- A peripheral is connected/disconnected
- A key on a keyboard is pressed
- A mouse button click
- A phone/video call is received
- A buffer requires more data
- A printer has a paper jam
- A printer runs out of paper
- A printer runs out of ink
- When switching from one application to another

**Give two other examples of interrupt signals** (W21 V3)
Any two from:
- A suitable description of any error that might occur
- A peripheral is connected/disconnected
- A key on a keyboard is pressed
- A mouse button click
- A phone/video call is received
- A buffer requires more data
- A printer runs out of paper
- A printer runs out of ink
- Opening an application
- When switching from one application to another

---

### 3.2 Input and Output Devices

#### Input Devices
**Identify three devices to input personal data** (S21 V1)
Any three from:
- Keyboard
- Mouse
- Microphone
- Keypad
- Touchscreen
- Touchpad

**Identify two other input devices** (S21 V3)
Any two from:
- Keyboard
- Microphone
- 2D/3D Scanner
- Sensor
- Touchscreen
- Keypad
- Webcam
- Joystick

**Identify other input device for mobile phone** (W21 V1)
- Microphone

**Identify input device for ticket machine** (W21 V2)
Any one from:
- Touchscreen
- Trackpad / touchpad
- Microphone
- QR code reader
- Barcode reader
- Magnetic strip reader
- RFID reader

#### Output Devices
**Identify output device for ticket machine** (W21 V2)
Any one from:
- Printer
- Speaker
- Light/LED
- Actuator

**Identify two output devices** (W22 V2)
- Screen, speaker, printer, actuator, LED

#### Touchscreen
**State touchscreen technology type** (W21 V1)
- capacitive

**Complete paragraph about capacitive and resistive touchscreens** (W21 V2)
- Capacitive
- Conductive // Capacitive
- Change
- Coordinates
- Resistive
- Circuit
- Manufacture

#### Keyboard and Mouse
**Complete paragraph about keyboard operation** (S21 V2)
- Switch
- Circuit
- Current
- Calculated
- Character
- Binary

**Complete paragraph about optical mouse operation** (S21 V3)
- LED
- Photoelectric
- Lens
- Magnifies
- Microswitch
- USB

#### Barcode and Scanner
**Complete table about 3D scanner, barcode, QR code** (W21 V2)
| Statement | 3D scanner (✓) | Barcode reader (✓) | QR code reader (✓) |
|-----------|----------------|-------------------|-------------------|
| uses position and alignment markers for orientation when scanning | | | ✓ |
| scans the shape and appearance of an object | ✓ | | |
| uses reflected light from a laser to convert a black-and-white pattern into binary | | ✓ | ✓ |
| can often be built into an Electronic Point Of Sale (EPOS) terminal, for example, a supermarket checkout | | ✓ | ✓ |
| it is an example of an input device | ✓ | ✓ | ✓ |

**Identify if sensor is input, storage, or output device** (W21 V3)
| Device | Tick (✓) |
|--------|----------|
| input | ✓ |
| storage | |
| output | |

---

### 3.3 Data Storage

#### Storage Types
**Complete table about HDD, SSD, USB characteristics** (S21 V1)
| Statement | HDD (✓) | SSD (✓) | USB flash memory (✓) |
|-----------|---------|---------|---------------------|
| it has no moving parts | ✓ | ✓ | ✓ |
| it is non-volatile | ✓ | ✓ | ✓ |
| it can use NAND gates to store data | | ✓ | ✓ |
| it uses magnetic properties to store data | ✓ | | |
| it has the smallest physical size | | ✓ | ✓ |
| it has the slowest read/write speeds | ✓ | | |

**Complete table about magnetic, solid-state, optical storage** (S21 V2)
| Statement | Magnetic (✓) | Solid state (✓) | Optical (✓) |
|-----------|-------------|-----------------|-------------|
| no moving parts are used to store data | | ✓ | |
| pits and lands are used to store data | | | ✓ |
| data is stored on platters | ✓ | | |
| flash memory is used to store data | | ✓ | |
| parts are rotated to store data | ✓ | | ✓ |
| data can be stored permanently | ✓ | ✓ | ✓ |

**Identify storage type for each device** (S21 V3)
- Magnetic
- Solid state
- Optical

#### Storage Examples
**Give example of magnetic storage** (S21 V2)
Any one from:
- Hard disk drive // HDD
- Magnetic tape

**Give example of optical storage** (S21 V2)
Any one from:
- CD
- DVD
- Blu-ray disk

#### Storage Selection
**Identify storage type for web server and justify** (S21 V2)
One for type of storage, two for matching justification:

**Magnetic // HDD:**
- (Web server) is likely to receive many requests a day
- (Web server) will likely need to store a lot of data and magnetic is high capacity
- Magnetic is cheaper to buy for storage per unit than solid state
- Magnetic is capable of more of read/write requests over time // has more longevity // SSD has more limited number of read/write requests (before it is no longer usable)
- No requirement for it to be portable, so moving parts does not matter

**Solid-state // SSD:**
- (Web server) is likely to receive many requests a day
- (Web server) will likely need to store a lot of data and solid-state is high capacity
- Solid-state is more energy efficient
- Solid-state runs cooler so will not overheat
- Solid state has faster read/write speeds to handle volume of traffic

**Classify internal SSD and justify choice** (W21 V1)
- Secondary
- It is non-volatile storage
- It is not directly accessed by the CPU

#### Storage Operation
**Describe operation of USB flash memory** (S21 V2)
Any three from:
- Data is flashed onto (silicon) chips
- Uses NAND/NOR technology // can use flip-flops
- Uses transistors/control gates/floating gates …
- … to control the flow of electrons
- It is a type of EEPROM technology
- When data is stored the transistor is converted from 1 to 0 / 0 to 1
- Writes (and reads) sequentially

**Describe operation of HDD and how it stores data** (S21 V3)
Any four from:
- It has platters
- Platters/disk divided into tracks
- Platter/disk is spun
- Has a read/write arm that moves across storage media
- Read/writes data using electromagnets
- Uses magnetic fields to control magnetic dots of data
- Magnetic field determines binary value

**Describe operation of SSD and how it stores data** (W21 V1)
Any four from:
- Uses flash memory
- Data is flashed onto (silicon) chips
- Uses NAND/NOR technology // Can use flip-flops
- Uses transistors/control gates/floating gates …
- … to control the flow of electrons
- It is a type of EEPROM technology
- When data is stored the transistor is converted from 1 to 0 / 0 to 1
- Writes (and reads) sequentially

---

### 3.4 Network Hardware

#### MAC Address
**Identify who assigns MAC address** (S21 V3)
- manufacturer

**Identify similarity between IP and MAC address** (S21 V1)
Any one from:
- Both addresses can be used to identify a computer/device
- Both are unique
- Both can be represented as hexadecimal
- Both addresses do not change if IP address is static

**Identify two differences between IP and MAC address** (S21 V1)
Any two from:
- An IP address is assigned by the network/router/ISP, A MAC address is assigned by the manufacturer
- An IP address can be changed (if dynamic), MAC address cannot be changed
- IP address has 4/8 groups of values, MAC address has 6 groups/pairs of values
- IP address is 32-bit/128-bit, MAC address is 48-bit
- IP address does not contain serial number/manufacturer number, MAC address does
- IP(v4) address is denary and MAC address is hexadecimal

---

## Topic 4: Software

### 4.1 Types of Software

#### Operating System
**State two other functions of operating system** (W21 V1)
Any two from:
- Interrupt / error-handling
- Peripheral management
- Providing user interface
- Platform for running applications // installing / removing software
- Manages security // access rights/levels // user account management
- Managing time slicing // multitasking

**Give example of HTML structure** (S21 V2)
Any one from:
- Placement of text/image
- Margins
- Line break
- Padding

**Give two examples of HTML presentation** (S21 V2)
Any two from:
- Font colour
- Font style
- Font size
- Background colour
- Image size
- Border properties

**Explain why HTML is separated into structure and presentation** (S21 V2)
Any two from:
- Can easily change/edit the style of the webpage
- So, CSS can be used to create a template/style sheet
- Can add new content and apply the same style easily
- Can re-use the presentation/style for other websites

#### Software Licensing
**Describe freeware and free software** (W21 V3)
Any four from (MAX 3 per software licence):

**Freeware:**
- User does not have access to the source code
- Has copyright
- User does not have the right to edit the software
- Normally distributed for free // no cost

**Free software:**
- User has access to the source code
- Still has copyright // Is copyleft
- User has the right to edit and share the software
- Normally has a fee // cost to buy

**Identify type of software for trial version** (W21 V3)
- Distribute as shareware

---

### 4.2 Translators and IDEs

#### Programming Languages
**Complete table about programming language types** (S21 V3)
| Statement | High-level language (✓) | Assembly language (✓) | Machine code (✓) |
|-----------|------------------------|----------------------|------------------|
| It requires a translator to be processed by a computer | ✓ | ✓ | |
| It is an example of low-level language | | ✓ | ✓ |
| It uses mnemonics | | ✓ | |
| It uses English-like statements | ✓ | | |
| It can be used to directly manipulate hardware in the computer | | ✓ | ✓ |
| It is portable | ✓ | | |

**State type of programming language used** (W21 V1)
- High-level

#### Translators
**Identify translator during development and benefits** (W21 V1)
One mark for the correct translator, two marks for the benefit(s):
- Interpreter
- Easier to debug
- … as errors are immediately reported when detected

**Alternative:**
- Compiler
- All errors are reported in a single report
- … meaning they can all be fixed at the same time
- No need to recompile code every time a test is run

**Identify translator for final program and benefits** (W21 V1)
One mark for the correct translator, two marks for the benefits:
- Compiler
- Creates an executable file
- … so, translator is no longer needed to run it
- Source code cannot be stolen // can be provided without the source code

**Give one similarity between compiler and interpreter** (W21 V2)
Any one from:
- They both translate high-level language into machine code / low-level language
- They both check for errors
- They both report errors

**Describe two differences between compiler and interpreter** (W21 V2)
Four from (Max 2 per translator):
- An interpreter translates and executes the code line by line
- … whereas a compiler translates and executes the whole code all in one go
- An interpreter stops translating and reports an error as it finds one
- … whereas a compiler produces an error report at the end of translation
- An interpreter does not produce an executable file
- … but a compiler does produce an executable file
- An interpreter will execute the code until it finds an error
- … whereas a compiler will not execute any code if there are errors present
- An interpreter allows correction of errors in real-time
- … whereas a compiler needs to retranslate the code each time after errors are found and corrected

**Identify one other type of translator** (W21 V2)
- Assembler

**Explain why compiler used instead of interpreter** (W21 V3)
Any four from:
- Creates an executable file
- … so, would not release source code
- … so, the source code cannot be stolen/edited.
- … so, would not need to be translated every time // so, translator is not required
- … making it machine independent

---

## Topic 5: The Internet and its Uses

### 5.1 The Internet and the World Wide Web

#### Internet Terms
**Complete table with web page and Internet terms** (W21 V1)
| Terms | Description |
|-------|-------------|
| HTML | the language used to create a web page |
| Browser | the type of software application used to display a web page |
| IP address | an address given to a computer, by a network, to allow the computer to be uniquely identified |
| Cookie | a text file sent by a web server to collect data about a user's browsing habits |
| Internet Service Provider // ISP | the company that provides a connection to the Internet |

#### Web Browser
**Describe how web pages are requested and displayed** (S21 V1)
Any four from:
- Browser sends URL to DNS
- … using HTTP/HTTPS
- IP address is found on DNS
- DNS returns IP address to the browser
- Browser sends request to web server/IP address
- Web server sends web pages back to browser
- Browser interprets/renders the HTML (to display web pages)
- Security certificates exchanged

#### Cookies
**Describe how cookies store and auto-enter payment details** (S21 V2)
Any three from:
- Webserver sends (cookie) file to user's browser
- User's payment details stored in encrypted text file // data is encrypted to be stored
- Cookie file is stored by browser/on user's HDD/SSD
- When user revisits website, webserver requests cookie file // webserver can access the data stored in the cookie file (to automatically enter details)
- … and browser sends cookie file back to webserver (to automatically enter the details)

**Explain why users may be concerned about cookies** (S21 V2)
Four from:
- User does not see what information is stored // might collect data that user does not know about …
- … so, user may feel their privacy is affected
- A profile could be built about the user …
- … that could expose a user's identity // lead to identity theft
- Sensitive information stored in cookies could be intercepted in transmission …
- Other websites could gain access to the cookies stored on a user's computer …
- Computer could be hacked to obtain data stored in cookies …
- … so, payment information could be stolen and used by a third party

---

### 5.2 Digital Currency
(No questions in 2021 paper)

---

### 5.3 Cyber Security

#### Firewall
**Complete paragraph about firewall operation** (S21 V1)
- Software
- Network
- Criteria
- Accept // reject
- Reject // accept
- Hacking

**Explain how firewall keeps mobile device secure** (W21 V2)
- Monitors incoming/outgoing traffic
- Sets criteria for acceptable traffic
- Blocks traffic not meeting criteria
- Prevents unauthorized access

#### Security Methods
**Identify three other methods to keep data secure** (S21 V1)
Any three from:
- Password
- Biometrics (device)
- Encryption
- Physical methods (e.g. locks)
- Two-factor authentication // Two-step verification
- Anti-viruses

**State two software security methods** (W21 V1)
Any two from:
- Encryption
- Biometric device
- Firewall
- Anti-spyware
- Two-factor authentication // two-step verification

**Identify three methods to prevent data viewing** (W21 V2)
Any three from:
- Password
- Add a biometric device to the laptop // set biometric password
- Use two-step verification // Use two factor authentication
- Physically lock the laptop away in a secure cupboard // Taking laptop with him at all times

#### Email Attacks
**Describe what is meant by phishing and pharming** (S21 V1)
Any six from:

**Phishing:**
- Legitimate looking email sent to user
- encourages user to click a link that directs user to a fake website
- User encouraged to enter personal details into a fake website // designed to obtain personal details from a user

**Pharming:**
- Malicious code/malware is downloaded/installed // software downloaded without users' knowledge
- … that re-directs user to fake website (when legitimate URL entered)
- User encouraged to enter personal details into a fake website // designed to obtain personal details from a user

**Explain how personal details were obtained using phishing** (S21 V3)
- Legitimate looking/fake email sent to user
- … that contains a link to a fake website
- User clicks link and enters personal details (into fake website)

**State purpose of phishing and pharming** (W21 V3)
- To obtain a user's personal data

#### Malware
**Complete table about virus, spyware, DoS attack** (S21 V2)
| Statement | Virus (✓) | Spyware (✓) | Denial of service (✓) |
|-----------|-----------|-------------|----------------------|
| captures all data entered using a keyboard | | ✓ | |
| can be installed onto a web server | ✓ | ✓ | |
| prevents access to a website | | | ✓ |
| is malicious code on a computer | ✓ | ✓ | |
| is self-replicating | ✓ | | |
| damages the files on a user's hard drive | ✓ | | |

**Identify three other Internet security risks** (S21 V2)
Any three from:
- Phishing
- Pharming
- Hacking // cracking

**Identify three other Internet security risks** (S21 V3)
Any two from:
- Pharming
- Spyware
- Hacking/cracking

**Identify three other Internet security risks** (W21 V3)
Any three from:
- Hacking // Cracking
- Virus
- Spyware
- Malware

**State purpose of denial of service attack** (W21 V3)
- To disrupt the operation of a web server/network

**Explain why DoS attack prevents website access** (S21 V1)
Two from:
- Web server has been flooded with traffic // web server has been sent many requests at once
- … so, server is brought to a halt / crashes

---

### 5.4 Data Backup

**State three ways data could be accidentally damaged** (S21 V2)
Any three from:
- Human error
- Power failure/surge
- Hardware failure
- Software failure
- Fire
- Flood

**Identify two ways data can be accidentally damaged** (S21 V3)
Any two from:
- Hardware failure
- Software failure
- Power failure/surge
- Fire
- Flood
- Natural disaster

**Give two ways to prevent accidental data damage** (S21 V3)
Any two from:
- Use verification methods before deleting files
- Keep data in a fireproof box
- Do not drink liquids near a computer
- Use surge protection // UPS
- Correct shutdown procedures
- Access rights
- Back data up

---

## Topic 6: Automated and Emerging Technologies

### 6.1 Automated Systems

#### Sensors
**Identify two sensors for security light system** (S21 V2)
- Light sensor
- Motion sensor // infra-red sensor

**Identify two sensors for counting people** (W21 V3)
- Pressure sensor
- Motion sensor

**Identify suitable sensor for each washing machine task** (W21 V1)
| Task | Sensor |
|------|--------|
| checking the water is 30 °C | Temperature |
| checking the water acidity level after detergent is added | pH |
| checking the weight of the clothes to make sure that the machine is not overloaded | Pressure |

**Complete table with suitable sensors for each task** (S21 V3)
| Task | Sensor |
|------|--------|
| Check if a vehicle is too high | Infrared/light |
| Count the vehicles entering the car park | Magnetic field // pressure |
| Check if a vehicle is parked in a parking space | Pressure // magnetic field // infrared/light |

#### Sensor and Microprocessor Control
**Describe how temperature sensor and microprocessor maintain greenhouse temperature** (S21 V1)
Eight from:
- Sensor send data/readings/signal to microprocessor
- Data is converted from analogue to digital (using ADC)
- Microprocessor compares/checks data to stored values/range of values …
- … If data is greater than 30 / above the range microprocessor sends signal to open window and to turn heater off
- … If data is below 25 the microprocessor sends signal to turn on heater and to close window
- … If data is between 25 and 30 / within the range no action taken
- Actuator is used to operate heater/window
- Whole process is continuous

**Describe how sensors and microprocessor control security light** (S21 V2)
Eight from:
- Sensors send data to microprocessor
- Data is converted to digital (using ADC)
- Microprocessor compares data to stored value(s) …
- … if one value or neither values are within range/out of range/match no action is taken
- … If both values are out of range/in range/match microprocessor sends signal to switch light on …
- … 1-minute timer is started
- Actuator used to switch on/off light
- When timer reaches 1 minute, microprocessor sends signal to switch light off
- Whole process is continuous

**Describe how sensor and microprocessor display red or green light** (S21 V3)
Six from:
- Sensor sends data to microprocessor
- Data is converted from analogue to digital (using ADC)
- Data is compared to stored value …
- … If data is greater than stored value microprocessor sends signal to turn red light on and the green light off
- … If data is less than stored value microprocessor sends signal to turn green light on the red light off
- … If data still within range, no action taken/existing light remains on
- Lights turned on/off using actuator
- Process is continuous

**Describe how sensor and microprocessor maintain water temperature** (W21 V1)
Six from:
- Sensor sends data to microprocessor
- Data is converted from analogue to digital (using ADC)
- Data is compared to stored value (of 30)
- If data is below 30 then a microprocessor sends signal is sent to a heater to heat the water up/add hot water
- If data is above 30 then a microprocessor sends signal is sent to turn the heater off to allow the water to cool down/add cold water
- Actuator used to turn heater on/off // Actuator used to add water
- If data is 30 then no action is taken
- It is a continuous process

**Explain how sensors and microprocessor count correct mat hits** (W21 V2)
Seven from:
- Timer is started
- Pressure sensor (within each mat)
- Sensor sends data to microprocessor
- Analogue data is converted to digital (using ADC)
- Microprocessor compares data to stored value(s)
- If data matches / in/out range microprocessor stops timer
- If data matches / in/out range microprocessor checks if data has come from correct colour mat sensor
- If data matches / in/out range microprocessor checks to see if timer is stopped at less than 1 second
- If data matches / in/out range microprocessor increments counter if timer is less than 1 second and colour/mat is correct
- If correct colour/mat is hit, timer is reset and the whole process is repeated
- If data has not come from the correct colour mat sensor the game ends

---

### 6.2 Robotics
(No questions in 2021 paper)

---

### 6.3 Artificial Intelligence

#### Logic Circuits
**Draw logic circuit for given logic statement** (S21 V1)
One mark per each correct logic gate, with correct input:

[Logic circuit diagram required]

**Draw logic circuit for given logic statement** (S21 V2)
One mark for each correct logic gate with correct input.

[Logic circuit diagram required]

**Draw logic circuit for given logic statement** (W21 V1)
One mark per each correct logic gate with the correct input(s).

[Logic circuit diagram required]

**Draw logic circuit for given logic statement** (W21 V2)
One mark per each correct logic gate with correct input(s).

[Logic circuit diagram required]

**Draw logic circuit for given logic statement** (W21 V3)
One mark per each correct logic gate with correct inputs.

[Logic circuit diagram required]

#### Truth Tables
**Identify four errors in truth table** (S21 V1)
- Row 1
- Row 3
- Row 4
- Row 5

**Identify four errors in truth table** (S21 V2)
- Row 2
- Row 3
- Row 7
- Row 8

**Identify four errors in truth table** (S21 V3)
- Row 1
- Row 4
- Row 7
- Row 8

**Complete truth table for logic statement** (W21 V1)
4 marks per 8 correct outputs, 3 marks per 6/7 correct outputs, 2 marks per 4/5 correct outputs, 1 mark per 2/3 correct outputs.

| A | B | C | Working space | X |
|---|---|---|--------------|---|
| 0 | 0 | 0 | | 0 |
| 0 | 0 | 1 | | 0 |
| 0 | 1 | 0 | | 0 |
| 0 | 1 | 1 | | 1 |
| 1 | 0 | 0 | | 0 |
| 1 | 0 | 1 | | 1 |
| 1 | 1 | 0 | | 0 |
| 1 | 1 | 1 | | 1 |

**Complete truth table for logic statement** (W21 V2)
4 marks for 8 correct outputs, 3 marks for 6/7 correct outputs, 2 marks for 4/5 correct outputs, 1 mark per 2/3 correct outputs.

| A | B | C | Working space | X |
|---|---|---|--------------|---|
| 0 | 0 | 0 | | 1 |
| 0 | 0 | 1 | | 1 |
| 0 | 1 | 0 | | 1 |
| 0 | 1 | 1 | | 1 |
| 1 | 0 | 0 | | 1 |
| 1 | 0 | 1 | | 1 |
| 1 | 1 | 0 | | 1 |
| 1 | 1 | 1 | | 0 |

**Complete truth table for logic statement** (W21 V3)
4 marks for 8 correct outputs, 3 marks for 6/7 correct outputs, 2 marks for 4/5 correct outputs, 1 mark per 2/3 correct outputs.

| A | B | C | Working space | X |
|---|---|---|--------------|---|
| 0 | 0 | 0 | | 1 |
| 0 | 0 | 1 | | 0 |
| 0 | 1 | 0 | | 1 |
| 0 | 1 | 1 | | 1 |
| 1 | 0 | 0 | | 1 |
| 1 | 0 | 1 | | 0 |
| 1 | 1 | 0 | | 1 |
| 1 | 1 | 1 | | 1 |

#### Logic Gates
**Identify three logic gates used in circuit** (S21 V3)
- AND
- NOR
- XOR

**State name and draw symbol of gate not in statement** (W21 V1)
One mark per logic gate name and one mark per correct drawing:
- NAND

[Logic gate symbol diagram required]

**Identify two logic gates not in statement** (W21 V2)
- NOR
- XOR / EOR

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