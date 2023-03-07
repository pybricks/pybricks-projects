from pybricks.iodevices import LWP3Device
from pybricks.parameters import Color
from pybricks.tools import wait

# Device identifier for the Duplo Hub.
DUPLO_TRAIN_ID = 0x20

# Mapping that converts colors to LEGO color identifiers.
COLORS = {
    Color.NONE: 0,
    Color.MAGENTA: 2,
    Color.BLUE: 3,
    Color.GREEN: 6,
    Color.YELLOW: 7,
    Color.ORANGE: 8,
    Color.RED: 9,
}

class DuploTrain():
    """Class to connect to the Duplo train and send commands to it."""

    def __init__(self):
        """Scans for a train, connect, and prepare it to receive commands."""
        print("Searching for the train. Make sure it is on.")
        self.device = LWP3Device(DUPLO_TRAIN_ID, name=None, timeout=10000)
        self.device.write(bytes([0x0a, 0x00, 0x41, 0x01, 0x01, 0x01, 0x00, 0x00, 0x00, 0x01]))
        print("Connected!")
        wait(500)

    def choo_choo(self):
        """Plays the choo choo sound."""
        self.device.write(bytes([0x08, 0x00, 0x81, 0x01, 0x11, 0x51, 0x01, 0x09]))

    def light(self, color):
        """Turns on the train light at the requested color."""
        if color not in COLORS:
            return
        self.device.write(bytes([0x08, 0x00, 0x81, 0x11, 0x11, 0x51, 0x00, COLORS[color]]))

    def drive(self, power):
        """Drives at a given "power" level between -100 and 100."""
        power = max(-100, min(power, 100))
        if power < 0:
            power += 256
        self.device.write(bytes([0x08, 0x00, 0x81, 0x00, 0x01, 0x51, 0x00, power]))
