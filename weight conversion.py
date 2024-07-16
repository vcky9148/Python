import tkinter as tk

def convert():
    try:
        kg_value = float(entry_kg.get())
        pounds_value = kg_value * 2.20462
        label_result.config(text=f"{kg_value:.2f} kg is equal to {pounds_value:.2f} pounds")
    except ValueError:
        label_result.config(text="Please enter a valid number")

def clear():
    entry_kg.delete(0, tk.END)
    label_result.config(text="")

# Create the main window
root = tk.Tk()
root.title("Weight Converter")

# Create and place widgets
label_kg = tk.Label(root, text="Enter weight in kilograms:")
label_kg.grid(row=0, column=0, pady=10)

entry_kg = tk.Entry(root)
entry_kg.grid(row=0, column=1, pady=10)

convert_button = tk.Button(root, text="Convert", command=convert)
convert_button.grid(row=1, column=0, columnspan=2, pady=5)

clear_button = tk.Button(root, text="Clear", command=clear)
clear_button.grid(row=2, column=0, columnspan=2, pady=5)

label_result = tk.Label(root, text="")
label_result.grid(row=3, column=0, columnspan=2, pady=10)

# Start the event loop
root.mainloop()
