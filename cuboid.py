"""
cuboid.py
This program calculates the volume of a cuboid.
"""

# Get dimensions from user
height = float(input("Enter the height of the cuboid: "))
width = float(input("Enter the width of the cuboid: "))
depth = float(input("Enter the depth of the cuboid: "))

# Calculate volume
volume = height * width * depth

# Output result
print("The volume of the cuboid is:", volume, "cubic units")
