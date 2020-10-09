from pybricks.hubs import MoveHub
from pybricks.parameters import Color
from pybricks.tools import wait

# Initialize the hub.
hub = MoveHub()

# Make an animation with multiple colors.
hub.light.animate([Color.RED, Color.GREEN, None], interval=500)

wait(10000)

# Cycle through a rainbow of colors.
hub.light.animate([Color(h=i*8) for i in range(45)], interval=40)

wait(10000)
