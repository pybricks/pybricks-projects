from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, Remote
from pybricks.robotics import DriveBase
from pybricks.geometry import Axis
from pybricks.parameters import Button, Direction as Dir, Icon, Port


HAPPY_BIRTHDAY_SONG = [
    'G3/8', 'G3/8', 'A3/4', 'G3/4', 'C4/4', 'B3/2',
    'G3/8', 'G3/8', 'A3/4', 'G3/4', 'D4/4', 'C4/2',
    'G3/8', 'G3/8', 'G4/4', 'E4/4',
    'C4/8', 'C4/8', 'B3/4', 'A3/4',
    'F4/8', 'F4/8', 'E4/4', 'C4/4', 'D4/4', 'C4/2'
]


class RemoteControlledDriveBase:
    def __init__(
            self,
            wheel_diameter: float,   # milimeters
            axle_track: float,       # milimeters
            left_motor_port: Port = Port.A,
            left_motor_pos_dir: Dir = Dir.COUNTERCLOCKWISE,
            right_motor_port: Port = Port.B,
            right_motor_pos_dir: Dir = Dir.CLOCKWISE):
        self.drive_base = \
            DriveBase(left_motor=Motor(left_motor_port,
                                       left_motor_pos_dir),
                      right_motor=Motor(right_motor_port,
                                        right_motor_pos_dir),
                      wheel_diameter=wheel_diameter,
                      axle_track=axle_track)

        self.remote = Remote()
        print('Remote Connected!')

    def drive_by_remote(self,
                        speed: float = 1000,    # mm/s
                        turn_rate: float = 90   # rotational deg/s
                        ):
        remote_button_pressed = self.remote.buttons.pressed()

        # forward
        if remote_button_pressed == (Button.LEFT_PLUS,
                                     Button.RIGHT_PLUS):
            self.drive_base.drive(speed=speed, turn_rate=0)

        # backward
        elif remote_button_pressed == (Button.LEFT_MINUS,
                                       Button.RIGHT_MINUS):
            self.drive_base.drive(speed=-speed, turn_rate=0)

        # turn left on the spot
        elif remote_button_pressed == (Button.RIGHT_MINUS,
                                       Button.LEFT_PLUS):
            self.drive_base.drive(speed=0, turn_rate=-turn_rate)

        # turn right on the spot
        elif remote_button_pressed == (Button.LEFT_MINUS,
                                       Button.RIGHT_PLUS):
            self.drive_base.drive(speed=0, turn_rate=turn_rate)

        # turn left forward
        elif remote_button_pressed == (Button.LEFT_PLUS,):
            self.drive_base.drive(speed=speed, turn_rate=-turn_rate)

        # turn right forward
        elif remote_button_pressed == (Button.RIGHT_PLUS,):
            self.drive_base.drive(speed=speed, turn_rate=turn_rate)

        # turn left backward
        elif remote_button_pressed == (Button.LEFT_MINUS,):
            self.drive_base.drive(speed=-speed, turn_rate=turn_rate)

        # turn right backward
        elif remote_button_pressed == (Button.RIGHT_MINUS,):
            self.drive_base.drive(speed=-speed, turn_rate=-turn_rate)

        # otherwise stop
        else:
            self.drive_base.stop()


class BirthdayCandleBlower(RemoteControlledDriveBase):
    WHEEL_DIAMETER = 44   # milimeters
    AXLE_TRACK = 100      # milimeters

    def __init__(self,
                 fan_motor_port: Port = Port.A,
                 left_motor_port: Port = Port.D,
                 right_motor_port: Port = Port.C):
        super().__init__(
            wheel_diameter=self.WHEEL_DIAMETER,
            axle_track=self.AXLE_TRACK,
            left_motor_port=left_motor_port,
            left_motor_pos_dir=Dir.COUNTERCLOCKWISE,
            right_motor_port=right_motor_port,
            right_motor_pos_dir=Dir.CLOCKWISE)

        self.hub = PrimeHub(top_side=Axis.X, front_side=Axis.Z)

        self.fan_motor = Motor(fan_motor_port, Dir.CLOCKWISE)

    def smile(self):
        self.hub.display.image(image=Icon.HAPPY)

    def sing_happy_birthday_by_remote_center_button(self):
        if self.remote.buttons.pressed() == (Button.CENTER,):
            self.hub.speaker.play_notes(
                notes=HAPPY_BIRTHDAY_SONG,
                tempo=120)

    def spin_fan_by_remote_red_buttons(self):
        remote_button_pressed = self.remote.buttons.pressed()

        if remote_button_pressed == (Button.LEFT,):
            self.fan_motor.run(speed=-1000)

        elif remote_button_pressed == (Button.RIGHT,):
            self.fan_motor.run(speed=1000)

        else:
            self.fan_motor.stop()


# initialize Birthday Candle Blower
candle_blower = BirthdayCandleBlower()

# make it smile
candle_blower.smile()

# remote-control it to drive around, sing and blow candles
while True:
    candle_blower.drive_by_remote()
    candle_blower.sing_happy_birthday_by_remote_center_button()
    candle_blower.spin_fan_by_remote_red_buttons()
