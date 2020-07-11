from pybricks.pupdevices import Light
from pybricks.parameters import Port
from pybricks.tools import wait

# Initialize the light.
light = Light(Port.A)

# Blink the light forever.
while True:
    # Turn the light on at 100% brightness.
    light.on(100)
    wait(500)

    # Turn the light off.
    light.off()
    wait(500)
