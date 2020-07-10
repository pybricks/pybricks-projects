from pybricks.pupdevices import TiltSensor, DCMotor
from pybricks.parameters import Port
from pybricks.tools import wait

# Initialize the train motor.
# If you have a motor with encoders, use the Motor class instead.
train = DCMotor(Port.A)

# Initialize the tilt sensor.
sensor = TiltSensor(Port.B)

# Measure the tilt while the train is on a flat surface.
pitch_start, roll_start = sensor.tilt()

# Start driving.
train.dc(-50)

# We need to reach a constant speed before we can check tilt again,
# because acceleration affects tilt. So we wait a second.
wait(1000)

# Wait for the train to sense the hill.
while True:
    pitch_now, roll_now = sensor.tilt()

    wait(10)

    # If we reached an extra 3 degrees, exit/break the loop.
    if pitch_now >= pitch_start + 8:
        break

# Drive backwards for a few seconds and then stop.
train.dc(40)
wait(3000)
train.dc(0)
