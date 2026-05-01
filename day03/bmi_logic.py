def calculate_bmi(weight, height):
    """Business Logic: Calculates BMI from weight (kg) and height (m)"""
    if height <= 0:
        return 0
    return round(weight / (height ** 2), 2)