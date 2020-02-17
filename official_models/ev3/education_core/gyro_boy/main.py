#!/usr/bin/env pybricks-micropython

"""
Example LEGO® MINDSTORMS® EV3 Gyro Boy Program
----------------------------------------------

This program requires LEGO® EV3 MicroPython v2.0.
Download: https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3

Building instructions can be found at:
https://education.lego.com/en-us/support/mindstorms-ev3/building-instructions#building-core
"""

import urandom

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, UltrasonicSensor, ColorSensor, GyroSensor
from pybricks.parameters import Port, Button, Color, ImageFile, SoundFile
from pybricks.tools import wait, StopWatch

# Initialize the EV3 brick.
ev3 = EV3Brick()

left_motor = Motor(Port.D)
right_motor = Motor(Port.A)
arm_motor = Motor(Port.C)

# Initialize the Color Sensor. It is used to detect the colors that command
# which way the robot should move
color_sensor = ColorSensor(Port.S1)

gyro_sensor = GyroSensor(Port.S2)

ultrasonic_sensor = UltrasonicSensor(Port.S4)


fall_timer = StopWatch()
control_loop_timer = StopWatch()
action_timer = StopWatch()

GYRO_CALIBRATION_LOOP_COUNT = 200
GYRO_OFFSET_FACTOR = 0.0005
TARGET_LOOP_PERIOD = 25  # ms
ARM_MOTOR_SPEED = 600  # deg/s

# The colors on the stand are mapped to steering and drive speed values.
ACTION_MAP = {
    Color.RED: (0, 0),  # stop
    Color.GREEN: (0, 150),  # drive forward
    Color.BLUE: (-70, 0),  # turn left
    Color.YELLOW: (70, 0),  # turn right
    Color.WHITE: (0, -75),  # drive backward
}


# This function monitors the color sensor and ultrasonic sensor. It is important
# that no blocking calls are made in this function, otherwise it will affect the
# control loop time in the main program.
def update_action():
    arm_motor.reset_angle(0)
    action_timer.reset()

    # drive forward for 4 seconds to leave stand
    yield 0, 40
    while action_timer.time() < 4000:
        yield

    # stop
    yield 0, 0

    # start checking sensors on arms
    while True:
        # Look up the detected color in the action map
        action = ACTION_MAP.get(color_sensor.color())

        # If the color was found, beep for 0.1 seconds and then yield the action
        if action is not None:
            action_timer.reset()
            ev3.speaker.beep(1000, -1)
            while action_timer.time() < 100:
                yield
            ev3.speaker.beep(0, -1)
            yield action

        # If the measured distance of the ultrasonic sensor is less than 250
        # millimeters, then back up slowly.
        if ultrasonic_sensor.distance() < 250:
            yield 0, -10

            # Wiggle the arms back and forth
            arm_motor.run_angle(ARM_MOTOR_SPEED, 30, wait=False)
            while not arm_motor.control.done():
                yield
            arm_motor.run_angle(ARM_MOTOR_SPEED, -60, wait=False)
            while not arm_motor.control.done():
                yield
            arm_motor.run_angle(ARM_MOTOR_SPEED, 30, wait=False)
            while not arm_motor.control.done():
                yield

            # Randomly turn left or right for 4 seconds
            yield urandom.choice([70, -70]), -10
            action_timer.reset()
            while action_timer.time() < 4000:
                yield

            action_timer.reset()
            ev3.speaker.beep(1000, -1)
            while action_timer.time() < 100:
                yield
            ev3.speaker.beep(0, -1)

            yield 0, 0

        action_timer.reset()
        while action_timer.time() < 100:
            yield


# If we fall over in the middle of an action, the arm motors could be moving or
# the speaker could be beeping, so we need to stop those.
def stop_action():
    ev3.speaker.beep(0, -1)
    arm_motor.run_target(ARM_MOTOR_SPEED, 0)


while True:
    ev3.screen.load_image(ImageFile.SLEEPING)
    ev3.light.off()

    # Reset sensors and variables
    left_motor.reset_angle(0)
    right_motor.reset_angle(0)
    fall_timer.reset()

    motor_position_sum = 0
    wheel_angle = 0
    motor_position_change = [0, 0, 0, 0]
    drive_speed, steering = 0, 0
    control_loop_count = 0
    robot_body_angle = -0.25

    action_task = update_action()

    # Calibrate gyro offset
    while True:
        gyro_minimum_rate, gyro_maximum_rate = 440, -440
        gyro_sum = 0
        for _ in range(GYRO_CALIBRATION_LOOP_COUNT):
            gyro_sensor_value = gyro_sensor.speed()
            gyro_sum += gyro_sensor_value
            if gyro_sensor_value > gyro_maximum_rate:
                gyro_maximum_rate = gyro_sensor_value
            if gyro_sensor_value < gyro_minimum_rate:
                gyro_minimum_rate = gyro_sensor_value
            wait(5)
        if gyro_maximum_rate - gyro_minimum_rate < 2:
            break
    gyro_offset = gyro_sum / GYRO_CALIBRATION_LOOP_COUNT

    ev3.speaker.play_file(SoundFile.SPEED_UP)
    ev3.screen.load_image(ImageFile.AWAKE)
    ev3.light.on(Color.GREEN)

    while True:
        # calculate control loop period
        if control_loop_count == 0:
            control_loop_period = TARGET_LOOP_PERIOD
            control_loop_timer.reset()
        else:
            control_loop_period = (control_loop_timer.time() / 1000 /
                                   control_loop_count)
        control_loop_count += 1

        # calculate robot body angle and speed
        gyro_sensor_value = gyro_sensor.speed()
        gyro_offset *= (1 - GYRO_OFFSET_FACTOR) * gyro_offset
        gyro_offset += GYRO_OFFSET_FACTOR * gyro_sensor_value
        robot_body_rate = gyro_sensor_value - gyro_offset
        robot_body_angle += robot_body_rate * control_loop_period

        # calculate wheel angle and speed
        left_motor_angle = left_motor.angle()
        right_motor_angle = right_motor.angle()
        previous_motor_sum = motor_position_sum
        motor_position_sum = left_motor_angle + right_motor_angle
        change = motor_position_sum - previous_motor_sum
        motor_position_change.insert(0, change)
        del motor_position_change[-1]
        wheel_angle += change - drive_speed * control_loop_period
        wheel_rate = sum(motor_position_change) / 4 / control_loop_period

        # calculate output power
        output_power = (-0.01 * drive_speed) + (0.8 * robot_body_rate +
                                                15 * robot_body_angle +
                                                0.08 * wheel_rate +
                                                0.12 * wheel_angle)
        if output_power > 100:
            output_power = 100
        if output_power < -100:
            output_power = -100

        # drive motors
        left_motor.dc(output_power - 0.1 * steering)
        right_motor.dc(output_power + 0.1 * steering)

        # check if robot fell down
        if abs(output_power) < 100:
            fall_timer.reset()
        elif fall_timer.time() > 1000:
            break

        action = next(action_task)
        if action is not None:
            steering, drive_speed = action

        # make sure loop time is at least TARGET_LOOP_PERIOD
        wait(TARGET_LOOP_PERIOD - control_loop_period)

    # Handle falling over
    stop_action()
    left_motor.stop()
    right_motor.stop()
    ev3.light.on(Color.RED)
    ev3.screen.load_image(ImageFile.KNOCKED_OUT)
    ev3.speaker.play_file(SoundFile.SPEED_DOWN)
    wait(3000)
