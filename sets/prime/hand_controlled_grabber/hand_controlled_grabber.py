"""
This program is for Hand-Controlled Grabbers
(in the "Invention Squad: Super Clean-Up" lesson unit).

Follow the corresponding building instructions in the LEGO® SPIKE™ Prime App.

Press the Force Sensor to grab objects, and release the Force Sensor to let go.
"""

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import ForceSensor, Motor
from pybricks.parameters import Port


# Configure the Hub, the Force Sensor and the Motor
hub = PrimeHub()
force_sensor = ForceSensor(Port.E)
motor = Motor(Port.A)


while True:
    # Grab when the Force Sensor is pressed
    if force_sensor.pressed():
        motor.run(speed=-1000)

    # else let go
    else:
        motor.run_until_stalled(speed=1000)
