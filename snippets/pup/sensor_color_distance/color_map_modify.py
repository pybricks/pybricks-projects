from pybricks.pupdevices import ColorDistanceSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait

# Initialize the sensor.
sensor = ColorDistanceSensor(Port.A)

# Get the current color settings.
hues, saturation, values = sensor.color_map()

# Let's say we have used the hsv() method to determine
# that the orange hue is 10. We can add it like this.
hues[Color.ORANGE] = 10

# Also, let's say that we are not interested in blue.
# So, we remove it from the hues dictionary.
hues.pop(Color.BLUE)

# Now save the new settings
sensor.color_map(hues, saturation, values)

# Now use the color() method as usual. Now it can also detect ORANGE
# and it will not report BLUE, because we removed it from the hues.
while True:
    print(sensor.color())
    wait(100)
