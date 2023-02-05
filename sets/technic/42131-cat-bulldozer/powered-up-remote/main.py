from pybricks.pupdevices import Motor, Remote
from pybricks.parameters import Button, Color, Direction, Port
from pybricks.tools import wait, StopWatch

# Connect to the remote.
remote = Remote()

# Default speed and acceleration. You can change
# them to make it more realistic.
SWITCH_SPEED = 720
DRIVE_SPEED = 1000
DRIVE_ACCELERATION = 2500
FUNCTION_POWER = 100

# Initialize the motors.
left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.B)
function_motor = Motor(Port.C)
switch_motor = Motor(Port.D)

left_motor.control.limits(acceleration=DRIVE_ACCELERATION)
right_motor.control.limits(acceleration=DRIVE_ACCELERATION)

# Buttons paired with the green button to make a command.
COMMANDS = {
    Button.LEFT_PLUS: ("Blade up/down", 0, Color.BLUE),
    Button.LEFT_MINUS: ("Blade tilt", 270, Color.RED),
    Button.RIGHT_PLUS: ("Ladder", 180, Color.YELLOW),
    Button.RIGHT_MINUS: ("Ripper", 90, Color.GREEN),
}

# Find the right end left endstop positions
right_end = switch_motor.run_until_stalled(500, duty_limit=50)
left_end = switch_motor.run_until_stalled(-500, duty_limit=50)

# The full switch motion ranges 270 degrees. Everything beyond that
# is play towards the endstops, equal in both directions. Since we
# are currently at the left endpoint, we can reset the angle
# accordingly. This way, the functions # are simply at the
# relative positions 0, 90, 180, 270.
switch_motor.reset_angle(-(right_end - left_end - 270) / 2)


def switch_target(target_angle):
    # Try up to 5 times.
    for i in range(5):

        # Keep track of how long we've tried.
        watch = StopWatch()
        switch_motor.run_target(SWITCH_SPEED, target, wait=False)

        # Wait until the stopwatch times out.
        while watch.time() < 2000:
            wait(10)
            # We're done if the motor is on target, so exit
            # this function.
            if switch_motor.control.done():
                return

        # Otherwise, we got stuck, so try wiggling around to
        # release it.
        print("Getting unstuck.")
        switch_motor.run_target(SWITCH_SPEED, 0, wait=False)
        wait(1500)
        switch_motor.run_target(SWITCH_SPEED, 270, wait=False)
        wait(1500)


while True:

    # Check which buttons are pressed
    wait(10)
    pressed = remote.buttons.pressed()

    # If the center button is pressed, process the
    # corresponding command.
    if Button.CENTER in pressed:

        # Stop driving
        right_motor.stop()
        left_motor.stop()
        function_motor.stop()

        # Go through the commands.
        for button, command in COMMANDS.items():

            # Check if the command has a matching button.
            if button in pressed:

                # Now we can unpack the command.
                name, target, color = command

                # Execute command.
                print("Selected:", name)
                remote.light.on(color)
                switch_target(target)

                # Wait for the button to be released.
                while button in remote.buttons.pressed():
                    wait(10)

    # Activate function_motor motor based on the red buttons.
    if Button.LEFT in pressed:
        function_motor.dc(FUNCTION_POWER)
    elif Button.RIGHT in pressed:
        function_motor.dc(-FUNCTION_POWER)
    else:
        function_motor.stop()

    # Choose drive speed based on +/- buttons.
    left_speed = 0
    right_speed = 0
    if Button.LEFT_PLUS in pressed:
        left_speed += DRIVE_SPEED
    if Button.LEFT_MINUS in pressed:
        left_speed -= DRIVE_SPEED
    if Button.RIGHT_PLUS in pressed:
        right_speed += DRIVE_SPEED
    if Button.RIGHT_MINUS in pressed:
        right_speed -= DRIVE_SPEED

    # Activate the driving motors.
    left_motor.run(left_speed)
    right_motor.run(right_speed)
