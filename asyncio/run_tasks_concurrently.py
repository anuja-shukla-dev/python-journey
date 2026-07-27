import asyncio

async def task1():
    for i in range(3):
        await asyncio.sleep(1)
        print("Task 1")

async def task2():
    for i in range(2):
        await asyncio.sleep(2)
        print("Task 2")

async def main():
    await asyncio.gather(
        task1(),
        task2()
    )

asyncio.run(main())