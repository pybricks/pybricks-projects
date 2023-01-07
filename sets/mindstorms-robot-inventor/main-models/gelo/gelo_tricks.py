"""
Use the color sensor to command Gelo to do tricks!

When the program runs, hold one of the colors on
the color "bone" (red, green, blue or yellow) in
front of the color sensor to see Gelo perform a
trick for you.

This works best when Gelo is on carpet.
"""

from pybricks.parameters import Color, Side
from pybricks.tools import wait, StopWatch
from pybricks.geometry import Axis

from gelo import Gelo


##################################################
# Fancy Python stuff!
##################################################

# map of colors to trick functions
tricks = {}


def trick(color):
    """
    Decorator to assign colors to a trick.
    """
    def decorator(func):
        tricks[color] = func

        return func

    return decorator


##################################################
# Define one trick for each color!
##################################################


@trick(Color.BLUE)
def buck(gelo: Gelo):
    """
    Tells Gelo to kick up its back legs.
    """
    # tip over
    gelo.kick(130)

    # kick back legs
    gelo.kick(470, legs="back")

    # stand back up
    gelo.kick(-120, legs="front")


@trick(Color.GREEN)
def headstand(gelo: Gelo):
    """
    Tells Gelo to stand on its head.
    """
    # tip over
    gelo.kick(220)

    # hold the position for a bit
    wait(1500)

    # go back down
    gelo.kick(-20)
    wait(200)
    gelo.kick(-250)
    wait(500)


@trick(Color.RED)
def flip(gelo: Gelo):
    """
    Tells Gelo to flip all the way over on
    its back.
    """
    # big kick to flip over
    gelo.kick(300)


@trick(Color.YELLOW)
def spin(gelo: Gelo):
    """
    Tells Gelo to spin around in a circle.
    """
    timer = StopWatch()
    rate = 0

    # TODO: replace this when we get a proper
    # imu.heading() method. This is not very
    # accurate due to the low sample rate and
    # wild movements.
    def full_circle():
        nonlocal rate

        # integrate average rate over time to get angle
        rate = (
            99 * rate + gelo.hub.imu.angular_velocity(Axis.Z)
        ) / 100
        angle = rate * timer.time() / 1000

        return angle >= 360

    gelo.walk_until(full_circle, steer=90)


##################################################
# The main program!
##################################################


with Gelo() as gelo:
    while True:
        # make sure Gelo is right-side up
        # before continuing
        while gelo.hub.imu.up() != Side.TOP:
            gelo.hub.speaker.beep(50)
            wait(2000)

        # get in "ready" position
        gelo.stand()

        # wait until a color is detected
        color = gelo.wait_color()
        gelo.hub.speaker.beep()

        # look up the trick to perform
        do_trick = tricks[color]

        # perform the trick
        do_trick(gelo)
