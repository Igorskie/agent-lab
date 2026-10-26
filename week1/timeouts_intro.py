import asyncio
import time

import httpx


async def fetch_delay(client: httpx.AsyncClient, seconds: int) -> int:
    resp = await client.get(f"http://localhost:8080/delay/{seconds}")
    resp.raise_for_status()
    return resp.status_code


async def main() -> None:
    started = time.perf_counter()
    results = []
    try:
        async with asyncio.timeout(3):
            async with httpx.AsyncClient() as client:
                results = await asyncio.gather(
                    fetch_delay(client, 1),
                    fetch_delay(client, 8),
                    fetch_delay(client, 1),
                    return_exceptions=True,
                )
    except TimeoutError:
        print("Gave up: total budget exceeded")

    for r in results:
        if isinstance(r, Exception):
            print(f"Error: {type(r).__name__}: {r}")
        else:
            print(f"Success: {r}")

    elapsed = time.perf_counter() - started
    print(f"total elapsed time: {elapsed:.1f}s")


asyncio.run(main())
