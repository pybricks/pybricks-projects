from pybricks.pupdevices import ColorDistanceSensor, PFMotor
from pybricks.parameters import Port, Color, Direction
from pybricks.tools import wait

# Initialize the sensor.
sensor = ColorDistanceSensor(Port.B)

# You can use multiple motors on different channels.
arm = PFMotor(sensor, 1, Color.BLUE)
wheel = PFMotor(sensor, 4, Color.RED, Direction.COUNTERCLOCKWISE)

# Accelerate both motors. Only these values are available.
# Other values will be rounded down to the nearest match.
for duty in [15, 30, 45, 60, 75, 90, 100]:
    arm.dc(duty)
    wheel.dc(duty)
    wait(1000)

# To make the signal more reliable, there is a short
# pause between commands. So, they change speed and
# stop at a slightly different time.

# Brake both motors.
arm.brake()
wheel.brake()
