---
permalink: /projects/sets/mindstorms/ev3-home-main/track3r/
title: "LEGO Mindstorms EV3 Home Edition: Track3r"
maintainer:
    user: "TheVinhLuong102"
    name: "The Lương-Phạm Family"
image:
    local: "track3r.jpeg"
    credit: "LEGO"
description:
    "TRACK3R is a crawler-mounted, all-terrain robot with four interchangeable tools. Start by building the body of the robot, then discover the possibilities of the four different TRACK3R tools: the bi-blade blender, the blasting bazooka, the gripping claw, and the hammer."
building_instructions:
    external: https://www.lego.com/cdn/product-assets/product.bi.additional.extra.pdf/31313_X_TRACK3R.pdf
---

These programs require LEGO® EV3 MicroPython v2.0 downloadable at https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3.


There are 4 Track3r variants with 4 different tools:

- Track3r with Bi-blade Spinner
- Track3r with Blasting Bazooka
- Track3r with Gripping Claw
- Track3r with Heavy Hammer

The code for the `Track3r` class is in `track3r_base.py` as follows:

{% include copy-code.html %}
```python
{% include_relative track3r_base.py %}
```

The code for the `Track3r` with Biblade_spinner is in `track3r_with_biblade_spinner.py` as follows:

{% include copy-code.html %}
```python
{% track3r_with_biblade_spinner %}
```

The code for the `Track3r` with Blasting bazooka is in `track3r_with_blasting_bazooka.py` as follows:

{% include copy-code.html %}
```python
{% track3r_with_blasting_bazooka %}
```

The code for the `Track3r` with Gripping claw is in `track3r_with_gripping_claw.py` as follows:

{% include copy-code.html %}
```python
{% track3r_with_gripping_claw %}
```

The code for the `Track3r` with Heavy hammer is in `track3r_with_heavy_hammer.py` as follows:

{% include copy-code.html %}
```python
{% track3r_with_heavy_hammer %}
```
