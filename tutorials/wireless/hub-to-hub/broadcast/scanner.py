import asyncio
import struct
import binascii
from bleak import BleakScanner

LINE_UP = '\033[1A'


def toHex(data):
    if data:
        return ''.join('{:02x}'.format(x) for x in data)
    return ''


def extractTopic(data, topics):
    hash = int.from_bytes(data[1:5], "little", signed=False)
    for t in topics:
        if binascii.crc32(bytes(t, "utf-8")) == hash:
            return t
    return toHex(data[1:5])


def extractTuples(data):
    n = data[5]
    if n > 8 or n < 0:
        return tuple()
    typesBits = int.from_bytes(data[6:8], "little", signed=False)
    values = []
    index = 8
    is_single_object = False
    if n == 0:  # single object
        is_single_object = True
        n = 1
    for _ in range(n):
        type = typesBits & 0x03
        typesBits = typesBits >> 2
        if type == 0:
            size = 0
            for c in data[index:]:
                if c == 0:
                    break
                size += 1
            str = data[index:index + size].decode("utf-8")
            values.append(str)
            index += size + 1
        elif type == 1:
            values.append(int.from_bytes(
                data[index:index + 2], "little", signed=True))
            index += 2
        elif type == 2:
            values.append(int.from_bytes(
                data[index:index + 4], "little", signed=True))
            index += 4
        elif type == 3:
            values.append(struct.unpack(
                "f", data[index:index + 4])[0])
            index += 4
        else:
            break
    if (is_single_object):
        return values[0]
    return tuple(values)


def dump(devices, topics=[], compact=True):
    for d in devices.values():
        data = d.manufacturer_data[0x397]
        topic = extractTopic(data, topics)
        print(d.local_name, toHex(data), topic,
              extractTuples(data), '          ')
    # Move cursor up in compact mode
    if compact:
        for d in devices:
            print(LINE_UP, end='')


async def main(topics=[], compact=True):
    stop_event = asyncio.Event()
    hubs = {}
    print("LEGO devices:")

    def callback(device, advertising_data):
        if (advertising_data.manufacturer_data and
                0x0397 in advertising_data.manufacturer_data):
            hubs[device.address] = advertising_data
            dump(hubs, topics, compact)

    async with BleakScanner(callback) as scanner:
        await stop_event.wait()

asyncio.run(main(["tilt", "distance"]))
