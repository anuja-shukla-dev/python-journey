import asyncio

async def countdown():
    for i in range(10,0,-1):
        await asyncio.sleep(1)
        print(i)

asyncio.run(countdown())