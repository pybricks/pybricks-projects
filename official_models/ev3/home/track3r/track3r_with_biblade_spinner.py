#!/usr/bin/env pybricks-micropython

"""
Example LEGO® MINDSTORMS® EV3 Track3r Program
---------------------------------------------

This program requires LEGO® EV3 MicroPython v2.0 downloadable at:
https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3

Building instructions can be found at:
https://www.lego.com/en-us/themes/mindstorms/buildarobot
"""

from pybricks.parameters import Button
from pybricks.tools import wait

from track3r_base import Track3r


class Track3rWithBiBladeSpinner(Track3r):
    """
    Track3r spins its blade when the Beacon button is pressed
    (inspiration from LEGO Mindstorms EV3 Home Edition: Track3r: Tutorial #5)
    """
    def spin_blade_by_ir_beacon(self, speed: float = 1000):
        if Button.BEACON in \
                self.ir_sensor.buttons(channel=self.ir_beacon_channel):
            self.medium_motor.run(speed=speed)

        else:
            self.medium_motor.stop()

    def main(self, speed: float = 1000):
        while True:
            self.drive_by_ir_beacon(speed=speed)
            self.spin_blade_by_ir_beacon(speed=speed)
            wait(1)


if __name__ == '__main__':
    TRACK3R = Track3rWithBiBladeSpinner()
    TRACK3R.main(speed=1000)
