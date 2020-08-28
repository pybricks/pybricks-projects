#!/usr/bin/env pybricks-micropython

"""
Example LEGO® MINDSTORMS® EV3 Track3r Program
---------------------------------------------

This program requires LEGO® EV3 MicroPython v2.0 downloadable at:
https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3

Building instructions can be found at:
https://www.lego.com/en-us/themes/mindstorms/buildarobot
"""

from pybricks.media.ev3dev import ImageFile, SoundFile
from pybricks.parameters import Button, Stop
from pybricks.tools import wait

from track3r_base import Track3r


class Track3rWithHeavyHammer(Track3r):
    """
    Track3r hammers down when the Beacon button is pressed
    (inspiration from LEGO Mindstorms EV3 Home Edition: Track3r: Tutorial #4)
    """
    def hammer_by_ir_beacon(self, speed: float = 1000):
        if Button.BEACON in \
                self.ir_sensor.buttons(channel=self.ir_beacon_channel):
            self.ev3_brick.screen.load_image(ImageFile.ANGRY)

            self.medium_motor.run_time(
                speed=speed,
                time=1000,
                then=Stop.COAST,
                wait=True)

            self.ev3_brick.speaker.play_file(file=SoundFile.LAUGHING_2)

            self.medium_motor.run_time(
                speed=-speed,
                time=1000,
                then=Stop.COAST,
                wait=True)

    def main(self, speed: float = 1000):
        self.medium_motor.run_time(
            speed=-200,
            time=1000,
            then=Stop.COAST,
            wait=True)

        while True:
            self.drive_by_ir_beacon(speed=speed)
            self.hammer_by_ir_beacon(speed=speed)
            wait(1)


if __name__ == '__main__':
    TRACK3R = Track3rWithHeavyHammer()
    TRACK3R.main(speed=1000)
