#!/usr/bin/env pybricks-micropython
from pybricks.parameters import Port
from pybricks.nxtdevices import VernierAdapter

from math import log


# Conversion formula for Surface Temperature Sensor
def convert_raw_to_temperature(voltage):

    # Convert the raw voltage to the NTC resistance
    # according to the Vernier Adapter EV3 block.
    counts = voltage/5000*4096
    ntc = 15000*(counts)/(4130-counts)

    # Handle log(0) safely: make sure that ntc value is positive.
    if ntc <= 0:
        ntc = 1

    # Apply Steinhart-Hart equation as given in the sensor documentation.
    K0 = 1.02119e-3
    K1 = 2.22468e-4
    K2 = 1.33342e-7
    return 1/(K0 + K1*log(ntc) + K2*log(ntc)**3)


# Initialize the adapter on port 1
thermometer = VernierAdapter(Port.S1, convert_raw_to_temperature)

# Get the measured value and print it
temp = thermometer.value()
print(temp)
