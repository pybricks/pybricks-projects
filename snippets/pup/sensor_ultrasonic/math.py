from pybricks.pupdevices import UltrasonicSensor
from pybricks.parameters import Port
from pybricks.tools import wait, StopWatch

# The math module is part of standard MicroPython:
# https://docs.micropython.org/en/latest/library/math.html
from math import pi, sin

# Initialize the sensor.
eyes = UltrasonicSensor(Port.A)

# Initialize a timer.
watch = StopWatch()

# We want one full light cycle to last three seconds.
PERIOD = 3000

while True:
    # The phase is where we are in the unit circle now.
    phase = watch.time()/PERIOD*2*pi

    # Each light follows a sine wave with a mean of 50, with an amplitude of 50.
    # We offset this sine wave by 90 degrees for each light, so that all the
    # lights do something different.
    brightness = [sin(phase + offset*pi/2) * 50 + 50 for offset in range(4)]

    # Set the brightness values for all lights. The * symbol unpacks the list
    # of brightness values into separate arguments.
    eyes.lights.on(*brightness)

    # Wait some time.
    wait(50)
