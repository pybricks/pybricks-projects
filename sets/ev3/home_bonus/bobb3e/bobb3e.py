from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, InfraredSensor
from pybricks.media.ev3dev import SoundFile
from pybricks.parameters import Button, Direction, Port
from pybricks.robotics import DriveBase
from pybricks.tools import wait


class Bobb3e:
    WHEEL_DIAMETER = 24   # milimeters
    AXLE_TRACK = 100      # milimeters

    def __init__(
            self,
            left_motor_port: str = Port.B, right_motor_port: str = Port.C,
            lift_motor_port: str = Port.A,
            ir_sensor_port: str = Port.S4, ir_beacon_channel: int = 1):
        self.ev3_brick = EV3Brick()
        
        self.drive_base = \
            DriveBase(
                left_motor=
                    Motor(port=left_motor_port,
                          positive_direction=Direction.COUNTERCLOCKWISE),
                right_motor=
                    Motor(port=right_motor_port,
                          positive_direction=Direction.COUNTERCLOCKWISE),
                wheel_diameter=self.WHEEL_DIAMETER,
                axle_track=self.AXLE_TRACK)

        self.lift_motor = Motor(port=lift_motor_port,
                                positive_direction=Direction.CLOCKWISE)

        self.ir_sensor = InfraredSensor(port=ir_sensor_port)
        self.ir_beacon_channel = ir_beacon_channel

        self.reversing = False

    def drive_or_operate_forks_by_ir_beacon(
            self,
            driving_speed: float = 1000,    # mm/s
            turn_rate: float = 90   # rotational speed deg/s
            ):
        """
        Read the commands from the remote control and convert them into actions
        such as go forward, lift and turn.
        """
        while True:
            ir_beacon_button_pressed = \
                set(self.ir_sensor.buttons(channel=self.ir_beacon_channel))

            # lower the forks
            if ir_beacon_button_pressed == {Button.LEFT_UP, Button.LEFT_DOWN}:
                self.reversing = False

                self.drive_base.stop()

                self.lift_motor.run(speed=100)

            # raise the forks
            elif ir_beacon_button_pressed == \
                    {Button.RIGHT_UP, Button.RIGHT_DOWN}:
                self.reversing = False

                self.drive_base.stop()

                self.lift_motor.run(speed=-100)

            # forward
            elif ir_beacon_button_pressed == {Button.LEFT_UP, Button.RIGHT_UP}:
                self.reversing = False

                self.drive_base.drive(
                    speed=driving_speed,
                    turn_rate=0)

                self.lift_motor.hold()

            # backward
            elif ir_beacon_button_pressed == \
                    {Button.LEFT_DOWN, Button.RIGHT_DOWN}:
                self.reversing = True

                self.drive_base.drive(
                    speed=-driving_speed,
                    turn_rate=0)

                self.lift_motor.hold()

            # turn left on the spot
            elif ir_beacon_button_pressed == \
                    {Button.LEFT_UP, Button.RIGHT_DOWN}:
                self.reversing = False

                self.drive_base.drive(
                    speed=0,
                    turn_rate=-turn_rate)

                self.lift_motor.hold()

            # turn right on the spot
            elif ir_beacon_button_pressed == \
                    {Button.RIGHT_UP, Button.LEFT_DOWN}:
                self.reversing = False

                self.drive_base.drive(
                    speed=0,
                    turn_rate=turn_rate)

                self.lift_motor.hold()

            # turn left forward
            elif ir_beacon_button_pressed == {Button.LEFT_UP}:
                self.reversing = False

                self.drive_base.drive(
                    speed=driving_speed,
                    turn_rate=-turn_rate)

                self.lift_motor.hold()

            # turn right forward
            elif ir_beacon_button_pressed == {Button.RIGHT_UP}:
                self.reversing = False

                self.drive_base.drive(
                    speed=driving_speed,
                    turn_rate=turn_rate)

                self.lift_motor.hold()

            # turn left backward
            elif ir_beacon_button_pressed == {Button.LEFT_DOWN}:
                self.reversing = True

                self.drive_base.drive(
                    speed=-driving_speed,
                    turn_rate=turn_rate)

                self.lift_motor.hold()

            # turn right backward
            elif ir_beacon_button_pressed == {Button.RIGHT_DOWN}:
                self.reversing = True

                self.drive_base.drive(
                    speed=-driving_speed,
                    turn_rate=-turn_rate)

                self.lift_motor.hold()

            # otherwise stop
            else:
                self.reversing = False

                self.drive_base.stop()

                self.lift_motor.hold()

            wait(10)

    def sound_alarm_whenever_reversing(self):
        while True:
            if self.reversing:
                self.ev3_brick.speaker.play_file(file=SoundFile.BACKING_ALERT)

            wait(10)
