---
title: "Spik3r"
maintainer:
    user: "TheVinhLuong102"
    name: "The Lương-Phạm Family"
image:
    local: "spik3r.jpeg"
    credit: "LEGO"
description:
    "This six-legged creature doesn’t just look like a scorpion, it also acts like one. It turns sharply, snaps with it’s crushing claw, and it’s lightning tail is ready to fire at anyone or anything that gets in its way."
building_instructions:
    external: https://www.lego.com/cdn/product-assets/product.bi.additional.extra.pdf/31313_X_SPIK3R.pdf
---


This program requires LEGO® EV3 MicroPython v2.0 downloadable at https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3.

Spik3r works as follows:

- Spik3r stings with its Lightning Tail when the Beacon button is pressed

- Spik3r moves forward when the IR Beacon's two Up buttons are pressed, and turns right when only the Right Up button is pressed

- Spik3r crushes objects with its Claw when the Touch Sensor is pressed

The code for the `Spik3r` class is in `spik3r.py` as follows:

{% include copy-code.html %}
```python
{% include_relative spik3r.py %}
```

The code for the main program is in `main.py` as follows:

{% include copy-code.html %}
```python
{% include_relative main.py %}
```
