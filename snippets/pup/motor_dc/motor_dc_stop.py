from pybricks.pupdevices import DCMotor
from pybricks.parameters import Port
from pybricks.tools import wait

# Initialize a motor without rotation sensors on port A.
example_motor = DCMotor(Port.A)

# Start and stop 10 times.
for count in range(10):
    print("Counter:", count)

    example_motor.dc(70)
    wait(1000)

    example_motor.stop()
    wait(1000)
