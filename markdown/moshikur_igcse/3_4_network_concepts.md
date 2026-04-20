# 3.4 Network Concepts

> Source: https://moshikur.com/igcse-o-level-cs/chapter-3-hardware/3-4-network-concepts/

# 3.4 Network Concepts

---

>> Syllabus

## 3.4 Network Hardware

**3.4.1 Network Interface Card (NIC)**

- 3.4.1.1 Understand that a computer needs a NIC to access a network.

**3.4.2 Media Access Control (MAC) Address**

- 3.4.2.1 Understand what is meant by a MAC address.
- 3.4.2.2 Understand the purpose of a MAC address.
- 3.4.2.3 Understand the structure of a MAC address.
- 3.4.2.4 Know that MAC addresses are usually written in hexadecimal.
- 3.4.2.5 Know that MAC addresses are created using the manufacturer code and the serial code.

**3.4.3 Internet Protocol (IP) Address**

- 3.4.3.1 Understand what is meant by an IP address.
- 3.4.3.2 Understand the purpose of an IP address.
- 3.4.3.3 Understand that there are different types of IP address.
- 3.4.3.4 Understand the difference between static and dynamic IP addresses.
- 3.4.3.5 Understand the characteristics of IPv4 addresses.
- 3.4.3.6 Understand the characteristics of IPv6 addresses.
- 3.4.3.7 Identify the differences between IPv4 and IPv6.

**3.4.4 Router**

- 3.4.4.1 Describe the role of a router in a network.
- 3.4.4.2 Understand that a router sends data to a specific destination on a network.
- 3.4.4.3 Understand that a router can assign IP addresses.
- 3.4.4.4 Understand that a router can connect a local network to the internet.

---

## **3.4 Network Hardware**

[![Illustration of network hardware components including a Network Interface Card (NIC), Media Access Control (MAC) address, Internet Protocol (IP) addresses, and a router.](images/topic3_hardware/3_4_network_concepts/img_001.png)](https://i0.wp.com/moshikur.com/wp-content/uploads/2025/09/image-63.png?ssl=1)

---

# 3.4.1 Network Interface Card (NIC)

---

[![Illustration of a Network Interface Card (NIC) depicting its structure and design, with a label 'NIC' and a website at the bottom.](images/topic3_hardware/3_4_network_concepts/img_002.png)](https://i0.wp.com/moshikur.com/wp-content/uploads/2025/09/image-65.png?ssl=1)

### What is a Network Interface Card (NIC)?

A Network Interface Card (NIC) is a piece of **hardware inside a computer or device** that allows it to connect to a network. Without a NIC, a computer cannot communicate with other devices on the same network or access the internet.

---

### Key Features of a NIC

- Acts as the **connection point** between the computer and the network.
- Can be **wired (Ethernet)** or **wireless (Wi-Fi)**.
- Each NIC is given a **unique MAC address** at the point of manufacture.
- Installed as part of the computer’s motherboard or as a separate expansion card.

---

### Purpose of a NIC

- Enables a device to **send and receive data** across a network.
- Ensures that data is formatted and transmitted correctly.
- Identifies the device on the network using its MAC address.

---

### Why is a NIC Important?

- Without a NIC, devices could not connect to each other or to the internet.
- Provides the foundation for all types of networking, including home, school, and business networks.
- Supports both **local area networks (LANs)** and wider networks like the internet.

---

### Example Uses of NICs

- Connecting a desktop computer to a home router.
- Allowing a laptop to connect wirelessly to Wi-Fi.
- Enabling servers to connect to multiple networks at once.

---

[![Illustration of a Network Interface Card (NIC) and components related to a MAC address, featuring the MAC address '3A:7B:9C:00:5F:2D' and a computer connected to a network.](images/topic3_hardware/3_4_network_concepts/img_003.png)](https://i0.wp.com/moshikur.com/wp-content/uploads/2025/09/image-64.png?ssl=1)

### What is a MAC Address?

A **Media Access Control (MAC) address** is a unique identifier given to every **Network Interface Card (NIC)** when it is manufactured.

It is a **hardware address** that is permanently stored on the device and used to identify it on a network.

### Key Points to Understand

- A MAC address is written in **hexadecimal** (base 16).
- It consists of **12 hexadecimal digits**, usually grouped into 6 pairs (e.g., `A1:B2:C3:D4:E5:F6`).
- It is created using two parts:
  1. **Manufacturer code** – identifies who made the NIC.
  2. **Serial code** – unique to that specific device.

---

### Why It Matters

- A MAC address ensures that **no two devices on a network have the same hardware identifier**.
- It is the **first level of identification** in networking, allowing devices to be distinguished before IP addresses are used.

---

### Purpose of a MAC Address

The main purpose of a **Media Access Control (MAC) address** is to provide a **unique identifier** for every device on a network. This ensures that data sent across the network reaches the **correct destination device**.

---

### Key Points About Its Purpose

1. **Device Identification**
   - Each MAC address is unique to a device’s Network Interface Card (NIC).
   - It ensures that data is delivered to the correct computer, printer, or mobile device.
2. **Data Transmission**
   - When data is sent over a local network, it includes the MAC address of the destination device.
   - The network uses this to decide where to deliver the data.
3. **Network Security**
   - Networks can use **MAC filtering** to control which devices are allowed to connect.
   - This helps protect against unauthorised access.
4. **Hardware-Level Address**
   - Unlike IP addresses (which can change), the MAC address is fixed and tied to the hardware.
   - This makes it a reliable way to identify devices permanently.

---

### Structure of a MAC Address

A **MAC address** is made up of **12 hexadecimal digits** (0–9 and A–F). These are usually written as 6 pairs, separated by colons or hyphens, for example:

`3A:4F:7C:9B:2D:10`

---

### Parts of a MAC Address

1. **Manufacturer Code (OUI – Organisationally Unique Identifier)**
   - The first **3 pairs** (e.g., `3A:4F:7C`) identify the manufacturer of the Network Interface Card (NIC).
2. **Device Serial Number**
   - The last **3 pairs** (e.g., `9B:2D:10`) are unique to that specific device.
   - No two devices from the same manufacturer will have the same serial part.

---

### Key Features of the Structure

- Always **12 digits in hexadecimal**.
- Written in formats such as:
  - `AA:BB:CC:DD:EE:FF`
  - `AA-BB-CC-DD-EE-FF`
- Combines the **manufacturer’s ID** and a **unique device ID**.

---

### Why Hexadecimal?

MAC addresses are normally written in **hexadecimal (base 16)** instead of binary because:

- Binary addresses would be very long and difficult to read (48 bits).
- Hexadecimal is much shorter and easier for humans to work with.
- Each hexadecimal digit represents **4 bits**, making conversion between binary and hexadecimal simple.

---

### Example of Hexadecimal MAC Address

- **Binary format:** `00111010 01001111 01111100 10011011 00101101 00010000`
- **Hexadecimal format:** `3A:4F:7C:9B:2D:10`

Both represent the same address, but the hexadecimal version is **easier to read and write**.

---

MAC addresses are **48-bit numbers**, but they are almost always shown in **12-digit hexadecimal form** for convenience.

---

### How a MAC Address is Created

A MAC address is made up of two main parts:

1. **Manufacturer Code (OUI – Organisationally Unique Identifier)**
   - The first 3 pairs of digits (e.g., `3A:4F:7C`).
   - Assigned to the manufacturer by an international standards organisation.
   - Identifies which company produced the Network Interface Card (NIC).
2. **Serial Code (Device Identifier)**
   - The last 3 pairs of digits (e.g., `9B:2D:10`).
   - Unique to each device produced by that manufacturer.
   - Ensures no two devices from the same manufacturer share the same MAC address.

---

### Example

`3A:4F:7C:9B:2D:10`

- `3A:4F:7C` → Manufacturer code (OUI).
- `9B:2D:10` → Device’s unique serial code.

This combination of **manufacturer code + serial code** makes every MAC address in the world **unique**.

---

# 3.4.3 IP Address

---

[![Illustration depicting an IP address setup, featuring the text 'IP ADDRESS 192.168.1.10', alongside a computer, a wireless router, and a location icon.](images/topic3_hardware/3_4_network_concepts/img_004.png)](https://i0.wp.com/moshikur.com/wp-content/uploads/2025/09/image-66.png?ssl=1)

### What is an IP Address?

An **Internet Protocol (IP) address** is a unique number assigned to a device when it connects to a network, such as the internet.

It acts like a **postal address**, ensuring that data sent across a network arrives at the correct destination.

---

### Key Features of an IP Address

- It is a **logical address**, assigned by the network.
- Can change depending on the network (unlike a MAC address, which is fixed).
- Written in either **IPv4** (32-bit) or **IPv6** (128-bit) format.
- Used by routers and networking systems to **send and receive data packets**.

---

### Examples of IP Addresses

- IPv4: `192.168.1.10`
- IPv6: `2001:0db8:85a3:0000:0000:8a2e:0370:7334`

---

While a **MAC address** identifies a device at the hardware level, an **IP address** identifies a device’s location on a network.

---

### 3.4.3.2 Understand the Purpose of an IP Address

---

### Purpose of an IP Address

The main purpose of an **IP address** is to act as a **unique identifier for a device on a network** and to enable data to be sent and received correctly.

It provides the information needed for devices to **find each other** across local networks and the internet.

---

### Key Roles of an IP Address

1. **Device Identification**
   - Every device connected to a network is assigned an IP address.
   - This ensures that data can be directed to the correct device.
2. **Location Addressing**
   - An IP address shows the **location of the device** within a network.
   - Similar to how a postal address tells the mail service where to deliver letters.
3. **Data Transmission**
   - When data packets are sent, the **source IP address** identifies where they came from.
   - The **destination IP address** ensures they are delivered to the right device.
4. **Routing**
   - Routers use IP addresses to decide the **best path** for data to travel across networks.

---

Without IP addresses, devices would not be able to **communicate, send, or receive data** on a network.

---

### 3.4.3.3 Understand That There Are Different Types of IP Address

---

### Different Types of IP Address

1. **Public IP Address**
   - Assigned to a device by the Internet Service Provider (ISP).
   - Used to identify a device on the **internet**.
   - Example: when accessing a website, the public IP shows where the request comes from.
2. **Private IP Address**
   - Used within a **local area network (LAN)**.
   - Allows devices like laptops, printers, and phones to communicate with each other.
   - Example: `192.168.1.15` is a common private IP format.
3. **Static IP Address**
   - An IP address that does not change.
   - Manually assigned to a device.
   - Useful for servers, printers, or websites that must always be reachable at the same address.
4. **Dynamic IP Address**
   - An IP address that is automatically assigned by a **DHCP (Dynamic Host Configuration Protocol) server**.
   - Changes each time the device reconnects to the network.
   - Used for most home devices because it is easier to manage.

---

Different types of IP addresses are used depending on whether the device is on a **local network** or the **internet**, and whether it needs a **fixed or changing address**.

---

### 3.4.3.4 Understand the Difference Between Static and Dynamic IP Addresses

---

### Static IP Address

- A **fixed IP address** that does not change.
- Manually set up by the user or network administrator.
- Provides a **permanent identifier** for a device on a network.

**Advantages of Static IP**

- Reliable for devices that must always be located at the same address (e.g., servers, printers).
- Easier to run services such as websites or email servers.
- More stable for remote access.

**Disadvantages of Static IP**

- Requires manual configuration.
- Less secure because hackers can target a known IP address.
- More expensive, as ISPs often charge extra for static addresses.

---

### Dynamic IP Address

- An IP address that is **automatically assigned** by a DHCP server.
- Changes each time the device reconnects to the network or after a set period of time.

**Advantages of Dynamic IP**

- Easy to manage – no manual setup needed.
- More secure, as the address changes regularly.
- Usually provided at no extra cost.

**Disadvantages of Dynamic IP**

- Less reliable for hosting services that require a permanent address.
- Can cause problems for remote access.

---

- Static IP = fixed, permanent, better for servers.
- Dynamic IP = changes, automatic, better for everyday devices.

---

# 3.4.3.5 IPv4 Addresses

---

[![Illustration of an IPv4 address with the text 'IPv4 ADDRESS' and an example IP address '192.158.1.42', featuring a globe, cloud, computer, and Wi-Fi symbol.](images/topic3_hardware/3_4_network_concepts/img_005.png)](https://i0.wp.com/moshikur.com/wp-content/uploads/2025/09/image-67.png?ssl=1)

### What is IPv4?

IPv4 (**Internet Protocol version 4**) is the **fourth version** of the Internet Protocol and the most widely used addressing system. It assigns a unique identifier to every device connected to a network.

---

### Characteristics of IPv4 Addresses

1. **32-bit Address**
   - IPv4 uses a 32-bit system, which means there are around **4.3 billion unique addresses** available.
2. **Dotted Decimal Notation**
   - Written as **four numbers separated by dots**, for example:  
     `192.168.1.10`
   - Each number (called an **octet**) can range from 0 to 255.
3. **Unique to Each Device**
   - Every device must have a unique IPv4 address on a network.
4. **Public and Private Ranges**
   - Some IPv4 addresses are reserved for **public use** (internet).
   - Others are reserved for **private networks** (LANs).
5. **Widely Used**
   - IPv4 has been the standard for decades, but the supply of available addresses is running out.

---

### Example of IPv4 Addressing

- `192.168.0.1` → Commonly used for routers in home networks.
- `172.16.5.4` → Example of a private IP in a LAN.

---

# 3.4.3.6 IPv6 Addresses

---

[![Illustration of a laptop displaying an IPv6 address, with a globe, wireless signal icon, and web browser window icons in the background.](images/topic3_hardware/3_4_network_concepts/img_006.png)](https://i0.wp.com/moshikur.com/wp-content/uploads/2025/09/image-68.png?ssl=1)

### What is IPv6?

IPv6 (**Internet Protocol version 6**) is the **newer version** of the Internet Protocol. It was developed to replace IPv4 because the world was running out of available IPv4 addresses.

---

### Characteristics of IPv6 Addresses

1. **128-bit Address**
   - IPv6 uses a 128-bit system.
   - This provides an almost **unlimited number of addresses** (approximately (3.4 \times 10^{38})).
2. **Hexadecimal Format**
   - Written as **eight groups of four hexadecimal digits**, separated by colons.
   - Example:  
     `2001:0db8:85a3:0000:0000:8a2e:0370:7334`
3. **Shortened Notation**
   - Leading zeros in a group can be removed.
   - Consecutive groups of zeros can be replaced with `::` once in an address.
   - Example:  
     `2001:db8:85a3::8a2e:370:7334`
4. **Unique to Each Device**
   - Provides enough addresses for every device in the world, now and in the future.
5. **Improved Features**
   - Built-in support for better **security** and **routing efficiency** compared to IPv4.

---

### Key Point

- **IPv4 = 32-bit, limited addresses, decimal format.**
- **IPv6 = 128-bit, massive capacity, hexadecimal format.**

---

### 3.4.3.7 Identify the Differences Between IPv4 and IPv6

---

### Key Differences Between IPv4 and IPv6

| Feature | IPv4 | IPv6 |
| --- | --- | --- |
| Address Size | 32-bit | 128-bit |
| Format | Decimal, written as 4 octets (e.g., 192.168.1.1 ) | Hexadecimal, written as 8 groups (e.g., 2001:db8:85a3::7334 ) |
| Address Space | About 4.3 billion unique addresses | Almost unlimited ((3.4 \times 10^{38})) |
| Usage | Still the most widely used today | Newer, gradually replacing IPv4 |
| Security | Basic (security features added later) | Built-in support for stronger security |
| Efficiency | Less efficient for routing | Improved routing and simplified headers |
| Example | 192.168.0.1 | 2001:db8:85a3::8a2e:370:7334 |

---

### Summary

- **IPv4**: Older, limited in number, easier to write but running out of addresses.
- **IPv6**: Newer, huge address space, more secure, designed for the future of networking.

---

# 3.4.4.1 Router

---

[![Illustration of a wireless router with a signal icon and a web address displayed.](images/topic3_hardware/3_4_network_concepts/img_007.png)](https://i0.wp.com/moshikur.com/wp-content/uploads/2025/09/image-71.png?ssl=1)

### What is a Router?

A **router** is a networking device that connects different networks together and directs data between them. It acts as a **traffic controller**, making sure data packets are sent to the correct destination.

---

### Role of a Router in a Network

1. **Connects Networks**
   - Connects a **local area network (LAN)** to other networks, such as the internet.
2. **Directs Data Packets**
   - Examines the **IP addresses** in data packets.
   - Decides the best path for the data to travel.
   - Ensures that the data reaches the correct device.
3. **Assigns IP Addresses**
   - Often contains a **DHCP (Dynamic Host Configuration Protocol)** server.
   - Automatically assigns IP addresses to devices in a local network.
4. **Provides Security**
   - Can block unauthorised access through built-in **firewalls** and filtering.
5. **Network Management**
   - Helps manage traffic, preventing data congestion.
   - Can prioritise certain types of data (e.g., video streaming over file downloads).

---

### Example

When you use a home router:

- It connects your devices (laptops, phones, printers) to the **internet**.
- It makes sure the data you request (like a webpage) is sent specifically to **your device**, not someone else’s.

---

### 3.4.4.2 Understand That a Router Sends Data to a Specific Destination on a Network

---

### How a Router Sends Data

- When data is transmitted across a network, it is broken into **packets**.
- Each packet contains two important pieces of information:
  1. **Source IP Address** – where the packet came from.
  2. **Destination IP Address** – where the packet needs to go.
- The router reads the **destination IP address** and decides the best route for the packet to travel.
- It then forwards the packet to the correct device or towards the next network along the path.

---

### Example in a Home Network

- A user requests a webpage from their laptop.
- The laptop sends the request packet with the destination IP (website server).
- The router checks the address and forwards the packet to the internet.
- When the response comes back, the router ensures the data is sent **only to that laptop**, not to other devices in the house.

---

### Key Point

The router’s main job is to **direct data packets accurately**, ensuring they are delivered to the **correct device** on the correct network.

---

### 3.4.4.3 Understand That a Router Can Assign IP Addresses

---

### How Routers Assign IP Addresses

- Most routers include a service called **DHCP (Dynamic Host Configuration Protocol)**.
- DHCP automatically assigns an **IP address** to each device when it connects to the network.
- This removes the need for users to manually set up addresses.

---

### Process of Assigning IP Addresses

1. A device (e.g., laptop or phone) connects to the network.
2. The device sends a request for an IP address.
3. The router, using DHCP, assigns an available IP address from its pool.
4. The device can now send and receive data on the network.

---

### Why This is Important

- Prevents **IP conflicts** (two devices having the same IP).
- Saves time compared to manual configuration.
- Ensures all devices on a network can communicate smoothly.

---

### Example

When you connect your phone to Wi-Fi at home, the router automatically gives it an IP address like `192.168.1.25`, allowing it to join the network.

---

### 3.4.4.4 Understand That a Router Can Connect a Local Network to the Internet

---

### Connecting Local Networks to the Internet

One of the most important roles of a router is to act as a **gateway** between a **local area network (LAN)** (such as your home or school network) and the **wider internet**.

---

### How It Works

1. Devices in the LAN (computers, phones, printers) send data requests to the router.
2. The router forwards these requests to the **internet service provider (ISP)**.
3. The ISP connects to the wider internet and sends the response back to the router.
4. The router then delivers the response to the correct device on the local network.

---

### Example

- A laptop in a home network requests a website.
- The router forwards the request to the ISP.
- The ISP fetches the data from the web server.
- The router delivers the data back to the laptop, not to other devices.

Without a router, a local network would not be able to access the internet, as devices need the router to handle communication between the LAN and the wider world.

That completes **3.4 Network Hardware** (NIC, MAC address, IP address, Router).

# Activity 1

### 1 Understand the Purpose of a Network Interface Card (NIC)

Explain the purpose of a network interface card (NIC) in a computer. Why is it essential for accessing a network?

**Hint:** Think about the hardware component required to establish a connection between the computer and the network. What role does the NIC play in communication?

---

### 2 Understand the Structure and Purpose of a MAC Address

Define what a media access control (MAC) address is and describe its purpose. Include the structure of a MAC address.

**Hint:** Consider how the MAC address is unique to each device and why it is written in hexadecimal format. Think about manufacturer codes and serial codes.

---

### 3 Understand the Purpose of an IP Address

a) Explain what an internet protocol (IP) address is and its purpose in a network.

b) Describe two differences between IPv4 and IPv6.

**Hint:** Think about the structure of each version and the number of addresses supported. What makes IPv6 more future-proof than IPv4?

---

### 5 Explain the Role of a Router

a) Explain the role of a router in a network. Include how it assigns IP addresses and connects a local network to the internet.

b) Draw and annotate a diagram to represent the role of a router in a network.

**Hint:** Consider how routers direct data to specific destinations and allow devices to share a single internet connection.  
For the diagram, Include key components like devices connected to the router, IP address assignment, and connection to the internet.

---

### **6 Static and Dynamic IP Addresses**

Explain the difference between a static IP address and a dynamic IP address. Include examples of when each type is used.

*Hint:* Think about which devices need a consistent, unchanging address (e.g., servers) and which devices can use a temporary address.

---

### **7 Data Routing Example**

Imagine a home network with multiple devices (e.g., a smartphone, a laptop, and a smart TV). Explain how a router assigns IP addresses and manages data traffic between the devices.

*Hint:* Focus on how the router ensures each device gets the data it requested, like streaming video or downloading a file.

---

### **Domain Name System (DNS)**

The Domain Name System (DNS) is like the Internet’s phonebook. It translates human-readable domain names, such as `www.example.com`, into machine-readable IP addresses. Every time you type a web address into your browser, a DNS server resolves that name into an IP address so the computer can find and access the website. Without DNS, we would need to remember complex IP addresses for every site we visit.

### **Gateways**

A gateway is a device that acts as a “translator” between two different networks. For instance, when a local network wants to communicate with the Internet (or another network with different protocols), the gateway ensures that the data passes through correctly. It works as a bridge between networks using different protocols, allowing seamless communication between systems.

### **Advanced Role of Routers**

In addition to routing data packets to their destinations, routers play an advanced role in prioritizing network traffic. This means that routers can decide which data packets are more important, ensuring that critical tasks like video calls or online gaming get higher priority over less time-sensitive tasks like downloading a file. Routers also manage connections between devices on a local network and external networks such as the Internet.

---