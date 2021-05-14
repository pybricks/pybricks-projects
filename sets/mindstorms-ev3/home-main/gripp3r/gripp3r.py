from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, InfraredSensor
from pybricks.media.ev3dev import SoundFile
from pybricks.parameters import Button, Direction, Port, Stop

from rc_tank_util import RemoteControlledTank


class Gripp3r(RemoteControlledTank):
    WHEEL_DIAMETER = 26   # milimeters
    AXLE_TRACK = 115      # milimeters

    def __init__(
            self,
            left_track_motor_port: Port = Port.B,
            right_track_motor_port: Port = Port.C,
            gripping_motor_port: Port = Port.A,
            touch_sensor_port: Port = Port.S1,
            ir_sensor_port: Port = Port.S4,
            ir_beacon_channel: int = 1):
        super().__init__(
            wheel_diameter=self.WHEEL_DIAMETER,
            axle_track=self.AXLE_TRACK,
            left_motor_port=left_track_motor_port,
            right_motor_port=right_track_motor_port,
            ir_sensor_port=ir_sensor_port,
            ir_beacon_channel=ir_beacon_channel)

        self.ev3_brick = EV3Brick()

        self.gripping_motor = Motor(port=gripping_motor_port,
                                    positive_direction=Direction.CLOCKWISE)

        self.touch_sensor = TouchSensor(port=touch_sensor_port)

        self.ir_sensor = InfraredSensor(port=ir_sensor_port)
        self.ir_beacon_channel = ir_beacon_channel

    def grip_or_release_by_ir_beacon(self, speed: float = 500):
        if Button.BEACON in \
                self.ir_sensor.buttons(channel=self.ir_beacon_channel):
            if self.touch_sensor.pressed():
                self.ev3_brick.speaker.play_file(file=SoundFile.AIR_RELEASE)

                self.gripping_motor.run_time(
                    speed=speed,
                    time=1000,
                    then=Stop.COAST,
                    wait=True)

            else:
                self.ev3_brick.speaker.play_file(file=SoundFile.AIRBRAKE)

                self.gripping_motor.run(speed=-speed)

                while not self.touch_sensor.pressed():
                    pass

                self.gripping_motor.stop()

            while Button.BEACON in \
                    self.ir_sensor.buttons(channel=self.ir_beacon_channel):
                pass
