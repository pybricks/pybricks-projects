from pybricks.hubs import ThisHub
from pybricks.pupdevices import TiltSensor, ColorLightMatrix
from pybricks.parameters import Port, Color
from pybricks.tools import wait

# Initialize the hub for sending and receiving.
hub = ThisHub(broadcast_channel=1, observe_channels=[2])

# Initialize the devices.
lights = ColorLightMatrix(Port.A)
sensor = TiltSensor(Port.B)

while True:
    # Read pitch and roll.
    pitch, roll = sensor.tilt()

    # Make small tilt zero.
    if abs(pitch) < 5:
        pitch = 0
    if abs(roll) < 5:
        roll = 0

    # Send the data!
    hub.ble.broadcast(pitch, roll)

    # Check for distance data.
    data = hub.ble.observe(2)

    # If there was distance data, use it to activate the light.
    if data is not None and data < 500:
        lights.on(Color.RED)
    else:
        lights.off()

    # Wait some time.
    wait(10)
