---
permalink: /projects/sets/mindstorms/ev3-home-bonus/robodoz3r/
title: "LEGO Mindstorms EV3 Home Edition: Fan Robots: Robodoz3r"
maintainer:
    user: "TheVinhLuong102"
    name: "The Lương-Phạm Family"
image:
    local: "robodoz3r.jpeg"
    credit: "LEGO"
description:
    "This robot bulldozer can be controlled using the IR Beacon or it can drive on it’s own, avoiding obstacles while clearing and pushing things with its bulldozer bucket."
building_instructions:
    external: https://www.lego.com/cdn/product-assets/product.bi.additional.extra.pdf/31313_X_ROBODOZ3R.pdf
---


# Example LEGO® MINDSTORMS® EV3 RoboDoz3r Program

This program requires LEGO® EV3 MicroPython v2.0 downloadable at https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3.

Building instructions can be found at https://www.lego.com/en-us/themes/mindstorms/buildarobot.

Control RoboDoz3r as follows:

- RoboDoz3r starts with the User-Controlled Mode. You can switch between the User-Controlled Mode and the Autonomous Mode by pressing the Touch Sensor.

- User-Controlled Mode:

    - Drive RoboDoz3r around according to instructions from Channel 1 of the IR Remote Control:
        - 2 Top/Up Buttons together: drive forward
        - 2 Bottom/Down Buttons together: drive backward
        - Top-Left/Red-Up and Bottom-Right/Blue-Down together: turn left on the spot
        - Top-Right/Blue-Up and Bottom-Left/Red-Down together: turn right on the spot
        - Top-Left/Red-Up: turn left forward
        - Top-Right/Blue-Up: turn right forward
        - Bottom-Left/Red-Down: turn left backward
        - Bottom-Right/Blue-Down: turn right backward

    - Use Channel 4 of the IR Remote Control to make RoboDoz3r raise the shovel by pressing either Up button, or lower the shovel by pressing either Down button

- Autonomous Mode: RoboDoz3r drives around on his own to clean up small things but avoids big obstacles by reversing and turning
