#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.tools import wait

from connection import SpikePrimeStreamReader

# Beep!
ev3 = EV3Brick()
ev3.speaker.beep()

# Create the connection. See README.md to find the address for your SPIKE hub.
spike = SpikePrimeStreamReader('F4:84:4C:AA:C8:A4')

# Now you can simply read values!
for i in range(100):
    print(spike.values())
    wait(100)
