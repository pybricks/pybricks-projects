#!/usr/bin/env pybricks-micropython


from pybricks.tools import wait

from r3ptar import R3ptar


r3ptar = R3ptar()

while True:
    r3ptar.drive_by_ir_beacon(speed=1000)
    r3ptar.strike_by_ir_beacon(speed=1000)
    r3ptar.hiss_if_touched()
    wait(1)
