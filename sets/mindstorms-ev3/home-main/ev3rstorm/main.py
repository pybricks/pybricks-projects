#!/usr/bin/env pybricks-micropython


from pybricks.media.ev3dev import ImageFile
from pybricks.tools import wait

from ev3rstorm import Ev3rstorm


ev3rstorm = Ev3rstorm()

ev3rstorm.ev3_brick.screen.load_image(ImageFile.TARGET)

while True:
    ev3rstorm.drive_by_ir_beacon(speed=1000)
    ev3rstorm.dance_randomly_if_ir_beacon_button_pressed()
    ev3rstorm.blast_bazooka_if_touched()
    wait(1)
