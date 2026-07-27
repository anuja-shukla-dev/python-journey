import asyncio 



async def factorial(num):
    if num == 0:
        return 1
    
    await asyncio.sleep(1)
    return num * (await factorial(num-1))

async def main():
    num1, num2, num3 = await asyncio.gather(
        factorial(5),
        factorial(4),
        factorial(6),
    )
    print(f"Factorial of 5: {num1}")
    print(f"Factorial of 4: {num2}")
    print(f"Factorial of 6: {num3}")

asyncio.run(main())