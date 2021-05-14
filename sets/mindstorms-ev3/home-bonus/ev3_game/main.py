#!/usr/bin/env pybricks-micropython


from pybricks.media.ev3dev import SoundFile
from pybricks.parameters import Color
from pybricks.tools import wait

from ev3_game import EV3Game


ev3_game = EV3Game()

ev3_game.start_up()

while True:
    ev3_game.cup_with_ball = 2

    ev3_game.select_level()

    ev3_game.ev3_brick.light.on(color=Color.GREEN)

    ev3_game.shuffle()

    ev3_game.reset_motor_positions()

    ev3_game.ev3_brick.light.off()

    correct_choice = False

    while not correct_choice:
        ev3_game.select_choice()

        ev3_game.cup_to_center()

        # The choice will be now in the middle, Position 2

        ev3_game.lift_cup()

        correct_choice = (ev3_game.cup_with_ball == 2)

        if correct_choice:
            ev3_game.ev3_brick.light.on(color=Color.GREEN)

            ev3_game.ev3_brick.speaker.play_file(file=SoundFile.CHEERING)

        else:
            ev3_game.ev3_brick.light.on(color=Color.RED)

            ev3_game.ev3_brick.speaker.play_file(file=SoundFile.BOO)

        wait(2000)

        ev3_game.calibrate_grip()
