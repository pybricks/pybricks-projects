from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor
from pybricks.media.ev3dev import ImageFile, SoundFile
from pybricks.parameters import Button, Color, Direction, Port, Stop
from pybricks.tools import wait

from random import choice, randint

from rc_tank_util import RemoteControlledTank


class EV3D4(RemoteControlledTank):
    WHEEL_DIAMETER = 20
    AXLE_TRACK = 110

    def __init__(
            self,
            left_motor_port: Port = Port.C, right_motor_port: Port = Port.B,
            head_motor_port: Port = Port.A,
            touch_sensor_port: Port = Port.S1,
            color_sensor_port: Port = Port.S3,
            ir_sensor_port: Port = Port.S4, ir_beacon_channel: int = 1):
        super().__init__(
            wheel_diameter=self.WHEEL_DIAMETER, axle_track=self.AXLE_TRACK,
            left_motor_port=left_motor_port, right_motor_port=right_motor_port,
            polarity='inversed',
            ir_sensor_port=ir_sensor_port, ir_beacon_channel=ir_beacon_channel)

        self.ev3_brick = EV3Brick()

        self.head_motor = Motor(port=head_motor_port,
                                positive_direction=Direction.CLOCKWISE)

        self.touch_sensor = TouchSensor(port=touch_sensor_port)

        self.color_sensor = ColorSensor(port=color_sensor_port)

        self.ir_beacon_channel = ir_beacon_channel

        self.state = 0

    def shake_head(self, left_first: bool = True, n_times: int = 1):
        speed_sign = 1 if left_first else -1

        for _ in range(n_times):
            self.head_motor.run_angle(
                speed=speed_sign * 500,
                rotation_angle=100,
                then=Stop.HOLD,
                wait=True)

            self.head_motor.run_angle(
                speed=-speed_sign * 500,
                rotation_angle=200,
                then=Stop.HOLD,
                wait=True)

            self.head_motor.run_angle(
                speed=speed_sign * 500,
                rotation_angle=100,
                then=Stop.HOLD,
                wait=True)

    def action_1(self):
        self.state = 1

        for _ in range(2):
            self.ev3_brick.light.on(color=Color.ORANGE)

            wait(100)

            self.ev3_brick.light.on(color=Color.GREEN)

            wait(100)

            self.ev3_brick.light.on(color=Color.RED)

            wait(100)

    def action_2(self):
        self.ev3_brick.speaker.play_file(file=SoundFile.CONFIRM)

        self.ev3_brick.speaker.play_file(file=SoundFile.SMACK)

        self.shake_head(left_first=True)

        self.ev3_brick.light.on(color=Color.RED)

    def action_3(self):
        self.ev3_brick.speaker.play_file(file=SoundFile.OVERPOWER)

        self.shake_head(
            left_first=False,
            n_times=3)

    def action_4(self):
        self.shake_head(
            left_first=True,
            n_times=2)

        self.ev3_brick.speaker.play_file(file=SoundFile.READY)

    def action_5(self):
        for _ in range(3):
            self.ev3_brick.screen.load_image(ImageFile.EV3)

            self.ev3_brick.light.on(color=Color.ORANGE)

            self.ev3_brick.light.on(color=Color.RED)

            self.ev3_brick.light.on(color=Color.GREEN)

    def main_switch_loop(self, driving_speed: float = 750):
        while True:
            if not (self.ir_sensor.buttons(channel=1) or
                    self.ir_sensor.buttons(channel=2) or
                    self.ir_sensor.buttons(channel=3) or
                    self.ir_sensor.buttons(channel=4)):
                self.driver.stop()

                if self.state == 1:
                    self.driver.turn(angle=-90)

                    self.driver.turn(angle=90)

                elif self.state == 2:
                    self.driver.straight(distance=-50)

                    self.driver.straight(distance=50)

                elif self.state == 3:
                    self.driver.straight(distance=50)

                    self.driver.straight(distance=-50)

                self.state = 0

            elif Button.BEACON in \
                    self.ir_sensor.buttons(channel=self.ir_beacon_channel):
                self.shake_head(left_first=choice((False, True)))

            else:
                self.drive_by_ir_beacon(speed=driving_speed)

            wait(10)

    def color_sensor_loop(self):
        """
        This is the Color Sensor Loop that supports 4 different behaviors that
        are triggered randomly
        """
        while True:
            if self.color_sensor.color == Color.RED:
                random_number = randint(1, 4)

                if random_number == 1:
                    self.action_1()

                elif random_number == 2:
                    self.action_2()

                elif random_number == 3:
                    self.action_3()

                elif random_number == 4:
                    self.action_4()

            wait(10)

    def touch_sensor_loop(self):
        """
        This is the Touch Sensor Loop that supports 5 different behaviors that
        are triggered randomly
        """
        while True:
            if self.touch_sensor.pressed():
                random_number = randint(1, 5)

                if random_number == 1:
                    self.action_1()

                elif random_number == 2:
                    self.state = 2
                    self.action_2()

                elif random_number == 3:
                    self.state = 3
                    self.action_3()

                elif random_number == 4:
                    self.state = 2
                    self.action_4()

                elif random_number == 5:
                    self.state = 3
                    self.action_5()

            wait(10)
