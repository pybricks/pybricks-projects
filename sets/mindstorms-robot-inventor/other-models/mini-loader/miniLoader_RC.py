from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, UltrasonicSensor, Remote
from pybricks.parameters import Button, Color, Direction, Port, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

# Define objects that correspond to the design of the Mini Loader 
hub = InventorHub()
left_motor = Motor(Port.F, positive_direction=Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.E, positive_direction=Direction.CLOCKWISE)
drive_base = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=80)
lift_motor = Motor(Port.D)
scoop_motor = Motor(Port.C)
eyes = UltrasonicSensor(Port.A)

# Motor speeds
DRIVE_SPEED = 150     # straight driving speed in mm/sec
TURN_RATE = 150       # turning speed in deg/sec
LIFT_SPEED = 200      # deg/sec
SCOOP_SPEED = 200     # deg/sec

# Preset lift and scoop positions (degrees relative to starting ready position)
LIFT_HIGH_POS = 320
LIFT_MIDDLE_POS = 130
LIFT_LOW_POS = 0
SCOOP_READY_POS = -5
SCOOP_DUMP_POS = 10
SCOOP_CARRY_POS = -90

# Connect to the remote (will stop the program if unsuccessful)
rc = Remote()

# Get the set of buttons on the remote that start out pressed 
pressed = rc.buttons.pressed()
was_pressed = pressed   # remembers which buttons were previously pressed


# Return True if the specified button is newly pressed (not held down)
def new_press(button):
    return (button in pressed) and not (button in was_pressed)
     

# This function controls the robot in drive mode
def drive_mode():
    # Pressing and holding either the left or right center button
    # reduces both the drive and steering speed.
    speed = DRIVE_SPEED
    steering = TURN_RATE    
    if (Button.LEFT in pressed) or (Button.RIGHT in pressed):
        speed *= 0.3
        steering *= 0.3    

    # Determine what speed and steering to use.
    # The left side controls drive direction, and the right side steers. 
    current_speed = 0
    current_steering = 0
    if (Button.LEFT_PLUS in pressed):
        current_speed += speed
    if (Button.LEFT_MINUS in pressed):
        current_speed -= speed
    if (Button.RIGHT_PLUS in pressed):
        current_steering += steering
    if (Button.RIGHT_MINUS in pressed):
        current_steering -= steering
    drive_base.drive(current_speed, current_steering)


# This function controls the robot in lift mode
def lift_mode():
    # The three left side buttons set the lift height (high, middle, or low)
    # and automatically adjust the scoop as appropriate.
    if new_press(Button.LEFT_PLUS):
        scoop_motor.run_target(SCOOP_SPEED, SCOOP_CARRY_POS, wait=False)
        lift_motor.run_target(LIFT_SPEED, LIFT_HIGH_POS)
    elif new_press(Button.LEFT):
        scoop_motor.run_target(SCOOP_SPEED, SCOOP_CARRY_POS, wait=False)
        lift_motor.run_target(LIFT_SPEED, LIFT_MIDDLE_POS)
    elif new_press(Button.LEFT_MINUS):
        scoop_motor.run_target(SCOOP_SPEED, SCOOP_READY_POS, wait=False)
        lift_motor.run_target(LIFT_SPEED, LIFT_LOW_POS)
    
    # Right side -/+ buttons dump/undump the scoop
    if new_press(Button.RIGHT_MINUS):
        scoop_motor.run_target(SCOOP_SPEED, SCOOP_DUMP_POS)
    if new_press(Button.RIGHT_PLUS):
        if lift_motor.angle() > LIFT_MIDDLE_POS / 2:    # can't carry if low
            scoop_motor.run_target(SCOOP_SPEED, SCOOP_CARRY_POS)

    # Holding Right Center drives straight forward until the distance sensor
    # is at 5 cm, or until the button is released.
    if new_press(Button.RIGHT):
        eyes.lights.on(100)
        while (eyes.distance() > 50) and (Button.RIGHT in rc.buttons.pressed()):
            drive_base.drive(DRIVE_SPEED, 0)
        drive_base.stop()
        eyes.lights.off()

   
# The remote has multiple modes, selected by the center button.
# This table lists the different mode functions and which color they show.
modes = (
    (drive_mode, Color.GREEN),
    (lift_mode, Color.ORANGE),
)
mode = 0    # index of current mode


# Set the mode to new_mode and update both the remote and hub status lights
def set_mode(new_mode):
    global mode
    mode = new_mode 
    color = modes[mode][1]
    hub.light.on(color)
    rc.light.on(color)


# Set the initial mode
set_mode(mode)

# The main loop repeatedly tests the remote buttons and reacts
while True:
    # Update the set of buttons that are currently pressed,
    # and also remember which ones were pressed the last time we looked.
    was_pressed = pressed
    pressed = rc.buttons.pressed()

    # The green center button changes modes
    if new_press(Button.CENTER):
        set_mode((mode + 1) % len(modes))   # next mode and wrap around

    # Execute the current mode
    modes[mode][0]()

