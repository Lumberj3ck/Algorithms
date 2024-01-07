import asyncio


async def counter(delay: int):
    print("One")
    await time.sleep(delay)
    print("Two")


async def main():
    await asyncio.gather(counter(2), counter(1), counter(1))


if __name__ == "__main__":
    import time

    start = time.perf_counter()
    start_time = time.time()
    asyncio.run(main())
    elapsed = time.perf_counter() - start
    elapsed_time = time.time() - start_time
    print(elapsed, elapsed_time)
