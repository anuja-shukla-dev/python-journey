import asyncio

async def print_numbers():
    for i in range(1,6):
        await asyncio.sleep(1)
        print(i)


asyncio.run(print_numbers())