import tkinter as tk
from tkinter import messagebox

def compute_tax():
    """Compute the tax owed based on income and tax rate."""
    try:
        income = float(income_entry.get())
        tax_rate = float(rate_entry.get())
        tax = income * tax_rate / 100
        tax_var.set(f"${tax:,.2f}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numeric values for income and tax rate.")

# --- Create main window ---
window = tk.Tk()
window.title("Tax Calculator")
window.geometry("320x200")
window.resizable(False, False)

# --- Labels and Entry fields ---
tk.Label(window, text="Enter income:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
income_entry = tk.Entry(window)
income_entry.grid(row=0, column=1, padx=10)

tk.Label(window, text="Enter tax rate (%):").grid(row=1, column=0, padx=10, pady=10, sticky="e")
rate_entry = tk.Entry(window)
rate_entry.grid(row=1, column=1, padx=10)

# --- Compute Button ---
compute_btn = tk.Button(window, text="Compute Tax", command=compute_tax)
compute_btn.grid(row=2, column=0, columnspan=2, pady=10)

# --- Tax Display ---
tk.Label(window, text="Tax owed:").grid(row=3, column=0, padx=10, sticky="e")
tax_var = tk.StringVar()
tax_label = tk.Label(window, textvariable=tax_var, relief="sunken", width=15, anchor="w")
tax_label.grid(row=3, column=1, padx=10)

# --- Run the GUI ---
window.mainloop()
