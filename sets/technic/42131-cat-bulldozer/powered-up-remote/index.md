---
title: "Powered Up Remote Control"
maintainer:
    user: "pybricks"
    name: "The Pybricks Team"
image:
    local: "42131-cat-bulldozer-remote.jpg"
description:
    "Control the Cat Bulldozer with the Powered Up Remote!"
video:
    youtube: "N7OmW-7u8fA"
building_instructions:
    external:
    - https://www.lego.com/cdn/product-assets/product.bi.core.pdf/6403271.pdf
    - https://www.lego.com/cdn/product-assets/product.bi.core.pdf/6403276.pdf
code: "#program"
---


# Program

This program lets you drive and operate the Cat® D11 Bulldozer using the
Powered Up remote control. No smartphone required!

When the program begins, it resets the function selector to the zero position,
corresponding to the blade up and down movement. You can select any function
by pressing the *green button* along with one of the gray buttons. This will
change the remote light and switch the function selector as follows:

* Left ＋ (blue): Moves the blade up and down.
* Left − (red): Tilts the blade back and forth.
* Right ＋ (yellow): Moves the ladder up and down.
* Right − (green): Moves the ripper up and down.

Once the function is selected, use the red buttons to control the motor that
powers the selected function.

Use the gray buttons to control the tracks. You can change
the ``DRIVE_ACCELERATION`` value in the code to a lower value to make the
vehicle start and stop driving more gradually. You can also change the speed
by reducing the ``DRIVE_SPEED`` value.


{% include copy-code.html %}
```python
{% include_relative main.py %}
```
# Credits

This program was inspired by Pybricks user AVCampos' program first shared on
[Eurobricks](https://www.eurobricks.com/forum/index.php?/forums/topic/182012-42131-cat-d11-bulldozer/&page=46&tab=comments#comment-3455837). Be sure
to check out his code and [video](https://www.youtube.com/watch?v=gy3nFvojZ2o)
for additional inspiration.

And thanks to Jim van Gulik who lent his bulldozer to the Pybricks team to
make this program and video.
