"""
Program: Convert Years to Minutes
Author: [Your Name]

This program calculates the number of minutes in a given number of years.
It asks the user to input the number of years, and then it uses the formula:

    minutes = years × 365 × 24 × 60

to compute the total minutes (assuming non-leap years). The result is displayed with commas for readability.
"""

# Get the number of years from the user
years = int(input("Enter the number of years: "))

# Calculate the number of minutes (non-leap year assumption)
minutes = years * 365 * 24 * 60

# Display the result
print(f"There are {minutes:,} minutes in {years} year(s).")
