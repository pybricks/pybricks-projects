from pybricks.pupdevices import Light
from pybricks.parameters import Port
from pybricks.tools import wait, StopWatch

# The math module is part of standard MicroPython:
# https://docs.micropython.org/en/latest/library/math.html
from math import pi, cos

# Initialize the light and a StopWatch.
light = Light(Port.A)
watch = StopWatch()

# Cosine pattern properties.
PERIOD = 2000
MAX = 100

# Make the brightness fade in and out.
while True:
    # Get phase of the cosine.
    phase = watch.time()/PERIOD*2*pi

    # Evaluate the brightness.
    brightness = (0.5 - 0.5*cos(phase))*MAX

    # Set light brightness and wait a bit.
    light.on(brightness)
    wait(10)
