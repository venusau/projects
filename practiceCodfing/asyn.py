import asyncio

async def say_hello(delay, name):
    await asyncio.sleep(delay)
    print(f"Hello, {name}!")

async def main():
    # Create tasks to execute asynchronously
    task1 = asyncio.create_task(say_hello(2, "Alice"))
    task2 = asyncio.create_task(say_hello(1, "Bob"))

    # Wait for all tasks to complete
    await task1
    await task2

# Run the main coroutine
asyncio.run(main())
