from pybricks.hubs import InventorHub
from pybricks.parameters import Color
from pybricks.tools import wait

# Initialize the hub
hub = InventorHub()

# Keep blinking red on and off.
hub.light.blink(Color.RED, [500, 500])

wait(10000)

# Keep blinking green slowly and then quickly.
hub.light.blink(Color.GREEN, [500, 500, 50, 900])

wait(10000)
