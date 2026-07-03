import asyncio
import aiohttp

websites = [
    "https://www.google.com",
    "https://www.github.com",
    "https://www.python.org",
    "https://www.wikipedia.org",
    "https://www.thiswebsitedoesnotexist123456.com"  # Invalid
]

async def main():
    async with aiohttp.ClientSession() as session:
        check_websites = (check(session, website) for website in websites)
        await asyncio.gather(*check_websites)


async def check(session, website):
    try:
        async with session.get(website) as response:
            print(f"{website} -> {response.status}")
        
    except Exception as e:
        print(f"{website} -> failed {e}")

if __name__ == "__main__":
    asyncio.run(main())