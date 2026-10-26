import asyncio
import time

import httpx


async def fetch_delay(client: httpx.AsyncClient, seconds: int) -> int:
    resp = await client.get(f"http://localhost:8080/delay/{seconds}")
    resp.raise_for_status()
    data = resp.json()
    return resp.status_code


async def main() -> None:
    started = time.perf_counter()
    async with httpx.AsyncClient() as client:
        a, b, c = await asyncio.gather(
            fetch_delay(client, 1), fetch_delay(client, 2), fetch_delay(client, 1)
        )
    elapsed = time.perf_counter() - started
    print(f"results: {a} {b} {c} in {elapsed:.1f}s")


asyncio.run(main())
