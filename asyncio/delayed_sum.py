import asyncio

async def add(a,b):
    await asyncio.sleep(2)
    return a+b

async def main():
    L = await asyncio.gather(
        add(4,2)
    )
    print(L)

asyncio.run(main())