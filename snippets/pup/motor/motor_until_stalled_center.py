from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait

# Initialize a motor on port A.
example_motor = Motor(Port.A)

# Please have a look at the previous example first. This example
# finds two endspoints and then makes the middle the zero point.

# The run_until_stalled gives us the angle at which it stalled.
# We want to know this value for both endpoints.
left_end = example_motor.run_until_stalled(-200, duty_limit=30)
right_end = example_motor.run_until_stalled(200, duty_limit=30)

# We have just moved to the rightmost endstop. So, we can reset
# this angle to be half the distance between the two endpoints.
# That way, the middle corresponds to 0 degrees.
example_motor.reset_angle((right_end - left_end) / 2)

# From now on we can simply run towards zero to reach the middle.
example_motor.run_target(200, 0)

wait(1000)
