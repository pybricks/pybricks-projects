#!/usr/bin/env pybricks-micropython

"""
Example LEGO® MINDSTORMS® EV3 Track3r Program
---------------------------------------------

This program requires LEGO® EV3 MicroPython v2.0 downloadable at:
https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3

Building instructions can be found at:
https://www.lego.com/en-us/themes/mindstorms/buildarobot
"""

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Direction, Port
from pybricks.tools import wait

from rc_tank_util import RemoteControlledTank


class Track3r(RemoteControlledTank):
    WHEEL_DIAMETER = 26   # milimeters
    AXLE_TRACK = 140      # milimeters

    def __init__(
            self,
            left_track_motor_port: Port = Port.B,
            right_track_motor_port: Port = Port.C,
            medium_motor_port: Port = Port.A,
            ir_sensor_port: Port = Port.S4,
            ir_beacon_channel: int = 1):
        super().__init__(
            wheel_diameter=self.WHEEL_DIAMETER,
            axle_track=self.AXLE_TRACK,
            left_motor_port=left_track_motor_port,
            right_motor_port=right_track_motor_port,
            ir_sensor_port=ir_sensor_port,
            ir_beacon_channel=ir_beacon_channel)

        self.ev3_brick = EV3Brick()

        self.medium_motor = Motor(port=medium_motor_port,
                                  positive_direction=Direction.CLOCKWISE)

    def main(self, speed: float = 1000):
        """
        Driving Track3r around by the IR beacon
        """
        while True:
            self.drive_by_ir_beacon(speed=speed)
            wait(1)


if __name__ == '__main__':
    TRACK3R = Track3r()
    TRACK3R.main(speed=1000)
