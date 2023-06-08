import asyncio

from bleak import BleakScanner as bs

async def main():
    devices = await bs.discover(timeout=10.0)
    for d in devices:
        print(d)


if __name__ == "__main__":
    asyncio.run(main())