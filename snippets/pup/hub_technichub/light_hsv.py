from pybricks.hubs import TechnicHub
from pybricks.parameters import Color
from pybricks.tools import wait

# Initialize the hub.
hub = TechnicHub()

# Show the color at 30% brightness.
hub.light.on(Color.RED * 0.3)

wait(2000)

# Use your own custom color.
hub.light.on(Color(h=30, s=100, v=50))

wait(2000)

# Go through all the colors.
for hue in range(360):
    hub.light.on(Color(hue))
    wait(10)
