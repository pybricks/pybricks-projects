from pybricks.pupdevices import UltrasonicSensor
from pybricks.parameters import Port
from pybricks.tools import wait

# Initialize the sensor.
eyes = UltrasonicSensor(Port.A)

while True:
    # Print the measured distance.
    print(eyes.distance())

    # If an object is detected closer than 500mm:
    if eyes.distance() < 500:
        # Turn the lights on.
        eyes.lights.on(100)
    else:
        # Turn the lights off.
        eyes.lights.off()

    # Wait some time so we can read what is printed.
    wait(100)
