
import tkinter as tk
from tkinter import messagebox

def fahrenheit_to_celsius():
    """Convert Fahrenheit to Celsius."""
    try:
        f = float(fahrenheit_entry.get())
        c = (f - 32) * 5 / 9
        celsius_var.set(f"{c:.2f}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for Fahrenheit.")

def celsius_to_fahrenheit():
    """Convert Celsius to Fahrenheit."""
    try:
        c = float(celsius_entry.get())
        f = (c * 9 / 5) + 32
        fahrenheit_var.set(f"{f:.2f}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for Celsius.")

def clear_fields():
    fahrenheit_var.set("32.0")
    celsius_var.set("0.0")

# --- Create main window ---
window = tk.Tk()
window.title("Temperature Converter")
window.geometry("300x150")
window.resizable(False, False)

# --- Row 1: Labels ---
tk.Label(window, text="Fahrenheit").grid(row=0, column=0, padx=10, pady=5)
tk.Label(window, text="Celsius").grid(row=0, column=1, padx=10, pady=5)

# --- Row 2: Entry fields ---
fahrenheit_var = tk.StringVar(value="32.0")
celsius_var = tk.StringVar(value="0.0")

fahrenheit_entry = tk.Entry(window, textvariable=fahrenheit_var, width=10, justify="center")
fahrenheit_entry.grid(row=1, column=0, padx=10, pady=5)

celsius_entry = tk.Entry(window, textvariable=celsius_var, width=10, justify="center")
celsius_entry.grid(row=1, column=1, padx=10, pady=5)

# --- Row 3: Buttons ---
to_celsius_btn = tk.Button(window, text=">>>>", command=fahrenheit_to_celsius)
to_celsius_btn.grid(row=2, column=0, padx=10, pady=10)

to_fahrenheit_btn = tk.Button(window, text="<<<<", command=celsius_to_fahrenheit)
to_fahrenheit_btn.grid(row=2, column=1, padx=10, pady=10)

clear_btn = tk.Button(window, text="Clear", command=clear_fields)
clear_btn.grid(row=3, column=0, columnspan=2, pady=5)

# --- Run the GUI loop ---
window.mainloop()

