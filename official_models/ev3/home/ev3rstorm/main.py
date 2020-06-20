#!/usr/bin/env pybricks-micropython

"""
Example LEGO® MINDSTORMS® EV3 Ev3rstorm Program
-----------------------------------------------

This program requires LEGO® EV3 MicroPython v2.0.
Download: https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3

Building instructions can be found at:
https://www.lego.com/en-us/themes/mindstorms/buildarobot
"""

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor, InfraredSensor
from pybricks.media.ev3dev import ImageFile, SoundFile
from pybricks.robotics import DriveBase
from pybricks.parameters import Button, Direction, Port, Stop
from pybricks.tools import wait

from random import randint


class RemoteControlledTank:
    """
    This reusable mixin provides the capability of driving a robot with a Driving Base by the IR beacon
    """
    def __init__(
            self,
            wheel_diameter: float, axle_track: float,   # both in milimeters
            left_motor_port: Port = Port.B, right_motor_port: Port = Port.C,
            ir_sensor_port: Port = Port.S4, ir_beacon_channel: int = 1):
        self.drive_base = DriveBase(left_motor=Motor(port=left_motor_port,
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
            self.drive_base.drive(
                speed=speed,
                turn_rate=0)

        # backward
        elif ir_beacon_button_pressed == {Button.LEFT_DOWN, Button.RIGHT_DOWN}:
            self.drive_base.drive(
                speed=-speed,
                turn_rate=0)

        # turn left on the spot
        elif ir_beacon_button_pressed == {Button.LEFT_UP, Button.RIGHT_DOWN}:
            self.drive_base.drive(
                speed=0,
                turn_rate=-turn_rate)

        # turn right on the spot
        elif ir_beacon_button_pressed == {Button.RIGHT_UP, Button.LEFT_DOWN}:
            self.drive_base.drive(
                speed=0,
                turn_rate=turn_rate)

        # turn left forward
        elif ir_beacon_button_pressed == {Button.LEFT_UP}:
            self.drive_base.drive(
                speed=speed,
                turn_rate=-turn_rate)

        # turn right forward
        elif ir_beacon_button_pressed == {Button.RIGHT_UP}:
            self.drive_base.drive(
                speed=speed,
                turn_rate=turn_rate)

        # turn left backward
        elif ir_beacon_button_pressed == {Button.LEFT_DOWN}:
            self.drive_base.drive(
                speed=-speed,
                turn_rate=turn_rate)

        # turn right backward
        elif ir_beacon_button_pressed == {Button.RIGHT_DOWN}:
            self.drive_base.drive(
                speed=-speed,
                turn_rate=-turn_rate)

        # otherwise stop
        else:
            self.drive_base.stop()


class Ev3rstorm(RemoteControlledTank):
    WHEEL_DIAMETER = 26   # milimeters
    AXLE_TRACK = 102      # milimeters


    def __init__(
            self,
            left_track_motor_port: Port = Port.B, right_track_motor_port: Port = Port.C,
            bazooka_blast_motor_port: Port = Port.A,
            touch_sensor_port: Port = Port.S1, color_sensor_port: Port = Port.S3,
            ir_sensor_port: Port = Port.S4, ir_beacon_channel: int = 1):
        super().__init__(
            wheel_diameter=self.WHEEL_DIAMETER, axle_track=self.AXLE_TRACK,
            left_motor_port=left_track_motor_port, right_motor_port=right_track_motor_port,
            ir_sensor_port=ir_sensor_port, ir_beacon_channel=ir_beacon_channel)

        self.ev3_brick = EV3Brick()
        
        self.bazooka_blast_motor = Motor(port=bazooka_blast_motor_port,
                                         positive_direction=Direction.CLOCKWISE)

        self.touch_sensor = TouchSensor(port=touch_sensor_port)
        self.color_sensor = ColorSensor(port=color_sensor_port)


    def dance_randomly_if_ir_beacon_button_pressed(self):
        """
        Ev3rstorm dances by turning by random angles on the spot when the Beacon button is pressed
        """
        while Button.BEACON in self.ir_sensor.buttons(channel=self.ir_beacon_channel):
            self.drive_base.turn(angle=randint(-360, 360))

    
    def blast_bazooka_if_touched(self):
        """
        Ev3rstorm blasts his bazooka when his Touch Sensor is pressed
        (inspiration from LEGO Mindstorms EV3 Home Edition: Ev3rstorm: Tutorial #5)
        """
        MEDIUM_MOTOR_N_ROTATIONS_PER_BLAST = 3
        MEDIUM_MOTOR_ROTATIONAL_DEGREES_PER_BLAST = MEDIUM_MOTOR_N_ROTATIONS_PER_BLAST * 360

        if self.touch_sensor.pressed():
            if self.color_sensor.ambient() < 15:
                self.ev3_brick.speaker.play_file(file=SoundFile.UP)

                self.bazooka_blast_motor.run_angle(
                    speed=2 * MEDIUM_MOTOR_ROTATIONAL_DEGREES_PER_BLAST,   # shoot quickly in half a second
                    rotation_angle=-MEDIUM_MOTOR_ROTATIONAL_DEGREES_PER_BLAST,
                    then=Stop.HOLD,
                    wait=True)

                self.ev3_brick.speaker.play_file(file=SoundFile.LAUGHING_1)

            else:
                self.ev3_brick.speaker.play_file(file=SoundFile.DOWN)

                self.bazooka_blast_motor.run_angle(
                    speed=2 * MEDIUM_MOTOR_ROTATIONAL_DEGREES_PER_BLAST,   # shoot quickly in half a second
                    rotation_angle=MEDIUM_MOTOR_ROTATIONAL_DEGREES_PER_BLAST,
                    then=Stop.HOLD,
                    wait=True)

                self.ev3_brick.speaker.play_file(file=SoundFile.LAUGHING_2)


    def main(self,
             driving_speed: float = 1000   # mm/s
            ):
        """
        Ev3rstorm's main program performing various capabilities
        """
        self.ev3_brick.screen.load_image(ImageFile.TARGET)

        while True:
            self.drive_by_ir_beacon(speed=driving_speed)
            self.dance_randomly_if_ir_beacon_button_pressed()
            self.blast_bazooka_if_touched()
            wait(1)


if __name__ == '__main__':
    EV3RSTORM = Ev3rstorm()
    EV3RSTORM.main(driving_speed=1000)
