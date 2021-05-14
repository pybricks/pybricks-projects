#!/usr/bin/env pybricks-micropython


from bobb3e import Bobb3e

from pybricks.experimental import run_parallel


bobb3e = Bobb3e()

bobb3e.ev3_brick.screen.print('BOBB3E')

run_parallel(
    bobb3e.drive_or_operate_forks_by_ir_beacon,
    bobb3e.sound_alarm_whenever_reversing)
