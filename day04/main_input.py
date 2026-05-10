from bmi_logic import calculate_bmi

if __name__ == "__main__":
 w = float(input("Enter weight (kg): "))
 h = float(input("Enter height (m): "))
result = calculate_bmi(w, h)
print(f"Your BMI is: {result}")
from bmi_logic import calculate_bmi, save_to_history
from bmi_logic import calculate_bmi, save_to_history

if __name__ == "__main__":
    # 1. קבלת קלט מהמשתמש
    weight = float(input("Enter weight (kg): "))
    height = float(input("Enter height (m): "))
    
    # 2. חישוב ה-BMI
    bmi = calculate_bmi(weight, height)
    
    # 3. שמירה להיסטוריה
    save_to_history(weight, height, bmi)
    
    # 4. הדפסת התוצאה
    print(f"Your BMI is: {bmi}")
    print("Result saved to history.txt")