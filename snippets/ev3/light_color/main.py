#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.tools import wait
from pybricks.parameters import Color

# Initialize the EV3
ev3 = EV3Brick()

# Turn on a red light
ev3.light.on(Color.RED)

# Wait
wait(1000)

# Turn the light off
ev3.light.off()
