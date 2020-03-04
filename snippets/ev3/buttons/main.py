#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.tools import wait
from pybricks.parameters import Button

# Initialize the EV3
ev3 = EV3Brick()

# Wait until any of the buttons are pressed
while not any(ev3.buttons.pressed()):
    wait(10)

# Do something if the left button is pressed
if Button.LEFT in ev3.buttons.pressed():
    print("The left button is pressed.")

# Wait until all buttons are released
while any(ev3.buttons.pressed()):
    wait(10)
