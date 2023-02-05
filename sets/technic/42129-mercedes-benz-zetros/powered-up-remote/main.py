from pybricks.pupdevices import Motor, DCMotor, Remote
from pybricks.parameters import Port, Direction, Button, Color
from pybricks.tools import wait

# Connect to the remote.
remote = Remote()

# Initialize the drive motors.
drive_motor1 = Motor(Port.A)
drive_motor2 = Motor(Port.B)

# Lower the acceleration so it starts and stops realistically.
drive_motor1.control.limits(acceleration=1000)
drive_motor2.control.limits(acceleration=1000)

# Find the steering endpoint on the left and right.
# The middle is in between.
steer_motor = Motor(Port.D, Direction.COUNTERCLOCKWISE)
left_end = steer_motor.run_until_stalled(-400)
right_end = steer_motor.run_until_stalled(400)

# Return to the center.
max_steering = (right_end - left_end) / 2
steer_motor.reset_angle(max_steering)
steer_motor.run_target(speed=200, target_angle=0)

# Initialize the differential as unlocked.
lock_motor = DCMotor(Port.C)
LOCK_POWER = 60
lock_motor.dc(-LOCK_POWER)
wait(600)
lock_motor.stop()
locked = True

# Now we can start driving!
while True:
    # Check which buttons are pressed.
    pressed = remote.buttons.pressed()

    # Choose the steer angle based on the left controls.
    steer_angle = 0
    if Button.LEFT_PLUS in pressed:
        steer_angle -= max_steering
    if Button.LEFT_MINUS in pressed:
        steer_angle += max_steering

    # Steer to the selected angle.
    steer_motor.run_target(1000, steer_angle, wait=False)

    # Choose the drive speed based on the right controls.
    drive_speed = 0
    if Button.RIGHT_PLUS in pressed:
        drive_speed += 1000
    if Button.RIGHT_MINUS in pressed:
        drive_speed -= 1000

    # Apply the selected speed.
    drive_motor1.run(drive_speed)
    drive_motor2.run(drive_speed)

    # Button for differential lock
    if Button.CENTER in pressed:
        # Stop the drive motors
        drive_motor1.stop()
        drive_motor2.stop()

        # Run lock motor for half a second.
        remote.light.on(Color.RED)
        lock_motor.dc(LOCK_POWER if locked else -LOCK_POWER)
        wait(500)
        lock_motor.stop()

        # Update lock state.
        locked = not locked
        remote.light.on(Color.BLUE if locked else Color.GREEN)

    # Wait.
    wait(10)
