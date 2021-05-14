from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor, InfraredSensor
from pybricks.media.ev3dev import SoundFile
from pybricks.parameters import Button, Color, Direction, Port, Stop


class Dinor3x:
    FAST_WALK_SPEED = 800
    NORMAL_WALK_SPEED = 400
    SLOW_WALK_SPEED = 200

    def __init__(
            self,
            jaw_motor_port: Port = Port.A,
            left_motor_port: Port = Port.B, right_motor_port: Port = Port.C,
            touch_sensor_port: Port = Port.S1,
            color_sensor_port: Port = Port.S3,
            ir_sensor_port: Port = Port.S4, ir_beacon_channel: int = 1):
        self.ev3_brick = EV3Brick()

        self.jaw_motor = Motor(port=jaw_motor_port,
                               positive_direction=Direction.CLOCKWISE)

        self.left_motor = Motor(port=left_motor_port,
                                positive_direction=Direction.CLOCKWISE)
        self.right_motor = Motor(port=right_motor_port,
                                 positive_direction=Direction.CLOCKWISE)

        self.touch_sensor = TouchSensor(port=touch_sensor_port)

        self.color_sensor = ColorSensor(port=color_sensor_port)

        self.ir_sensor = InfraredSensor(port=ir_sensor_port)
        self.ir_beacon_channel = ir_beacon_channel

        self.roaring = False
        self.walk_speed = self.NORMAL_WALK_SPEED

    def roar_by_ir_beacon(self):
        """
        Dinor3x roars when the Beacon button is pressed
        """
        if Button.BEACON in \
                self.ir_sensor.buttons(channel=self.ir_beacon_channel):
            self.roaring = True
            self.open_mouth()
            self.roar()

        elif self.roaring:
            self.roaring = False
            self.close_mouth()

    def change_speed_by_color(self):
        """
        Dinor3x changes its speed when detecting some colors
        - Red: walk fast
        - Green: walk normally
        - White: walk slowly
        """
        if self.color_sensor.color() == Color.RED:
            self.ev3_brick.speaker.say(text='RUN!')
            self.walk_speed = self.FAST_WALK_SPEED
            self.walk(speed=self.walk_speed)

        elif self.color_sensor.color() == Color.GREEN:
            self.ev3_brick.speaker.say(text='Normal')
            self.walk_speed = self.NORMAL_WALK_SPEED
            self.walk(speed=self.walk_speed)

        elif self.color_sensor.color() == Color.WHITE:
            self.ev3_brick.speaker.say(text='slow...')
            self.walk_speed = self.SLOW_WALK_SPEED
            self.walk(speed=self.walk_speed)

    def walk_by_ir_beacon(self):
        """
        Dinor3x walks or turns according to instructions from the IR Beacon
        - 2 top/up buttons together: walk forward
        - 2 bottom/down buttons together: walk backward
        - Top Left / Red Up: turn left on the spot
        - Top Right / Blue Up: turn right on the spot
        - Bottom Left / Red Down: stop
        - Bottom Right / Blue Down: calibrate to make the legs straight
        """
        ir_buttons_pressed = \
            set(self.ir_sensor.buttons(channel=self.ir_beacon_channel))

        # forward
        if ir_buttons_pressed == {Button.LEFT_UP, Button.RIGHT_UP}:
            self.walk(speed=self.walk_speed)

        # backward
        elif ir_buttons_pressed == {Button.LEFT_DOWN, Button.RIGHT_DOWN}:
            self.walk(speed=-self.walk_speed)

        # turn left on the spot
        elif ir_buttons_pressed == {Button.LEFT_UP}:
            self.turn(speed=self.walk_speed)

        # turn right on the spot
        elif ir_buttons_pressed == {Button.RIGHT_UP}:
            self.turn(speed=-self.walk_speed)

        # stop
        elif ir_buttons_pressed == {Button.LEFT_DOWN}:
            self.left_motor.hold()
            self.right_motor.hold()

        # calibrate legs
        elif ir_buttons_pressed == {Button.RIGHT_DOWN}:
            self.calibrate_legs()

    def calibrate_legs(self):
        self.left_motor.run(speed=100)
        self.right_motor.run(speed=200)

        while self.touch_sensor.pressed():
            pass

        self.left_motor.hold()
        self.right_motor.hold()

        self.left_motor.run(speed=400)

        while not self.touch_sensor.pressed():
            pass

        self.left_motor.hold()

        self.left_motor.run_angle(
            rotation_angle=-0.2 * 360,
            speed=500,
            then=Stop.HOLD,
            wait=True)

        self.right_motor.run(speed=400)

        while not self.touch_sensor.pressed():
            pass

        self.right_motor.hold()

        self.right_motor.run_angle(
            rotation_angle=-0.2 * 360,
            speed=500,
            then=Stop.HOLD,
            wait=True)

        self.left_motor.reset_angle(angle=0)
        self.right_motor.reset_angle(angle=0)

    def walk(self, speed: float = 400):
        self.calibrate_legs()

        self.left_motor.run(speed=-speed)
        self.right_motor.run(speed=-speed)

    def turn(self, speed: float = 400):
        self.calibrate_legs()

        if speed >= 0:
            self.left_motor.run_angle(
                rotation_angle=180,
                speed=speed,
                then=Stop.HOLD,
                wait=True)

        else:
            self.right_motor.run_angle(
                rotation_angle=180,
                speed=-speed,
                then=Stop.HOLD,
                wait=True)

        self.left_motor.run(speed=speed)
        self.right_motor.run(speed=-speed)

    def close_mouth(self):
        self.jaw_motor.run_time(
            speed=-200,
            time=1000,
            then=Stop.COAST,
            wait=False)

    def open_mouth(self):
        self.jaw_motor.run_time(
            speed=200,
            time=1000,
            then=Stop.COAST,
            wait=False)

    def roar(self):
        self.ev3_brick.speaker.play_file(file=SoundFile.T_REX_ROAR)

        self.jaw_motor.run_angle(
            speed=400,
            rotation_angle=-60,
            then=Stop.HOLD,
            wait=True)

        for _ in range(12):
            self.jaw_motor.run_time(
                speed=-400,
                time=0.05 * 1000,
                then=Stop.HOLD,
                wait=True)

            self.jaw_motor.run_time(
                speed=400,
                time=0.05 * 1000,
                then=Stop.HOLD,
                wait=True)

        self.jaw_motor.run_time(
            speed=200,
            time=0.5 * 1000,
            then=Stop.COAST,
            wait=True)
