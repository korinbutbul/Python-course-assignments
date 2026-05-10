
# Day 3 Assignment: Modular BMI Calculator

This project demonstrates a modular approach to software development by separating business logic from the user interface.

## Project Structure
* **bmi_logic.py**: Contains the core calculation logic (Business Logic).
* **main_input.py**: Standard terminal interface using `input()`.
* **main_argv.py**: Command-line interface using `sys.argv`.
* **main_gui.py**: Graphical User Interface using `tkinter`.
* **test_bmi.py**: Automated tests to verify the calculation accuracy.

## How to Run
1. **Standard Input:** `python main_input.py`
2. **Command Line:** `python main_argv.py <weight> <height>` (e.g., `python main_argv.py 70 1.75`)
3. **GUI:** `python main_gui.py`
4. **Tests:** `python test_bmi.py`

## Features Implemented
* Separation of concerns: Logic is separated from UI for reusability.
* Automated testing with `assert`.
* Use of `.gitignore` to exclude `__pycache__`.
* Handling user input via multiple methods (Terminal, CLI arguments, and GUI).

## AI Disclosure
* **AI Tool:** Gemini
* **Usage:** I used GiminiAI for his help with writing and error solving. Assisted in structuring the modular files, generating the `tkinter` GUI boilerplate, and explaining the `sys.argv` implementation. .