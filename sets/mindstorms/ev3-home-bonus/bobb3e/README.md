---
permalink: /projects/sets/mindstorms/ev3-home-bonus/bobb3e/
title: "LEGO Mindstorms EV3 Home Edition: Fan Robots: Bobb3e"
maintainer:
    user: "TheVinhLuong102"
    name: "The Lương-Phạm Family"
image:
    local: "bobb3e.jpeg"
    credit: "LEGO"
video:
    youtube: "i3jsJiVKYsg"
description:
    "This remote controlled Bobcat® can be steered to move and lift objects with the control buttons on the IR Beacon."
building_instructions:
    external: https://www.lego.com/cdn/product-assets/product.bi.additional.extra.pdf/31313_X_BOBB3E.pdf
---


This program requires LEGO® EV3 MicroPython v2.0 downloadable at https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3

Control Bobb3e as follows:

- Make Bobb3e lower the forks by pressing the IR Remote Control's 2 Left Buttons together; make him raise the forks by pressing the 2 Right Buttons together

- Drive Bobb3e around according to instructions from the IR Beacon:
    - 2 Top/Up Buttons together: drive forward
    - 2 Bottom/Down Buttons together: drive backward
    - Top-Left/Red-Up and Bottom-Right/Blue-Down together: turn left on the spot
    - Top-Right/Blue-Up and Bottom-Left/Red-Down together: turn right on the spot
    - Top-Left/Red-Up: turn left forward
    - Top-Right/Blue-Up: turn right forward
    - Bottom-Left/Red-Down: turn left backward
    - Bottom-Right/Blue-Down: turn right backward

- Bobb3e beeps his alarm whenever reversing

The code for the `Bobb3e` class is in `bobb3e.py` as follows:

{% include copy-code.html %}
```python
{% include_relative bobb3e.py %}
```

The code for the main program is in `main.py` as follows:

{% include copy-code.html %}
```python
{% include_relative main.py %}
```
