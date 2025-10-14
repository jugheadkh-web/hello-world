"""
Program: Tax Calculator
Author: [Your Name]

This program calculates the total cost including tax for a given purchase amount.

Analysis:
- Inputs: purchase amount (float), tax rate (as a decimal, e.g., 0.07 for 7%)
- Calculate tax amount: purchase amount * tax rate
- Calculate total cost: purchase amount + tax
- Round all output values to two decimal places for proper currency formatting

Design (Pseudocode):
1. Prompt user for the purchase amount.
2. Prompt user for the tax rate (as decimal).
3. Compute the sales tax.
4. Compute the total amount due.
5. Round the sales tax and total to two decimal places.
6. Display the results.
"""

# Step 1–2: Input from user
purchase_amount = float(input("Enter the purchase amount: $"))
tax_rate = float(input("Enter the tax rate (e.g., 0.07 for 7%): "))

# Step 3–4: Perform calculations
sales_tax = purchase_amount * tax_rate
total_due = purchase_amount + sales_tax

# Step 5: Round values
sales_tax = round(sales_tax, 2)
total_due = round(total_due, 2)

# Step 6: Output the results
print(f"\nSales Tax: ${sales_tax:.2f}")
print(f"Total Due: ${total_due:.2f}")
