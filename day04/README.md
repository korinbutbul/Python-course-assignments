# Day 04: BMI Calculator with History Logging

This project is an enhanced version of the BMI Calculator

## Features
- **BMI Calculation:** Core logic to calculate Body Mass Index based on weight and height.
- **History Logging:** Automatically saves every calculation result, including a timestamp, to a local file named `history.txt`.
- **Multiple Interfaces:** Supports both Command Line Interface (CLI) and Graphical User Interface (GUI).
- **Unit Testing:** Includes automated tests to ensure the calculation logic is accurate.

## Project Structure
- `bmi_logic.py`: Contains the core calculation and file-saving functions.
- `main_input.py`: CLI-based interface for user input.
- `main_gui.py`: Tkinter-based graphical interface.
- `test_bmi.py`: Test suite for the BMI logic.
- `history.txt`: Local log file (excluded from Git for privacy).

## How to Run
To run the CLI version:
```bash
python day04/main_input.py
-Gemini -for technical guidance, troubleshooting terminal errors, and assistance in structuring the code.