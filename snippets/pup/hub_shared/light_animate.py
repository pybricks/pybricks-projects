from pybricks.hubs import ExampleHub
from pybricks.parameters import Color
from pybricks.tools import wait
# MOVEHUB SKIP_NEXT 1
from math import sin, pi

# Initialize the hub.
hub = ExampleHub()

# Make an animation with multiple colors.
hub.light.animate([Color.RED, Color.GREEN, None], interval=500)

wait(10000)

# MOVEHUB SKIP_NEXT 6
# Make the color RED grow faint and bright using a sine pattern.
hub.light.animate(
    [Color.RED * (0.5 * sin(i / 15 * pi) + 0.5) for i in range(30)], 40)

wait(10000)

# Cycle through a rainbow of colors.
hub.light.animate([Color(h=i*8) for i in range(45)], interval=40)

wait(10000)
