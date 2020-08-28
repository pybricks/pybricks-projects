#!/usr/bin/env pybricks-micropython

"""
Example LEGO® MINDSTORMS® EV3 R3ptar Program
--------------------------------------------

This program requires LEGO® EV3 MicroPython v2.0 downloadable at:
https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3

Building instructions can be found at:
https://www.lego.com/en-us/themes/mindstorms/buildarobot
"""

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, InfraredSensor
from pybricks.media.ev3dev import SoundFile
from pybricks.parameters import Button, Direction, Port, Stop
from pybricks.tools import wait


class R3ptar:
    """
    R3ptar can be driven around by the IR Remote Control,
    strikes when the Beacon button is pressed,
    and hisses when the Touch Sensor is pressed
    (inspiration from LEGO Mindstorms EV3 Home Edition: R3ptar: Tutorial #4)
    """

    def __init__(
            self,
            steering_motor_port: Port = Port.A,
            driving_motor_port: Port = Port.B,
            striking_motor_port: Port = Port.D,
            touch_sensor_port: Port = Port.S1,
            ir_sensor_port: Port = Port.S4,
            ir_beacon_channel: int = 1):
        self.ev3_brick = EV3Brick()

        self.steering_motor = Motor(port=steering_motor_port,
                                    positive_direction=Direction.CLOCKWISE)
        self.driving_motor = Motor(port=driving_motor_port,
                                   positive_direction=Direction.CLOCKWISE)
        self.striking_motor = Motor(port=striking_motor_port,
                                    positive_direction=Direction.CLOCKWISE)

        self.touch_sensor = TouchSensor(port=touch_sensor_port)

        self.ir_sensor = InfraredSensor(port=ir_sensor_port)
        self.ir_beacon_channel = ir_beacon_channel

    def drive_by_ir_beacon(
            self,
            speed: float = 1000,    # mm/s
            ):
        ir_beacons_pressed = \
            set(self.ir_sensor.buttons(channel=self.ir_beacon_channel))

        if ir_beacons_pressed == {Button.LEFT_UP, Button.RIGHT_UP}:
            self.driving_motor.run(speed=speed)

        elif ir_beacons_pressed == {Button.LEFT_DOWN, Button.RIGHT_DOWN}:
            self.driving_motor.run(speed=-speed)

        elif ir_beacons_pressed == {Button.LEFT_UP}:
            self.steering_motor.run(speed=-500)
            self.driving_motor.run(speed=speed)

        elif ir_beacons_pressed == {Button.RIGHT_UP}:
            self.steering_motor.run(speed=500)
            self.driving_motor.run(speed=speed)

        elif ir_beacons_pressed == {Button.LEFT_DOWN}:
            self.steering_motor.run(speed=-500)
            self.driving_motor.run(speed=-speed)

        elif ir_beacons_pressed == {Button.RIGHT_DOWN}:
            self.steering_motor.run(speed=500)
            self.driving_motor.run(speed=-speed)

        else:
            self.steering_motor.hold()
            self.driving_motor.stop()

    def strike_by_ir_beacon(self, speed: float = 1000):
        if Button.BEACON in \
                self.ir_sensor.buttons(channel=self.ir_beacon_channel):
            self.striking_motor.run_time(
                speed=speed,
                time=1000,
                then=Stop.COAST,
                wait=True)

            self.striking_motor.run_time(
                speed=-speed,
                time=1000,
                then=Stop.COAST,
                wait=True)

            while Button.BEACON in \
                    self.ir_sensor.buttons(channel=self.ir_beacon_channel):
                pass

    def hiss_if_touched(self):
        if self.touch_sensor.pressed():
            self.ev3_brick.speaker.play_file(file=SoundFile.SNAKE_HISS)

    def main(self, speed: float = 1000):
        """
        R3ptar's main program performing various capabilities
        """
        while True:
            self.drive_by_ir_beacon(speed=speed)
            self.strike_by_ir_beacon(speed=speed)
            self.hiss_if_touched()
            wait(1)


if __name__ == '__main__':
    R3PTAR = R3ptar()
    R3PTAR.main(speed=1000)
