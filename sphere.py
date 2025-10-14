"""
sphere.py
This program calculates and displays the diameter, circumference, surface area,
and volume of a sphere given its radius.

- Input: Radius of the sphere (float)
- Output: Diameter, circumference, surface area, and volume (all floats)

1. Prompt the user to enter the radius of the sphere.
2. Use the following formulas:
   - Diameter = 2 * radius
   - Circumference = 2 * π * radius
   - Surface Area = 4 * π * radius^2
   - Volume = (4/3) * π * radius^3
3. Display all results with appropriate labels.
"""

import math

# Input from user
radius = float(input("Enter the radius of the sphere: "))

# Calculations
diameter = 2 * radius
circumference = 2 * math.pi * radius
surface_area = 4 * math.pi * (radius ** 2)
volume = (4 / 3) * math.pi * (radius ** 3)

# Output
print(f"Diameter: {diameter:.2f} units")
print(f"Circumference: {circumference:.2f} units")
print(f"Surface Area: {surface_area:.2f} square units")
print(f"Volume: {volume:.2f} cubic units")
