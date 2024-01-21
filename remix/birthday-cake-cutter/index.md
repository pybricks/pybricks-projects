---
title: "Birthday Bot: Cake Cutter"
maintainer:
  user: "TheVinhLuong102"
  name: "The Lương-Phạm Family"
image:
  local: "birthday-cake-cutter.jpg"
video:
  youtube: "yckg0h2E-Ac"
description:
    "Strong with a lot of torque, this robot is ready to cut the cake with a knife wielded by its powerful arm. It drives around on four wheels and also sings Happy Birthday. Member of the Lương-Phạm family's Birthday Bots squad, alongside Birthday Candle Blower and Birthday Gift Presenter."
building_instructions:
  local: TODO
code: "#program"
---


Control the Birthday Cake Cutter by the Powered-Up Remote as follows:

- Switch between two modes:
  - Left Red Button: Driving Mode (center button of Hub will turn green)
  - Right Red Button: Cake-Cutting Mode (center button of Hub will turn red)

- Driving Mode: (refer to the `RemoteControlledDriveBase` code below)
  - 2 Top/Plus buttons together: drive forward
  - 2 Bottom/Minus buttons together: drive backward
  - Top-Left/Left-Plus and Bottom-Right/Right-Minus together: turn left on the spot
  - Top-Right/Right-Plus and Bottom-Left/Left-Minus together: turn right on the spot
  - Top-Left/Left-Plus: turn left forward
  - Top-Right/Right-Plus: turn right forward
  - Bottom-Left/Left-Minus: turn left backward
  - Bottom-Right/Right-Minus: turn right backward

- Cake-Cutting Mode: 
  - Arm Control:
    - Bottom-Left/Left-Minus: bring arm backward
    - Top-Left/Left-Plus: bring arm forward
  - Knife Control:
    - Bottom-Right/Right-Minus: bring knife backward
    - Top-Right/Right-Plus: bring knife forward

- Singing Happy Birthday: green Center button


## Technical Design and Safety Notes

For the Arm and Knife to cut hard cakes, we design them with high torque. (The opposite is true for its friend Candle Blower, which needs high speed and low torque for its fan.)

For safety, this robot uses a plastic butter knife. If you want a big, sharp metal knife instead, you have to re-design the knife holder (and operate at your own risk!).


## Program

{% include copy-code.html %}
```python
{% include_relative main.py %}
```
