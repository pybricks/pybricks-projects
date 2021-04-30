from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Port, Button, Stop
from pybricks.tools import wait

# Tuning parameters
SPEED_MAX = 1000
SPEED_TURN = 500
SPEED_OFFLINE = 400

# Initialize the hub, motors, and sensor
hub = InventorHub()
steer_motor = Motor(Port.A)
drive_motor = Motor(Port.B)
sensor = ColorSensor(Port.C)


def wait_for_button(b):
    # Wait for press
    while b not in hub.buttons.pressed():
        wait(10)
    # and release
    while b in hub.buttons.pressed():
        wait(10)


# Use the color saturation value to track line
def get_light():
    return sensor.hsv().s


def calibrate():
    global a_steer_limit
    global l_min, l_max, sign_edge

    # Find the Right and Left hard limits
    a_right_limit = steer_motor.run_until_stalled(400, then=Stop.BRAKE, duty_limit=100)
    a_left_limit = steer_motor.run_until_stalled(-400, then=Stop.BRAKE, duty_limit=100)

    # Calculate the steering limit as average of two extremes then reset
    # angle to the negative limit since steering motor is now at neg. extreme
    a_steer_limit = (a_right_limit - a_left_limit) // 2
    steer_motor.reset_angle(-a_steer_limit)

    # Scan from -30 to 30 to get min max of light sensor value
    steer_motor.run_target(1000, -30, then=Stop.BRAKE)
    l_min = 1024
    l_max = 0
    l_left = get_light()
    steer_motor.run(100)

    while steer_motor.angle() < 30:
        l = get_light()
        if l > l_max:
            l_max = l
        if l < l_min:
            l_min = l
        wait(5)

    steer_motor.stop()
    l_right = get_light()
    # sign_edge is positive 1 if left edge and -1 if right edge
    sign_edge = 1 if l_left < l_right else -1

    # Center the steering
    steer_motor.run_target(1000, 0, then=Stop.BRAKE, wait=False)


def track_speed_control():
    l_mid = (l_max + l_min + 1) // 2
    m = 20.0 / (l_max - l_mid)

    # Calculate a threshold to determine steering is not near the edge
    l_off_edge_thresh = (l_max - l_mid) * 0.7

    # Set max speed, acceleration, and max power for drive motor
    drive_motor.stop()  # must be stopped to set limits
    drive_motor.control.limits(1000, 2000, 100)

    while not any(hub.buttons.pressed()):
        # Get a new light value and subtract mid to get signed error from edge
        l = sign_edge * (get_light() - l_mid)

        # Create a new target for the steering motor to move toward the
        # approximate position of the edge
        a = steer_motor.angle()
        t = a - m * l

        # Clamp the target angle to within +- a_steer_limit
        t = min(t, a_steer_limit)
        t = max(t, -a_steer_limit)

        # Now update target to move toward edge of line
        steer_motor.track_target(t)

        # Speed control
        if abs(l) < l_off_edge_thresh:
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
    wait_for_button(Button.RIGHT)
    calibrate()
    track_speed_control()
