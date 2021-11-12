from pybricks.pupdevices import DCMotor, ColorDistanceSensor
from pybricks.tools import StopWatch
from pybricks.parameters import Port

# Initialize the motor and the sensor.
motor = DCMotor(Port.A)
sensor = ColorDistanceSensor(Port.B)

# These are the sensor reflection values in this setup.
# Adapt them to match your ambient light conditions.
LIGHT = 57
DARK = 16

# Threshold values. We add a bit of hysteresis to make
# sure we skip extra changes on the edge of each track.
hysteresis = (LIGHT - DARK) / 4
threshold_up = (LIGHT + DARK) / 2 + hysteresis
threshold_down = (LIGHT + DARK) / 2 - hysteresis

# Initial position state.
on_track = True
position = 0

# Desired drive speed in mm per second.
SPEED = 300

# It's two studs (16 mm) for each position increase.
MM_PER_COUNT = 16

# Start a timer.
watch = StopWatch()

while True:

    # Measure the reflection.
    reflection = sensor.reflection()

    # If the reflection exceeds the threshold, increment position.
    if (reflection > threshold_up and on_track) or (reflection < threshold_down and not on_track):
        on_track = not on_track
        position += 1
        
    # Compute the target position based on the time.
    target_count = watch.time() / 1000 * SPEED / MM_PER_COUNT

    # The duty cycle is the position error times a constant gain.
    duty = 2*(target_count - position)

    # Apply the duty cycle.
    motor.dc(duty)
