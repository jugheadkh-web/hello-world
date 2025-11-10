import turtle

def koch_curve(t, length, level):
    """
    Draws a Koch curve segment.

    Parameters:
        t      : Turtle object
        length : length of the line segment
        level  : recursion depth
    """
    if level == 0:
        t.forward(length)
    else:
        length /= 3.0
        koch_curve(t, length, level - 1)
        t.left(60)
        koch_curve(t, length, level - 1)
        t.right(120)
        koch_curve(t, length, level - 1)
        t.left(60)
        koch_curve(t, length, level - 1)

def koch_snowflake(t, length, level):
    """
    Draws a full Koch snowflake.

    Parameters:
        t      : Turtle object
        length : length of one side of the base triangle
        level  : recursion depth
    """
    for _ in range(3):
        koch_curve(t, length, level)
        t.right(120)

import turtle
from koch_curve import koch_snowflake

screen = turtle.Screen()
t = turtle.Turtle()
t.speed(0)  # Fastest drawing

# Draw a Koch snowflake with side length 300 and recursion level 2
koch_snowflake(t, 300, 2)

screen.mainloop()
