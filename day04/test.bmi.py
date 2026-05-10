from bmi_logic import calculate_bmi

def test_bmi():
    # בדיקת מקרה רגיל
    assert calculate_bmi(80, 1.80) == 24.69
    # בדיקת מקרה גבול (גובה 0)
    assert calculate_bmi(80, 0) == 0
    print("Tests passed!")

if __name__ == "__main__":
    test_bmi()