# Example LEGO® MINDSTORMS® EV3 Dinor3x Program

This program requires LEGO® EV3 MicroPython v2.0 downloadable at https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3.

Building instructions can be found at https://www.lego.com/en-us/themes/mindstorms/buildarobot.

NOTE: please add a Color Sensor to Dinor3x's back or tail. 

Dinor3x works as follows:

- Dinor3x roars when the Beacon button is pressed

- Dinor3x changes its speed when detecting some colors
    - Red: walk fast
    - Green: walk normally
    - White: walk slowly

- Dinor3x walks or turns according to instructions from the IR Beacon
    - 2 top/up buttons together: walk forward
    - 2 bottom/down buttons together: walk backward
    - Top Left / Red Up: turn left on the spot
    - Top Right / Blue Up: turn right on the spot
    - Bottom Left / Red Down: stop
    - Bottom Right / Blue Down: calibrate to make the legs straight
