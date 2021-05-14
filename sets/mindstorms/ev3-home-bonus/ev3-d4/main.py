#!/usr/bin/env pybricks-micropython


from threading import Thread

from ev3_d4 import EV3D4


ev3_d4 = EV3D4()

Thread(target=ev3_d4.color_sensor_loop).start()
Thread(target=ev3_d4.touch_sensor_loop).start()
ev3_d4.main_switch_loop()
