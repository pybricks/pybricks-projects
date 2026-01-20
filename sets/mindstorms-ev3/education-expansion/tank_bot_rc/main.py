#!/usr/bin/env pybricks-micropython

"""
Example LEGO® MINDSTORMS® EV3 Tank Bot Program
----------------------------------------------

This program requires LEGO® EV3 MicroPython v2.0.
Download: https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3

Building instructions can be found at:
https://education.lego.com/en-us/support/mindstorms-ev3/building-instructions#building-expansion
"""

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, GyroSensor
from pybricks.parameters import Port, Direction, Button, Color
from pybricks.tools import StopWatch, wait, run_task, multitask
from pybricks.robotics import DriveBase
from pybricks.messaging import RFCOMMSocket, local_address

from micropython import const

import ustruct

# Initialize the EV3 brick.
ev3 = EV3Brick()

# Configure 2 motors on Ports B and C.  Set the motor directions to
# counterclockwise, so that positive speed values make the robot move
# forward.  These will be the left and right motors of the Tank Bot.
left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.D, Direction.COUNTERCLOCKWISE)

# The wheel diameter of the Tank Bot is about 54 mm.
WHEEL_DIAMETER = 54

# The axle track is the distance between the centers of each of the
# wheels.  This is about 200 mm for the Tank Bot.
AXLE_TRACK = 200

# The Driving Base is comprised of 2 motors.  There is a wheel on each
# motor.  The wheel diameter and axle track values are used to make the
# motors move at the correct speed when you give a drive command.
robot = DriveBase(left_motor, right_motor, WHEEL_DIAMETER, AXLE_TRACK)

SPEED_SCALE = 6  # Scale factor for speed (768 // 127)
TURN_SCALE = 2  # Scale factor for turn rate (320 // 127)

async def main():
    sock = RFCOMMSocket()
    print('Local address: ', local_address())
    ev3.light.on(Color.RED)
    print('Waiting for connection...')
    await sock.listen()
    print('Connected!')
    ev3.light.on(Color.GREEN)

    while True:
        (msg, _) = await multitask(sock.read(2), wait(100), race=True)

        if msg is None:
            # Connection timed out.
            break

        axis1, axis2 = ustruct.unpack('>bb', msg)

        speed = axis2 * SPEED_SCALE  # -768 to +768 mm/s
        turn_rate = axis1 * TURN_SCALE  # -320 to +320 deg/s
        robot.drive(speed, turn_rate)

    robot.stop()
    print('Client disconnected or timed out.')
    sock.close()

run_task(main())