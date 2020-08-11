from pybricks.pupdevices import ColorDistanceSensor, PFMotor
from pybricks.parameters import Port, Color
from pybricks.tools import wait

# Initialize the sensor.
sensor = ColorDistanceSensor(Port.B)

# Initialize a motor on channel 1, on the red output.
motor = PFMotor(sensor, 1, Color.RED)

# Rotate and then stop.
motor.dc(100)
wait(1000)
motor.stop()
wait(1000)

# Rotate the other way at half speed, and then stop.
motor.dc(-50)
wait(1000)
motor.stop()
