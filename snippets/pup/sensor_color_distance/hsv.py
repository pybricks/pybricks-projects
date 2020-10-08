from pybricks.pupdevices import ColorDistanceSensor
from pybricks.parameters import Port
from pybricks.tools import wait

# Initialize the sensor.
sensor = ColorDistanceSensor(Port.A)

while True:
    # The standard color() method always "rounds" the
    # measurement to the nearest "whole" color.
    # That's useful for most applications.

    # But you can get the original hue, saturation,
    # and value without "rounding", as follows:
    color = sensor.hsv()

    # Print the results.
    print(color)

    # Wait so we can read the value.
    wait(500)
