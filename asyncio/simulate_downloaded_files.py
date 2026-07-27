import asyncio
import random

async def download(file_name):
    delay = random.randint(1,5)
    print(f"Downloading {file_name}")
    await asyncio.sleep(delay)
    print(f"Downloaded {file_name}")

async def main():
    await asyncio.gather(
        download("file 1"),
        download("file 2"),
        download("file 3")
    )

asyncio.run(main())

