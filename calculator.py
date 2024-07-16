import tkinter as tk

def button_click(symbol):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + symbol)

def clear_display():
    entry.delete(0, tk.END)

def calculate_result():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width=30, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

for i in range(len(buttons)):
    btn = tk.Button(root, text=buttons[i], padx=20, pady=10, command=lambda x=buttons[i]: button_click(x))
    btn.grid(row=i // 4 + 1, column=i % 4, padx=5, pady=5)

clear_button = tk.Button(root, text="C", padx=20, pady=10, command=clear_display)
clear_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

equal_button = tk.Button(root, text="=", padx=20, pady=10, command=calculate_result)
equal_button.grid(row=5, column=2, columnspan=2, padx=5, pady=5)

root.mainloop()
