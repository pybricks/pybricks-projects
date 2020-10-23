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


class Track3rWithBlastingBazooka(Track3r):
    """
    Track3r blasts his bazooka when the Beacon button is pressed
    (inspiration from LEGO Mindstorms EV3 Home Edition: Track3r: Tutorial #2)
    """
    def blast_bazooka_by_ir_beacon(self, speed: float = 1000):
        if Button.BEACON in \
                self.ir_sensor.buttons(channel=self.ir_beacon_channel):
            self.medium_motor.run_angle(
                speed=speed,
                rotation_angle=3 * 360,   # about 3 rotations for 1 shot
                then=Stop.HOLD,
                wait=True)

            self.ev3_brick.speaker.play_file(file=SoundFile.LAUGHING_1)

            while Button.BEACON in \
                    self.ir_sensor.buttons(channel=self.ir_beacon_channel):
                pass

    def main(self, speed: float = 1000):
        self.ev3_brick.screen.load_image(ImageFile.PINCHED_MIDDLE)

        while True:
            self.drive_by_ir_beacon(speed=speed)
            self.blast_bazooka_by_ir_beacon(speed=speed)
            wait(1)


if __name__ == '__main__':
    TRACK3R = Track3rWithBlastingBazooka()
    TRACK3R.main(speed=1000)
