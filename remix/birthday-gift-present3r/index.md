---
title: "Birthday Bot: Gift Presenter"
maintainer:
  user: "TheVinhLuong102"
  name: "The Lương-Phạm Family"
image:
  local: "birthday-gift-present3r.jpg"
video:
  youtube: "PAk9mxus1Nk"
description:
  "A gentlemanly robot who wheels around, sings Happy Birthday and presents gifts with its arms! Member of the Lương-Phạm family's Birthday Bots squad, alongside Birthday Candle Blower and Birthday Cake Cutter."
building_instructions:
  local: TODO
code: "#program"
---


Control the Birthday Gift Present3r by the IR Beacon as follows:

- Driving by IR Beacon channel #1: (refer to the `rc_tank_util.RemoteControlledTank` code below)
  - 2 Top/Up buttons together: drive forward
  - 2 Bottom/Down buttons together: drive backward
  - Top-Left/Red-Up and Bottom-Right/Blue-Down together: turn left on the spot
  - Top-Right/Blue-Up and Bottom-Left/Red-Down together: turn right on the spot
  - Top-Left/Red-Up: turn left forward
  - Top-Right/Blue-Up: turn right forward
  - Bottom-Left/Red-Down: turn left backward
  - Bottom-Right/Blue-Down: turn right backward

- Singing Happy Birthday: IR Beacon button (any channel)

- Controlling the arms by IR Beacon channel #4: 
  - Lowering the arms: Bottom-Left/Red-Down or Bottom-Right/Blue-Down
  - Raising the arms: Top-Left/Red-Up or Top-Right/Blue-Up


## Program

{% include copy-code.html %}
```python
{% include_relative main.py %}
```

`BirthdayGiftPresent3r` uses a remote-controlled tank driving utility whose code is in `rc_tank_util.py` as follows:

{% include copy-code.html %}
```python
{% include_relative rc_tank_util.py %}
```
