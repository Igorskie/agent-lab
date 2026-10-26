import asyncio

import httpx


async def fetch_status(client: httpx.AsyncClient, code: int) -> int:
    resp = await client.get(f"http://localhost:8080/status/{code}")
    resp.raise_for_status()
    return resp.status_code


async def main() -> None:
    async with httpx.AsyncClient() as client:
        results = await asyncio.gather(
            fetch_status(client, 200),
            fetch_status(client, 500),
            fetch_status(client, 200),
            return_exceptions=True,
        )

    for r in results:
        if isinstance(r, Exception):
            print(f"Error: {r}")
        else:
            print(f"Success: {r}")


asyncio.run(main())
