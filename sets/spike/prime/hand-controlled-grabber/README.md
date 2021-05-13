---
permalink: /projects/sets/spike/prime/hand-controlled-grabber/
title: "LEGO® Education SPIKE™ Prime: Hand-Controlled Grabber"
maintainer:
    user: "TheVinhLuong102"
    name: "The Lương-Phạm Family"
image:
    local: "hand-controlled-grabber.png"
    credit: "LEGO"
video:
    youtube: "8uyx5npo4LA"
description:
    "Use the Grabber to pick up objects and bring them around!"
building_instructions:
    external:
    - https://education.lego.com/v3/assets/blt293eea581807678a/blt56a81c75560c9a81/5f8802cbf71916144453a493/supercleaup-bi-pdf-book1of3.pdf
    - https://education.lego.com/v3/assets/blt293eea581807678a/bltb8840f08a6d0362b/5f8802dc2792080f7721405c/supercleaup-bi-pdf-book3of3.pdf
---


The program requires PyBricks v3 firmware installed on the Prime Hub.

Press the Force Sensor to grab objects, and release the Force Sensor to let go of them.

The programming code is as follows:

{% include copy-code.html %}
```python
{% include_relative hand-controlled-grabber.py %}
```