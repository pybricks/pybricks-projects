---
permalink: /projects/sets/mindstorms/ev3-home-bonus/Kraz3/
title: "LEGO Mindstorms EV3 Home Edition: Fan Robots: Kraz3"
maintainer:
    user: "TheVinhLuong102"
    name: "The Lương-Phạm Family"
image:
    local: "kraz3.jpeg"
    credit: "LEGO"
video:
    youtube: "8rJMC98Pjqk"
description:
    "This robot is fun companion with a crazy attitude that reacts to it’s little IR Beacon bug friend. You can control it with the custom program, the IR Beacon, or simply set it to follow it’s little friend around the room."
building_instructions:
    external: https://www.lego.com/cdn/product-assets/product.bi.additional.extra.pdf/31313_X_KRAZ3.pdf
---


This program requires LEGO® EV3 MicroPython v2.0 downloadable at https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3.

Drive Kraz3 around according to instructions from Channel 1 of the IR Remote Control:
    - 2 Top/Up Buttons together: drive forward
    - 2 Bottom/Down Buttons together: drive backward
    - Top-Left/Red-Up: turn left forward
    - Top-Right/Blue-Up: turn right forward
    - Bottom-Left/Red-Down: turn left backward
    - Bottom-Right/Blue-Down: turn right backward

Kraz3 makes a kung-fu move when you press the Touch Sensor or the IR Beacon button.

Kraz3 reacts in funny ways to different colors.

The code for the `Kraz3` class is in `kraz3.py` as follows:

{% include copy-code.html %}
```python
{% include_relative kraz3.py %}
```

The code for the main program is in `main.py` as follows:

{% include copy-code.html %}
```python
{% include_relative main.py %}
```
