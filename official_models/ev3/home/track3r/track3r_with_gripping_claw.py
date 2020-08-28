#!/usr/bin/env pybricks-micropython

"""
Example LEGO® MINDSTORMS® EV3 Track3r Program
---------------------------------------------

This program requires LEGO® EV3 MicroPython v2.0 downloadable at:
https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3

Building instructions can be found at:
https://www.lego.com/en-us/themes/mindstorms/buildarobot
"""

from pybricks.media.ev3dev import SoundFile
from pybricks.parameters import Button
from pybricks.tools import wait

from track3r_base import Track3r


class Track3rWithGrippingClaw(Track3r):
    """
    Track3r grips or releases its claw when the Beacon button is pressed
    (inspiration from LEGO Mindstorms EV3 Home Edition: Track3r: Tutorial #3)
    """
    is_gripping = False

    def grip_or_release_claw_by_ir_beacon(self, speed: float = 1000):
        if Button.BEACON in \
                self.ir_sensor.buttons(channel=self.ir_beacon_channel):
            if self.is_gripping:
                self.medium_motor.run(speed=-speed)
                self.ev3_brick.speaker.play_file(file=SoundFile.AIR_RELEASE)
                self.is_gripping = False

            else:
                self.medium_motor.run(speed=speed)
                self.ev3_brick.speaker.play_file(file=SoundFile.AIRBRAKE)
                self.is_gripping = True

            while Button.BEACON in \
                    self.ir_sensor.buttons(channel=self.ir_beacon_channel):
                pass

    def main(self, speed: float = 1000):
        while True:
            self.drive_by_ir_beacon(speed=speed)
            self.grip_or_release_claw_by_ir_beacon(speed=speed)
            wait(1)


if __name__ == '__main__':
    TRACK3R = Track3rWithGrippingClaw()
    TRACK3R.main(speed=1000)
