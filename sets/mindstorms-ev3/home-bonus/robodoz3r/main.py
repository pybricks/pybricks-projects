#!/usr/bin/env pybricks-micropython


from pybricks.media.ev3dev import SoundFile
from pybricks.tools import wait

from time import time

from robodoz3r import RoboDoz3r


robodoz3r = RoboDoz3r()

robodoz3r.ev3_brick.screen.print('ROBODOZ3R')

robodoz3r.ev3_brick.speaker.play_file(SoundFile.MOTOR_START)

motor_idle_start_time = time()
while time() - motor_idle_start_time <= 2:
    robodoz3r.ev3_brick.speaker.play_file(SoundFile.MOTOR_IDLE)

while True:
    while not robodoz3r.touch_sensor.pressed():
        robodoz3r.raise_or_lower_shovel_by_ir_beacon()
        robodoz3r.drive_by_ir_beacon(speed=1000)
        wait(10)

    robodoz3r.ev3_brick.speaker.play_file(SoundFile.AIRBRAKE)

    while not robodoz3r.touch_sensor.pressed():
        if robodoz3r.ir_sensor.distance() < 50:
            robodoz3r.driver.stop()

            wait(1000)

            robodoz3r.driver.straight(distance=-100)

            robodoz3r.driver.turn(angle=90)

        else:
            robodoz3r.driver.drive(
                speed=500,
                turn_rate=0)

        wait(10)

    robodoz3r.ev3_brick.speaker.play_file(SoundFile.AIRBRAKE)
