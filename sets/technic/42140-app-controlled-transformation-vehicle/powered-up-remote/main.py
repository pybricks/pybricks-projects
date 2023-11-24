from pybricks.hubs import TechnicHub
from pybricks.pupdevices import Motor, Remote
from pybricks.parameters import Port, Stop, Direction, Button, Color, Side
from pybricks.tools import wait, StopWatch

# Motor speed
# Speed levels
speed_levels = [400, 800, 1470]  # Slow, Medium, Fastest
current_speed_index = 1  # Start with Medium speed
SPEED = speed_levels[current_speed_index]

# Initialize the hub, motors, and remote
hub = TechnicHub()
left_motor = Motor(Port.B)
right_motor = Motor(Port.A)
remote = Remote()
inactivity_timer = StopWatch()

# Increase motor acceleration
left_motor.control.limits(speed=1470, acceleration=4000)
right_motor.control.limits(speed=1470, acceleration=4000)

# Variables to track the previous state of the red buttons
prev_left_button_pressed = False
prev_right_button_pressed = False

# Main control loop
while True:
    # Check which buttons are pressed
    buttons_pressed = remote.buttons.pressed()

    # Detect single presses on the red buttons
    left_button_pressed = Button.LEFT in buttons_pressed
    right_button_pressed = Button.RIGHT in buttons_pressed

    if left_button_pressed and not prev_left_button_pressed:
        current_speed_index = max(0, current_speed_index - 1)  # Decrease speed index
        SPEED = speed_levels[current_speed_index]  # Update SPEED

    if right_button_pressed and not prev_right_button_pressed:
        current_speed_index = min(
            len(speed_levels) - 1, current_speed_index + 1
        )  # Increase speed index
        SPEED = speed_levels[current_speed_index]  # Update SPEED

    # Store the current state for the next iteration
    prev_left_button_pressed = left_button_pressed
    prev_right_button_pressed = right_button_pressed

    # Determine hub orientation
    # Note: Slight bugginess when flipping from Orange to Blue side
    # Might be improved by including FRONT here
    invert_direction = hub.imu.up() == Side.BOTTOM

    # Control motors with remote
    left_speed = 0
    right_speed = 0

    if Button.LEFT_PLUS in buttons_pressed:
        left_speed = SPEED
    elif Button.LEFT_MINUS in buttons_pressed:
        left_speed = -SPEED

    if Button.RIGHT_PLUS in buttons_pressed:
        right_speed = -SPEED
    elif Button.RIGHT_MINUS in buttons_pressed:
        right_speed = SPEED

    # Swap motor direction if the hub is upside down
    if invert_direction:
        left_speed, right_speed = right_speed, left_speed  # Swap the motor controls

    # Run motors
    left_motor.run(left_speed)
    right_motor.run(right_speed)

    # Update light color based on orientation
    hub.light.on(Color.ORANGE if invert_direction else Color.BLUE)
    remote.light.on(Color.ORANGE if invert_direction else Color.BLUE)

    # Check for inactivity - Power off if left untouched to save batteries
    # Reset the timer if there's any button pressed
    if buttons_pressed:
        inactivity_timer.reset()

    if inactivity_timer.time() > 120000:  # 2 minute in milliseconds
        hub.system.shutdown()

    # Small delay to prevent overloading the CPU
    wait(10)
