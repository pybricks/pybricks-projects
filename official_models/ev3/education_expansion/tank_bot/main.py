#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import Motor, GyroSensor
from pybricks.parameters import Port, Stop, Direction, Button, ImageFile
from pybricks.tools import wait
from pybricks.robotics import DriveBase

# Configure 2 motors on Ports B and C.  Set the motor directions to
# counterclockwise, so that positive speed values make the robot move
# forward.  These will be the left and right motors of the Tank Bot.
left_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.D, Direction.COUNTERCLOCKWISE)

# The wheel diameter of the Tank Bot is about 54 mm.
wheel_diameter = 54

# The axle track is the distance between the centers of each of the
# wheels.  This is about 200 mm for the Tank Bot.
axle_track = 200

# The Driving Base is comprised of 2 motors.  There is a wheel on each
# motor.  The wheel diameter and axle track values are used to make the
# motors move at the correct speed when you give a drive command.
robot = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)

# Set up the Gyro Sensor.  It is used to measure the angle of the robot.
# Keep the Gyro Sensor and EV3 steady when connecting the cable and
# during start-up of the EV3.
gyro_sensor = GyroSensor(Port.S4)

# Initialize the speed, steering, and overshoot variables.
speed = 250
steering = 60
overshoot = 5


def right_angle():
    # This function drives the robot forward, turn a right angle, drive
    # forward again, and then turn 180 degrees to drive back along the
    # same path and return to its initial position.

    # Reset the Gyro Sensor angle.
    gyro_sensor.reset_angle(0)

    # Drive forward for 3 seconds.
    robot.drive_time(speed, 0, 3000)
    robot.stop(Stop.BRAKE)

    # Turn clockwise until the angle is 90 degrees.
    robot.drive(0, steering)
    brick.sound.beeps(3)
    while gyro_sensor.angle() < 90 - overshoot:
        pass
    robot.stop(Stop.HOLD)

    # Drive forward for 3 seconds.
    robot.drive_time(speed, 0, 3000)
    robot.stop(Stop.BRAKE)

    # Turn clockwise until the angle is 270 degrees.
    robot.drive(0, steering)
    brick.sound.beeps(3)
    while gyro_sensor.angle() < 270 - overshoot:
        pass
    robot.stop(Stop.HOLD)

    # Drive forward for 3 seconds.
    robot.drive_time(speed, 0, 3000)
    robot.stop(Stop.BRAKE)

    # Turn counterclockwise until the angle is 180 degrees.
    robot.drive(0, -steering)
    brick.sound.beeps(3)
    while gyro_sensor.angle() > 180 + overshoot:
        pass
    robot.stop(Stop.HOLD)

    # Drive forward for 3 seconds.
    robot.drive_time(speed, 0, 3000)
    robot.stop(Stop.BRAKE)

    # Turn clockwise until the angle is 360 degrees.
    robot.drive(0, steering)
    brick.sound.beeps(3)
    while gyro_sensor.angle() < 360 - overshoot:
        pass
    robot.stop(Stop.HOLD)


def polygon(sides, length):
    # This function drives the robot along a polygon path.  It uses the
    # number of sides to calculate the angle to turn to, and the length
    # to calculate the time to drive straight.

    # Reset the Gyro Sensor angle.
    gyro_sensor.reset_angle(0)

    # Calculate the angle to turn to and the time to drive straight.
    angle = 360 / sides
    time = length / speed * 1000

    # Drive along the polygon path.
    for side in range(1, sides + 1):
        target_angle = side * angle - overshoot

        # Drive forward.
        robot.drive_time(speed, 0, time)
        robot.stop(Stop.BRAKE)

        # Turn clockwise until the angle equals the target angle.
        robot.drive(0, steering)
        brick.sound.beeps(3)
        while gyro_sensor.angle() < target_angle:
            pass
        robot.stop(Stop.HOLD)


# This is the main part of the program.  It is a loop that repeats
# endlessly.
#
# First, it waits until any Brick Button is pressed.
# Second, it displays the chosen pattern on the screen.
# Finally, it drives in the chosen pattern.
#
# Then the process starts over, so another pattern can be chosen.
while True:

    # Display a question mark to indicate that the robot should await
    # instructions.
    brick.display.clear()
    brick.display.image(ImageFile.QUESTION_MARK)

    # Wait until any Brick Button is pressed.
    while not any(brick.buttons()):
        wait(10)

    brick.display.clear()

    # Respond to the Brick Button press.  Display the chosen pattern on
    # the screen and drive in this pattern.
    if Button.UP in brick.buttons():
        # Drive in a right angle.
        brick.display.text("Right Angle", (50, 60))
        wait(1000)
        right_angle()

    if Button.LEFT in brick.buttons():
        # Drive in a triangle shape.
        brick.display.text("Triangle", (50, 60))
        wait(2000)
        polygon(3, 850)

    if Button.CENTER in brick.buttons():
        # Drive in a square shape.
        brick.display.text("Square", (50, 60))
        wait(2000)
        polygon(4, 700)

    if Button.RIGHT in brick.buttons():
        # Drive in a pentagon shape.
        brick.display.text("Pentagon", (50, 60))
        wait(2000)
        polygon(5, 575)

    if Button.DOWN in brick.buttons():
        # Drive in a hexagon shape.
        brick.display.text("Hexagon", (50, 60))
        wait(2000)
        polygon(6, 490)

    wait(100)
