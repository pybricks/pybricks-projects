#!/usr/bin/env python3
from os import scandir
from json import dump

# Get list of folder names
names = [f.name for f in scandir('.') if f.is_dir()]

# Make the workspace dictionary
workspace = {
    "folders": [
        {
            "path": name
        }
        for name in names
    ],
    "settings": {
        "debug.openDebug": "neverOpen"
    }
}

# Save workspace
with open('snippets_ev3.code-workspace', 'w') as f:
    dump(workspace, f, indent=4)
