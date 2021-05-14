#!/usr/bin/env pybricks-micropython


from pybricks.tools import wait

from rac3_truck import Rac3Truck


rac3_truck = Rac3Truck()

rac3_truck.reset()

wait(1000)

while True:
    rac3_truck.drive_by_ir_beacon()
