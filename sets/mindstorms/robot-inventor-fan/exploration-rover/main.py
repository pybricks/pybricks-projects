from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Port, Direction, Icon, Color
from pybricks.tools import wait, StopWatch


class ExplorationRover():
    """Control the Mars Exploration Rover."""
    
    # In this robot, we want to detect red and cyan/teal "mars rocks".
    ROCK_COLORS = (Color.RED, Color.CYAN)

    # These are the gears between the motor and the rear wheels.
    REAR_GEARS = (8, 24, 12, 20)
    
    # An animation of heart icons of varying brightness, giving a heart beat.
    HEART_BEAT = [Icon.HEART * i/100 for i in list(range(0, 100, 4)) + list(range(100, 0, -4))]
    
    def __init__(self):
        # Initialize each motor with the correct direction and gearing.
        self.left_rear_wheels = Motor(Port.E, Direction.CLOCKWISE, self.REAR_GEARS)
        self.right_rear_wheels = Motor(Port.F, Direction.COUNTERCLOCKWISE, self.REAR_GEARS)
        self.left_front_wheel = Motor(Port.C, Direction.COUNTERCLOCKWISE, None)
        self.right_front_wheel = Motor(Port.D, Direction.CLOCKWISE, None)

        # Initialize sensors, named after the Perseverance Mars Rover instruments.
        self.mast_cam = UltrasonicSensor(Port.B)
        self.sherloc = ColorSensor(Port.A)
        
        # Initialize the hub and start the animation
        self.hub = InventorHub()
        self.hub.display.animate(self.HEART_BEAT, 30)
    
    def calibrate(self):
        # First, measure the color of the floor. This makes it easy to explicitly
        # ignore the floor later. This is useful if your floor has a wood color,
        # which can appear red or yellow to the sensor.
        self.floor_color = self.sherloc.hsv()
        
        # Set up all the colors we want to distinguish, including no color at all.
        self.sherloc.detectable_colors(self.ROCK_COLORS + (self.floor_color, None))

    def drive(self, speed, steering, time=None):
        # Drive the robot at a given speed and steering for a given amount of time.
        # Speed and steering is expressed as degrees per second of the wheels.
        self.left_rear_wheels.run(speed + steering)
        self.left_front_wheel.run(speed + steering)
        self.right_rear_wheels.run(speed - steering)
        self.right_front_wheel.run(speed - steering)

        # If the user specified a time, wait for this duration and then stop.
        if time is not None:
            wait(time)
            self.stop()
        
    def stop(self):
        # Stops all the wheels.
        self.left_rear_wheels.stop()
        self.left_front_wheel.stop()
        self.right_rear_wheels.stop()
        self.right_front_wheel.stop()

    def scan_rock(self, time):
        # Stops the robot and moves the scan arm.
        self.stop()
        self.left_front_wheel.run(100)
        
        # During the given duration, scan for rocks.
        watch = StopWatch()
        while watch.time() < time:
            
            # If a rock color is detected, display it and make a sound.
            if self.sherloc.color() in self.ROCK_COLORS:
                self.hub.display.image(Icon.CIRCLE)
                self.hub.speaker.beep()
            else:
                self.hub.display.off()
            
            wait(10)
                
        # Turn the arm motor and restore the heartbeat animation again.
        self.hub.display.animate(self.HEART_BEAT, 30)
        self.left_front_wheel.stop()


# The main program starts here. First, initialize the robot.
rover = ExplorationRover()

# Make sure the sensor is at the lowest point and pointing at the floor for
# correct calibration. Then this will calibrate for the floor color.
rover.calibrate()

# Drive around while watching out for colored rocks and obstacles.
while True:
    # Start driving.
    rover.drive(speed=100, steering=0)

    # Wait until we see a rock or another obstacle.
    while rover.sherloc.color() not in rover.ROCK_COLORS and rover.mast_cam.distance() > 500:
        wait(10)

    # If it's a rock, scan it.
    if rover.sherloc.color() in rover.ROCK_COLORS:
        rover.scan_rock(time=5000)
    
    # Back up.
    rover.drive(speed=-100, steering=0, time=2000)

    # Turn around.
    rover.drive(speed=0, steering=100, time=2000)
