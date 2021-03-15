"""
This program is for Kiki the Dog.

Follow the corresponding building instructions in the LEGO® SPIKE™ Prime App.

Kiki shall respond to the blue, yellow or green objects by displaying something
on the Hub's screen.
"""

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import ColorSensor
from pybricks.parameters import Color, Icon, Port


# Configure the Hub and the Color Sensor
hub = PrimeHub()
color_sensor = ColorSensor(Port.B)


# Kiki walks around and sees things
while True:
    # if he sees blue, he thinks it's the sky above
    if color_sensor.color() == Color.BLUE:
        hub.display.image([
            [100, 100, 100, 100, 100],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ])

    # if he sees yellow, he thinks it's a house
    elif color_sensor.color() == Color.YELLOW:
        hub.display.image(Icon.UP)

    # if he sees green, he thinks it's the grass below
    elif color_sensor.color() == Color.GREEN:
        hub.display.image([
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [100, 100, 100, 100, 100]
        ])

    else:
        hub.display.off()
