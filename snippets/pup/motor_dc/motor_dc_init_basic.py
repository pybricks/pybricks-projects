from pybricks.pupdevices import DCMotor
from pybricks.parameters import Port
from pybricks.tools import wait

# Initialize a motor without rotation sensors on port A.
example_motor = DCMotor(Port.A)

# Make the motor go clockwise (forward) at 70% duty cycle ("70% power").
example_motor.dc(70)

# Wait for three seconds.
wait(3000)

# Make the motor go counterclockwise (backward) at 70% duty cycle.
example_motor.dc(-70)

# Wait for three seconds.
wait(3000)
