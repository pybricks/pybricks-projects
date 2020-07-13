from pybricks.pupdevices import ColorSensor
from pybricks.parameters import Port
from pybricks.tools import wait

# Initialize the sensor.
sensor = ColorSensor(Port.A)

while True:
    # Read the color and reflection
    color = sensor.color()
    reflection = sensor.reflection()

    # Print the measured color and reflection.
    print(color, reflection)

    # Move the sensor around and see how
    # well you can detect colors.

    # Wait so we can read the value.
    wait(100)
