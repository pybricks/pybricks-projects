# SPDX-License-Identifier: MIT
# Copyright (c) 2020 Henrik Blidh
# Copyright (c) 2022-2023 The Pybricks Authors

import asyncio
from contextlib import suppress
from bleak import BleakScanner, BleakClient

UART_SERVICE_UUID = "6E400001-B5A3-F393-E0A9-E50E24DCCA9E"
UART_RX_CHAR_UUID = "6E400002-B5A3-F393-E0A9-E50E24DCCA9E"
UART_TX_CHAR_UUID = "6E400003-B5A3-F393-E0A9-E50E24DCCA9E"

# Replace this with the name of your hub if you changed
# it when installing the Pybricks firmware.
HUB_NAME = "Pybricks Hub"


async def main():
    main_task = asyncio.current_task()

    def handle_disconnect(_):
        print("Hub was disconnected.")

        # If the hub disconnects before this program is done,
        # cancel this program so it doesn't get stuck waiting
        # forever.
        if not main_task.done():
            main_task.cancel()

    ready_event = asyncio.Event()

    def handle_rx(_, data: bytearray):
        if data == b"rdy":
            ready_event.set()
        else:
            print("Received:", data)

    # Do a Bluetooth scan to find the hub.
    device = await BleakScanner.find_device_by_name(HUB_NAME)

    if device is None:
        print(f"could not find hub with name: {HUB_NAME}")
        return

    # Connect to the hub.
    async with BleakClient(device, handle_disconnect) as client:

        # Subscribe to notifications from the hub.
        await client.start_notify(UART_TX_CHAR_UUID, handle_rx)

        # Shorthand for sending some data to the hub.
        async def send(data):
            # Wait for hub to say that it is ready to receive data.
            await ready_event.wait()
            # Prepare for the next ready event.
            ready_event.clear()
            # Send the data to the hub.
            await client.write_gatt_char(UART_RX_CHAR_UUID, data)

        # Tell user to start program on the hub.
        print("Start the program on the hub now with the button.")

        # Send a few messages to the hub.
        for i in range(5):
            await send(b"fwd")
            await asyncio.sleep(1)
            await send(b"rev")
            await asyncio.sleep(1)
            print(".", end="", flush=True)

        # Send a message to indicate stop.
        await send(b"bye")

        print("done.")

    # Hub disconnects here when async with block exits.


# Run the main async program.
if __name__ == "__main__":
    with suppress(asyncio.CancelledError):
        asyncio.run(main())
