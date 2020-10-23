Keyboard Remote

This program demonstrates how to use experimental 'getchar' (similar to 'input' but non-blocking).
The easiest way is running the program through the Pybricks IDE and use the I/O window, 
pressing Q/A/O/P/R keys to control the car:

Q - move forward
A - move backwards
O - turn left
P - turn right
R - reset steering (zero also works)

each time 'O' or 'P' is pressed the steering is increased a bit until the maximum is reached. 'R' or '0' resets the steering.

You can tweak these two parameters for a better driving experience:

TIME_DRIVE 

time in ms that the car moves forward or backward each time a 'Q' or 'A' is pressed
(smaller values will slow it down but it will react faster)

STEP_STEER

angle in degrees that is increased/decreased to the current steering angle each time 'O' or 'P' is pressed

Pressing 'R' or '0' resets the steering angle. Perhaps you want to pre-define some steering values and use
keys like '1' or '2' for turning the weels immediately to those values instead of increasing by steps?

For advanced users, you can replace the keyboard by an external program that connects to the hub through the Nordic UART Service
and sends the same key codes.
