from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, InfraredSensor
from pybricks.media.ev3dev import ImageFile, SoundFile
from pybricks.parameters import Direction, Port, Stop, Color
from pybricks.tools import wait

from time import sleep, time
from random import randint, uniform


class Wack3m:
    N_WHACK_TIMES = 10

    def __init__(
            self,
            left_motor_port: str = Port.B, right_motor_port: str = Port.C,
            middle_motor_port: str = Port.A,
            touch_sensor_port: str = Port.S1, ir_sensor_port: str = Port.S4):
        self.ev3_brick = EV3Brick()

        self.left_motor = Motor(port=left_motor_port,
                                positive_direction=Direction.CLOCKWISE)
        self.right_motor = Motor(port=right_motor_port,
                                 positive_direction=Direction.CLOCKWISE)
        self.middle_motor = Motor(port=middle_motor_port,
                                  positive_direction=Direction.CLOCKWISE)

        self.touch_sensor = TouchSensor(port=touch_sensor_port)

        self.ir_sensor = InfraredSensor(port=ir_sensor_port)

    def start_up(self):
        self.ev3_brick.light.on(color=Color.RED)

        self.ev3_brick.screen.print('WACK3M')

        self.left_motor.run_time(
            speed=-1000,
            time=1000,
            then=Stop.HOLD,
            wait=True)

        self.left_motor.reset_angle(angle=0)

        self.middle_motor.run_time(
            speed=-1000,
            time=1000,
            then=Stop.HOLD,
            wait=True)

        self.middle_motor.reset_angle(angle=0)

        self.right_motor.run_time(
            speed=-1000,
            time=1000,
            then=Stop.HOLD,
            wait=True)

        self.right_motor.reset_angle(angle=0)

    def play(self):
        while True:
            self.ev3_brick.speaker.play_file(file=SoundFile.START)

            self.ev3_brick.screen.load_image(ImageFile.TARGET)

            self.ev3_brick.light.on(color=Color.ORANGE)

            while not self.touch_sensor.pressed():
                wait(10)

            self.ev3_brick.speaker.play_file(file=SoundFile.GO)

            self.ev3_brick.light.on(color=Color.GREEN)

            total_response_time = 0

            sleep(1)

            for _ in range(self.N_WHACK_TIMES):
                self.ev3_brick.light.on(color=Color.GREEN)

                self.ev3_brick.screen.load_image(ImageFile.EV3_ICON)

                sleep(uniform(0.1, 3))

                which_motor = randint(1, 3)

                if which_motor == 1:
                    self.left_motor.run_angle(
                        speed=1000,
                        rotation_angle=90,
                        then=Stop.COAST,
                        wait=True)

                    start_time = time()

                    self.ev3_brick.screen.load_image(ImageFile.MIDDLE_LEFT)

                    self.left_motor.run_time(
                        speed=-1000,
                        time=500,
                        then=Stop.HOLD,
                        wait=True)

                    proximity = self.ir_sensor.distance()
                    while abs(self.ir_sensor.distance() - proximity) <= 4:
                        wait(10)

                elif which_motor == 2:
                    self.middle_motor.run_angle(
                        speed=1000,
                        rotation_angle=210,
                        then=Stop.COAST,
                        wait=True)

                    start_time = time()

                    self.ev3_brick.screen.load_image(ImageFile.NEUTRAL)

                    self.middle_motor.run_time(
                        speed=-1000,
                        time=500,
                        then=Stop.COAST,
                        wait=True)

                    proximity = self.ir_sensor.distance()
                    while abs(self.ir_sensor.distance() - proximity) <= 5:
                        wait(10)

                else:
                    self.right_motor.run_angle(
                        speed=1000,
                        rotation_angle=90,
                        then=Stop.COAST,
                        wait=True)

                    start_time = time()

                    self.ev3_brick.screen.load_image(ImageFile.MIDDLE_RIGHT)

                    self.right_motor.run_time(
                        speed=-1000,
                        time=500,
                        then=Stop.HOLD,
                        wait=True)

                    proximity = self.ir_sensor.distance()
                    while abs(self.ir_sensor.distance() - proximity) <= 5:
                        wait(10)

                response_time = time() - start_time

                self.ev3_brick.screen.load_image(ImageFile.DIZZY)

                self.ev3_brick.screen.print(response_time)

                self.ev3_brick.light.on(color=Color.RED)

                self.ev3_brick.speaker.play_file(file=SoundFile.BOING)

                total_response_time += response_time

            average_response_time = total_response_time / self.N_WHACK_TIMES

            self.ev3_brick.screen.clear()
            self.ev3_brick.screen.print(
                'Avg. Time: {:.1f}s'.format(average_response_time))

            if average_response_time <= 1:
                self.ev3_brick.speaker.play_file(file=SoundFile.FANTASTIC)
            else:
                self.ev3_brick.speaker.play_file(SoundFile.GOOD_JOB)

            self.ev3_brick.speaker.play_file(file=SoundFile.GAME_OVER)

            self.ev3_brick.light.on(color=Color.RED)

            sleep(4)
