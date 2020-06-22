#!/usr/bin/env pybricks-micropython

"""
Example LEGO® MINDSTORMS® EV3 Track3r Program
---------------------------------------------

This program requires LEGO® EV3 MicroPython v2.0.
Download: https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3

Building instructions can be found at:
https://www.lego.com/en-us/themes/mindstorms/buildarobot
"""

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, InfraredSensor
from pybricks.media.ev3dev import ImageFile, SoundFile
from pybricks.robotics import DriveBase
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


class Track3r(RemoteControlledTank):
    WHEEL_DIAMETER = 26   # milimeters
    AXLE_TRACK = 140      # milimeters


    def __init__(
            self,
            left_track_motor_port: Port = Port.B, right_track_motor_port: Port = Port.C,
            medium_motor_port: Port = Port.A,
            ir_sensor_port: Port = Port.S4, ir_beacon_channel: int = 1):
        super().__init__(
            wheel_diameter=self.WHEEL_DIAMETER, axle_track=self.AXLE_TRACK,
            left_motor_port=left_track_motor_port, right_motor_port=right_track_motor_port,
            ir_sensor_port=ir_sensor_port, ir_beacon_channel=ir_beacon_channel)

        self.ev3_brick = EV3Brick()

        self.medium_motor = Motor(port=medium_motor_port,
                                  positive_direction=Direction.CLOCKWISE)

 
    def main(self):
        """
        Driving Track3r around by the IR beacon
        """
        while True:
            self.drive_by_ir_beacon(speed=1000)
            wait(1)


class Track3rWithBlastingBazooka(Track3r):
    """
    Track3r blasts his bazooka when the Beacon button is pressed
    (inspiration from LEGO Mindstorms EV3 Home Edition: Track3r: Tutorial #2)
    """
    def blast_bazooka_by_ir_beacon(
            self, 
            speed: float = 1000   # degrees per second
        ):
        if Button.BEACON in self.ir_sensor.buttons(channel=self.ir_beacon_channel):
            self.medium_motor.run_angle(
                speed=speed,
                rotation_angle=3 * 360,   # about 3 rotations for 1 shot
                then=Stop.HOLD,
                wait=True) 

            self.ev3_brick.speaker.play_file(file=SoundFile.LAUGHING_1)
               
            while Button.BEACON in self.ir_sensor.buttons(channel=self.ir_beacon_channel):
                pass


    def main(self):
        self.ev3_brick.screen.load_image(ImageFile.PINCHED_MIDDLE)
            
        while True:
            self.drive_by_ir_beacon()
            self.blast_bazooka_by_ir_beacon()
            wait(1)


class Track3rWithGrippingClaw(Track3r):
    """
    Track3r grips or releases its claw when the Beacon button is pressed
    (inspiration from LEGO Mindstorms EV3 Home Edition: Track3r: Tutorial #3)
    """

    is_gripping = False
    
    def grip_or_release_claw_by_ir_beacon(
            self,
            speed: float = 1000   # degrees per second
        ):
        if Button.BEACON in self.ir_sensor.buttons(channel=self.ir_beacon_channel):
            if self.is_gripping:
                self.medium_motor.run(speed=-speed)
                self.ev3_brick.speaker.play_file(file=SoundFile.AIR_RELEASE)
                self.is_gripping = False

            else:
                self.medium_motor.run(speed=speed)
                self.ev3_brick.speaker.play_file(file=SoundFile.AIRBRAKE)
                self.is_gripping = True

            while Button.BEACON in self.ir_sensor.buttons(channel=self.ir_beacon_channel):
                pass


    def main(self):
        while True:
            self.drive_by_ir_beacon()
            self.grip_or_release_claw_by_ir_beacon()
            wait(1)


class Track3rWithHeavyHammer(Track3r):
    """
    Track3r hammers down when the Beacon button is pressed
    (inspiration from LEGO Mindstorms EV3 Home Edition: Track3r: Tutorial #4)
    """
    def hammer_by_ir_beacon(self):
        if Button.BEACON in self.ir_sensor.buttons(channel=self.ir_beacon_channel):
            self.ev3_brick.screen.load_image(ImageFile.ANGRY)

            self.medium_motor.run_time(
                speed=1000,
                time=1000,
                then=Stop.HOLD,
                wait=True)

            self.ev3_brick.speaker.play_file(file=SoundFile.LAUGHING_2)

            self.medium_motor.run_time(
                speed=-1000,
                time=1000,
                then=Stop.HOLD,
                wait=True)


    def main(self):
        self.medium_motor.run_time(
            speed=-200,
            time=1000,
            then=Stop.HOLD,
            wait=True)

        while True:
            self.drive_by_ir_beacon()
            self.hammer_by_ir_beacon()
            wait(1)


class Track3rWithBiBladeSpinner(Track3r):
    """
    Track3r spins its blade when the Beacon button is pressed
    (inspiration from LEGO Mindstorms EV3 Home Edition: Track3r: Tutorial #5)
    """
    def spin_blade_by_ir_beacon(
            self,
            speed: float = 1000   # degrees per second
        ):
        if Button.BEACON in self.ir_sensor.buttons(channel=self.ir_beacon_channel):
            self.medium_motor.run(speed=speed)

        else:
            self.medium_motor.stop()

            
    def main(self):
        while True:
            self.drive_by_ir_beacon()
            self.spin_blade_by_ir_beacon()
            wait(1)


if __name__ == '__main__':
    TRACK3R = Track3rWithBlastingBazooka()
    TRACK3R.main()
