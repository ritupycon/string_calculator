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

