from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, InfraredSensor
from pybricks.parameters import Button, Direction, Port, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait


class Rac3Truck(EV3Brick):
    WHEEL_DIAMETER = 30   # milimeters
    AXLE_TRACK = 120      # milimeters

    def __init__(
            self,
            left_motor_port: str = Port.B, right_motor_port: str = Port.C,
            polarity: str = 'inversed',
            steer_motor_port: str = Port.A,
            ir_sensor_port: str = Port.S4, ir_beacon_channel: int = 1):
        if polarity == 'normal':
            self.left_motor = Motor(port=left_motor_port,
                                    positive_direction=Direction.CLOCKWISE)
            self.right_motor = Motor(port=right_motor_port,
                                     positive_direction=Direction.CLOCKWISE)
        else:
            self.left_motor = \
                Motor(port=left_motor_port,
                      positive_direction=Direction.COUNTERCLOCKWISE)
            self.right_motor = \
                Motor(port=right_motor_port,
                      positive_direction=Direction.COUNTERCLOCKWISE)
        self.driver = DriveBase(left_motor=self.left_motor,
                                right_motor=self.right_motor,
                                wheel_diameter=self.WHEEL_DIAMETER,
                                axle_track=self.AXLE_TRACK)

        self.steer_motor = Motor(port=steer_motor_port,
                                 positive_direction=Direction.CLOCKWISE)

        self.ir_sensor = InfraredSensor(port=ir_sensor_port)
        self.ir_beacon_channel = ir_beacon_channel

    def reset(self):
        self.steer_motor.run_time(
            speed=300,
            time=1500,
            then=Stop.COAST,
            wait=True)

        self.steer_motor.run_angle(
            speed=-500,
            rotation_angle=120,
            then=Stop.HOLD,
            wait=True)

        self.steer_motor.reset_angle(angle=0)

    def steer_left(self):
        if self.steer_motor.angle() > -65:
            self.steer_motor.run_target(
                speed=-200,
                target_angle=-65,
                then=Stop.HOLD,
                wait=True)

        else:
            self.steer_motor.hold()

    def steer_right(self):
        if self.steer_motor.angle() < 65:
            self.steer_motor.run_target(
                speed=200,
                target_angle=65,
                then=Stop.HOLD,
                wait=True)

        else:
            self.steer_motor.hold()

    def steer_center(self):
        if self.steer_motor.angle() < -7:
            self.steer_motor.run_target(
                speed=200,
                target_angle=4,
                then=Stop.HOLD,
                wait=True)

        elif self.steer_motor.angle() > 7:
            self.steer_motor.run_target(
                speed=-200,
                target_angle=-4,
                then=Stop.HOLD,
                wait=True)

        self.steer_motor.hold()

        wait(100)

    def drive_by_ir_beacon(self):
        ir_beacon_button_pressed = \
            set(self.ir_sensor.buttons(channel=self.ir_beacon_channel))

        # forward
        if ir_beacon_button_pressed == {Button.LEFT_UP, Button.RIGHT_UP}:
            self.driver.drive(
                speed=800,
                turn_rate=0)

            self.steer_center()

        # backward
        elif ir_beacon_button_pressed == {Button.LEFT_DOWN, Button.RIGHT_DOWN}:
            self.driver.drive(
                speed=-800,
                turn_rate=0)

            self.steer_center()

        # turn left forward
        elif ir_beacon_button_pressed == {Button.LEFT_UP}:
            self.left_motor.run(speed=600)
            self.right_motor.run(speed=1000)

            self.steer_left()

        # turn right forward
        elif ir_beacon_button_pressed == {Button.RIGHT_UP}:
            self.left_motor.run(speed=1000)
            self.right_motor.run(speed=600)

            self.steer_right()

        # turn left backward
        elif ir_beacon_button_pressed == {Button.LEFT_DOWN}:
            self.left_motor.run(speed=-600)
            self.right_motor.run(speed=-1000)

            self.steer_left()

        # turn right backward
        elif ir_beacon_button_pressed == {Button.RIGHT_DOWN}:
            self.left_motor.run(speed=-1000)
            self.right_motor.run(speed=-600)

            self.steer_right()

        # otherwise stop
        else:
            self.driver.stop()

            self.steer_center()
