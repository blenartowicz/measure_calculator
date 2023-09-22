import tkinter as tk
from tkinter import ttk

def get_value():
    calc_value = float(entry_var.get())  # Convert input value to float
    combo_val = combo.get()

    if combo_val == "uncje na gramy":
        fun_result = calc_value * 28
    elif combo_val == "funty na kilogramy":
        fun_result = calc_value * 0.45
    elif combo_val == "filiżanki na mililitry":
        fun_result = calc_value * 236
    elif combo_val == "uncja na mililitry": 
        fun_result = calc_value / 29.5

    result.set(str(fun_result))

window = tk.Tk()
window.title("Program do liczenia miar US-PL")
window.geometry("450x200")

label_title = tk.Label(text='Najpierw wybierz odpowiednie miary, potem wpisz wartości i naciśnij Przelicz')
label_title.grid(column=0, row=0)

combo = ttk.Combobox(window, values=["uncje na gramy", "funty na kilogramy", "filiżanki na mililitry", "uncja na mililitry"])
combo.grid(column=0, row=1)

entry_var = tk.StringVar()
value_entry = ttk.Entry(window, textvariable=entry_var)
value_entry.grid(column=0, row=2)

button = ttk.Button(master=window, text="Przelicz", command=get_value)
button.grid(column=0, row=3)

result = tk.StringVar()
result.set("")

result_label = tk.Label(window, textvariable=result)
result_label.grid(column=0, row=4)  # Change the row to 3

window.mainloop()
