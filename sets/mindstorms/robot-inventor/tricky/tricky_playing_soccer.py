"""
This program is for Tricky's "Soccer: Penalty Kick" activity.

Follow the corresponding building instructions in the LEGO® MINDSTORMS®
Robot Inventor App.

For each penalty kick practice round, place Tricky in front of
the red ball and the goal, then trigger the run-up and the kick
by placing something near the Distance Sensor behind Tricky.
"""

from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Color, Direction, Port, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait


class TrickyPlayingSoccer:

    WHEEL_DIAMETER = 44
    AXLE_TRACK = 88
    KICK_SPEED = 1000

    def __init__(self):
        # Configure the hub, the kicker motor, and the sensors.
        self.hub = InventorHub()
        self.kicker_motor = Motor(Port.C)
        self.distance_sensor = UltrasonicSensor(Port.D)
        self.color_sensor = ColorSensor(Port.E)

        # Configure the drive base.
        left_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
        right_motor = Motor(Port.A)
        self.drive_base = DriveBase(left_motor, right_motor,
                                    self.WHEEL_DIAMETER, self.AXLE_TRACK)

        # Prepare tricky to start kicking!
        self.distance_sensor.lights.off()
        self.reset_kicker_motor()
        self.distance_sensor.lights.on(100)

    def reset_kicker_motor(self):
        # Prepare the kicker motor for kicking.
        self.hub.light.off()
        self.kicker_motor.run_until_stalled(-self.KICK_SPEED, Stop.HOLD)
        self.kicker_motor.run_angle(self.KICK_SPEED, 325)

    def kick(self):
        # Kick the ball!
        self.kicker_motor.track_target(360)

    def run_to_and_kick_ball(self):
        # Drive until we see the red ball.
        self.drive_base.drive(speed=1000, turn_rate=0)
        while self.color_sensor.color() != Color.RED:
            wait(10)
        self.hub.light.on(Color.RED)
        self.hub.speaker.beep(frequency=100, duration=100)
        self.kick()
        self.drive_base.stop()
        self.hub.light.off()

    def celebrate(self):
        # Celebrate with light and sound.
        self.hub.display.image([
            [00, 11, 33, 11, 00],
            [11, 33, 66, 33, 11],
            [33, 66, 99, 66, 33],
            [11, 33, 66, 33, 11],
            [00, 11, 33, 11, 00]
        ])
        self.hub.speaker.beep(frequency=1000, duration=1000)
        self.hub.light.animate(
            [Color.CYAN, Color.GREEN, Color.MAGENTA],
            interval=100)

        # Celebrate by dancing around.
        self.drive_base.drive(speed=0, turn_rate=360)
        self.kicker_motor.run_angle(self.KICK_SPEED, 5 * 360)

        # Party's over! Let's stop everything.
        self.hub.display.off()
        self.hub.light.off()
        self.drive_base.stop()


# Initialize tricky.
tricky = TrickyPlayingSoccer()

# Keep practicing penalty kicks.
while True:
    # Wait until the player puts an object near the Distance Sensor
    # to trigger Tricky. Then start running towards the ball and the goal.
    if tricky.distance_sensor.distance() < 100:
        tricky.run_to_and_kick_ball()
        tricky.celebrate()
    wait(10)
