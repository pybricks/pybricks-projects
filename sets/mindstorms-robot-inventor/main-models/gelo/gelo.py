from pybricks.hubs import InventorHub
from pybricks.geometry import Axis
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Color, Direction, Port, Side
from pybricks.tools import wait, StopWatch

#######################################################
# Constants
#######################################################

_CW = Direction.CLOCKWISE
_CCW = Direction.COUNTERCLOCKWISE

# index to limits() tuple
_TORQUE = const(2)

_BEEP_START = const(1)
_BEEP_END = const(2)
_BEEP_ERROR = const(3)

DEFAULT_COLORS = [
    Color.RED,
    Color.GREEN,
    Color.BLUE,
    Color.YELLOW,
    Color.NONE,
]

#######################################################
# Helper context managers
#######################################################


class Acceleration:
    """
    Context manager for temporarily changing acceleration
    of the legs.

    Args:
        legs:
            A list of legs.
        accel:
            The acceleration in mm/s/s.
    """
    def __init__(self, legs: list[Motor], accel: int):
        self._legs = legs
        self._accel = accel
        self._limits = {}

    def __enter__(self):
        for leg in self._legs:
            self._limits[leg] = leg.control.limits()
            leg.control.limits(acceleration=self._accel)

    def __exit__(self, exc, value, trace):
        for leg in self._legs:
            leg.control.limits(*self._limits[leg])


class IgnoreException:
    """
    A context manager that supresses exceptions.
    """

    def __enter__(self):
        return self

    def __exit__(self, exc, value, trace):
        # Don't supress BaseException like SystemExit
        # or KeyboardInterrupt.
        if exc:
            return issubclass(exc, Exception)


#######################################################
# Helper functions
#######################################################


def copy_sign(x, y):
    """
    Like math.copysign(), but for integers.
    """
    if y < 0:
        return -x

    return x


def wait_gen(time):
    """
    Yields until time has elapsed.

    Args:
        time:
            The length of time to wait in milliseconds.
    """
    timer = StopWatch()

    while timer.time() < time:
        yield


def wait_until_gen(condition):
    """
    Yields until condition is met.

    Args:
        condition:
            A function that returns ``False`` to keep waiting
            and ``True`` when the condition is met.
    """
    while not condition():
        yield

#######################################################
# Main class
#######################################################


class Gelo:
    """
    Object used to control the Gelo model from the Robot Inventor set.
    """
    def __init__(self):
        self.hub = InventorHub(front_side=-Axis.X)
        self.hub.display.orientation(Side.BOTTOM)

        self.back_right = Motor(Port.A, _CCW)
        self.back_left = Motor(Port.B, _CW)
        self.front_right = Motor(Port.C, _CCW)
        self.front_left = Motor(Port.D, _CW)
        self.color = ColorSensor(Port.F)
        self.ultrasonic = UltrasonicSensor(Port.E)

        self._all_legs = [
            self.back_right,
            self.back_left,
            self.front_right,
            self.front_left,
        ]

        self._back_legs = [
            self.back_right,
            self.back_left,
        ]

        self._front_legs = [
            self.front_right,
            self.front_left,
        ]

        self._leg_map = {
            "all": self._all_legs,
            "front": self._front_legs,
            "back": self._back_legs,
        }

        # 90% of full load for all motors
        self._near_max_load = 90 * sum(
            leg.control.limits()[_TORQUE] for leg in self._all_legs
        ) // 100

        self._zero = {
            self.back_right: 0,
            self.back_left: 0,
            self.front_right: 0,
            self.front_left: 0,
        }

    def __enter__(self):
        self.color.lights.off()
        self.ultrasonic.lights.on(10)
        self._beep(_BEEP_START)

        return self

    def __exit__(self, exc, value, trace):
        # if there was an exception we will indicate
        # indicate that the program stopped because
        # of an error
        error = exc and issubclass(exc, Exception)

        if error:
            self.hub.light.on(Color.RED)

        for leg in self._all_legs:
            with IgnoreException():
                leg.stop()

        with IgnoreException():
            self.ultrasonic.lights.off()

        with IgnoreException():
            self.color.lights.off()

        wait(500)

        if error:
            self._beep(_BEEP_ERROR)
        else:
            self._beep(_BEEP_END)

    def _beep(self, kind):
        """
        Beep indications for program start and end.

        Args:
            kind:
                The kind of beep.
        """
        if kind == _BEEP_ERROR:
            for b in [100, 50]:
                self.hub.speaker.beep(b, 300)
        else:
            beeps = [100, 200, 300]

            if kind == _BEEP_END:
                beeps = reversed(beeps)

            for b in beeps:
                self.hub.speaker.beep(b)

    def _steer(self, steer: int) -> dict[int, int]:
        """
        Creates a steering offset map.

        Args:
            steer:
                The amount steer. 90 for left,
                0 for straight and -90 for right.
        """
        steer = max(-90, min(steer, 90))

        # A: 0, B: 180, C: 180, D: 0 will walk straight.
        # A: 90, B 180, C: 90, D: 0 will turn in place to the right
        # A: 0, B 270, C: 180, D: 270 will turn in place to the left

        return {
            self.back_right: -steer if steer < 0 else 0,
            self.back_left: (180 + steer) if steer > 0 else 180,
            self.front_right: (180 + steer) if steer < 0 else 180,
            self.front_left: (360 - steer) if steer > 0 else 0,
        }

    def _reset_legs(self, offset: dict[int, int], absolute: bool):
        """
        Resets the angle measurement of all of the legs to zero.

        Args:
            offset:
                The offset mapping that determines the
                phase of each leg.
            absolute:
                If true, use the absolute position of
                the motor instead of zero.
        """

        for leg in self._all_legs:
            # Reset to position read by absolute encoder.
            leg.reset_angle()

            # Ensure legs travel shortest distance to reach opposition
            # after init. Often, the legs will coast past 180 when
            # stopping so when the program restarts, they come up
            # with and angle of -176 degrees, for example, and would
            # have to rotate nearly 360 degrees to reach opposition.
            if offset[leg] - leg.angle() > 180:
                leg.reset_angle(leg.angle() + 360)

        if not absolute:
            # Adjust the angle of each so that the average of all
            # legs is 0 while keeping the relative position of each
            # motor.
            avg = sum(
                leg.angle() - offset[leg] for leg in self._all_legs
            ) // len(self._all_legs)

            for leg in self._all_legs:
                leg.reset_angle(leg.angle() - avg)

    def _track_target(self, offset: dict[int, int], target: int):
        """
        Runs ``Motor.track_target`` for all legs at the same time.

        Args:
            offset:
                The offset map containing the phase for each leg in
                degrees.
            target:
                The target angle for the legs in degrees.
        """
        for leg in self._all_legs:
            leg.track_target(target + offset[leg])

    def oppose_legs_gen(self, speed=400):
        """
        Yields until legs are in opposing (walking) positions.
        """
        offset = self._steer(0)

        self._reset_legs(offset, absolute=False)

        for leg in self._all_legs:
            leg.run_target(speed, offset[leg], wait=False)

        while not all(map(Motor.done, self._all_legs)):
            yield

    def oppose_legs(self, speed=400):
        """
        Moves legs to opposing (walking) positions.
        """
        for _ in self.oppose_legs_gen(speed):
            wait(10)

    def stand_gen(self, speed=400):
        """
        Yields until all legs have moved to the standing position.

        Args:
            The speed to turn the motors in degrees per second.
        """
        self._reset_legs(self._zero, absolute=True)

        for leg in self._front_legs:
            leg.run_target(speed, -45, wait=False)

        for leg in self._back_legs:
            leg.run_target(speed, -90, wait=False)

        while not all(map(Motor.done, self._all_legs)):
            yield

    def stand(self, speed=400):
        """
        Moves legs to the standing position.

        Args:
            The speed to turn the motors in degrees per second.
        """
        for _ in self.stand_gen(speed):
            wait(10)

    def _move_legs_gen(self, legs, angle, speed):
        for leg in legs:
            leg.run_angle(speed, angle, wait=False)

        while not all(map(Motor.done, legs)):
            yield

    def walk_gen(self, speed=800, steer=0):
        """
        Yields forever while moving the legs in a walking motion.
        """
        offset = self._steer(steer)

        self._reset_legs(offset, absolute=False)

        # The actual fastest rate the motors can turn on
        # Gelo is somewhere between 700 and 900 deg/sec
        # depedning on battery voltage and terrain.
        # We will adjust the rate down if needed.
        target_rate = max(-900, min(speed, 900))

        timer = StopWatch()

        while True:
            angle = target_rate * timer.time() // 1000
            self._track_target(offset, angle)

            load = sum(map(Motor.load, self._all_legs))

            # If we are trying to go faster than the motors
            # can actually turn, we need reduce the rate so
            # that they can keep up.
            if abs(load) > self._near_max_load:
                target_rate -= copy_sign(10, target_rate)

            yield

    def walk(self, time=5000, speed=800, steer=0):
        """
        Moves legs in a walking motion for a certain amount of time.

        Args:
            time:
                The length of time to walk in milliseconds.
            speed:
                The speed to walk at. Values between 100 and 800 work
                best. Making the speed negative will walk backwards.
            steer:
                How much the robot should veer to the left or right.
                Allowable values are -90 to +90. Positive values will
                turn left and negative values will turn right.
        """
        for _ in zip(self.walk_gen(speed, steer), wait_gen(time)):
            wait(10)

    def walk_until(self, condition, speed=800, steer=0):
        """
        Moves legs in a walking motion until condition is met.

        Args:
            condition:
                A function that returns ``False`` when walking
                should continue and ``True`` when walking should stop.
            speed:
                The speed to walk at. Values between 100 and 800 work
                best. Making the speed negative will walk backwards.
            steer:
                How much the robot should veer to the left or right.
                Allowable values are -90 to +90. Positive values will
                turn left and negative values will turn right.
        """
        for _ in zip(
            self.walk_gen(speed, steer),
            wait_until_gen(condition),
        ):
            wait(10)

    def kick_gen(self, angle, speed=1000, legs="all"):
        """
        Yields until the legs have kicked (moved with high
        acceleration).

        Args:
            angle:
                The relative angle to move the legs in degrees.
            speed:
                The speed to move the legs in degrees per second.
            legs:
                The legs to kick. Can be "all", "front" or "back".
                Default is "all" legs.
        """
        legs = self._leg_map[legs]
        with Acceleration(legs, 10_000):
            for _ in self._move_legs_gen(legs, angle, speed):
                yield

    def kick(self, angle, speed=1000, legs="all"):
        """
        Kicks the legs (moves with high acceleration).

        Args:
            angle:
                The relative angle to move the legs in degrees.
            speed:
                The speed to move the legs in degrees per second.
            legs:
                The legs to kick. Can be "all", "front" or "back".
                Default is "all" legs.
        """
        for _ in self.kick_gen(angle, speed, legs):
            wait(10)

    def color_gen(self, colors=DEFAULT_COLORS):
        """
        Yields currently detected color and sets light to match.

        Args:
            color:
                Optional list of colors to detect.
                Default is red, green, blue, yellow.

        Yields:
            The detected color.
        """
        if Color.NONE not in colors:
            raise ValueError(
                "must include Color.NONE in list of colors"
            )

        self.color.detectable_colors(colors)

        while True:
            color = self.color.color()
            self.hub.light.on(color)

            yield color

    def wait_color(self, colors=DEFAULT_COLORS):
        """
        Waits for a color to be detected.

        Args:
            color:
                Optional list of colors to detect.
                Default is red, green, blue, yellow.

        Returns:
            The detected color.
        """
        for color in self.color_gen(colors):
            if color != Color.NONE:
                return color

            wait(10)


#######################################################
# Simple program
#######################################################

# This file is mainly used as an import by other files
# but if we run this file, it will still do something.

if __name__ == "__main__":
    with Gelo() as gelo:
        gelo.walk()
