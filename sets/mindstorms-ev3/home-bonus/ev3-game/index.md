---
title: "Fan Robot: EV3 Game"
maintainer:
    user: "TheVinhLuong102"
    name: "The Lương-Phạm Family"
image:
    local: "ev3-game.jpeg"
    credit: "LEGO"
video:
    youtube: "OdSyquY3RXA&t"
description:
    "This robot is all set to play tricks on you. Hide the red ball under the shell, use the IR Beacon to set your level, and watch the robot shuffle and hide the ball – but where? Challenge your friends to see who can find the red ball first!"
building_instructions:
    external: https://www.lego.com/cdn/product-assets/product.bi.additional.extra.pdf/31313_X_EV3%20GAME.pdf
---


This program requires LEGO® EV3 MicroPython v2.0 downloadable https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3.

EV3Game works as follows:

- Put a small ball or marble under the middle cup. 

- Choose the difficulty level by the IR beacon buttons: the Up buttons raise the level (up to 9) and the Down buttons lower the level (minimum 1). The level is printed on the screen.

- Press the Touch Sensor to start the game and make the robot shuffle the cups.

- Guess which cup has the ball by pressing:
  - Left Up IR button: choose left cup
  - Beacon IR button (press twice): choose middle cup
  - Right Up IR button: choose right cup

- Repeat again and again to play many games.

The code for the `EV3Game` class is in `ev3_game.py` as follows:

{% include copy-code.html %}
```python
{% include_relative ev3_game.py %}
```

The code for the main program is in `main.py` as follows:

{% include copy-code.html %}
```python
{% include_relative main.py %}
```
