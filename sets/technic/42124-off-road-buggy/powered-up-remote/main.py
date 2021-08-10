# Remote is currently in beta. This program only works with firmware
# installed from <https://beta.pybricks.com>.

from pybricks.pupdevices import Motor, Remote
from pybricks.parameters import Port, Direction, Stop, Button
from pybricks.tools import wait

# Initialize the motors.
steer = Motor(Port.B)
front = Motor(Port.A, Direction.COUNTERCLOCKWISE)

# Lower the acceleration so the car starts and stops realistically.
front.control.limits(acceleration=1000)

# Connect to the remote.
remote = Remote()

# Find the steering endpoint on the left and right.
# The middle is in between.
left_end = steer.run_until_stalled(-200, then=Stop.HOLD)
right_end = steer.run_until_stalled(200, then=Stop.HOLD)

# We are now at the right. Reset this angle to be half the difference.
# That puts zero in the middle.
steer.reset_angle((right_end - left_end) / 2)
steer.run_target(speed=200, target_angle=0, wait=False)

# Now we can start driving!
while True:
    # Check which buttons are pressed.
    pressed = remote.buttons.pressed()

    # Choose the steer angle based on the left controls.
    steer_angle = 0
    if Button.LEFT_PLUS in pressed:
        steer_angle -= 75
    if Button.LEFT_MINUS in pressed:
        steer_angle += 75

    # Steer to the selected angle.
    steer.run_target(500, steer_angle, wait=False)

    # Choose the drive speed based on the right controls.
    drive_speed = 0
    if Button.RIGHT_PLUS in pressed:
        drive_speed += 1000
    if Button.RIGHT_MINUS in pressed:
        drive_speed -= 1000

    # Apply the selected speed.
    front.run(drive_speed)

    # Wait.
    wait(10)
