
"""
Employee Weekly Pay Calculator
[Kevin Harvison]

This program calculates an employee's total weekly pay based on:
- Hourly wage
- Total regular hours worked
- Total overtime hours worked

Design (Pseudocode):
1. Get hourly wage from user.
2. Get number of regular hours worked.
3. Get number of overtime hours worked.
4. Calculate regular pay: regular_hours × hourly_wage.
5. Calculate overtime pay: overtime_hours × hourly_wage × 1.5.
6. Add both to get total pay.
7. Display total weekly pay.
"""

# Get inputs from the user
hourly_wage = float(input("Enter hourly wage: $"))
regular_hours = float(input("Enter number of regular hours worked: "))
overtime_hours = float(input("Enter number of overtime hours worked: "))

# Calculate regular and overtime pay
regular_pay = regular_hours * hourly_wage
overtime_pay = overtime_hours * hourly_wage * 1.5

# Calculate total pay
total_pay = regular_pay + overtime_pay

# Display the result
print(f"\nTotal Weekly Pay: ${total_pay:.2f}")
