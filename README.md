# Binary Calculator

**Desktop calculator for binary arithmetic, bitwise operations, and bit manipulation.**

A Python Tkinter application for performing binary calculations. Supports arithmetic operations, bitwise logic, bit shifting, and two's complement—ideal for studying binary systems, digital logic, and low-level programming.

## Features

- ➕ **Arithmetic**: Addition, Subtraction, Multiplication, Division
- 🔧 **Bitwise Operations**: AND, OR, NOT
- ⬅️ **Shift Operations**: Left/Right bit shifting
- 📊 **Two's Complement**: Calculate binary negation
- ✅ **Input Validation**: Accepts only binary digits (0s and 1s)
- 🎯 **Real-time Results**: Instant calculation display

## Requirements

- Python 3.x
- Tkinter (included with Python by default)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd binary-calculator
```

2. Run the application:
```bash
python binary_calculator.py
```

## Usage

1. Launch the application
2. Enter binary numbers in the input fields
3. Click the desired operation button:
   - **Add** - Binary addition
   - **Subtract** - Binary subtraction
   - **Multiply** - Binary multiplication
   - **Divide** - Binary division
   - **AND/OR/NOT** - Bitwise operations
   - **Shift** - Left/Right bit shifting
   - **Complement** - Two's complement calculation
4. View the result at the bottom of the window

### Example


Input: 1010 + 1100
Output: 10110

Input: 1111 (Two's Complement)
Output: 0001


## How It Works

- **is_binary()** - Validates if input contains only 0s and 1s
- **validate_binary_input()** - Checks field content before processing
- **align_bits()** - Pads binary strings for proper alignment
- **binary_to_decimal()** - Converts binary to decimal representation
- **decimal_to_binary()** - Converts decimal back to binary
- **Operation functions** - Executes arithmetic, bitwise, and shift operations

## Use Cases

- 🎓 **Learning**: Understand binary arithmetic and bitwise logic
- 🔐 **Cybersecurity**: Explore binary manipulations for cryptography
- 💻 **Programming**: Debug bit-level operations
- 🎮 **Game Development**: Work with binary flags and bit masks

## Notes

- All calculations use Python's built-in binary support
- Results displayed in binary format
- Supports positive and negative numbers via two's complement
- User-friendly GUI with real-time validation












