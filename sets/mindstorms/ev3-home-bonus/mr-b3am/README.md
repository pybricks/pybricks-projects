---
permalink: /projects/sets/mindstorms/ev3-home-bonus/mr-b3am/
title: "LEGO® MINDSTORMS® EV3 Home Edition: Fan Robots: Mr. B3am"
maintainer:
    user: "TheVinhLuong102"
    name: "The Lương-Phạm Family"
image:
    local: "mr-b3am.png"
    credit: "LEGO"
video:
    youtube: "dZYliR8eHSo"
description:
    "This funny-looking robot is ready to organize all your LEGO® Technic beams. Simply insert the beams into the machine, and MR B3AM will detect their color and size."
building_instructions:
    external: https://www.lego.com/cdn/product-assets/product.bi.additional.extra.pdf/31313_X_MR%20B3AM.pdf
---


This program requires LEGO® EV3 MicroPython v2.0 downloadable at https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3.

NOTE: Mr. B3am can detect and measure accurately Black and Red Technic beams.

The code for the `MrB3am` class is in `mr_b3am.py` as follows:

{% include copy-code.html %}
```python
{% include_relative mr_b3am.py %}
```

The code for the main program is in `main.py` as follows:

{% include copy-code.html %}
```python
{% include_relative main.py %}
```
