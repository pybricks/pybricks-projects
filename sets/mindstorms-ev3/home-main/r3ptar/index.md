---
title: "LEGO® MINDSTORMS® EV3 Home Edition: R3ptar"
maintainer:
    user: "TheVinhLuong102"
    name: "The Lương-Phạm Family"
image:
    local: "r3ptar.jpeg"
    credit: "LEGO"
description:
    "One of the most loved robots, the standing 35 cm. / 13.8 inch tall R3PTAR robot slithers across the floor like a real cobra, and strikes at lightning speed with it’s pointed red fangs."
building_instructions:
    external: https://www.lego.com/cdn/product-assets/product.bi.additional.extra.pdf/31313_X_R3PTAR.pdf
---


This program requires LEGO® EV3 MicroPython v2.0 downloadable at https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3.

R3ptar can be driven around by the IR Remote Control, strikes when the Beacon button is pressed, and hisses when the Touch Sensor is pressed.

The code for the `R3ptar` class is in `r3ptar.py` as follows:

{% include copy-code.html %}
```python
{% include_relative r3ptar.py %}
```

The code for the main program is in `main.py` as follows:

{% include copy-code.html %}
```python
{% include_relative main.py %}
```
