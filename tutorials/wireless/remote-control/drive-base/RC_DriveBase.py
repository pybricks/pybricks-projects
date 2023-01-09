from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, Remote
from pybricks.parameters import Button, Color, Direction, Port, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

# Define objects for a simple two motor rover using a DriveBase 
hub = InventorHub()
left_motor = Motor(Port.A, positive_direction=Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.B, positive_direction=Direction.CLOCKWISE)
drive_base = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=96)

# Speeds and accelerations to use
STRAIGHT_SPEED = 300    # straight driving speed (mm/sec)
TURN_RATE = 150         # turning rate (deg/sec)

# Connect to the remote
hub.light.on(Color.YELLOW)    # turn hub light yellow while trying to connect
rc = Remote()    # will stop the program if it can't connect
# Set status light on both hub and remote to green to indicate connection
hub.light.on(Color.GREEN)
rc.light.on(Color.GREEN)

# The main loop repeatedly tests the remote buttons and reacts
while True:
    # Get the set of buttons that are currently pressed,
    pressed = rc.buttons.pressed()

    # Determine what straight driving speed to use
    if (Button.LEFT_PLUS in pressed):
        speed = STRAIGHT_SPEED
    elif (Button.LEFT_MINUS in pressed):
        speed = -STRAIGHT_SPEED
    else:
        speed = 0

    # Determine what turn rate to use
    if (Button.RIGHT_PLUS in pressed):
        turn_rate = TURN_RATE
    elif (Button.RIGHT_MINUS in pressed):
        turn_rate = -TURN_RATE
    else:
        turn_rate = 0

    # Update the driving and turning speeds
    drive_base.drive(speed, turn_rate)

