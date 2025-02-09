# String Calculator

A simple string calculator that allows you to add numbers from a string, handle custom delimiters, and manage edge cases like negative numbers.

## Features

- **Sum of numbers**: Given a string of comma-separated numbers, return their sum.
- **Handles empty strings**: Returns `0` if the input is empty.
- **Supports new line separators**: Numbers can be separated by both commas and newlines.
- **Custom delimiters**: Allows a custom delimiter to be used at the start of the string (e.g., `//[delimiter]\n[numbers]`).
- **Negative number exception**: If any negative number is included, an exception is thrown with the negative numbers listed.

## Requirements

- Python 3.x

## Installation

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/string_calculator.git
2. Navigate to Project Directory
   ```bash
   cd string_calculator
3. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate

## Usage

### Add method:
The add() method takes a string of comma-separated numbers and returns their sum.
```baash
from src.string_calculator import StringCalculator

calc = StringCalculator()

result = calc.add("1,2,3")
print(result)  # Output: 6

### Handling custom delimeters
You can specify a custom delimiter at the beginning of the string using the following format: //[delimiter]\n[numbers].
For example:
```bash
result = calc.add("//;\n1;2;3")
print(result)  # Output: 6

### handling negative numbers
If a string contains negative numbers, the calculator will raise an exception and list all negative numbers.
```bash
try:
    result = calc.add("-1,2,-3")
except ValueError as e:
    print(e)  # Output: negative numbers not allowed -1, -3

### Newline separator:
The string can also include newline characters to separate numbers:
```bash
result = calc.add("1\n2,3")
print(result)  # Output: 6

## Running test
The project uses unittest for testing. To run the tests, follow these steps:

1.Make sure your virtual environment is activated (if using one).
2.Run the tests using the command below:
```bash
python -m unittest discover -s tests

This will run all tests located in the tests directory.
