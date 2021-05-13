---
title: "LEGO® MINDSTORMS® EV3 Home Edition: Ev3rstorm"
maintainer:
    user: "TheVinhLuong102"
    name: "The Lương-Phạm Family"
image:
    local: "ev3rstorm.jpeg"
    credit: "LEGO"
description:
    "EV3RSTORM is the most advanced of the LEGO® MINDSTORMS® robots. Equipped with a blasting bazooka and a spinning tri-blade, EV3RSTORM is superior in both intelligence as well as in fighting power."
building_instructions:
    external: https://www.lego.com/cdn/product-assets/product.bi.additional.extra.pdf/31313_X_EV3RSTORM.pdf
---


This program requires LEGO® EV3 MicroPython v2.0 downloadable at https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3.

Ev3rstorm works as follows:

- You can drive Ev3rstorm around with the IR beacon.

- Ev3rstorm dances by turning by random angles on the spot when the Beacon button is pressed.

- Ev3rstorm blasts his bazooka when his Touch Sensor is pressed. If you cover the Color Sensor then he will shoot upwards, or he will shoot downwards.

The code for the `Ev3rstorm` class is in `ev3rstorm.py` as follows:

{% include copy-code.html %}
```python
{% include_relative ev3rstorm %}
```

`Ev3rstorm` uses a remote-controlled tank driving utility whose code is in `rc_tank_util.py` as follows:

{% include copy-code.html %}
```python
{% include_relative rc_tank_util.py %}
```

The code for the main program is in `main.py` as follows:

{% include copy-code.html %}
```python
{% include_relative main.py %}
```
