from pybricks.ev3devices import Motor, InfraredSensor
from pybricks.robotics import DriveBase
from pybricks.parameters import Button, Direction, Port


class RemoteControlledTank:
    """
    This reusable mixin provides the capability of driving a robot
    with a Driving Base by the IR beacon
    """
    def __init__(
            self,
            wheel_diameter: float, axle_track: float,   # both in milimeters
            left_motor_port: Port = Port.B, right_motor_port: Port = Port.C,
            ir_sensor_port: Port = Port.S4, ir_beacon_channel: int = 1):
        self.drive_base = \
            DriveBase(
                left_motor=Motor(port=left_motor_port,
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
        ir_beacon_button_pressed = \
            set(self.ir_sensor.buttons(channel=self.ir_beacon_channel))

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
