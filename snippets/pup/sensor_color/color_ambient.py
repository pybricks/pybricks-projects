from pybricks.pupdevices import ColorSensor
from pybricks.parameters import Port
from pybricks.tools import wait

# Initialize the sensor.
sensor = ColorSensor(Port.A)

# Repeat forever.
while True:

    # Get the ambient color values. Instead of scanning the color of a surface,
    # this lets you scan the color of light sources like lamps or screens.
    hsv = sensor.hsv(surface=False)
    color = sensor.color(surface=False)

    # Get the ambient light intensity.
    ambient = sensor.ambient()

    # Print the measurements.
    print(hsv, color, ambient)

    # Point the sensor at a computer screen or colored light. Watch the color.
    # Also, cover the sensor with your hands and watch the ambient value.

    # Wait so we can read the printed line
    wait(100)
