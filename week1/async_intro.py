import asyncio
import time


async def fake_api_call(name: str, seconds: float) -> str:
    print(f"start {name}")
    await asyncio.sleep(seconds)  # stands in for waiting on a network response
    print(f"done  {name}")
    return name


async def main() -> None:
    started = time.perf_counter()
    a, b = await asyncio.gather(fake_api_call("A", 2), fake_api_call("B", 1))
    elapsed = time.perf_counter() - started
    print(f"results: {a}, {b} in {elapsed:.1f}s")


asyncio.run(main())
