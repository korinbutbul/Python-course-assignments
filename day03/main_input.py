from bmi_logic import calculate_bmi

if __name__ == "__main__":
    w = float(input("Enter weight (kg): "))
    h = float(input("Enter height (m): "))
    result = calculate_bmi(w, h)
    print(f"Your BMI is: {result}")