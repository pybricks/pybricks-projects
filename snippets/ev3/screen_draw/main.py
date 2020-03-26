#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.tools import wait


# Initialize the EV3
ev3 = EV3Brick()


# Draw a rectangle
ev3.screen.draw_box(10, 10, 40, 40)

# Draw a solid rectangle
ev3.screen.draw_box(20, 20, 30, 30, fill=True)

# Draw a rectangle with rounded corners
ev3.screen.draw_box(50, 10, 80, 40, 5)

# Draw a circle
ev3.screen.draw_circle(25, 75, 20)

# Draw a triangle using lines
x1, y1 = 65, 55
x2, y2 = 50, 95
x3, y3 = 80, 95
ev3.screen.draw_line(x1, y1, x2, y2)
ev3.screen.draw_line(x2, y2, x3, y3)
ev3.screen.draw_line(x3, y3, x1, y1)

# Wait some time to look at the shapes
wait(5000)
