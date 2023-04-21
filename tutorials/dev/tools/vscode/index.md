---
title: "Using Pybricks with Visual Studio Code"
maintainer:
    user: "pybricks"
    name: "The Pybricks Team"
image:
    local: "pybricks-vscode.png"
description:
    "Configure Visual Studio Code to use Pybricks."
---

## Introduction

[Visual Studio Code] is a free code editor available from Microsoft. For
new users we recommend using [Pybricks Code] instead. However, if you are an
advanced user that prefers VS Code, read on.

[Visual Studio Code]: https://code.visualstudio.com
[Pybricks Code]: https://code.pybricks.com

## Creating a new project

If you are using Pybricks on LEGO® MINDSTORMS® EV3, we recommend using the
official [LEGO® MINDSTORMS® EV3 MicroPython][ev3-ext] extension for VS Code.
Everything you need to know from how to install the extension to how to create
a new project is detailed in the [official docs][ev3-docs].

For Powered Up hubs, you can create a new project by simply creating a new,
empty folder on your computer and opening that folder in VS Code.

[ev3-ext]: https://marketplace.visualstudio.com/items?itemName=lego-education.ev3-micropython
[ev3-docs]: https://pybricks.com/ev3-micropython

## Code completion

To get code completion/intellisene working in VS Code you will need to install
the [Pylance] extension and the [pybricks] Python package (preferably in a
virtual environment).

[Pylance]: https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance
[pybricks]: https://pypi.org/project/pybricks

### Installing Python and the Pylance extension

To use Pylance, you will need [Python] installed on your computer. You can
install Python from the [official site][py-dl], or using your favorite package
manager. On Linux, Python is most likely already installed.

On Ubuntu, you will also need to ensure the `venv` package is installed.

    sudo apt install python3-venv

Then follow the link above or search for "Pylance" in the *Extensions* in VS Code
and click *Install* to install the *Pylance* extension.

[Python]: https://www.python.org
[py-dl]: https://www.python.org/downloads

### Setting up a virtual environment

Once *Python* and *Pylance* are installed, you can use VS Code to set up an
isolated *virtual environment*.

- Open your project folder in VS Code.
- If you created your project using the *LEGO® MINDSTORMS® EV3 MicroPython*
  extension, you will need to edit the `.vscode/settings.json` file and change
  `"python.languageServer": "None"` to `"python.languageServer": "Pylance"`
  and save the file, otherwise skip this step.
- Use <kbd>F1</kbd> or <kbd>CTRL</kbd>+<kbd>SHIFT</kbd>+<kbd>P</kbd>
  (<kbd>⌘</kbd>+<kbd>⇧</kbd>+<kbd>P</kbd> on macOS) to open the command palette
  in VS Code.
- Type in "py create env" to search for *Python: Create Environment* and select
  that option.
- It will ask you to "Select and environment type". Choose *Venv*.
- It will ask you to "Select Interpreter". Choose the one you want. If you
  aren't sure, choose the one that says *Global*.
- There will now be a new subfolder in your project named `.venv` that contains
  the virtual environment and VS Code should set it as the interpreter to use
  for your project.
- To use the virtual environment, open the command pallette again and search
  for "py create term" and select *Python: Create Terminal*.
- This should open a new terminal and present a prompt that starts with `(.venv)`,
  if all when well.

The equivalent command line invocation of steps above is:

    # macOS/Linux
    python3 -m venv .venv
    . .venv/bin/activate

<!--></!-->

    # Windows PowerShell
    py -3 -m venv .venv
    .venv/scripts/activate

### Installing the pybricks package

Once you have a `(.venv)` prompt as described in the previous section, you can
install the `pybricks` package by typing the following in the terminal with the
`(.venv)` prompt:

    pip install pybricks

If you are using Pybricks v2.0 with EV3, type this instead to get the correct
version:

    pip install "pybricks<3"

Then you need to restart the Python language server to pick up the new package.
In the command pallette, search for "py restart" and select *Python: Restart
Language Server*.

Now code completion and intellisense should be working. You can try it by
opening an existing file and hovering over text to see the relative documentation
or you can create a new `.py` file and start typing `from pybricks.` and see
suggestions on what comes next.

## Downloading and running programs

If you are using Pybricks on EV3, then refer again to the [official docs][ev3-docs]
to learn how to use the Debug adapter from the *LEGO® MINDSTORMS® EV3 MicroPython*
extension to download and run your programs.

For Powered up hubs, you must use the [pybricksdev] command line tool instead.

Install the `pybricksdev` package in the virtual environment:

    pip install pybricksdev

Then run the following command (replacing `my_program` with the actual name
  of the program you want to run).

    pybricksdev run ble my_program.py

If you have more than one active hub, you can specify a specific hub by name:

    pybricksdev run ble --name "my hub" my_program.py


[pybricksdev]: https://pypi.org/project/pybricksdev

### Common mistakes

Clicking any of the "run" buttons in VS Code (other than the one mentioned in
the EV3 docs) will try to run the program on your computer instead of downloading
and running it on the hub. When you do this, it may appear as nothing happened
or if you didn't install the `pybricks` package, you might get an error that
the `pybricks` package could not be found. Be sure you follow the steps above
to download and run a program.
