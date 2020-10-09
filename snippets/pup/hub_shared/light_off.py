from pybricks.hubs import ExampleHub
from pybricks.parameters import Color
from pybricks.tools import wait

# Initialize the hub.
hub = ExampleHub()

# Turn the light on and off 5 times.
for i in range(5):

    hub.light.on(Color.RED)
    wait(1000)

    hub.light.off()
    wait(500)
