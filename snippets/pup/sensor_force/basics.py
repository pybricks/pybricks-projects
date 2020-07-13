from pybricks.pupdevices import ForceSensor
from pybricks.parameters import Port
from pybricks.tools import wait

# Initialize the sensor.
button = ForceSensor(Port.A)

while True:
    # Read all the information we can get from this sensor.
    force = button.force()
    dist = button.distance()
    press = button.pressed()
    touch = button.touched()

    # Print the values
    print("Force", force, "Dist:", dist, "Pressed:", press, "Touched:", touch)

    # Push the sensor button see what happens to the values.

    # Wait some time so we can read what is printed.
    wait(200)
