from pybricks.iodevices import XboxController
from pybricks.parameters import Direction, Port
from pybricks.pupdevices import Motor
from pybricks.robotics import Car

# Set up all devices.
front = Motor(Port.A, Direction.CLOCKWISE)
rear = Motor(Port.B, Direction.CLOCKWISE)
steer = Motor(Port.D, Direction.CLOCKWISE)
car = Car(steer, [front, rear])
controller = XboxController()


# The main program starts here.
while True:

    # Drive using the trigger inputs.
    brake, acceleration = controller.triggers()
    car.drive_power(acceleration - brake)

    # Steer with the left joystick.
    horizontal, vertical = controller.joystick_left()
    car.steer(horizontal)
