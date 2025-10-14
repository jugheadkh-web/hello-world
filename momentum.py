"""
momentum.py
This program calculates the momentum of an object using the formula:

momentum = mass × velocity

- Input: mass in kilograms (float), velocity in meters per second (float)
- Output: momentum (float) in kg·m/s

1. Prompt the user to enter the object's mass in kilograms.
2. Prompt the user to enter the object's velocity in meters per second.
3. Compute momentum using the formula: momentum = mass × velocity.
4. Display the result with a label and round to two decimal places.
"""

# Input
mass = float(input("Enter the object's mass in kilograms: "))
velocity = float(input("Enter the object's velocity in meters per second: "))

# Calculation
momentum = mass * velocity

# Output
print(f"The object's momentum is {momentum:.2f} kg·m/s")
