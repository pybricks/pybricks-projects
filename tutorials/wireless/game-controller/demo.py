# SPDX-License-Identifier: MIT
# Copyright (c) 2020 Henrik Blidh
# Copyright (c) 2022-2023 The Pybricks Authors

"""
Example program for computer-to-hub communication.

Requires Pybricks firmware >= 3.3.0.
"""

import asyncio
from contextlib import suppress
from bleak import BleakScanner, BleakClient
import time
import sys

PYBRICKS_COMMAND_EVENT_CHAR_UUID = "c5f50002-8280-46da-89f4-6d8051e4aeef"

# Replace this with the name of your hub if you changed
# it when installing the Pybricks firmware.
HUB_NAME = sys.argv[1] if len(sys.argv) > 1 else "Pybricks Hub"

event_condition = asyncio.Condition()
lastevent = {}
async def gameplay():
    global lastevent
    from evdev import InputDevice, categorize, ecodes, list_devices

    while True:
        devices = list_devices()
        if len(devices):
            break
        await asyncio.sleep(1)
        
    print(devices)
    gamepad = InputDevice(devices[0])
    
    print(gamepad)
    async for event in gamepad.async_read_loop():
        if event.code != 0 or event.type != 0 or event.value != 0:
            async with event_condition:
                lastevent[(event.code, event.type)] = event.value
                #print('raw', event.code, event.type, event.value)
                event_condition.notify()                

        
async def send_task():
    print("Connecting...")
    main_task = asyncio.current_task()

    def handle_disconnect(_):
        print("Hub was disconnected.")

        # If the hub disconnects before this program is done,
        # cancel this program so it doesn't get stuck waiting
        # forever.
        if not main_task.done():
            main_task.cancel()

    def handle_rx(sender, data: bytearray):
        if data[0] == 0x01:  # "write stdout" event (0x01)            
            payload = data[1:]
            print("Received: ", payload)

    def detection_info(a1, a2):
        print("Detected: ", a1, a2)
        
    # Do a Bluetooth scan to find the hub.
    device = await BleakScanner.find_device_by_name(HUB_NAME, detection_callback=detection_info, timeout=5)

    if device is None:
        print(f"could not find hub with name: {HUB_NAME}")
        return
    
    # Connect to the hub.
    async with BleakClient(device, handle_disconnect) as client:
        print(f"Address {client.address}")
        
        # Subscribe to notifications from the hub.
        await client.start_notify(PYBRICKS_COMMAND_EVENT_CHAR_UUID, handle_rx)

        # Shorthand for sending some data to the hub.
        async def send(data):
            before = time.time()
            await client.write_gatt_char(
                PYBRICKS_COMMAND_EVENT_CHAR_UUID,
                b"\x06" + data,  # prepend "write stdin" command (0x06)
                response = True
            )
            #print(f"{(time.time() - before) * 1000}ms elapsed")
            
        # Tell user to start program on the hub.
        print("Start the program on the hub now with the button.")
        
        global lastevent

        while True:
            local = None

            # BLE works in connection windows; so if we try to send and
            # wait for the response right at the start of the window that
            # effectively adds latency between inputs. 28ms is a heuristic
            # based on a 30ms timing window
            await asyncio.sleep(.028)
            
            async with event_condition:
                while len(lastevent) == 0:
                    await event_condition.wait()
                local = lastevent.copy()
                lastevent = {}

            if local is not None:
                lst = []

                for key in local:
                    value = local[key]
                    print(key, value)
                    lst = lst + [key[0], key[1], value]
                    if len(lst) >= 18:
                        await send(bytearray(lst))
                if len(lst) > 0:
                    await send(bytearray(lst))
                    

        print("done.")

    # Hub disconnects here when async with block exits.

async def main():
    gameplay_task = asyncio.create_task(gameplay())
    await send_task()
    gameplay_task.cancel()

# Run the main async program.
if __name__ == "__main__":
    with suppress(asyncio.CancelledError):
        asyncio.run(main())

