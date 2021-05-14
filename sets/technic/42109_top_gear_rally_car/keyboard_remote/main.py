from pybricks.hubs import TechnicHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Stop
from pybricks.tools import wait
from pybricks.experimental import getchar

hub = TechnicHub()

drive = Motor(Port.D)
steer = Motor(Port.B)

SPEED_DRIVE = 100
TIME_DRIVE = 30
STEP_STEER = 15
SPEED_STEER = 720
MAX_STEER = 75

steer.reset_angle()
steer.run_target(SPEED_STEER, 0, then=Stop.BRAKE)

while True:
    c = getchar()
    if c == ord('q'):
        drive.dc(SPEED_DRIVE)
        wait(TIME_DRIVE)
    elif c == ord('a'):
        drive.dc(-SPEED_DRIVE)
        wait(TIME_DRIVE)
    elif c == ord('o'):
        if steer.angle() > -MAX_STEER:
            steer.run_angle(SPEED_STEER, -STEP_STEER, then=Stop.BRAKE)
    elif c == ord('p'):
        if steer.angle() < MAX_STEER:
            steer.run_angle(SPEED_STEER, STEP_STEER, then=Stop.BRAKE)
    elif c == ord('r') or c == ord('0'):
        steer.run_target(SPEED_STEER, 0, then=Stop.BRAKE)
    else:
        drive.stop()
