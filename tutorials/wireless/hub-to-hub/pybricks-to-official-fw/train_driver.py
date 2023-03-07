from pybricks.hubs import EssentialHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Color, Port
from pybricks.tools import wait

# This imports the DuploTrain from the duplo.py file.
from duplo import DuploTrain

# Initialize the hub and devices. You can use any other hub too.
hub = EssentialHub()
dial = Motor(Port.A)
sensor = ColorSensor(Port.B)

# Connect to the train.
train = DuploTrain()

# These variables are used to monitor the angle and color state.
last_angle = 0
last_color = Color.BLACK

while True:
    # If the measured color changed, play choo choo
    # and set the hub and train light to match.
    color = sensor.color()
    if last_color != color:
        last_color = color
        if color != Color.NONE:
            train.choo_choo()
        hub.light.on(color)
        train.light(color)
        
    # Read the angle and discard low values.
    angle = dial.angle()
    if abs(angle) < 25:
        angle = 0

    # Skip updating on small changes to reduce traffic.
    if abs(last_angle - angle) < 10:
        wait(10)
        continue

    # Send new speed.
    last_angle = angle
    train.drive(angle)
