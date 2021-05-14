#!/usr/bin/env pybricks-micropython


from dinor3x import Dinor3x


dino = Dinor3x()

dino.close_mouth()

while True:
    dino.roar_by_ir_beacon()
    dino.change_speed_by_color()
    dino.walk_by_ir_beacon()
