from pybricks.pupdevices import ColorDistanceSensor
from pybricks.parameters import Port
from pybricks.tools import wait

# Initialize the sensor.
sensor = ColorDistanceSensor(Port.A)

# Show the default color map.
print(sensor.color_map())

while True:
    # Read the HSV values.
    h, s, v = sensor.hsv()

    # Read the corresponding color based on the existing settings.
    color = sensor.color()

    # Print the measured values.
    print("Hue:", h, "Sat:", s, "Val:", v, "Col:", color)

    # Wait so we can read the value.
    wait(100)
