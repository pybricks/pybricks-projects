#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.tools import print
from pybricks.parameters import Button

# Initialize the EV3
ev3 = EV3Brick()

# Check that all buttons are in the enum
checked = []
verify = [
    Button.LEFT,
    Button.RIGHT,
    Button.UP,
    Button.DOWN,
    Button.CENTER,
]

# Check ability to call pressed in tight loop
print("Wait until all buttons are released.")
while (any(ev3.buttons.pressed())):
    pass

# Check that all buttons work
print("Wait until all buttons have been pressed at least once.")

# Wait for all buttons to be checked
while len(checked) != len(verify):
    # Wait for any button and remember state:
    pressed = ev3.buttons.pressed()

    # Process pressed buttons
    for b in pressed:
        # Check that button is allowed
        if b not in verify:
            raise ValueError
        # Add button to checked buttons
        if b not in checked:
            print("You pressed:", b)
            checked.append(b)

print("SUCCESS")
