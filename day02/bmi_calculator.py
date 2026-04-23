# BMI (Body Mass Index) Calculator
# Formula: weight / (height^2)

print("--- Scientific BMI Calculator ---")

# Getting input from user
# We use float() because weight and height are decimal numbers
try:
    weight = float(input("Enter your weight in kg (e.g. 49.5): "))
    height = float(input("Enter your height in meters (e.g. 1.63): "))

    # Calculation
    bmi = weight / (height ** 2)

    # Output with rounding to 2 decimal places
    print(f"\nYour BMI is: {round(bmi, 2)}")

    # Interpretation
    if bmi < 18.5:
        print("Status: Underweight")
    elif 18.5 <= bmi < 25:
        print("Status: Normal weight")
    else:
        print("Status: Overweight")

except ValueError:
    print("Error: Please enter numbers only (use a dot for decimals).")