from pybricks.pupdevices import Motor, Remote
from pybricks.parameters import Port, Direction, Stop, Button
from pybricks.tools import wait, StopWatch
import pybricks.hubs

# This program provides controls for the Audi e-tron Technic set.
# It provides basic throttle + steering and the red buttons
# increase / decrease speed by three levels: slow, medium, fast.
# The hub will shut down after two minutes of inactivity to
# save power.
#
# Controls:
# Left remote + / -  = Throttle: Forward & Reverse
# Right remote + / - = Steering
# Red left button    = Decrease speed
# Red right button   = Increase speed
#

# Speed levels
speed_levels = [500, 1000, 2000]  # Slow, Medium, Fastest
current_speed_index = 1  # Start with Medium speed
SPEED = speed_levels[current_speed_index]  # Initialize SPEED with the medium speed

# Initialize the motors.
steer = Motor(Port.D)  # Steering motor
front = Motor(Port.B, Direction.COUNTERCLOCKWISE, profile=300)  # Front wheel drive
rear = Motor(Port.A, Direction.COUNTERCLOCKWISE, profile=300)  # Rear wheel drive

# Set the acceleration and speed limits for the motors.
front.control.limits(speed=2000, acceleration=2000)
rear.control.limits(speed=2000, acceleration=2000)

# Connect to the powered up remote.
remote = Remote()

# Calibrate the steering motor.
left_end = steer.run_until_stalled(-200, then=Stop.HOLD)
right_end = steer.run_until_stalled(200, then=Stop.HOLD)
steer.reset_angle((right_end - left_end) / 2)
steer.run_target(speed=1000, target_angle=0, wait=False)

# Variables to track the previous state of the red buttons.
prev_left_button_pressed = False
prev_right_button_pressed = False

# Initialize inactivity timer
inactivity_timer = StopWatch()

# Now we can start driving!
while True:
    pressed = remote.buttons.pressed()

    # Reset the timer if there's any button pressed
    if pressed:
        inactivity_timer.reset()

    # Shut down if inactive for 2 minutes (120 seconds)
    if inactivity_timer.time() > 120000:  # 2 minutes in milliseconds
        hub.system.shutdown()

    # Detect single presses on the red buttons.
    left_button_pressed = Button.LEFT in pressed
    right_button_pressed = Button.RIGHT in pressed

    if left_button_pressed and not prev_left_button_pressed:
        current_speed_index = max(0, current_speed_index - 1)  # Decrease speed index
        SPEED = speed_levels[current_speed_index]  # Update SPEED

    if right_button_pressed and not prev_right_button_pressed:
        current_speed_index = min(len(speed_levels) - 1, current_speed_index + 1)  # Increase speed index
        SPEED = speed_levels[current_speed_index]  # Update SPEED

    # Store the current state for the next iteration
    prev_left_button_pressed = left_button_pressed
    prev_right_button_pressed = right_button_pressed

    # Steering.
    steer_angle = 0
    if Button.RIGHT_MINUS in pressed:
        steer_angle += 75
    if Button.RIGHT_PLUS in pressed:
        steer_angle -= 75

    steer.run_target(500, steer_angle, wait=False)

    # Throttle: Forward & Reverse.
    drive_speed = 0
    if Button.LEFT_PLUS in pressed:
        drive_speed -= SPEED
    if Button.LEFT_MINUS in pressed:
        drive_speed += SPEED

    front.run(drive_speed)
    rear.run(drive_speed)

    wait(25)
