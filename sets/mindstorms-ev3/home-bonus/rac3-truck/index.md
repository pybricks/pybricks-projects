---
title: "Rac3 Truck"
maintainer:
    user: "TheVinhLuong102"
    name: "The Lương-Phạm Family"
image:
    local: "rac3-truck.jpeg"
    credit: "LEGO"
video:
    youtube: "EAzsLYTumW4"
description:
    "Want a remote controlled truck? Got it! This is one fun cool ride. You can modify the truck to make it go faster by adding gears, and you can add a custom-built trailer so the truck can be used as a transport vehicle."
building_instructions:
    external: https://www.lego.com/cdn/product-assets/product.bi.additional.extra.pdf/31313_X_RAC3%20TRUCK.pdf
---


This program requires LEGO® MINDSTORMS® EV3 MicroPython v2.0 downloadable at https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3.

Drive Rac3 Truck around according to instructions from Channel 1 of the IR Remote Control:
    - 2 Top/Up Buttons together: drive forward
    - 2 Bottom/Down Buttons together: drive backward
    - Top-Left/Red-Up: turn left forward
    - Top-Right/Blue-Up: turn right forward
    - Bottom-Left/Red-Down: turn left backward
    - Bottom-Right/Blue-Down: turn right backward

The code for the `Rac3Truck` class is in `rac3_truck.py` as follows:

{% include copy-code.html %}
```python
{% include_relative rac3_truck.py %}
```

The code for the main program is in `main.py` as follows:

{% include copy-code.html %}
```python
{% include_relative main.py %}
```
