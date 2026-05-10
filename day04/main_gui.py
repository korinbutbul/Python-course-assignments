import tkinter as tk
from bmi_logic import calculate_bmi

def on_calculate():
    w = float(entry_w.get())
    h = float(entry_h.get())
    label_res.config(text=f"BMI: {calculate_bmi(w, h)}")

root = tk.Tk()
root.title("BMI Calculator")

tk.Label(root, text="Weight:").pack()
entry_w = tk.Entry(root)
entry_w.pack()

tk.Label(root, text="Height:").pack()
entry_h = tk.Entry(root)
entry_h.pack()

tk.Button(root, text="Calculate", command=on_calculate).pack()
label_res = tk.Label(root, text="")
label_res.pack()

root.mainloop()
import tkinter as tk
from bmi_logic import calculate_bmi, save_to_history

def on_calculate():
    try:
        w = float(entry_w.get())
        h = float(entry_h.get())
        bmi = calculate_bmi(w, h)
        save_to_history(w, h, bmi) # שמירה להיסטוריה
        label_res.config(text=f"BMI: {bmi}\n(Saved to history.txt)")
    except ValueError:
        label_res.config(text="Please enter valid numbers")

root = tk.Tk()
root.title("BMI Calculator with History")

tk.Label(root, text="Weight (kg):").pack()
entry_w = tk.Entry(root)
entry_w.pack()

tk.Label(root, text="Height (m):").pack()
entry_h = tk.Entry(root)
entry_h.pack()

tk.Button(root, text="Calculate & Save", command=on_calculate).pack()
label_res = tk.Label(root, text="")
label_res.pack()

root.mainloop()
bmi = calculate_bmi(w, h)
save_to_history(w, h, bmi)  
