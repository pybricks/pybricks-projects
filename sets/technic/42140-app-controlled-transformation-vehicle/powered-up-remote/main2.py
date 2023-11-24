from pybricks.pupdevices import Motor, Remote
from pybricks.hubs import TechnicHub
from pybricks.parameters import Button, Color, Direction, Port
from pybricks.tools import wait, StopWatch

# This drives like a car.
# Left +/- control going forwards/backwards, and right +/- turn.
# When the vehicle is moving turn is gradual, when it's stationary turn is faster.

remote = Remote()

hub = TechnicHub()

# Set very high speed limits to ensure maximum is reached.
DRIVE_SPEED = 10000
TURN_SPEED = 650
DRIVE_ACCELERATION = 7000

# Initialize the motors.
right_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
left_motor = Motor(Port.B)

left_motor.control.limits(acceleration=DRIVE_ACCELERATION)
right_motor.control.limits(acceleration=DRIVE_ACCELERATION)

while True:
    # Check which buttons are pressed
    wait(10)
    pressed = remote.buttons.pressed()

    # Choose forward/backward and turn right/left based on pressed buttons
    left_speed = 0
    right_speed = 0
    pitch, roll = hub.imu.tilt()
    sign = -1 if abs(roll) > 90 else 1
    speed = sign * DRIVE_SPEED
    turn = sign * TURN_SPEED
    if Button.LEFT_PLUS in pressed or Button.LEFT_MINUS in pressed:
        # Going forwards/backwards
        left_speed = speed
        right_speed = speed

        # Turn slowly when moving
        turn_right = Button.RIGHT_PLUS in pressed
        turn_left = Button.RIGHT_MINUS in pressed
        if (turn_right and sign > 0) or (turn_left and sign < 0):
            right_speed = turn
        elif turn_right or turn_left:
            left_speed = turn

        if Button.LEFT_MINUS in pressed:
            left_speed *= -1
            right_speed *= -1
    else:
        # Not moving, fast turn
        if Button.RIGHT_PLUS in pressed:
            left_speed = DRIVE_SPEED
            right_speed = -DRIVE_SPEED
        if Button.RIGHT_MINUS in pressed:
            left_speed = -DRIVE_SPEED
            right_speed = DRIVE_SPEED

    # Activate the driving motors.
    left_motor.run(left_speed)
    right_motor.run(right_speed)
