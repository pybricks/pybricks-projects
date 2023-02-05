from pybricks.pupdevices import TiltSensor, ColorLightMatrix
from pybricks.parameters import Port, Color
from pybricks.tools import wait
from pybricks.experimental import Broadcast

# Initialize the devices.
lights = ColorLightMatrix(Port.A)
sensor = TiltSensor(Port.B)

# Initialize broadcast with two topics.
radio = Broadcast(topics=["tilt", "distance"])

while True:
    # Read pitch and roll.
    pitch, roll = sensor.tilt()

    # Make small tilt zero.
    if abs(pitch) < 5:
        pitch = 0
    if abs(roll) < 5:
        roll = 0

    # Send the data!
    radio.send("tilt", (pitch, roll))

    # Check for distance data.
    data = radio.receive("distance")

    # If there was distance data, use it to activate the light.
    if data and data < 500:
        lights.on(Color.RED)
    else:
        lights.off()

    # Wait some time.
    wait(10)
