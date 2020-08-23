#!/usr/bin/env pybricks-micropython

"""
Example LEGO® MINDSTORMS® EV3 Gripp3r Program
---------------------------------------------

This program requires LEGO® EV3 MicroPython v2.0.
Download: https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3

Building instructions can be found at:
https://www.lego.com/en-us/themes/mindstorms/buildarobot
"""

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, InfraredSensor
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile
from pybricks.parameters import Button, Direction, Port, Stop
from pybricks.tools import wait


class RemoteControlledTank:
    """
    This reusable mixin provides the capability of driving a robot with a Driving Base by the IR beacon
    """
    def __init__(
            self,
            wheel_diameter: float, axle_track: float,   # both in milimeters
            left_motor_port: Port = Port.B, right_motor_port: Port = Port.C,
            ir_sensor_port: Port = Port.S4, ir_beacon_channel: int = 1):
        self.driver = DriveBase(left_motor=Motor(port=left_motor_port,
                                                 positive_direction=Direction.CLOCKWISE),
                                right_motor=Motor(port=right_motor_port,
                                                  positive_direction=Direction.CLOCKWISE),
                                wheel_diameter=wheel_diameter,
                                axle_track=axle_track)

        self.ir_sensor = InfraredSensor(port=ir_sensor_port)
        self.ir_beacon_channel = ir_beacon_channel
    
    
    def drive_by_ir_beacon(
            self,
            speed: float = 1000,    # mm/s
            turn_rate: float = 90   # rotational speed deg/s
        ):
        ir_beacon_button_pressed = set(self.ir_sensor.buttons(channel=self.ir_beacon_channel))

        # forward
        if ir_beacon_button_pressed == {Button.LEFT_UP, Button.RIGHT_UP}:
            self.driver.drive(
                speed=speed,
                turn_rate=0)

        # backward
        elif ir_beacon_button_pressed == {Button.LEFT_DOWN, Button.RIGHT_DOWN}:
            self.driver.drive(
                speed=-speed,
                turn_rate=0)

        # turn left on the spot
        elif ir_beacon_button_pressed == {Button.LEFT_UP, Button.RIGHT_DOWN}:
            self.driver.drive(
                speed=0,
                turn_rate=-turn_rate)

        # turn right on the spot
        elif ir_beacon_button_pressed == {Button.RIGHT_UP, Button.LEFT_DOWN}:
            self.driver.drive(
                speed=0,
                turn_rate=turn_rate)

        # turn left forward
        elif ir_beacon_button_pressed == {Button.LEFT_UP}:
            self.driver.drive(
                speed=speed,
                turn_rate=-turn_rate)

        # turn right forward
        elif ir_beacon_button_pressed == {Button.RIGHT_UP}:
            self.driver.drive(
                speed=speed,
                turn_rate=turn_rate)

        # turn left backward
        elif ir_beacon_button_pressed == {Button.LEFT_DOWN}:
            self.driver.drive(
                speed=-speed,
                turn_rate=turn_rate)

        # turn right backward
        elif ir_beacon_button_pressed == {Button.RIGHT_DOWN}:
            self.driver.drive(
                speed=-speed,
                turn_rate=-turn_rate)

        # otherwise stop
        else:
            self.driver.stop()


class Gripp3r(RemoteControlledTank):
    WHEEL_DIAMETER = 26   # milimeters
    AXLE_TRACK = 115      # milimeters


    def __init__(
            self,
            left_track_motor_port: Port = Port.B, right_track_motor_port: Port = Port.C,
            grip_motor_port: Port = Port.A,
            touch_sensor_port: Port = Port.S1,
            ir_sensor_port: Port = Port.S4, ir_beacon_channel: int = 1):
        super().__init__(
            wheel_diameter=self.WHEEL_DIAMETER, axle_track=self.AXLE_TRACK,
            left_motor_port=left_track_motor_port, right_motor_port=right_track_motor_port,
            ir_sensor_port=ir_sensor_port, ir_beacon_channel=ir_beacon_channel)

        self.ev3_brick = EV3Brick()

        self.grip_motor = Motor(port=grip_motor_port,
                                positive_direction=Direction.CLOCKWISE)

        self.touch_sensor = TouchSensor(port=touch_sensor_port)

        self.ir_sensor = InfraredSensor(port=ir_sensor_port)
        self.ir_beacon_channel = ir_beacon_channel


    def grip_or_release_by_ir_beacon(self, speed: float = 500):
        if Button.BEACON in self.ir_sensor.buttons(channel=self.ir_beacon_channel):
            if self.touch_sensor.pressed():
                self.ev3_brick.speaker.play_file(file=SoundFile.AIR_RELEASE)

                self.grip_motor.run_time(
                    speed=speed,
                    time=1000,
                    then=Stop.BRAKE,
                    wait=True)

            else:
                self.ev3_brick.speaker.play_file(file=SoundFile.AIRBRAKE)

                self.grip_motor.run(speed=-speed)

                while not self.touch_sensor.pressed():
                    pass

                self.grip_motor.stop()

            while Button.BEACON in self.ir_sensor.buttons(channel=self.ir_beacon_channel):
                pass


    def main(self):
        """
        Gripp3r's main program performing various capabilities
        """
        self.grip_motor.run_time(
            speed=-500,
            time=1000,
            then=Stop.BRAKE,
            wait=True)
    
        while True:
            self.drive_by_ir_beacon(speed=1000)
            self.grip_or_release_by_ir_beacon(speed=500)
            wait(1)


if __name__ == '__main__':
    GRIPP3R = Gripp3r()
    GRIPP3R.main()
