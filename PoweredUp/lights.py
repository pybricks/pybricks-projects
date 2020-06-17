from pybricks.pupdevices import Light
from pybricks.hubs import CPlusHub
from pybricks.parameters import Port
from pybricks.tools import wait, StopWatch
from math import cos, pi

hub = CPlusHub()
print(hub.battery.voltage())

# Initialize the light and a StopWatch
lightA = Light(Port.A)
lightB = Light(Port.B)
lightC = Light(Port.C)
lightD = Light(Port.D)
watch = StopWatch()

# Cosine pattern properties
PERIOD = 2
MAX = 100

iCounter=0
iLuce=0
# Make the brightness fade in and out
while True:
    # Get the time in seconds
    time = watch.time()/1000
    
    # Evaluate the cosine
    brightness = (0.5-0.5*cos(time*2*pi/PERIOD))*MAX
    
    iCounter=iCounter+1 
    if iCounter==10:
        if iLuce==0:
            iLuce=100
        else:
            iLuce=0
        
        lightC.on(iLuce)
        lightD.on(100-iLuce)
        iCounter=0
        
    # Turn on the light, wait, then repeat
    lightA.on(brightness)
    lightB.on(100-brightness)
    wait(10)
