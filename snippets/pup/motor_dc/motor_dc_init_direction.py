from pybricks.pupdevices import DCMotor
from pybricks.parameters import Port, Direction
from pybricks.tools import wait

# Initialize a motor without rotation sensors on port A,
# with the positive direction as counterclockwise.
example_motor = DCMotor(Port.A, Direction.COUNTERCLOCKWISE)

# When we choose a positive duty cycle, the motor now goes counterclockwise.
example_motor.dc(70)

# This is useful when your (train) motor is mounted in reverse or upside down.
# By changing the positive direction, your script will be easier to read,
# because a positive value now makes your train/robot go forward.

# Wait for three seconds.
wait(3000)
