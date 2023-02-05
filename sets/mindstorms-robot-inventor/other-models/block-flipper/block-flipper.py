from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = InventorHub()
lift = Motor(Port.A)
turntable = Motor(Port.B)
wrist = Motor(Port.D)
claw = Motor(Port.F)

# This is beyond a max motor speed (deg/s) and so ensures full speed
FULL_SPEED = 2000

# Turntable, lift, and claw positions
LEFT_POS = 115
CENTER_POS = 0
RIGHT_POS = -115
LIFT_UP_POS = 100
LIFT_DOWN_POS = 5
CLAW_OPEN_POS = -50
CLAW_CLOSED_POS = 0

# Get the default motor max speed, acceleration, and torque
(max_speed, accel, torque) = claw.control.limits()  


# Get the motors ready at their starting position
def setup():
    # Increase the default acceleration for the claw, turntable, and wrist
    claw.control.limits(FULL_SPEED, accel * 5, torque * 5)
    turntable.control.limits(FULL_SPEED, accel * 5, torque * 5)
    wrist.control.limits(FULL_SPEED, accel * 3, torque)

    # Decrease precision for the lift and claw since these are critical path
    (speed_slop, pos_slop) = claw.control.target_tolerances()
    claw.control.target_tolerances(speed_slop * 4, pos_slop * 4)
    lift.control.target_tolerances(speed_slop * 2, pos_slop * 2)

    # If the wrist starts upside down, then we need to first close and lift it
    # before it gets flipped to 0, to keep it from hitting the platform.
    if abs(wrist.angle()) > 90:
        claw.run_target(FULL_SPEED, CLAW_CLOSED_POS, wait=False)
        lift.run_target(FULL_SPEED, LIFT_UP_POS)
        if wrist.angle() < -90:   # then run_target would go the wrong way 
            wrist.reset_angle(360 + wrist.angle())  # forces counter-clockwise

    # Start with turntable centered, lift down, wrist upright, and claw open 
    turntable.run_target(FULL_SPEED, CENTER_POS, wait=False, then=Stop.BRAKE)
    lift.run_target(FULL_SPEED, LIFT_DOWN_POS, wait=False, then=Stop.BRAKE)
    wrist.run_target(FULL_SPEED, 0, wait=False, then=Stop.BRAKE)
    claw.run_target(FULL_SPEED, CLAW_OPEN_POS)
    wait(500)    # give all motors time to finish


# Start lifting up and wait a bit to be clear to rotate
def start_lifting():
    # Use higher acceleration and torque for the lift when lifting up
    lift.control.limits(FULL_SPEED, accel * 2, torque * 2)
    lift.run_target(FULL_SPEED, LIFT_UP_POS, wait=False)
    wait(150)


# Move the turntable to pos, then lower the lift, overlapping the motions
# during the final specified degrees of turntable movement.
def turn_and_lower(pos, overlap):
    turntable.run_target(FULL_SPEED, pos, wait=False)
    while abs(turntable.angle() - pos) > overlap:
        pass
    # Use faster acceleration, default decelleration, and very low torque 
    # for the lift when lowering because gravity is also pulling it down.
    lift.control.limits(FULL_SPEED, (accel * 2, accel), torque / 10)
    lift.run_target(FULL_SPEED, LIFT_DOWN_POS)


# Move a block from source_pos to dest_pos.
# The arm is assumed to start down, open, and not at source_pos.
def move(source_pos, dest_pos):
    # Raise up and move to source
    start_lifting()
    turn_and_lower(source_pos, 400)

    # Grab the block with a short burst of claw power then maintain light grip
    claw.dc(100)
    wait(70)
    claw.dc(35)

    # Lift and invert the block
    start_lifting()
    if abs(wrist.angle()) > 90:
        wrist.run_angle(FULL_SPEED, -180, wait=False)
    else:
        wrist.run_angle(FULL_SPEED, 180, wait=False)

    # Pivot and lower to the destination platform, then open claw to release 
    turn_and_lower(dest_pos, 150)
    claw.run_target(FULL_SPEED, CLAW_OPEN_POS, wait=False)


# Main program
setup()
while True:
    # This 3-move sequence can repeat forever
    move(LEFT_POS, CENTER_POS)
    move(RIGHT_POS, LEFT_POS)
    move(CENTER_POS, RIGHT_POS)
