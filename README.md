# IP Details Calculator

A lightweight Python script to calculate the **Network ID** and **Broadcast ID** from a given IP address and Subnet Mask using bitwise operations.

## Features

- Parses IPv4 addresses and subnet masks.
- Uses efficient bitwise AND (`&`) and OR (`|`) operations for network calculations.
- Outputs exact Network and Broadcast addresses.

---

## Tech Stack

- **Language:** Python 3.x
- **Modules:** Built-in operations only (No third-party dependencies required).

---

## How It Works (Core Logic)

The script processes the IP address and Subnet Mask octet by octet (4 parts):

1. **Network ID Calculation:** Performs a bitwise **AND** operation between the IP octet and Mask octet.
   $$\text{Network Octet} = \text{IP Octet} \ \& \ \text{Mask Octet}$$
2. **Broadcast ID Calculation:** Inverts the Subnet Mask octet ($255 - \text{Mask Octet}$) and performs a bitwise **OR** operation with the calculated Network octet.
   $$\text{Broadcast Octet} = \text{Network Octet} \ | \ (255 - \text{Mask Octet})$$

---

## Project Structure

- `ip_calc.py` - The primary Python script containing the calculation function and sample inputs.

---

## How to Run

1. Make sure you have Python installed on your system.
2. Clone or download this project folder.
3. Open your terminal or command prompt in the project directory.
4. Run the script using the following command:

```bash
python ip_calc.py
