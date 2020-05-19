#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.tools import wait
from pybricks.ev3devices import Motor
from pybricks.robotics import DriveBase
from pybricks.parameters import Port

from connection import SpikePrimeStreamReader

# Beep!
ev3 = EV3Brick()
ev3.speaker.beep()

# Create the connection. See README.md to find the address for your SPIKE hub.
spike = SpikePrimeStreamReader('F4:84:4C:AA:C8:A4')

# Initialize the motors and drive base
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

while True:
    # Read the orientation
    yaw, pitch, roll = spike.orientation()

    # Set speed and turn rate based on orientation
    robot.drive(-pitch*6, roll*2)
    wait(20)
