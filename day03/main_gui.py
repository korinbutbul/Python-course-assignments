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