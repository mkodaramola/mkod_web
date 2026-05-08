import asyncio
from bleak import BleakScanner, BleakClient

DEVICE_NAME = "Nano33_AirMouse"

async def main():
    print("Scanning for BLE device...")
    devices = await BleakScanner.discover()

    target = None
    for d in devices:
        if d.name == DEVICE_NAME:
            target = d
            break

    if not target:
        print("Device not found")
        return

    print(f"Connecting to {target.address}")

    async with BleakClient(target.address) as client:
        print("Connected")
        print("This device is HID-based.")
        print("Mouse movement handled by OS.")
        print("Python script running for monitoring only.")

        while True:
            await asyncio.sleep(1)

asyncio.run(main())
