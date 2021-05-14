from pybricks.pupdevices import Motor, ColorDistanceSensor
from pybricks.parameters import Port, Direction, Stop
from pybricks.tools import wait

from usys import stdin
from uselect import poll

# Register the standard input so we can read keyboard presses.
keyboard = poll()
keyboard.register(stdin)

# Initialize the motors.
steer = Motor(Port.C)
front = Motor(Port.A, Direction.COUNTERCLOCKWISE)
rear = Motor(Port.B, Direction.COUNTERCLOCKWISE)

# Lower the acceleration so the car starts and stops realistically.
front.control.limits(acceleration=1000)
rear.control.limits(acceleration=1000)

# Find the steering endpoint on the left and right. The difference
# between them is the total angle it takes to go from left to right.
# The middle is in between.
left_end = steer.run_until_stalled(-200, then=Stop.HOLD)
right_end = steer.run_until_stalled(200, then=Stop.HOLD)

# We are now at the right. Reset this angle to be half the difference.
# That puts zero in the middle. From now on, running to 0 means to
# the middle.
steer.reset_angle((right_end - left_end) / 2)
steer.run_target(speed=200, target_angle=0, then=Stop.COAST)

# Now keep setting steering and driving based on keypad key:
#
#     <     ^     >
#      \    |    /
#       7   8   9
#
#  <--  4   5   6  -->
#
#       1   2   3
#      /    |    \
#     <     v     >

while True:

    # If there's no new character, skip the rest of the loop
    if not keyboard.poll(0):
        continue

    # Read the key.
    key = stdin.read(1)
    print("You pressed:", key)

    # If the keys 1, 4, or 7 are pressed, steer left
    # If the keys 3, 6, or 9 are pressed, steer right
    # Otherwise steer to the middle
    if key in ('1', '4', '7'):
        steer_angle = -90
    elif key in ('3', '6', '9'):
        steer_angle = 90
    else:
        steer_angle = 0

    steer.run_target(200, steer_angle, wait=False, then=Stop.COAST)

    # If the keys 7, 8, or 9 are pressed, go forward
    # If the keys 1, 2, or 3 are pressed, go backward
    # Otherwise stop driving
    if key in ('7', '8', '9'):
        sign = 1
    elif key in ('1', '2', '3'):
        sign = -1
    else:
        sign = 0

    front.run(sign * 800)
    rear.run(sign * 800)
