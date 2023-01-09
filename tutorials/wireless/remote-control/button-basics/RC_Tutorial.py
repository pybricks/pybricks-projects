from pybricks.hubs import TechnicHub    # change hub type as necessary
from pybricks.pupdevices import Motor, Remote
from pybricks.parameters import Button, Color, Port

# Define the hub object. 
# For other hub types, change TechnicHub here and on the line 1 import 
hub = TechnicHub()

# This tutorial uses two motors on ports A and B
left_motor = Motor(Port.A)
right_motor = Motor(Port.B)

# Define the max and current motor speed to use
MAX_SPEED = 720       # deg/sec
speed = MAX_SPEED

# Try to connect to the remote
hub.light.on(Color.YELLOW)    # turn hub light yellow while trying to connect
rc = Remote()    # will stop the program if it can't connect
# Set status light on both hub and remote to green to indicate connection
hub.light.on(Color.GREEN)
rc.light.on(Color.GREEN)

# Get the set of buttons on the remote that start out pressed 
pressed = rc.buttons.pressed()

# The main loop repeatedly tests the remote buttons and reacts (forever)
while True:
    # Update the set of buttons that are currently pressed,
    # and also remember which ones were pressed the last time we checked.
    was_pressed = pressed
    pressed = rc.buttons.pressed()

    # 1. Press and hold Left Plus to spin the left motor
    if Button.LEFT_PLUS in pressed:
        left_motor.run(speed)
    else:
        left_motor.stop()

    # 2. Tap Left Minus to turn the left motor exactly 720 degrees backwards
    if Button.LEFT_MINUS in pressed and Button.LEFT_MINUS not in was_pressed:
        left_motor.run_angle(speed, -720)

    # 3. Press and hold Right Plus to spin the right motor forward,
    # or Right Minus to spin it backward, or neither to stop it.
    if Button.RIGHT_PLUS in pressed:
        right_motor.run(speed)
    elif Button.RIGHT_MINUS in pressed:
        right_motor.run(-speed)
    else:
        right_motor.stop()

    # 4. Press and hold Right Center to reduce the motor speed while doing 1-3
    if Button.RIGHT in pressed:
        speed = MAX_SPEED / 4
    else:
        speed = MAX_SPEED
