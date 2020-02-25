#!/usr/bin/env pybricks-micropython
from pybricks.parameters import Port
from pybricks.iodevices import Ev3devSensor


class MySensor(Ev3devSensor):
    """Example of extending the Ev3devSensor class."""

    def __init__(self, port):
        """Initialize the sensor."""

        # Initialize the parent class.
        super().__init__(port)

        # Get the sysfs path.
        self.path = '/sys/class/lego-sensor/sensor' + str(self.sensor_index)

    def get_modes(self):
        """Get a list of mode strings so we don't have to look them up."""

        # The path of the modes file.
        modes_path = self.path + '/modes'

        # Open the modes file.
        with open(modes_path, 'r') as m:

            # Read the contents.
            contents = m.read()

            # Strip the newline symbol, and split at every space symbol.
            return contents.strip().split(' ')


# Initialize the sensor
sensor = MySensor(Port.S3)

# Show where this sensor can be found
print(sensor.path)

# Print the available modes
modes = sensor.get_modes()
print(modes)

# Read mode 0 of this sensor
val = sensor.read(modes[0])
print(val)
