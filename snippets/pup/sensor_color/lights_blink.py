from pybricks.pupdevices import ColorSensor
from pybricks.parameters import Port
from pybricks.tools import wait

# Initialize the sensor.
sensor = ColorSensor(Port.A)

# Repeat forever.
while True:

    # Turn on one light at a time, at half the brightness.
    # Do this for all 3 lights and repeat that 5 times.
    for i in range(5):
        sensor.lights.on(50, 0, 0)
        wait(100)
        sensor.lights.on(0, 50, 0)
        wait(100)
        sensor.lights.on(0, 0, 50)
        wait(100)

    # Turn all lights on at maximum brightness.
    sensor.lights.on(100)
    wait(500)

    # Turn all lights off.
    sensor.lights.off()
    wait(500)
