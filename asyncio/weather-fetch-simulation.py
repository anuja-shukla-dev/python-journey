import asyncio

async def get_temperature():
    await asyncio.sleep(2)
    return 32

async def get_humidity():
    await asyncio.sleep(1)
    return 68

async def get_wind_speed():
    await asyncio.sleep(3)
    return 15

async def main():
    temp, humidity, wind = await asyncio.gather(
    get_temperature(),
    get_humidity(),
    get_wind_speed()
)
    print(f"Temperature: {temp}°C")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind} km/h")


asyncio.run(main())