from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor
from pybricks.parameters import Button, Direction, Port

from rc_tank_util import RemoteControlledTank


class RoboDoz3r(RemoteControlledTank):
    WHEEL_DIAMETER = 24   # milimeters
    AXLE_TRACK = 100      # milimeters

    def __init__(
            self,
            left_motor_port: Port = Port.C, right_motor_port: Port = Port.B,
            shovel_motor_port: Port = Port.A,
            touch_sensor_port: Port = Port.S1,
            ir_sensor_port: Port = Port.S4,
            tank_drive_ir_beacon_channel: int = 1,
            shovel_control_ir_beacon_channel: int = 4):
        super().__init__(
            wheel_diameter=self.WHEEL_DIAMETER, axle_track=self.AXLE_TRACK,
            left_motor_port=left_motor_port, right_motor_port=right_motor_port,
            polarity='inversed',
            ir_sensor_port=ir_sensor_port,
            ir_beacon_channel=tank_drive_ir_beacon_channel)

        self.ev3_brick = EV3Brick()

        self.shovel_motor = Motor(port=shovel_motor_port,
                                  positive_direction=Direction.CLOCKWISE)

        self.touch_sensor = TouchSensor(port=touch_sensor_port)

        self.shovel_control_ir_beacon_channel = \
            shovel_control_ir_beacon_channel

    def raise_or_lower_shovel_by_ir_beacon(self):
        """
        If the channel 4 is selected on the IR remote
        then you can control raising and lowering the shovel on the RoboDoz3r.
        - Raise the shovel by either Up button
        - Raise the shovel by either Down button
        """
        ir_beacon_button_pressed = \
            set(self.ir_sensor.buttons(
                    channel=self.shovel_control_ir_beacon_channel))

        # raise the shovel
        if ir_beacon_button_pressed.intersection(
                {Button.LEFT_UP, Button.RIGHT_UP}):
            self.shovel_motor.run(speed=100)

        # lower the shovel
        elif ir_beacon_button_pressed.intersection(
                {Button.LEFT_DOWN, Button.RIGHT_DOWN}):
            self.shovel_motor.run(speed=-100)

        else:
            self.shovel_motor.hold()
