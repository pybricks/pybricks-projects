---
title: "LEGO® MINDSTORMS® EV3 Home Edition: Fan Robots: EV3-D4"
maintainer:
    user: "TheVinhLuong102"
    name: "The Lương-Phạm Family"
image:
    local: "ev3-d4.png"
    credit: "LEGO"
video:
    youtube: "rtmRZpR0lNA"
description:
    "Inspired by R2D2 from Star Wars, this robot can interact with you, follow you wherever you go or move around the room wherever you want – all via the IR Beacon. The EV3D4 supports a wide set of behaviors that can easily be programmed or extended in the EV3 software."
building_instructions:
    external: https://www.lego.com/cdn/product-assets/product.bi.additional.extra.pdf/31313_X_EV3D4.pdf
---


This program requires LEGO® EV3 MicroPython v2.0 downloadable at https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3.

Drive EV3-D4 around according to instructions from Channel 1 of the IR Remote Control:
    - 2 Top/Up Buttons together: drive forward
    - 2 Bottom/Down Buttons together: drive backward
    - Top-Left/Red-Up: turn left forward
    - Top-Right/Blue-Up: turn right forward
    - Bottom-Left/Red-Down: turn left backward
    - Bottom-Right/Blue-Down: turn right backward

Make him shake his head by pressing the IR Beacon button.

Make him perform random funny actions by pressing his Touch Sensor or show his Color Sensor a red object.

The code for the `EV3D4` class is in `ev3_d4.py` as follows:

{% include copy-code.html %}
```python
{% include_relative ev3_d4.py %}
```

`EV3D4` uses a remote-controlled tank driving utility whose code is in `rc_tank_util.py` as follows:

{% include copy-code.html %}
```python
{% include_relative rc_tank_util.py %}
```

The code for the main program is in `main.py` as follows:

{% include copy-code.html %}
```python
{% include_relative main.py %}
```
