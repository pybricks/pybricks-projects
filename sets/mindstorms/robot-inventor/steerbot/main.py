from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Port, Button, Stop
from pybricks.tools import wait


# Initialize the hub, motors, and sensor
hub = InventorHub()
steer_motor = Motor(Port.A)
drive_motor = Motor(Port.B)
sensor = ColorSensor(Port.C)


def WaitForButton(b):
    # Wait for press
    while b not in hub.buttons.pressed():
        wait (10)
    # and release
    while b in hub.buttons.pressed():
        wait (10)


# Use the color saturation value to track line
def GetLight():
    return (sensor.hsv().s)


def Calibrate():
    global aSteerLimit
    global lMin, lMax, signEdge

    # Find the Right and Left hard limits
    aRightLimit = steer_motor.run_until_stalled(400, then=Stop.BRAKE, duty_limit=100)
    aLeftLimit = steer_motor.run_until_stalled(-400, then=Stop.BRAKE, duty_limit=100)

    # Calculate the steering limit as average of two extremes then reset
    # angle to the negative limit since steering motor is now at neg. extreme
    aSteerLimit = (aRightLimit-aLeftLimit)//2
    steer_motor.reset_angle(-aSteerLimit)

    # Scan from -30 to 30 to get min max of light sensor value
    steer_motor.run_target(1000,-30, then=Stop.BRAKE)
    lMin = 1024; lMax = 0
    lLeft = GetLight()
    steer_motor.run(100)
    c = 0
    while steer_motor.angle() < 30:
        c += 1
        l = GetLight()
        if l > lMax: lMax = l
        if l < lMin: lMin = l
        wait(5)
    steer_motor.stop()
    lRight = GetLight()
    # signEdge is positive 1 if left edge and -1 if right edge
    signEdge = 1 if lLeft < lRight else -1

    # Center the steering
    steer_motor.run_target(1000,0,then=Stop.BRAKE,wait=False)


SPEED_MAX = 1000
SPEED_TURN = 500
SPEED_OFFLINE = 400


def TrackSpeedControl():
    global lMin, lMax, signEdge
    global aSteerLimit

    lMid = (lMax+lMin+1)//2
    m = 20.0/(lMax-lMid)

    # Calculate a threshold to determine steering is not near the edge
    lOffEdgeThresh = (lMax-lMid) * 0.7

    # Set max speed, acceleration, and max power for drive motor
    drive_motor.stop()  # must be stopped to set limits
    drive_motor.control.limits(1000,2000,100)

    while hub.buttons.pressed() == []:
        # Get a new light value and subtract mid to get signed error from edge
        l = signEdge * (GetLight()-lMid)

        # Create a new target for the steering motor to move toward the
        # approximate position of the edge
        a = steer_motor.angle()
        t = a - m*l

        # Clamp the target angle to within +- aSteerLimit
        t = min(t, aSteerLimit)
        t = max(t, -aSteerLimit)

        # Now update target to move toward edge of line
        steer_motor.track_target(t)

        # Speed control
        if abs(l) < lOffEdgeThresh:
            # On edge of line
            if abs(t) < 25:
                # and going straight
                drive_motor.run(SPEED_MAX)
            else:
                drive_motor.run(SPEED_TURN)
        else:
            drive_motor.run(SPEED_OFFLINE)

        wait(3)

    drive_motor.run(0)
    steer_motor.track_target(0)
    wait(200)
    steer_motor.stop()
    drive_motor.stop()
    while not any(hub.buttons.pressed()):
        wait(10)


while True:
    WaitForButton(Button.RIGHT)
    Calibrate()
    TrackSpeedControl()
