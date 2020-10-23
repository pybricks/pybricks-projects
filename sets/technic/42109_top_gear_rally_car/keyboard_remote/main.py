from pybricks.hubs import TechnicHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Stop
from pybricks.tools import wait
from pybricks.experimental import getchar

hub = TechnicHub()

mDrive = Motor(Port.D)
mSteer = Motor(Port.B)
mSteer.reset_angle()

SPEED_DRIVE = 100
TIME_DRIVE = 30
STEP_STEER = 15
SPEED_STEER = 720
MAX_STEER = 75

mSteer.run_target(SPEED_STEER, 0, then=Stop.BRAKE)

while True:
    c = getchar()
    if c == ord('q'):
        mDrive.dc(SPEED_DRIVE)
        wait(TIME_DRIVE)
    elif c == ord('a'):
        mDrive.dc(-SPEED_DRIVE)
        wait(TIME_DRIVE)
    elif c == ord('o'):
        if mSteer.angle() > -MAX_STEER:
            mSteer.run_angle(SPEED_STEER, -STEP_STEER, then=Stop.BRAKE)
    elif c == ord('p'):
        if mSteer.angle() < MAX_STEER:
            mSteer.run_angle(SPEED_STEER, STEP_STEER, then=Stop.BRAKE)
    elif c == ord('r') or c == ord('0'):
        mSteer.run_target(SPEED_STEER, 0, then=Stop.BRAKE)
    else:
        mDrive.stop()
