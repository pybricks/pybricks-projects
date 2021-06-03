---
title: "Gripp3r"
maintainer:
    user: "TheVinhLuong102"
    name: "The Lương-Phạm Family"
image:
    local: "gripp3r.jpeg"
    credit: "LEGO"
description:
    "The GRIPP3R robot is constructed for some heavy-duty lifting. It’s got the muscle to grab and drop a can of soda with its powerful grasping grippers."
building_instructions:
    external: https://www.lego.com/cdn/product-assets/product.bi.additional.extra.pdf/31313_X_GRIPP3R.pdf
---


This program requires LEGO® EV3 MicroPython v2.0 downloadable at https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3.

You can drive Gripp3r around and make it grip or release objects by the IR beacon.

The code for the `Gripp3r` class is in `gripp3r.py` as follows:

{% include copy-code.html %}
```python
{% include_relative gripp3r.py %}
```

`Gripp3r` uses a remote-controlled tank driving utility whose code is in `rc_tank_util.py` as follows:

{% include copy-code.html %}
```python
{% include_relative rc_tank_util.py %}
```

The code for the main program is in `main.py` as follows:

{% include copy-code.html %}
```python
{% include_relative main.py %}
```
