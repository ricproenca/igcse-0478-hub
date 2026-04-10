# Paper 1 Answers (2021)

This document contains marking scheme content for all 2021 Paper 1 exams, organized by syllabus structure.

---

## S21 V1

---

### Convert denary values from IP address to binary

**Answer:**
One mark per each correct register:

```
1     0    1     0     0    1        1        1

1     1    0     1     0    1        1        0
```

---

### Identify similarity between IP and MAC address

**Answer:**
Any one from:
- Both addresses can be used to identify a computer/device
- Both are unique
- Both can be represented as hexadecimal
- Both addresses do not change if IP address is static

---

### Identify two differences between IP and MAC address

**Answer:**
Any two from:
- An IP address is assigned by the network/router/ISP, A MAC address is assigned by the manufacturer
- An IP address can be changed (if dynamic), MAC address cannot be changed
- IP address has 4/8 groups of values, MAC address has 6 groups/pairs of values
- IP address is 32-bit/128-bit, MAC address is 48-bit
- IP address does not contain serial number/manufacturer number, MAC address does
- IP(v4) address is denary and MAC address is hexadecimal

---

### Identify three devices to input personal data

**Answer:**
Any three from:
- Keyboard
- Mouse
- Microphone
- Keypad
- Touchscreen
- Touchpad

---

### Complete table about HDD, SSD, USB characteristics

**Answer:**
One mark for each correct row.

| Statement | HDD (✓) | SSD (✓) | USB flash memory (✓) |
|-----------|---------|---------|---------------------|
| it has no moving parts | ✓ | ✓ | ✓ |
| it is non-volatile | ✓ | ✓ | ✓ |
| it can use NAND gates to store data | | ✓ | ✓ |
| it uses magnetic properties to store data | ✓ | | |
| it has the smallest physical size | | ✓ | ✓ |
| it has the slowest read/write speeds | ✓ | | |

---

### State two benefits of USB connection

**Answer:**
Any two from:
- It cannot be inserted incorrectly
- Supports different transmission speeds
- High speed transmission
- Automatically detected (not connected) // automatically downloads drivers
- Powers the device (for data transfer)
- Backward compatible

---

### Identify type of data transmission in USB

**Answer:**
- Serial

---

### Complete paragraph about firewall operation

**Answer:**
One mark per each correct term in the correct order:
- Software
- Network
- Criteria
- Accept // reject
- Reject // accept
- Hacking

---

### Identify three other methods to keep data secure

**Answer:**
Any three from:
- Password
- Biometrics (device)
- Encryption
- Physical methods (e.g. locks)
- Two-factor authentication // Two-step verification
- Anti-viruses

---

### Describe what is meant by phishing and pharming

**Answer:**
Any six from:

**Phishing:**
- Legitimate looking email sent to user
- encourages user to click a link that directs user to a fake website
- User encouraged to enter personal details into a fake website // designed to obtain personal details from a user

**Pharming:**
- Malicious code/malware is downloaded/installed // software downloaded without users' knowledge
- … that re-directs user to fake website (when legitimate URL entered)
- User encouraged to enter personal details into a fake website // designed to obtain personal details from a user

---

### Describe how temperature sensor and microprocessor maintain greenhouse temperature

**Answer:**
Eight from:
- Sensor send data/readings/signal to microprocessor
- Data is converted from analogue to digital (using ADC)
- Microprocessor compares/checks data to stored values/range of values …
- … If data is greater than 30 / above the range microprocessor sends signal to open window and to turn heater off
- … If data is below 25 the microprocessor sends signal to turn on heater and to close window
- … If data is between 25 and 30 / within the range no action taken
- Actuator is used to operate heater/window
- Whole process is continuous

---

### Draw logic circuit for given logic statement

**Answer:**
One mark per each correct logic gate, with correct input:

[Logic circuit diagram required]

---

### Identify four errors in truth table

**Answer:**
- Row 1
- Row 3
- Row 4
- Row 5

---

### Describe how sound files are compressed using lossless compression

**Answer:**
Four from:
- (Compression) algorithm is used
- No data will be removed // original file can be restored
- Example of type of algorithm that would be used e.g. RLE
- Repeated patterns in the music are identified
- … and indexed

NOTE: If another lossless method is described, marks can be awarded.

---

### State reason for using lossless compression

**Answer:**
Any one from:
- To provide the highest quality of music file (that compression will allow)
- The user is able to listen to the original sound file
- No loss of quality for the sound file provided

---

### Give benefit of compressing sound files

**Answer:**
Any one from:
- Allow for quicker streaming speed
- Would not require as much bandwidth (to stream)
- Does not need as much RAM
- Smoother listening experience // less lag
- Will not use as much of data allowance

---

### Give drawback of lossless vs lossy compression

**Answer:**
Two from:
- Streaming speed may be slower
- … and may affect listening experience // buffering may occur
- User may need more bandwidth to stream
- … that could be more expensive
- It would be a larger file size
- … so may take longer to upload
- … so will take up more storage space …
- … on webserver

---

### Describe how web pages are requested and displayed

**Answer:**
Any four from:
- Browser sends URL to DNS
- … using HTTP/HTTPS
- IP address is found on DNS
- DNS returns IP address to the browser
- Browser sends request to web server/IP address
- Web server sends web pages back to browser
- Browser interprets/renders the HTML (to display web pages)
- Security certificates exchanged

---

### Explain why DoS attack prevents website access

**Answer:**
Two from:
- Web server has been flooded with traffic // web server has been sent many requests at once
- … so, server is brought to a halt / crashes

---

### Identify whether odd or even parity for each binary value

**Answer:**
- Odd
- Odd
- Even
- Even

---

### Identify why parity check may not detect error

**Answer:**
Any one from:
- there is a transposition of bits
- it does not check the order of the bits (just the sum of 1s/0s)
- even number of bits change
- incorrect bits still add up to correct parity

---

### Describe how data is sent using parallel half-duplex

**Answer:**
Four from:
- Multiple bits are sent at the same time
- Uses multiple wires
- Data is sent in both directions …
- … but only one direction at a time

---

### State two drawbacks of parallel transmission

**Answer:**
Any two from:
- Bits may arrive skewed
- More expensive to setup/manufacture/purchase cable
- Limited distance
- More prone to interference/error

---

## S21 V2

---

### Complete table with hexadecimal and binary values

**Answer:**
One mark per each correct binary value. One mark per each correct hex value.

| Denary | Hexadecimal | 8-bit binary |
|--------|-------------|--------------|
| 49 | 31 | 00110001 |
| 123 | 7B | 01111011 |
| 200 | C8 | 11001000 |

---

### Give two benefits of converting binary to hexadecimal

**Answer:**
Any two from:
- Easier/quicker to read/write/understand
- Easier/quicker to identify errors/debug
- Takes up less screen/display space
- Less chance of making an error

---

### Identify three other uses of hexadecimal

**Answer:**
Any three from:
- MAC address
- URL
- Assembly language
- Error codes // error messages
- IP addresses
- Locations in memory
- Memory dumps

---

### Complete table about magnetic, solid-state, optical storage

**Answer:**
One mark per each correct row.

| Statement | Magnetic (✓) | Solid state (✓) | Optical (✓) |
|-----------|-------------|-----------------|-------------|
| no moving parts are used to store data | | ✓ | |
| pits and lands are used to store data | | | ✓ |
| data is stored on platters | ✓ | | |
| flash memory is used to store data | | ✓ | |
| parts are rotated to store data | ✓ | | ✓ |
| data can be stored permanently | ✓ | ✓ | ✓ |

---

### Give example of magnetic storage

**Answer:**
Any one from:
- Hard disk drive // HDD
- Magnetic tape

---

### Give example of optical storage

**Answer:**
Any one from:
- CD
- DVD
- Blu-ray disk

---

### Identify storage type for web server and justify

**Answer:**
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

---

### Describe operation of USB flash memory

**Answer:**
Any three from:
- Data is flashed onto (silicon) chips
- Uses NAND/NOR technology // can use flip-flops
- Uses transistors/control gates/floating gates …
- … to control the flow of electrons
- It is a type of EEPROM technology
- When data is stored the transistor is converted from 1 to 0 / 0 to 1
- Writes (and reads) sequentially

---

### Draw logic circuit for given logic statement

**Answer:**
One mark for each correct logic gate with correct input.

[Logic circuit diagram required]

---

### Identify four errors in truth table

**Answer:**
One mark per each correct row:
- Row 2
- Row 3
- Row 7
- Row 8

---

### Complete table about virus, spyware, DoS attack

**Answer:**
One mark per each correct row.

| Statement | Virus (✓) | Spyware (✓) | Denial of service (✓) |
|-----------|-----------|-------------|----------------------|
| captures all data entered using a keyboard | | ✓ | |
| can be installed onto a web server | ✓ | ✓ | |
| prevents access to a website | | | ✓ |
| is malicious code on a computer | ✓ | ✓ | |
| is self-replicating | ✓ | | |
| damages the files on a user's hard drive | ✓ | | |

---

### Identify three other Internet security risks

**Answer:**
Any three from:
- Phishing
- Pharming
- Hacking // cracking

---

### State three ways data could be accidentally damaged

**Answer:**
Any three from:
- Human error
- Power failure/surge
- Hardware failure
- Software failure
- Fire
- Flood

---

### Identify two sensors for security light system

**Answer:**
- Light sensor
- Motion sensor // infra-red sensor

---

### Describe how sensors and microprocessor control security light

**Answer:**
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

---

### Describe how cookies store and auto-enter payment details

**Answer:**
Any three from:
- Webserver sends (cookie) file to user's browser
- User's payment details stored in encrypted text file // data is encrypted to be stored
- Cookie file is stored by browser/on user's HDD/SSD
- When user revisits website, webserver requests cookie file // webserver can access the data stored in the cookie file (to automatically enter details)
- … and browser sends cookie file back to webserver (to automatically enter the details)

---

### Explain why users may be concerned about cookies

**Answer:**
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

### Give example of HTML structure

**Answer:**
Any one from:
- Placement of text/image
- Margins
- Line break
- Padding

NOTE: Any relevant example of structure can be awarded

---

### Give two examples of HTML presentation

**Answer:**
Any two from:
- Font colour
- Font style
- Font size
- Background colour
- Image size
- Border properties

NOTE: Any relevant example of presentation can be awarded

---

### Explain why HTML is separated into structure and presentation

**Answer:**
Any two from:
- Can easily change/edit the style of the webpage
- So, CSS can be used to create a template/style sheet
- Can add new content and apply the same style easily
- Can re-use the presentation/style for other websites

---

### Complete paragraph about keyboard operation

**Answer:**
One mark for each correct term in the correct order:
- Switch
- Circuit
- Current
- Calculated
- Character
- Binary

---

## S21 V3

---

### Identify who assigns MAC address

**Answer:**
- manufacturer

---

### Convert three hexadecimal values to binary

**Answer:**
One mark per each correct binary value:
- 00010100
- 10100000
- 11001001

---

### Convert two hexadecimal values to denary

**Answer:**
One mark per each correct denary value:
- 41
- 200

---

### Identify storage type for each device

**Answer:**
- Magnetic
- Solid state
- Optical

---

### Describe operation of HDD and how it stores data

**Answer:**
Any four from:
- It has platters
- Platters/disk divided into tracks
- Platter/disk is spun
- Has a read/write arm that moves across storage media
- Read/writes data using electromagnets
- Uses magnetic fields to control magnetic dots of data
- Magnetic field determines binary value

---

### Describe how lossy compression reduces video file size

**Answer:**
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

---

### Give two reasons for using lossy compression

**Answer:**
Any two from:
- Lossy decreases the file size more
- Take up less storage space on webserver/users' computer
- Quicker to upload/download
- May not need to be high quality
- Website will load faster for users
- Less lag/buffering when watching
- Takes up less bandwidth to download/upload
- Uses less data allowance

---

### Complete paragraph about optical mouse operation

**Answer:**
One mark per each correct term, in the correct place:
- LED
- Photoelectric
- Lens
- Magnifies
- Microswitch
- USB

---

### Identify two other input devices

**Answer:**
Any two from:
- Keyboard
- Microphone
- 2D/3D Scanner
- Sensor
- Touchscreen
- Keypad
- Webcam
- Joystick

---

### Explain how personal details were obtained using phishing

**Answer:**
- Legitimate looking/fake email sent to user
- … that contains a link to a fake website
- User clicks link and enters personal details (into fake website)

---

### Give two other Internet security risks

**Answer:**
Any two from:
- Pharming
- Spyware
- Hacking/cracking

---

### Complete table about programming language types

**Answer:**
One mark per each correct row.

| Statement | High-level language (✓) | Assembly language (✓) | Machine code (✓) |
|-----------|------------------------|----------------------|------------------|
| It requires a translator to be processed by a computer | ✓ | ✓ | |
| It is an example of low-level language | | ✓ | ✓ |
| It uses mnemonics | | ✓ | |
| It uses English-like statements | ✓ | | |
| It can be used to directly manipulate hardware in the computer | | ✓ | ✓ |
| It is portable | ✓ | | |

---

### Identify odd or even parity for each binary value

**Answer:**
- Odd
- Even
- Even
- Odd

---

### State why parity check does not identify error

**Answer:**
Any one from:
- There is a transposition of bits
- Bits still add up to correct parity

---

### Describe how data is sent using serial duplex

**Answer:**
- Data is sent one bit at a time
- Data is sent using a single wire
- Data is sent in both direction …
- … at the same time

---

### State drawback of serial transmission

**Answer:**
Any one from:
- Data transmission can be slower (than parallel)
- Additional data may need to be sent

---

### Identify two ways data can be accidentally damaged

**Answer:**
Any two from:
- Hardware failure
- Software failure
- Power failure/surge
- Fire
- Flood
- Natural disaster

---

### Give two ways to prevent accidental data damage

**Answer:**
Any two from:
- Use verification methods before deleting files
- Keep data in a fireproof box
- Do not drink liquids near a computer
- Use surge protection // UPS
- Correct shutdown procedures
- Access rights
- Back data up

---

### Identify three logic gates used in circuit

**Answer:**
- AND
- NOR
- XOR

---

### Identify four errors in truth table

**Answer:**
- Row 1
- Row 4
- Row 7
- Row 8

---

### Complete table with suitable sensors for each task

**Answer:**
One mark per each correct sensor.

| Task | Sensor |
|------|--------|
| Check if a vehicle is too high | Infrared/light |
| Count the vehicles entering the car park | Magnetic field // pressure |
| Check if a vehicle is parked in a parking space | Pressure // magnetic field // infrared/light |

---

### Describe how sensor and microprocessor display red or green light

**Answer:**
Six from:
- Sensor sends data to microprocessor
- Data is converted from analogue to digital (using ADC)
- Data is compared to stored value …
- … If data is greater than stored value microprocessor sends signal to turn red light on and the green light off
- … If data is less than stored value microprocessor sends signal to turn green light on the red light off
- … If data still within range, no action taken/existing light remains on
- Lights turned on/off using actuator
- Process is continuous

---

### Complete table about ALU, CU, RAM components

**Answer:**
One mark per each correct row.

| Statement | ALU (✓) | CU (✓) | RAM (✓) |
|-----------|---------|--------|---------|
| Stores data and instructions before they enter the central processing unit (CPU) | | | ✓ |
| Contains a register called the accumulator | ✓ | | |
| Manages the transmission of data and instructions to the correct components | | ✓ | |
| Contained within the CPU | ✓ | ✓ | |
| Uses the data bus to send data into or out of the CPU | ✓ | | ✓ |
| Carries out calculations on data | ✓ | | |

---

### Give two other registers in Von Neumann model

**Answer:**
Any two from:
- MAR
- MDR // MBR
- PC
- CIR // IR

---

## W21 V1

---

### Identify base of binary number system

**Answer:**
- Base-2

---

### Convert four hexadecimal values to denary

**Answer:**
- 9
- 16
- 40
- 161

---

### Identify other input device for mobile phone

**Answer:**
- Microphone

---

### State touchscreen technology type

**Answer:**
- capacitive

---

### Give name of signal that stops music for call

**Answer:**
- interrupt

---

### Complete table about checksum, check digit, parity

**Answer:**
One mark per each correct row.

| Statement | Checksum (✓) | Check digit (✓) | Parity check (✓) |
|-----------|-------------|-----------------|------------------|
| uses an additional bit to create an odd or even number of 1s | | | ✓ |
| checks for errors on data entry | | ✓ | |
| compares two calculated values to see if an error has occurred | ✓ | ✓ | |
| will not detect transposition errors | | | ✓ |
| sends additional values when data is transmitted from one computer to another | ✓ | | ✓ |

---

### Identify one other error-checking method

**Answer:**
- ARQ

---

### Calculate total file size of photographs

**Answer:**
Two marks for any two correct workings and one mark for the correct answer.

Working:
- 100 × 50 = 5000 bits
- 5000 × 8 = 40,000 bits
- 40,000 / 8 = 5,000 bytes
- 5,000 × 10 = 50,000 bytes
- 50,000 / 1024

Answer:
48.83 kB // 49 kB

NOTE: Alternative correct methods of working can be credited. Answer can be given to any number of dp.

---

### State compression type and justify choice

**Answer:**
One mark per correct method, two marks per justification:
- Lossless
- Lossy would remove data permanently // lossless would not remove any data permanently // File could be restored to original …
- … that could affect the quality (lossy) // … to maintain the quality (lossless)

---

### Complete paragraph about digital camera operation

**Answer:**
- Light
- Lens
- Charge-coupled
- Analogue-to-digital
- Pixel

---

### State two software security methods

**Answer:**
Any two from:
- Encryption
- Biometric device
- Firewall
- Anti-spyware
- Two-factor authentication // two-step verification

---

### State two other functions of operating system

**Answer:**
Any two from:
- Interrupt / error-handling
- Peripheral management
- Providing user interface
- Platform for running applications // installing / removing software
- Manages security // access rights/levels // user account management
- Managing time slicing // multitasking

---

### Complete table about MAR, MDR, PC registers

**Answer:**
One mark per each correct row.

| Statement | MAR (✓) | MDR (✓) | PC (✓) |
|-----------|---------|---------|--------|
| it is a register in the CPU | ✓ | ✓ | ✓ |
| it holds the address of the next instruction to be processed | ✓ | | ✓ |
| it holds the address of the data that is about to be fetched from memory | ✓ | | ✓ |
| it holds the data that has been fetched from memory | | ✓ | |
| it receives signals from the control unit | ✓ | ✓ | ✓ |
| it uses the address bus to send an address to another component | ✓ | | ✓ |

---

### Identify component that carries out calculations

**Answer:**
- Arithmetic Logic Unit // ALU

---

### Classify internal SSD and justify choice

**Answer:**
One mark per correct storage, two marks for justification:
- Secondary
- It is non-volatile storage
- It is not directly accessed by the CPU

---

### Describe operation of SSD and how it stores data

**Answer:**
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

### State type of programming language used

**Answer:**
- High-level

---

### Identify translator during development and benefits

**Answer:**
One mark for the correct translator, two marks for the benefit(s):
- Interpreter
- Easier to debug
- … as errors are immediately reported when detected

**Alternative:**
- Compiler
- All errors are reported in a single report
- … meaning they can all be fixed at the same time
- No need to recompile code every time a test is run

---

### Identify translator for final program and benefits

**Answer:**
One mark for the correct translator, two marks for the benefits:
- Compiler
- Creates an executable file
- … so, translator is no longer needed to run it
- Source code cannot be stolen // can be provided without the source code

---

### Identify suitable sensor for each washing machine task

**Answer:**
One mark per each correct sensor.

| Task | Sensor |
|------|--------|
| checking the water is 30 °C | Temperature |
| checking the water acidity level after detergent is added | pH |
| checking the weight of the clothes to make sure that the machine is not overloaded | Pressure |

---

### Describe how sensor and microprocessor maintain water temperature

**Answer:**
Six from:
- Sensor sends data to microprocessor
- Data is converted from analogue to digital (using ADC)
- Data is compared to stored value (of 30)
- If data is below 30 then a microprocessor sends signal is sent to a heater to heat the water up/add hot water
- If data is above 30 then a microprocessor sends signal is sent to turn the heater off to allow the water to cool down/add cold water
- Actuator used to turn heater on/off // Actuator used to add water
- If data is 30 then no action is taken
- It is a continuous process

---

### Draw logic circuit for given logic statement

**Answer:**
One mark per each correct logic gate with the correct input(s).

[Logic circuit diagram required]

---

### State name and draw symbol of gate not in statement

**Answer:**
One mark per logic gate name and one mark per correct drawing:
- NAND

[Logic gate symbol diagram required]

---

### Complete truth table for logic statement

**Answer:**
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

---

### Complete table with web page and Internet terms

**Answer:**
One mark per each correct term.

| Terms | Description |
|-------|-------------|
| HTML | the language used to create a web page |
| Browser | the type of software application used to display a web page |
| IP address | an address given to a computer, by a network, to allow the computer to be uniquely identified |
| Cookie | a text file sent by a web server to collect data about a user's browsing habits |
| Internet Service Provider // ISP | the company that provides a connection to the Internet |

---

## W21 V2

---

### Identify base of denary number system

**Answer:**
- Base-10

---

### Convert four hexadecimal values to denary

**Answer:**
- 5
- 32
- 26
- 171

---

### Identify correct binary for hexadecimal 25

**Answer:**
- 00100101

---

### Identify correct binary for hexadecimal 1B

**Answer:**
- 00011011

---

### Give use of hexadecimal in website development

**Answer:**
Any one from:
- To represent HTML colour codes
- In error messages

---

### Give use of hexadecimal in low-level programming

**Answer:**
Any one from:
- Assembly code/language
- Memory address locations
- In error messages
- Memory dump

---

### Identify output device for ticket machine

**Answer:**
Any one from:
- Printer
- Speaker
- Light/LED
- Actuator

---

### Identify input device for ticket machine

**Answer:**
Any one from:
- Touchscreen
- Trackpad / touchpad
- Microphone
- QR code reader
- Barcode reader
- Magnetic strip reader
- RFID reader

---

### Complete table about serial/parallel transmission

**Answer:**
One mark per each correct row.

| Statement | Serial simplex (✓) | Parallel simplex (✓) | Parallel half-duplex (✓) | Serial duplex (✓) |
|-----------|-------------------|---------------------|------------------------|------------------|
| bits are transmitted along a single wire | ✓ | | | ✓ |
| data is transmitted in both directions | | | ✓ | ✓ |
| it is only suitable for distances less than 5 metres | | ✓ | ✓ | |
| Bits from the same byte are transmitted one after the other | ✓ | | | ✓ |
| data may not arrive in the correct sequence | | ✓ | ✓ | |
| data is transmitted in both directions, but only one direction at a time | | | ✓ | |

---

### Give three benefits of USB connection

**Answer:**
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

### Complete paragraph about capacitive and resistive touchscreens

**Answer:**
One mark per each correct term in the correct order:
- Capacitive
- Conductive // Capacitive
- Change
- Coordinates
- Resistive
- Circuit
- Manufacture

---

### Identify three methods to prevent data viewing

**Answer:**
Any three from:
- Password
- Add a biometric device to the laptop // set biometric password
- Use two-step verification // Use two factor authentication
- Physically lock the laptop away in a secure cupboard // Taking laptop with him at all times

---

### Give three ways lossy compression reduces video size

**Answer:**
Any three from:
- A compression algorithm is used
- The resolution could be reduced
- Colour depth could be reduced // bits per pixel reduced
- Sounds not heard by human ear could be removed // Perceptual music shaping can be used
- Repeating frames could be removed

---

### Give drawback of using lossy compression

**Answer:**
Any one from:
- Quality may be reduced
- Data is lost // original file cannot be reconstructed

---

### Give reason for using lossless compression

**Answer:**
Any one from:
- Maintains quality // quality better than lossy
- Original file is retained // Data is not permanently lost
- A significant reduction in file size is not required

---

### Give two disadvantages of lossless compression

**Answer:**
Any two from:
- Takes more time to transmit file // Takes more time to upload to web server // Takes more time to download to customer // Web page will load slower
- Takes up more storage space
- Data usage would be increased
- Uses more bandwidth

---

### Give one similarity between compiler and interpreter

**Answer:**
Any one from:
- They both translate high-level language into machine code / low-level language
- They both check for errors
- They both report errors

---

### Describe two differences between compiler and interpreter

**Answer:**
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

---

### Identify one other type of translator

**Answer:**
- Assembler

---

### Complete table about 3D scanner, barcode, QR code

**Answer:**
One mark per each correct row.

| Statement | 3D scanner (✓) | Barcode reader (✓) | QR code reader (✓) |
|-----------|----------------|-------------------|-------------------|
| uses position and alignment markers for orientation when scanning | | | ✓ |
| scans the shape and appearance of an object | ✓ | | |
| uses reflected light from a laser to convert a black-and-white pattern into binary | | ✓ | ✓ |
| can often be built into an Electronic Point Of Sale (EPOS) terminal, for example, a supermarket checkout | | ✓ | ✓ |
| it is an example of an input device | ✓ | ✓ | ✓ |

---

### Explain how sensors and microprocessor count correct mat hits

**Answer:**
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

### Give three examples of when interrupt signal generated

**Answer:**
Any three from (e.g.):
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

NOTE: If three suitable different errors are described, this can be awarded three marks.

---

### State what happens without interrupt signals

**Answer:**
Any one from:
- The computer would only start a new task when it had finished processing the current task // by example
- Computer will not be able to multitask
- Errors may not be dealt with
- Computer would become impossible to use

---

### Explain how SSL protocol secures data transmission

**Answer:**
- Enables an encrypted link (between the browser and the web server) // It encrypts the data
- … based on the authentication of an (SSL) certificate // and will only send it if the certificate is authentic

---

### Identify alternative to SSL protocol

**Answer:**
- Transport Layer Security // TLS

---

### Give two ways to identify if website uses secure transmission

**Answer:**
Any two from:
- URL begins with HTTPS
- Padlock symbol is locked
- Check the certificate is valid

---

### Draw logic circuit for given logic statement

**Answer:**
One mark per each correct logic gate with correct input(s).

[Logic circuit diagram required]

---

### Complete truth table for logic statement

**Answer:**
4 marks for 8 correct outputs, 3 marks for 6/7 correct outputs, 2 marks for 4/5 correct outputs, 1 mark for 2/3 correct outputs.

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

---

### Identify two logic gates not in statement

**Answer:**
- NOR
- XOR / EOR

---

## W21 V3

---

### Identify largest file size

**Answer:**
One mark for the correct tick:

| File Size | Tick (✓) |
|-----------|----------|
| 999 kB | |
| 1 MB | ✓ |
| 850 000 bytes | |

---

### Identify smallest file size

**Answer:**
One mark for the correct tick:

| File Size | Tick (✓) |
|-----------|----------|
| 4000 MB | |
| 2 GB | ✓ |
| 2 500 000 kB | |

---

### Give binary value for denary display value

**Answer:**
One mark for correct binary value, one mark for leading zeros:
00000000 01000111

---

### Give binary value for updated display value

**Answer:**
One mark for leading zeros, one mark for correct binary value:
00000001 00000001

---

### Give denary display for binary value

**Answer:**
- 0516

---

### Identify two sensors for counting people

**Answer:**
- Pressure sensor
- Motion sensor

---

### Identify if sensor is input, storage, or output device

**Answer:**
One mark for the correct tick:

| Device | Tick (✓) |
|--------|----------|
| input | ✓ |
| storage | |
| output | |

---

### Complete table about ARQ, check digit, checksum

**Answer:**
One mark per each row:

| Statement | ARQ (✓) | Check digit (✓) | Checksum (✓) |
|-----------|---------|-----------------|--------------|
| checks for errors on data entry | | ✓ | |
| uses a process of acknowledgement and timeout | ✓ | | |
| compares two calculated values to see if an error has occurred | | ✓ | ✓ |
| may resend data until it is confirmed as received | ✓ | | |
| checks for errors in data after transmission from a computer to another | | | ✓ |

---

### Identify one other error-checking method

**Answer:**
- Parity check

---

### Describe role of interrupt in generating paper jam message

**Answer:**
Any four from:
- Printer generates interrupt
- Interrupt is given a priority
- Interrupt is queued
- Interrupt stops CPU from processing current task
- CPU will service interrupt // Interrupt handler services interrupt …
- … generating an output message to state there is a paper jam

---

### Give two other examples of interrupt signals

**Answer:**
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

NOTE: If two suitable different errors are described, this can be awarded two marks.

---

### Describe how data is sent using serial half-duplex

**Answer:**
Four from:
- Bits sent one at a time
- … down a single wire
- Data sent in both directions …
- … but only one direction at a time

---

### Explain why half-duplex needed instead of simplex

**Answer:**
Any two from:
- Simplex only sends data in one direction
- … so, printer may not be able to tell computer an error has occurred, and computer may not be able to send printer the document to be printed

NOTE: Award any valid contextual answer for MP2

---

### Complete table about Von Neumann components

**Answer:**
One mark per correct term or description.

| Component name | Description |
|----------------|-------------|
| Memory Address Register (MAR) | (A register that) holds the address of the data/instruction that needs to be fetched/processed // holds the address of where the data needs to be stored. |
| Program Counter (PC) | (A register that) holds the address of the next / current instruction to be processed. |
| Accumulator // ACC | This is a register that is built into the arithmetic logic unit. It temporary holds the result of a calculation. |
| Memory Data Register // MDR | This is a register that holds data or an instruction that has been fetched from memory. |
| Control Unit (CU) | Sends control signals to control the flow of data through the CPU // manages the execution of instructions in the CPU |
| Address bus | This carries addresses around the CPU. |

---

### Complete paragraph about MP3, MP4, MIDI files

**Answer:**
One mark per correct term in the correct order:
- MP4
- MP3
- Microphone
- Compressed
- MIDI
- Notes
- Can

---

### Explain why compiler used instead of interpreter

**Answer:**
Any four from:
- Creates an executable file
- … so, would not release source code
- … so, the source code cannot be stolen/edited.
- … so, would not need to be translated every time // so, translator is not required
- … making it machine independent

---

### Describe how lossless compression reduces file size

**Answer:**
Any three from:
- Compression algorithm used
- …, e.g. RLE
- Repeating frames/pixels are identified
- … and are collated/indexed
- No data is permanently removed
- It just records the changes between frames/pixels

---

### State reason for using lossless compression

**Answer:**
Any one from:
- Maintains quality // quality better than lossy
- Original file is retained // Data is not permanently lost
- A significant reduction in file size is not required

---

### Describe freeware and free software

**Answer:**
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

---

### Identify type of software for trial version

**Answer:**
- Distribute as shareware

---

### Give two ways to identify if website uses secure transmission

**Answer:**
Any two from:
- URL begins with HTTPS
- Padlock symbol is locked

---

### Draw logic circuit for given logic statement

**Answer:**
One mark per each correct logic gate with correct inputs.

[Logic circuit diagram required]

---

### Complete truth table for logic statement

**Answer:**
4 marks for 8 correct outputs, 3 marks for 6/7 correct outputs, 2 marks for 4/5 correct outputs, 1 mark for 2/3 correct outputs.

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

---

### Identify odd or even parity for each binary value

**Answer:**
- Even
- Even
- Odd
- Even

---

### State purpose of denial of service attack

**Answer:**
- To disrupt the operation of a web server/network

---

### State purpose of phishing and pharming

**Answer:**
- To obtain a user's personal data

---

### Identify three other Internet security risks

**Answer:**
Any three from:
- Hacking // Cracking
- Virus
- Spyware
- Malware

---

(End of file)
