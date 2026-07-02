import asyncio

async def fetch_data() -> str:
    print("fetching data")
    await asyncio.sleep(2)
    print("data fetched")

    return "API data"