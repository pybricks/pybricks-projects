# This header code came from the Pybricks template for the Inventor hub
from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = InventorHub()     

######################## Getting Started ########################

# Define variables (names) for the motors and sensors
arm = Motor(Port.E)
left_wheel = Motor(Port.A, positive_direction=Direction.COUNTERCLOCKWISE)
right_wheel = Motor(Port.B)    # default positive direction is clockwise
color_sensor = ColorSensor(Port.C)
eyes = UltrasonicSensor(Port.D)

# If connected to the Pybricks programming app by Bluetooth, 
# information that you print appears in the scrolling console pane.
print("Running Quick Reference functions...")


######################## Basic Motor Functions ########################

# Make some variables to use in the examples
speed = 500     # (deg/s) up to about 1000 for a MINDSTORMS motor
power = 75      # (percent) -100 (reverse) to 100 (forward)
time = 1000     # (ms) (milliseconds)
angle = 180     # (deg)
pos = 270       # (deg) accumulated and relative to 0 position

left_wheel.dc(power)       # run at % power (duty cycle) without speed control
left_wheel.dc(-power)      # negative power goes backwards
right_wheel.run(speed)     # accelerate to speed, maintain until told different 
right_wheel.run(-speed)    # negative speed goes backwards
right_wheel.run(0)         # controlled deceleration to 0 speed
right_wheel.stop()         # cut power and let coast
right_wheel.brake()        # stop with passive electric braking
right_wheel.hold()         # stop and actively maintain current position

arm.run_time(speed, time)      # run for time interval then stop
arm.run_angle(speed, angle)    # rotate by angle
arm.run_target(speed, 0)       # move to 0 position (absolute 0 if not reset)
arm.run_target(speed, pos)     # rotate to target position
arm.track_target(pos)          # update to new target position
arm.reset_angle(0)             # reset 0 position to motor's current position
arm.reset_angle()              # reset 0 position to motor's absolute 0

speed = left_wheel.speed()    # get current speed (deg/s)
pos = arm.angle()             # get net accumulated angle position (deg)


######################## Advanced Motor Functions ########################

# These options can be used for run_time(), run_angle(), and run_target()
# to allow motor movements to overlap with other movements or actions.
arm.run_target(speed, pos, wait=False)        # continue program right away
arm.run_target(speed, pos, then=Stop.COAST)   # specify a non-hold stop
arm.run_target(speed, pos, wait=False, then=Stop.BRAKE)   # using both options

done = arm.done()         # False if a measured movement is still running 
stalled = arm.stalled()   # True if motor is stalled trying to move
load = arm.load()         # get estimated load torque (mNm)

# The maximum power (duty) is specified very low here at 2% to force a stall.
# A more typical use might be something like 25%, depending on the load.
arm.run_until_stalled(speed, duty_limit=2)    # run until stall

max_speed = 700     # maximum allowed speed (deg/s)
accel = 500         # acceleration (deg/s^2)
decel = 1000        # deceleration (deg/s^2)
torque = 120        # maximum torque (mNm)
arm.control.limits(max_speed, accel, torque)           # decel = accel
arm.control.limits(max_speed, (accel, decel), torque)     
limits = arm.control.limits()      # get current limits (tuple of 3 numbers)


######################## Basic 2-Motor Driving ########################

# Variables to use in the examples
diameter = 56       # wheel diameter (mm) (the large tires are 56 mm)
track = 96          # left to right wheel spacing (mm) (hole spacing is 8 mm)
distance = 200      # travel distance (mm)
drive_speed = 200   # straight driving speed (mm/s)
turn_rate = 150     # turning speed (deg/s)
angle = 90          # heading angle change (deg)
radius = 120        # turning radius (mm)

# Make a DriveBase from two motors.
# Typically the motors in a vehicle will be facing opposite directions, 
# so make sure the two motors have their positive directions set correctly
# as in the definition of left_wheel and right_wheel above.
drive_base = DriveBase(left_wheel, right_wheel, diameter, track)

drive_base.straight(distance)      # straight forward for distance then stop
drive_base.straight(-distance)     # backwards
drive_base.turn(angle)             # turn in place to the right by angle
drive_base.turn(-angle)            # to the left
drive_base.curve(radius, angle)    # arc of radius to the right for angle
drive_base.curve(radius, -angle)   # to the left

drive_base.drive(drive_speed, turn_rate)    # drive/steer until told otherwise
drive_base.drive(0, 0)                      # decelerate to a stop
drive_base.stop()                           # coast to a stop


######################## Advanced 2-Motor Driving ########################

# These options can be used for straight(), turn(), and curve()
drive_base.straight(distance, wait=False)        # continue program right away
drive_base.straight(distance, then=Stop.BRAKE)   # specify a non-hold stop

straight_speed = 200    # straight driving speed (mm/s)
straight_accel = 400    # straight acceleration (mm/s^2)
turn_rate = 180         # turning rate (deg/s)
turn_accel = 300        # turning acceleration and deceleration (deg/s^2)
drive_base.settings(straight_speed, straight_accel, turn_rate, turn_accel)
settings = drive_base.settings()    # get current settings (tuple of 4 numbers)

distance = drive_base.distance()    # get estimated driven distance
angle = drive_base.angle()          # get estimated rotation angle since reset
drive_base.reset()                  # reset estimated rotation angle
done = drive_base.done()            # False if not done with measured driving
stalled = drive_base.stalled()      # True if stalled trying to drive


######################## Color Sensor ########################

# By default, color sensing returns one of:
#   Color.RED, Color.YELLOW, Color.GREEN, Color.BLUE, or Color.WHITE,
# or Color.NONE if not close enough to any of these.  
color = color_sensor.color()            # get detected color with LED on
ambient = color_sensor.color(False)     # get ambient color with LED off
if (ambient == Color.GREEN):
    print("It's green outside for some reason")

# Measure any color without rounding to nearest color in list
surface = color_sensor.hsv()     # measure exact color (hue, saturation, value)
if (surface.h < 60 and surface.s > 75 and surface.v > 50):  # Google HSV Color
    print("Surface is bright red")   

# Change the list of possible colors detected by the color() function
teal = Color(192, 84, 72)     # define a custom color (hue, saturation, value)
my_colors = [Color.BLUE, Color.BLACK, teal, surface]   # my list of colors
color_sensor.detectable_colors(my_colors)   # change color list used by color()

# Brightness sensing
intensity = color_sensor.reflection()  # get reflected intensity 0-100 (LED on)
intensity = color_sensor.ambient()     # get ambient intensity 0-100 (LED off)

# Control the LEDs on the sensor (there are 3 spaced in a circle)
color_sensor.lights.on(10)              # turn on all 3 at 10% intensity
color_sensor.lights.on([100, 0, 0])     # only 1 of 3 lights on at 100%
color_sensor.lights.off()               # all off


######################## Ultrasonic (Distance) Sensor ########################

distance = eyes.distance()    # distance (mm) or 2000 if nothing seen

# Control the LEDs on the sensor (there are 2 above the eyes and 2 below)
eyes.lights.on(100)                 # all lights on at 100% (0-100)
eyes.lights.on([100, 100, 0, 0])    # upper lights only
eyes.lights.off()                   # all lights off


######################## Basic Hub Functions ########################

hub.light.on(Color.GREEN)      # set status (center button) light color
hub.light.off()                # status light off

hub.display.off()              # all display pixels off
hub.display.pixel(0, 4, 75)    # pixel (0, 4) (upper-rightmost) on at 75%

from pybricks.parameters import Icon    # template does not import Icon
hub.display.icon(Icon.HEART)    # display standard icon (see parameters > Icon)

hub.display.char("!")             # display one letter/digit/symbol
hub.display.text("Hello")         # shows one character at a time
hub.display.text("Hey", 300, 40)  # each char for 300 ms, 40 ms pauses between
hub.display.number(45)            # display 2-digit number in a narrow font

hub.speaker.volume(50)          # set volume %, 100% is surprisingly loud
volume = hub.speaker.volume()   # get current volume
hub.speaker.beep()              # default beep sound
hub.speaker.beep(220, 40)       # frequency 220 hz, duration 40 ms

pressed = hub.buttons.pressed()   # get list of hub buttons currently pressed
if (Button.LEFT in pressed):
    print("Left arrow button is pressed")


######################## Advanced Hub Functions ########################

from pybricks.parameters import Side    # template does not import Side
hub.display.orientation(Side.LEFT)  # set display orientation to left side up

hub.light.blink(Color.RED, [200, 150])   # start blinking 200 ms on, 150 ms off

rainbow = [Color.RED, Color.ORANGE, Color.YELLOW, Color.GREEN, Color.BLUE]
hub.light.animate(rainbow, 50)      # rotate through color list 50 ms each

box_icon = ((100, 100, 100, 100, 100),   # 5 x 5 list of brightness (0-100)
            (100,   0,   0,   0, 100),
            (100,   0,   0,   0, 100),
            (100,   0,   0,   0, 100),
            (100, 100, 100, 100, 100))
hub.display.icon(box_icon)               # display a custom icon

frames = (Icon.ARROW_LEFT, Icon.ARROW_RIGHT, box_icon)   # list of icons
hub.display.animate(frames, 200)        # rotate icon frames 200 ms each 

notes = ["C4/16", "E4/16", "G4/16", "C5/4"]  # note octave/duration e.g. 16th
hub.speaker.play_notes(notes, 160)           # play note list at 160 beats/min

orientation = hub.imu.up()     # get current hub orientation (e.g. Side.TOP)
tilt_angles = hub.imu.tilt()   # gets a tuple (pitch, roll)
pitch = tilt_angles[0]
roll = tilt_angles[1]

# Accelerometer returns force in 3 axes in mm/s^2. Divide by 9810 to get g's.
accelerations = hub.imu.acceleration()     # gets a vector (x, y, z)
x_accel = accelerations[0]
y_accel = accelerations[1]
z_accel = accelerations[2]

# Gyro gets rotation rate in 3 axes in deg/s
angular_velocities = hub.imu.angular_velocity()    # gets a vector (x, y, z)
pitch_rate = angular_velocities[0]
roll_rate = angular_velocities[1]
yaw_rate = angular_velocities[2]

voltage = hub.battery.voltage()     # current battery voltage (mV)
current = hub.battery.current()     # battery current (mA)
charging = hub.charger.connected()  # True if charging via USB
current = hub.charger.current()     # charging current (mA)
status = hub.charger.status()       # 0=not, 1=charging, 2=complete, 3=problem

hub.system.set_stop_button(None)  # don't end program on center button
hub.system.set_stop_button([Button.LEFT, Button.RIGHT])  # both arrows to end
hub_name = hub.system.name()          # get hub name


######################## Basic Python Syntax ########################

# Define and change variables and do math
count = 1       # setting an unknown name defines a new variable
speed = 250     # speed was already defined above, so this changes it
count += 1      # increase count by 1
speed = 10 + (power - 30) * (angle / count) + abs(roll_rate) * 2.5

# Print variables and other values to the Pybricks console
print("speed = ", speed)
print("Sensors: color =", color_sensor.hsv(), " distance =", eyes.distance())

# Test for conditions with "if" 
if power < 10:   # forgeting the colon makes a syntax error on the next line
    print("Weak")   # Lines controlled by the if must be indented
if power == 100:       # Use == to compare equality, single = is syntax error
    print("Full power")
if color != Color.NONE:       # This tests "not equal to"
    drive_base.straight(-50)
    drive_base.turn(180)      # Each indented line is controlled by the if
distance = 100                # First un-indented line ends the if control

# if/else and compound tests
if distance >= 90 and distance <= 110:   # greater than or equal, less or equal
    drive_base.stop()
elif distance < 50:       # elif means "else if" to test for another condition
    drive_base.turn(180)
else:                     # if all tests fail, the else section executes
    drive_base.drive(speed, 0)

# Repeat loop with a count
for count in range(5):    # repeat the loop contents 5 times
    eyes.lights.on(100)
    wait(20)               # pause progam for 20 milliseconds
    eyes.lights.off()
    wait(20)

# Loop until a condition is met (use "while True:" to loop forever)
while Button.LEFT in hub.buttons.pressed():
    print("Waiting for button release...")  

# Define your own function (won't happen until you call it)
def my_action():
    drive_base.straight(-50)
    drive_base.turn(90)     # each indented line is inside the function

# Call your function to make it happen
my_action()

# Define a function with input parameters, and use variables
def back_up_and_turn(dist, turn):    # name the input parameters
    drive_base.straight(-dist)       # use the parameters like variables
    drive_base.turn(turn)   # parameter variables can only be used inside
    my_speed = 200   # variables defined inside are also only known inside
    global speed     # Say this to reference a variable defined outside...
    speed = my_speed + 100      # ...then you can set the outside speed.

# Call your function and give numbers (or other variables, etc.) for the inputs
back_up_and_turn(50, 90)      # dist will get 50, turn gets 90


######################## End ########################

print("That's it! See the Pybricks API documentation for more.")
