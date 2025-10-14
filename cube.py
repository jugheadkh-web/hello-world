"""
cube.py
This program calculates the surface area of a cube.
- Input: Length of one edge of the cube (integer)
- Output: Surface area of the cube (integer)

1. Prompt the user to enter the length of the edge of the cube.
2. Use the formula for surface area: surface_area = 6 * edge_length^2
3. Display the result with appropriate labeling.
"""

# Get user input
edge_length = int(input("Enter the length of the edge of the cube (in units): "))

# Calculate surface area
surface_area = 6 * (edge_length ** 2)

# Output result
print("The surface area of the cube is:", surface_area, "square units")
