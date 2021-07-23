---
title: "Powered Up Remote Control"
maintainer:
    user: "JorgePe"
    name: "Jorge Pereira"
image:
    local: "powered-up-remote-buggy.jpg"
description:
    "Control LEGO Technic vehicles with the Powered Up Remote."
video:
    youtube: st_lcMgz618
building_instructions:
    external: https://www.lego.com/cdn/product-assets/product.bi.core.pdf/6351188.pdf
code: "#program"
---

# How it works

Your MicroPython programs can connect to the Powered Up Remote so you can detect when
any of the buttons are pressed and react to it.

# Program

This program expands the [basic driving program](../driving) with the Powered
Up Remote.

After the program starts it connects to your remote (just press the green button)
then it makes a quick calibration of the steering and you are ready to drive.

Left Channel controls the steering and Right Channel drives the car.

{% include copy-code.html %}
```python
{% include_relative main.py %}
```
