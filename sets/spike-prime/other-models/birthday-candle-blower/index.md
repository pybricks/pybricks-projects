---
title: "Birthday Bot: Candle Blower"
maintainer:
  user: "TheVinhLuong102"
  name: "The Lương-Phạm Family"
image:
  local: "birthday-candle-blower.jpg"
video:
  youtube: "PAk9mxus1Nk"
description:
  "A cute robot who wheels around and sing Happy Birthday and blow candles by its powerful fan! Member of the Lương-Phạm family's Birthday Bots squad, alongside Birthday Cake Cutter and Birthday Gift Presenter."
building_instructions:
  local: TODO
code: "#program"
---


Control the Birthday Candle Blower by the Powered-Up Remote as follows:

- Driving: (refer to the `RemoteControlledDriveBase` code below)
  - 2 Top/Plus buttons together: drive forward
  - 2 Bottom/Minus buttons together: drive backward
  - Top-Left/Left-Plus and Bottom-Right/Right-Minus together: turn left on the spot
  - Top-Right/Right-Plus and Bottom-Left/Left-Minus together: turn right on the spot
  - Top-Left/Left-Plus: turn left forward
  - Top-Right/Right-Plus: turn right forward
  - Bottom-Left/Left-Minus: turn left backward
  - Bottom-Right/Right-Minus: turn right backward

- Singing Happy Birthday: the green Center button

- Spinning the Fan: 
  - Clockwise (from robot's point of view): red Right button
  - Counterclockwise: left Red button


## Program

{% include copy-code.html %}
```python
{% include_relative main.py %}
```
