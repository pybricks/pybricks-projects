from pybricks.hubs import MoveHub
from pybricks.pupdevices import ColorDistanceSensor, Motor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase
from pybricks.tools import wait


##################################
# Declare how the robot is built #
##################################

# Uses the BOOST Move hub.
hub = MoveHub()

# Built-in motors are used as a drive base.
drive = DriveBase(
    Motor(Port.A, Direction.COUNTERCLOCKWISE),
    Motor(Port.B),
    37,  # wheel diameter
    65)  # axle track

# Uses the BOOST Color and Distance sensor.
sensor = ColorDistanceSensor(Port.C)

# Motor that actuates the head and the part on the front.
# The gears are configured for the head.
actuator = Motor(Port.D, Direction.COUNTERCLOCKWISE, gears=(24, 40))

#################################
# Define some helpful functions #
#################################

# Returns true if R2-D2 is standing upright.
def is_upright():
    # R2 is actually leaning slightly forward when "upright".
    return hub.imu.acceleration()[2] <= 0


# Makes R2-D2 stand up straight if he is not already.
def stand_up():
    # If we are already upright, there is nothing to do.
    if is_upright():
        return

    # Drive has to be stopped before changing settings.
    drive.stop()

    # Save the old settings to restore later.
    settings = drive.settings()

    # Set speed and acceleration high so that
    # we can make R2-D2 jerk forward or backward.
    drive.settings(1000, 5000)

    # Drive quickly and stop to make R2-D2 change position.
    drive.straight(170)
    drive.stop()

    # Restore the old settings.
    drive.settings(*settings)

    drive.straight(-40)
    wait(500)

    if not is_upright():
        raise RuntimeError('failed to stand up')


# Makes R2-D2 go to tripod mode if he is not already.
def tripod():
    # If we are already not upright, there is nothing to do.
    if not is_upright():
        return

    drive.straight(200)

    if is_upright():
        raise RuntimeError('failed to go to tripod mode')


# Shakes head back and forth.
def shake_head():
    actuator.run_angle(300, -45)
    actuator.run_angle(300, 90)
    actuator.run_angle(300, -90)
    actuator.run_angle(300, 90)
    actuator.run_angle(300, -45)


# Turns body while holding head still.
def stare_and_turn(angle):
    # This only works when standing up.
    stand_up()

    # The speed for turning the head is chosen to match the
    # drive base turn rate and wait=False allows both motors
    # to run at the same time.
    actuator.run_angle(drive.settings()[2], -angle, wait=False)
    drive.turn(angle)


#################################
# Show some useful information. #
#################################

print('starting:', 'upright' if is_upright() else 'tripod')

# If you want to adjust the settings, it can be useful
# to print the defaults so you know where to start.
# print('default drive settings', drive.settings())


################
# MAIN PROGRAM #
################

try:
    # Try to drive forward, turn around and come back.
    for _ in range(2):
        tripod()
        drive.straight(300)
        stand_up()
        drive.turn(180)

    # Print a message so that we know when the program
    # completed successfully.
    print('done!')
except Exception:
    # If there was an error while the program was running,
    # R2-D2 shakes his head in disappointment.
    shake_head()

    # Then we raise the error again so we can see what
    # it is.
    raise
