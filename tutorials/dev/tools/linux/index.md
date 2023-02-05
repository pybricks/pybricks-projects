---
title: "Using Pybricks on Linux"
maintainer:
    user: "pybricks"
    name: "The Pybricks Team"
image:
    local: "../../dev.png"
description:
    "Configure udev and browser tools to use Pybricks."
---

# Adding udev rules on Linux

By default, Linux does not allow the use of unknown USB devices, so you need to add `udev` rules for your hubs. Pybricks provides a couple of ways to do this.

If you are using an Ubuntu-based Linux distro, you can install the `pbrick-rules` package from the Pybricks PPA. This method has the advantage of automatic updates.

{% include copy-code.html %}
```
sudo add-apt-repository --update ppa:pybricks/ppa
sudo apt install pbrick-rules
```

You can alternately install the rules using the `pybricksdev` command line tool:

{% include copy-code.html %}
```
pipx run pybricksdev udev | sudo tee /etc/udev/rules.d/99-pybricksdev.rules
```

If neither of these options is suitable, you can manually copy [this file](https://github.com/pybricks/pybricksdev/blob/master/pybricksdev/resources/99-pybricksdev.rules) to `/etc/udev/rules.d/99-pybricksdev.rules`.

After installing the `udev` rules, disconnect any affected devices and plug them back in. 

If this doesn't seem to work, try rebooting.
