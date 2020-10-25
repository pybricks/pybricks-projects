#!/usr/bin/env python3
"""Replaces all instances of ExampleHub in template with actual hub names.

Optionally skips examples that do not work on a platform.
"""
import os

# Which instance to replace
EXAMPLE_HUB = 'ExampleHub'

# Define which hubs to run
HUBS = ['MoveHub', 'CityHub', 'TechnicHub', 'PrimeHub', 'InventorHub']

# This flag indicates to skip next X lines in a script
SKIP_FLAG = 'SKIP_NEXT'
skip_remaining = 0

# Get list of scripts to be parsed
script_names = [f for f in os.listdir('.') if f != 'make_shared_examples.py']

for hub in HUBS:
    # Determine path to the hub
    hub_path = os.path.join('..', 'hub_' + hub.lower())
    os.makedirs(hub_path, exist_ok=True)

    # Go through all template scripts
    for script in (open(f, 'r') for f in script_names):

        # Open destination script:
        with open(os.path.join(hub_path, script.name), 'w') as dest_file:

            # Read script line by line
            for line in script.readlines():

                # Replace hub name if present
                line = line.replace(EXAMPLE_HUB, hub)

                # If there is a skip flag, parse it
                if skip_remaining == 0 and SKIP_FLAG in line:
                    idx = line.find(SKIP_FLAG)

                    # Get hub name and how many lines to skip
                    _, skip_hub, _, skip_len = line.split()

                    # Skip lines if needed, and always skip the flag itself
                    if hub.lower() == skip_hub.lower():
                        skip_remaining = int(skip_len) + 1
                    else:
                        skip_remaining = 1

                # If there are some lines left to skip, do so
                if skip_remaining > 0:
                    skip_remaining -= 1
                # Otherwise print the line
                else:
                    dest_file.writelines(line)
