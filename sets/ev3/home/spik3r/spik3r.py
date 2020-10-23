#!/usr/bin/env pybricks-micropython

"""
Example LEGO® MINDSTORMS® EV3 Spik3r Program
--------------------------------------------

This program requires LEGO® EV3 MicroPython v2.0 downloadable at:
https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3

Building instructions can be found at:
https://www.lego.com/en-us/themes/mindstorms/buildarobot
"""


from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor, InfraredSensor
from pybricks.media.ev3dev import ImageFile, SoundFile
from pybricks.parameters import Button, Direction, Port, Stop
from pybricks.tools import wait


class Spik3r:
    def __init__(
            self,
            crushing_claw_motor_port: Port = Port.A,
            moving_motor_port: Port = Port.B,
            lightning_tail_motor_port: Port = Port.D,
            touch_sensor_port: Port = Port.S1,
            color_sensor_port: Port = Port.S3,
            ir_sensor_port: Port = Port.S4,
            ir_beacon_channel: int = 1):
        self.ev3_brick = EV3Brick()

        self.crushing_claw_motor = \
            Motor(port=crushing_claw_motor_port,
                  positive_direction=Direction.CLOCKWISE)
        self.moving_motor = \
            Motor(port=moving_motor_port,
                  positive_direction=Direction.CLOCKWISE)
        self.lightning_tail_motor = \
            Motor(port=lightning_tail_motor_port,
                  positive_direction=Direction.CLOCKWISE)

        self.ir_sensor = InfraredSensor(port=ir_sensor_port)
        self.ir_beacon_channel = ir_beacon_channel

        self.touch_sensor = TouchSensor(port=touch_sensor_port)
        self.color_sensor = ColorSensor(port=color_sensor_port)

    def sting_by_ir_beacon(self, speed: float = 1000):
        """
        Spik3r stings with its Lightning Tail when the Beacon button is pressed
        (inspiration from LEGO Mindstorms EV3 Home Ed.: Spik3r: Tutorial #1)
        """
        if Button.BEACON in \
                self.ir_sensor.buttons(channel=self.ir_beacon_channel):
            self.lightning_tail_motor.run_angle(
                speed=-750,
                rotation_angle=220,
                then=Stop.HOLD,
                wait=False)

            self.ev3_brick.speaker.play_file(file=SoundFile.ERROR_ALARM)

            self.lightning_tail_motor.run_time(
                speed=-speed,
                time=1000,
                then=Stop.COAST,
                wait=True)

            self.lightning_tail_motor.run_time(
                speed=speed,
                time=1000,
                then=Stop.COAST,
                wait=True)

            while Button.BEACON in \
                    self.ir_sensor.buttons(channel=self.ir_beacon_channel):
                pass

    def move_by_ir_beacon(self, speed: float = 1000):
        """
        Spik3r moves forward when the IR Beacon's two Up buttons are pressed,
        and turns right when only the Right Up button is pressed
        (inspiration from LEGO Mindstorms EV3 Home Ed.: Spik3r: Tutorial #2)
        """
        ir_buttons_pressed = \
            set(self.ir_sensor.buttons(channel=self.ir_beacon_channel))

        if ir_buttons_pressed == {Button.RIGHT_UP, Button.LEFT_UP}:
            self.moving_motor.run(speed=speed)

        elif ir_buttons_pressed == {Button.RIGHT_UP}:
            self.moving_motor.run(speed=-speed)

        else:
            self.moving_motor.stop()

    def pinch_if_touched(self, speed: float = 1000):
        """
        Spik3r crushes objects with its Claw when the Touch Sensor is pressed
        (inspiration from LEGO Mindstorms EV3 Home Ed.: Spik3r: Tutorial #3)
        """
        if self.touch_sensor.pressed():
            self.crushing_claw_motor.run_time(
                speed=speed,
                time=1000,
                then=Stop.COAST,
                wait=True)

            self.crushing_claw_motor.run_time(
                speed=-speed,
                time=1000,
                then=Stop.COAST,
                wait=True)

    def main(self, speed: float = 1000):
        """
        Spik3r's main program performing various capabilities
        """
        self.ev3_brick.screen.load_image(ImageFile.WARNING)

        while True:
            self.move_by_ir_beacon(speed=speed)
            self.sting_by_ir_beacon(speed=speed)
            self.pinch_if_touched(speed=speed)
            wait(1)


if __name__ == '__main__':
    SPIK3R = Spik3r()
    SPIK3R.main(speed=1000)
