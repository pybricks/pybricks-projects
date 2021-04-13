#!/usr/bin/env pybricks-micropython


from pybricks.parameters import Stop
from pybricks.tools import wait

from gripp3r import Gripp3r


gripp3r = Gripp3r()

gripp3r.gripping_motor.run_time(
    speed=-500,
    time=1000,
    then=Stop.COAST,
    wait=True)

while True:
    gripp3r.drive_by_ir_beacon(speed=1000)
    gripp3r.grip_or_release_by_ir_beacon(speed=500)
    wait(1)
