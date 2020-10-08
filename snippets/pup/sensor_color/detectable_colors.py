from pybricks.pupdevices import ColorSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait

# Initialize the sensor.
sensor = ColorSensor(Port.A)

# First, decide which objects you want to detect.
# Then measure their color with the hsv() method,
# as shown in the previous example. Write them down
# as shown below. The name is optional, but it is
# useful when you print the color value.
green = Color(h=132, s=94, v=26, name='GREEN_BRICK')
magenta = Color(h=348, s=96, v=40, name='MAGENTA_BRICK')
brown = Color(h=17, s=78, v=15, name='BROWN_BRICK')
red = Color(h=359, s=97, v=39, name='RED_BRICK')

# Put your colors in a list or tuple.
# Including None is optional. Just omit it if
# you always want to get one of your colors.
my_colors = (green, magenta, brown, red, None)

# Save your colors.
sensor.detectable_colors(my_colors)

# color() works as usual, but it only
# returns one of your specified colors.
while True:
    color = sensor.color()

    # Print the color.
    print(color)

    # Check which one it is.
    if color == magenta:
        print("It works!")

    # Wait so we can read it.
    wait(100)
