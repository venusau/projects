import asyncio

async def greet(name):
    await asyncio.sleep(1)
    print(f"Hello, {name}!")

async def main():
    await greet("Alice")
    await greet("Bob")

asyncio.run(main())
