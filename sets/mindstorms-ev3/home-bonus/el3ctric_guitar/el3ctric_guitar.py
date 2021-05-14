from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, InfraredSensor
from pybricks.media.ev3dev import ImageFile
from pybricks.parameters import Color, Direction, Port, Stop
from pybricks.tools import wait


class El3ctricGuitar:
    NOTES = [1318, 1174, 987, 880, 783, 659, 587, 493, 440, 392, 329, 293]
    N_NOTES = len(NOTES)

    def __init__(
            self, lever_motor_port: Port = Port.D,
            touch_sensor_port: Port = Port.S1, ir_sensor_port: Port = Port.S4):
        self.ev3_brick = EV3Brick()

        self.lever_motor = Motor(port=lever_motor_port,
                                 positive_direction=Direction.CLOCKWISE)

        self.touch_sensor = TouchSensor(port=touch_sensor_port)

        self.ir_sensor = InfraredSensor(port=ir_sensor_port)

    def start_up(self):
        self.ev3_brick.screen.load_image(ImageFile.EV3)

        self.ev3_brick.light.on(color=Color.ORANGE)

        self.lever_motor.run_time(
            speed=50,
            time=1000,
            then=Stop.COAST,
            wait=True)

        self.lever_motor.run_angle(
            speed=50,
            rotation_angle=-30,
            then=Stop.BRAKE,
            wait=True)

        wait(100)

        self.lever_motor.reset_angle(angle=0)

    def play_note(self):
        if not self.touch_sensor.pressed():
            raw = sum(self.ir_sensor.distance() for _ in range(4)) / 4

            self.ev3_brick.speaker.beep(
                frequency=self.NOTES[
                            min(int(raw / 5), self.N_NOTES - 1)
                          ] - 11 * self.lever_motor.angle(),
                duration=100)

        wait(1)
