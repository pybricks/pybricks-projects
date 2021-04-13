#!/usr/bin/env pybricks-micropython


from pybricks.media.ev3dev import ImageFile
from pybricks.tools import wait

from spik3r import Spik3r


spik3r = Spik3r()

spik3r.ev3_brick.screen.load_image(ImageFile.WARNING)

while True:
    spik3r.move_by_ir_beacon(speed=1000)
    spik3r.sting_by_ir_beacon(speed=1000)
    spik3r.pinch_if_touched(speed=1000)
    wait(1)
