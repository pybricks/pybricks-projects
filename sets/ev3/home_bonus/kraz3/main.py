#!/usr/bin/env pybricks-micropython


from pybricks.experimental import run_parallel

from kraz3 import Kraz3


kraz3 = Kraz3()

run_parallel(
    kraz3.keep_driving_by_ir_beacon,
    kraz3.kungfu_maneouver_whenever_touched_or_remote_controlled,
    kraz3.keep_reacting_to_colors)
