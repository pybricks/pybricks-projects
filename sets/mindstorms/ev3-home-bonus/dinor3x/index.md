---
title: "LEGO® MINDSTORMS® EV3 Home Edition: Fan Robots: Dinor3x"
maintainer:
    user: "TheVinhLuong102"
    name: "The Lương-Phạm Family"
image:
    local: "dinor3x.jpeg"
    credit: "LEGO"
video:
    youtube: "eG5xdZ3l1AQ"
description:
    "This charming robotic triceratops dinosaur is capable of walking and turning on all fours."
building_instructions:
    external: https://www.lego.com/cdn/product-assets/product.bi.additional.extra.pdf/31313_X_DINOREX.pdf
---


This program requires LEGO® EV3 MicroPython v2.0 downloadable at https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3.

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

The code for the `Dinor3x` class is in `dinor3x.py` as follows:

{% include copy-code.html %}
```python
{% include_relative dinor3x.py %}
```

The code for the main program is in `main.py` as follows:

{% include copy-code.html %}
```python
{% include_relative main.py %}
```
