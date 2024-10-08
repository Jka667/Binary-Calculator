# Binary-Calculator


# Binary Calculator

This project is a Binary Calculator application built using Python's Tkinter library. It allows users to perform various binary arithmetic operations, including addition, subtraction, multiplication, division, bitwise operations, and two's complement calculations. The application provides a user-friendly interface for inputting binary numbers and displays the results in real-time.

## Features

- **Binary Arithmetic Operations**: 
  - Addition
  - Subtraction
  - Multiplication
  - Division
- **Bitwise Operations**:
  - AND
  - OR
  - NOT
- **Shift Operations**: 
  - Left and right bit shifting
- **Two's Complement Calculation**
- **Input Validation**: Ensures that only binary numbers (0s and 1s) are accepted.

## Installation

1. Ensure you have Python installed on your machine. This application is compatible with Python 3.x.
2. Install the Tkinter library if it is not already available. Tkinter usually comes pre-installed with Python. You can verify it by running:

   ```bash
   python -m tkinter
    If a small window opens, Tkinter is installed correctly.

3. Clone the repository or download the source code.
git clone <repository-url>

4. Navigate to the project directory.
cd binary-calculator

5. Run the application:
python binary_calculator.py

---------------------------USAGE------------------------------------------------
Launch the application. A window will open displaying fields for entering binary numbers, the shift direction, and a shift value.
Input the desired binary numbers into the respective fields.
Click the buttons for the operation you wish to perform (Add, Subtract, Multiply, Divide, Shift, Complement, AND, OR, NOT).
The result will be displayed at the bottom of the window.
Code Structure
is_binary(value): Checks if a string contains only bits (0 or 1).
validate_binary_input(entry, label_text): Validates the binary input in the entry field.
align_bits(binary1, binary2): Aligns two binary strings by padding them with zeros.
binary_to_decimal(binary): Converts a binary number to its decimal representation.
decimal_to_binary(number): Converts a decimal number to its binary representation.
Arithmetic and bitwise operation functions: Define actions for addition, subtraction, multiplication, division, and bitwise operations.
