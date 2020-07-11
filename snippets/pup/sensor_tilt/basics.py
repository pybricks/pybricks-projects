from pybricks.pupdevices import TiltSensor
from pybricks.parameters import Port
from pybricks.tools import wait

# Initialize the sensor.
accel = TiltSensor(Port.A)

while True:
    # Read the tilt angles relative to the horizontal plane.
    pitch, roll = accel.tilt()

    # Print the values
    print("Pitch:", pitch, "Roll:", roll)

    # Wait some time so we can read what is printed.
    wait(100)
