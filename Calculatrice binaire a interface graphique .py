import tkinter as tk
from tkinter import ttk

# Check if the string contains only bits (0 or 1)
def is_binary(value):
    return all(bit == '0' or bit == '1' for bit in value)

# Validate binary input in an entry field
def validate_binary_input(entry, label_text):
    value = entry.get()
    if not is_binary(value):
        result_label.config(text=f"Error: {label_text} must contain only 0 or 1.", foreground="red")
        return False
    return True

# Align two binary strings by padding with zeros to make them the same length
def align_bits(binary1, binary2):
    max_length = max(len(binary1), len(binary2))
    return binary1.zfill(max_length), binary2.zfill(max_length)

# Convert a binary number to decimal
def binary_to_decimal(binary):
    if not is_binary(binary):
        result_label.config(text="Error: The binary number must contain only 0 or 1.", foreground="red")
        return
    return int(binary, 2)

# Convert a decimal number to binary
def decimal_to_binary(number):
    return bin(number)[2:] if number > 0 else '0'

# Function to perform binary addition
def add():
    if not validate_binary_input(entry1, "Binary number 1") or not validate_binary_input(entry2, "Binary number 2"):
        return
    binary1 = entry1.get()
    binary2 = entry2.get()
    decimal1 = binary_to_decimal(binary1)
    decimal2 = binary_to_decimal(binary2)
    binary_sum = decimal_to_binary(decimal1 + decimal2)
    result_label.config(text=f"Sum in binary: {binary_sum}", foreground="green")

# Function to perform binary subtraction
def subtract():
    if not validate_binary_input(entry1, "Binary number 1") or not validate_binary_input(entry2, "Binary number 2"):
        return
    binary1 = entry1.get()
    binary2 = entry2.get()
    decimal1 = binary_to_decimal(binary1)
    decimal2 = binary_to_decimal(binary2)
    binary_difference = decimal_to_binary(abs(decimal1 - decimal2))
    result_label.config(text=f"Difference in binary: {binary_difference}", foreground="green")

# Function to perform binary multiplication
def multiply():
    if not validate_binary_input(entry1, "Binary number 1") or not validate_binary_input(entry2, "Binary number 2"):
        return
    binary1 = entry1.get()
    binary2 = entry2.get()
    decimal1 = binary_to_decimal(binary1)
    decimal2 = binary_to_decimal(binary2)
    binary_product = decimal_to_binary(decimal1 * decimal2)
    result_label.config(text=f"Product in binary: {binary_product}", foreground="green")

# Function to perform binary division
def divide():
    if not validate_binary_input(entry1, "Binary number 1") or not validate_binary_input(entry2, "Binary number 2"):
        return
    binary1 = entry1.get()
    binary2 = entry2.get()
    decimal1 = binary_to_decimal(binary1)
    decimal2 = binary_to_decimal(binary2)
    if decimal2 != 0:
        binary_quotient = decimal_to_binary(decimal1 // decimal2)
        result_label.config(text=f"Quotient in binary: {binary_quotient}", foreground="green")
    else:
        result_label.config(text="Error: Division by zero.", foreground="red")

# Function to perform left or right bit shifting
def shift():
    if not validate_binary_input(entry1, "Binary number 1"):
        return
    direction = entryDirection.get().upper()
    shift_value = int(entryShift.get())
    binary_to_shift = entry1.get()
    if direction == "L":
        shifted = binary_to_shift.ljust(len(binary_to_shift) + shift_value, '0')
    elif direction == "R":
        shifted = binary_to_shift.rjust(len(binary_to_shift) + shift_value, '0')[:len(binary_to_shift)]
    else:
        result_label.config(text="Error: Choose L for left or R for right.", foreground="red")
        return
    result_label.config(text=f"Shifted binary number: {shifted}", foreground="green")

# Function to perform two's complement
def complement2():
    binary = complement2_entry.get()
    negation = ''.join(str(1 - int(bit)) for bit in binary)
    one = "1" + "0" * (len(binary) - 1)
    addition = decimal_to_binary(binary_to_decimal(negation) + binary_to_decimal(one))
    result_label.config(text=f"Two's complement: {addition}", foreground="green")

# Function to perform bitwise AND operation
def bitwise_and():
    if not validate_binary_input(entry1, "Binary number 1") or not validate_binary_input(entry2, "Binary number 2"):
        return
    binary1 = entry1.get()
    binary2 = entry2.get()
    aligned1, aligned2 = align_bits(binary1, binary2)
    result = ''.join('1' if b1 == '1' and b2 == '1' else '0' for b1, b2 in zip(aligned1, aligned2))
    result_label.config(text=f"AND result: {result}", foreground="green")

# Function to perform bitwise OR operation
def bitwise_or():
    if not validate_binary_input(entry1, "Binary number 1") or not validate_binary_input(entry2, "Binary number 2"):
        return
    binary1 = entry1.get()
    binary2 = entry2.get()
    aligned1, aligned2 = align_bits(binary1, binary2)
    result = ''.join('1' if b1 == '1' or b2 == '1' else '0' for b1, b2 in zip(aligned1, aligned2))
    result_label.config(text=f"OR result: {result}", foreground="green")

# Function to perform bitwise NOT operation
def bitwise_not():
    if not validate_binary_input(entry1, "Binary number 1"):
        return
    binary1 = entry1.get()
    result = ''.join('1' if bit == '0' else '0' for bit in binary1)
    result_label.config(text=f"NOT result: {result}", foreground="green")

# Function to create a styled button
def create_styled_button(root, text, command, row, col):
    button = ttk.Button(root, text=text, command=command, style="TButton")
    button.grid(row=row, column=col, padx=10, pady=10, sticky="ew")

# Create the user interface with enhanced styling
def create_ui():
    global entry1, entry2, entryDirection, entryShift, complement2_entry, result_label

    root = tk.Tk()
    root.title("Binary Calculator")
    root.geometry("400x600")
    root.configure(bg="#f4f4f4")

    # Set the style for buttons and labels
    style = ttk.Style(root)
    style.configure("TButton", font=("Helvetica", 12), background="#4CAF50", foreground="black")
    style.configure("TLabel", font=("Helvetica", 12), background="#f4f4f4", padding=5)
    style.configure("TEntry", font=("Helvetica", 12))

    # Create the frames
    input_frame = tk.Frame(root, bg="#ffffff", padx=20, pady=20)
    input_frame.pack(padx=10, pady=10)

    operation_frame = tk.Frame(root, bg="#ffffff", padx=20, pady=20)
    operation_frame.pack(padx=10, pady=10)

    result_frame = tk.Frame(root, bg="#ffffff", padx=20, pady=20)
    result_frame.pack(padx=10, pady=10)

    # Labels and entries for binary inputs
    ttk.Label(input_frame, text="Binary number 1:").grid(row=0, column=0, sticky="w", pady=5)
    entry1 = ttk.Entry(input_frame)
    entry1.grid(row=0, column=1, pady=5)

    ttk.Label(input_frame, text="Binary number 2:").grid(row=1, column=0, sticky="w", pady=5)
    entry2 = ttk.Entry(input_frame)
    entry2.grid(row=1, column=1, pady=5)

    ttk.Label(input_frame, text="Shift Direction (L/R):").grid(row=2, column=0, sticky="w", pady=5)
    entryDirection = ttk.Entry(input_frame)
    entryDirection.grid(row=2, column=1, pady=5)

    ttk.Label(input_frame, text="Shift Value:").grid(row=3, column=0, sticky="w", pady=5)
    entryShift = ttk.Entry(input_frame)
    entryShift.grid(row=3, column=1, pady=5)

    ttk.Label(input_frame, text="Two's Complement:").grid(row=4, column=0, sticky="w", pady=5)
    complement2_entry = ttk.Entry(input_frame)
    complement2_entry.grid(row=4, column=1, pady=5)

    # Operation buttons
    create_styled_button(operation_frame, "Add", add, 0, 0)
    create_styled_button(operation_frame, "Subtract", subtract, 0, 1)
    create_styled_button(operation_frame, "Multiply", multiply, 0, 2)
    create_styled_button(operation_frame, "Divide", divide, 1, 0)
    create_styled_button(operation_frame, "Shift", shift, 1, 1)
    create_styled_button(operation_frame, "Complement", complement2, 1, 2)
    create_styled_button(operation_frame, "AND", bitwise_and, 2, 0)
    create_styled_button(operation_frame, "OR", bitwise_or, 2, 1)
    create_styled_button(operation_frame, "NOT", bitwise_not, 2, 2)

    # Result label
    result_label = ttk.Label(result_frame, text="", foreground="black")
    result_label.pack(pady=10)

    root.mainloop()

# Run the application
create_ui()
