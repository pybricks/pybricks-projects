#!/usr/bin/env pybricks-micropython


from pybricks.parameters import Button, Color
from pybricks.tools import wait

from mr_b3am import MrB3am


mr_b3am = MrB3am()

while True:
    mr_b3am.process_b3am()

    mr_b3am.report_result(debug=True)

    mr_b3am.ev3_brick.screen.draw_text(
        x=0, y=105,
        text='Press Enter...',
        text_color=Color.BLACK,
        background_color=None)

    while Button.CENTER not in mr_b3am.ev3_brick.buttons.pressed():
        wait(10)
