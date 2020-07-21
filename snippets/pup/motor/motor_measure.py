from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait

# Initialize a motor on port A.
example_motor = Motor(Port.A)

# Start moving at 300 degrees per second.
example_motor.run(300)

# Display the angle and speed 50 times.
for i in range(100):

    # Read the angle (degrees) and speed (degrees per second).
    angle = example_motor.angle()
    speed = example_motor.speed()

    # Print the values.
    print(angle, speed)

    # Wait some time so we can read what is displayed.
    wait(200)
