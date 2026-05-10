def calculate_bmi(weight, height):
    """Business Logic: Calculates BMI from weight (kg) and height (m)"""
    if height <= 0:
        return 0
    return round(weight / (height ** 2), 2)

import datetime

def calculate_bmi(weight, height):
    """Calculates BMI and returns it rounded to 2 decimal places."""
    if height <= 0:
        return 0
    return round(weight / (height ** 2), 2)

def save_to_history(weight, height, bmi):
    """Saves the calculation details and timestamp to a text file."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("history.txt", "a") as f:
        f.write(f"[{timestamp}] Weight: {weight}kg, Height: {height}m -> BMI: {bmi}\n")