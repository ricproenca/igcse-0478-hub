# CAIE Computer Science IGCSE — Chapter 3: Hardware
### Advanced Notes

---

## 3.1 Computer Architecture

### Role of the CPU

At the heart of every computer is a Central Processing Unit (CPU) which processes instructions and data that are input into the computer so that the result can be output.

---

### Microprocessors

A microprocessor is a type of integrated circuit that contains the CPU (and sometimes other components) on a single chip.

---

### CPU Components

#### Units

| Unit | Function |
|------|----------|
| Arithmetic Logic Unit (ALU) | Performs mathematical calculations and logical operations as required. |
| Control Unit (CU) | The control unit marshals and controls the operation of the fetch-execute cycle, coordinating the operation of the CPU and sending commands to other components — for instance, requesting that the arithmetic logic unit perform a calculation. It also decodes instructions. |

#### Registers

Registers are fast-to-access storage locations, used to store small amounts of data needed temporarily by the CPU during processing.

| Register | Function |
|----------|----------|
| Program Counter (PC) | Stores the address of the next instruction to be fetched from memory. It increments during each fetch-execute cycle to point to the next instruction. |
| Memory Address Register (MAR) | Stores the address of the data to be fetched or the address where the data is to be stored. |
| Memory Data Register (MDR) | Stores the data that is being fetched from or written to memory. It acts as a buffer between main memory and the CPU. |
| Current Instruction Register (CIR) | Stores the instruction currently being decoded and executed by the CPU. When an instruction is fetched, it is copied from the MDR to the CIR prior to decoding. |
| Accumulator (ACC) | Stores the results of calculations or operations carried out by the Arithmetic Logic Unit (ALU). Also temporarily holds data being processed. |

> *Note: data is the actual value or instruction being stored, used, or processed whereas an address is a location in memory where data is stored.*

---

#### Buses

A bus is a collection of wires through which data/signals are transmitted from one component to another.

| Bus | Function |
|-----|----------|
| Address bus | Carries memory addresses from the CPU to other components, like RAM or input/output devices. |
| Data bus | Transmits the actual data or instructions between the CPU and other components. |
| Control bus | Sends control signals and timing information between the CPU and other components. |

The address bus is unidirectional, meaning data only flows from the CPU to other components. The data bus and control bus are bidirectional, allowing data to flow both to and from the CPU.

---

### Fetch-Decode-Execute Cycle

The FDE cycle is the process the CPU continuously performs to run programs, by fetching instructions from memory, decoding them, and executing them.

#### Fetch

- The Program Counter (PC) holds the memory address of the next instruction to be executed.
- This address is copied into the Memory Address Register (MAR).
- The address bus carries this address from the MAR to RAM.
- The instruction stored at that memory address is fetched from RAM and sent to the Memory Data Register (MDR) via the data bus.
- The Program Counter (PC) is then incremented so it points to the next instruction in the sequence.

#### Decode

- The instruction in the MDR is copied to the CIR.
- The Control Unit (CU) reads the instruction from the CIR.
- It decodes the instruction to understand what action is required.
- The CU then sends control signals via the control bus to the correct parts of the CPU (such as the ALU, ACC, or memory).

#### Execute

- The appropriate component of the CPU carries out the instruction:
  - If it's a calculation or logic operation, the Arithmetic Logic Unit (ALU) performs it.
  - If it's a data movement, the data is transferred between registers or between the CPU and memory.
- The result of any operation is usually stored in the Accumulator (ACC) or written back to RAM.
- The cycle then repeats for the next instruction.

---

### CPU Performance Factors

| Factor | Description |
|--------|-------------|
| Clock speed | The clock is a device that sends a regular electrical signal which switches between low and high voltage at a regular frequency. This signal is used to synchronise the computer system's components; it controls the number of instructions carried out each second. With every tick of the clock, the CPU fetches, decodes, and executes one instruction. The greater the clock speed, the faster the CPU can execute instructions, improving performance. |
| Cache size | Cache is a small, fast memory device located on the CPU that stores frequently used data and instructions. A larger cache increases the amount of frequently used data that can be stored. This reduces the need for the CPU to access slower main memory (RAM), improving performance. |
| Number of cores | Cores are the individual processing units within a CPU. A CPU with more cores can process more instructions at once allowing it to handle multiple tasks simultaneously, making it faster and improving performance. However, not all programs are designed to use multiple cores, so performance may not always improve. |

---

### Instruction Sets

An instruction set is a complete list of all the machine code instructions that a particular CPU can understand and execute. These instructions tell the CPU what operations to perform, such as loading data, storing data, or carrying out arithmetic and logical operations. The instruction set is built into the CPU's hardware and can vary between different types of processors. A CPU can only execute instructions that are part of its own instruction set.

---

### Embedded Systems

An embedded system is a computer system that is designed to perform specific, dedicated functions within a larger mechanical or electronic system. It is "embedded" into a device to control particular operations of that device. This is different to a general purpose computer that is used to perform many different functions. For example, a washing machine or smart-fridge would be an embedded system, whereas a laptop or PC would be a general purpose computer.

Characteristics of embedded systems include:

- Designed for one specific task or set of related tasks
- Built into other devices and cannot easily be separated
- Have minimal or no user interface
- Optimised for efficiency and reliability
- Typically low power, small, and efficient

#### Examples

- **Domestic appliances** — embedded systems can control temperature, timers, spin speed and safety features in devices like washing machines, dishwashers and fridges
- **Cars** — embedded systems can manage engine control, braking systems, airbag deployment and infotainment
- **Security systems** — embedded systems can detect motion, control alarms, manage cameras and lock or unlock doors
- **Lighting systems** — embedded systems can automate brightness, timing, and respond to motion or ambient light sensors
- **Vending machines** — embedded systems can manage user input, dispense products, process payments and monitor stock levels

---

## 3.2 Input and Output Devices

### Input Devices

An input device allows data to be entered into a computer system so it can be processed. These devices are essential for interacting with digital systems, feeding in commands, text, images, sound, or other forms of data.

| Input device | What it does | Why it does it | When it might be used |
|--------------|-------------|----------------|----------------------|
| **Barcode scanner** | Reads a barcode and converts it into digital data | To identify products quickly using a unique code | At supermarket checkouts or in stock control systems |
| **Digital camera** | Captures photographs or videos as digital files | To input images into a computer | In photography, video calls, facial recognition, or media creation |
| **Keyboard** | Inputs text, numbers and commands using keys | To allow a user to type data or control the computer | Writing documents, entering passwords, coding |
| **Microphone** | Captures analogue sound and converts it to a digital signal | To input voice or audio | Voice recognition, audio recording, video calls |
| **Optical mouse** | Detects movement and clicks to control a pointer on the screen | To navigate and interact with software | Selecting icons, dragging files, gaming |
| **QR code scanner** | Reads QR codes and converts them into readable data (e.g. URLs or payment info) | To quickly access information or complete tasks like payments | Advertisements, contactless menus, ticketing |
| **Touch screen (resistive)** | Registers touch using pressure on two layers | Allows input through touch – cheaper and can be used with gloves | ATMs, older smartphones |
| **Touch screen (capacitive)** | Registers touch using electrical properties of the finger | More responsive and accurate than resistive touchscreens | Modern smartphones, tablets |
| **Touch screen (infra-red)** | Uses a grid of infra-red beams to detect where the screen is touched | Durable and can detect any input object (e.g. finger, pen, stylus) | Industrial applications, public kiosks |
| **2D scanner** | Captures flat documents as digital image files | To digitise physical documents | Scanning passports, ID cards, or photos |
| **3D scanner** | Captures the shape and appearance of 3D objects to create digital models | To recreate real-world objects digitally | In gaming, medical imaging, engineering, or 3D printing |

---

### Output Devices

An output device is any hardware component that presents data from a computer to the user or another system — this could be in visual, audio, or physical form.

| Output device | What it does | Why it does it | When it might be used |
|---------------|-------------|----------------|----------------------|
| **Actuator** | Produces physical movement (e.g. turns a motor or opens a valve) | Converts digital signals into real-world physical actions | Automatic doors, robotic arms, smart thermostats |
| **Digital Light Processing (DLP) projector** | Projects images onto a surface using tiny mirrors and a light source | To display large, high-quality visuals from a computer | Presentations, home cinema, classroom teaching |
| **Inkjet printer** | Sprays tiny drops of ink onto paper to form text and images | To produce colour or black-and-white prints on paper | Home or office printing |
| **Laser printer** | Uses lasers and heat to fuse toner powder to the paper | Faster and more efficient than inkjet for high-volume printing | Business environments, schools |
| **Light Emitting Diode (LED) screen** | Displays images using light-emitting diodes | Brighter and more energy-efficient than LCD | TVs, monitors, advertising boards |
| **Liquid Crystal Display (LCD) projector** | Uses a light source and liquid crystal panels to project images | To present digital visuals to an audience | Offices, classrooms, cinemas |
| **Liquid Crystal Display (LCD) screen** | Displays images using liquid crystals and a backlight | For low-power visual output | Computer monitors, smartphones, tablets |
| **Speaker** | Converts digital audio signals into sound | To output sound such as music, voice, or alerts | Media players, alarms, communication apps |
| **3D printer** | Builds objects layer by layer using materials like plastic or resin | Turns digital models into physical 3D objects | Engineering, product design, medical prosthetics |

---

### Sensors

A sensor is a device that detects or measures a physical property and sends this data to a computer system for processing.

| Sensor type | What it does | Type of data captured | When it might be used |
|-------------|-------------|----------------------|----------------------|
| **Acoustic sensor** | Detects sound or vibrations | Sound level | Environmental monitoring, sonar |
| **Accelerometer** | Measures acceleration, movement, or tilt | Motion / orientation | Smartphones (auto-rotate), fitness trackers, gaming controllers |
| **Flow sensor** | Measures the flow rate of liquids or gases | Flow rate | Water/gas meters, medical devices |
| **Gas sensor** | Detects presence or concentration of gases | Gas levels | Air quality monitors, carbon monoxide alarms |
| **Humidity sensor** | Measures the amount of moisture in the air | Humidity level | Weather stations, smart homes, industrial environments |
| **Infra-red sensor** | Detects infrared radiation, often used to detect heat, motion or distance | IR radiation / proximity | TV remotes, motion detectors, thermometers |
| **Level sensor** | Measures the level of liquids or solids in a container | Fill level | Fuel tanks, reservoirs, industrial tanks |
| **Light sensor** | Measures light intensity | Light level | Automatic brightness adjustment, street lights |
| **Magnetic field sensor** | Detects magnetic fields or changes in magnetism | Magnetic field strength | Security systems, metal detectors, smartphones (compass) |
| **Moisture sensor** | Detects moisture content in soil or materials | Moisture level | Smart irrigation, agriculture, flood detection |
| **pH sensor** | Measures acidity or alkalinity | pH value | Water quality testing, chemical labs |
| **Pressure sensor** | Detects force applied by gases or liquids | Pressure level | Tyre pressure monitors, weather forecasting, medical devices |
| **Proximity sensor** | Detects when an object is near, without physical contact | Distance / presence | Phones (screen off when near ear), automatic doors |
| **Temperature sensor** | Measures how hot or cold something is | Temperature | Thermostats, computers (cooling), fridges |

---

*This work by PMT Education is licensed under CC BY-NC-ND 4.0*
