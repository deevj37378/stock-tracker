import asyncio
import api

async def send_data(to: str):
    print(f"sending data to {to}...")
    await asyncio.sleep(2)
    print(f"data sent to {to}")

async def main():
    data = await api.fetch_data()
    print(data)
##this is synchronous, one step gets executed at once, if we want to send the data to different users at once we need to run the method asyncio.gather() what it does is that it gathers all the data at once and sends it at once not step by step.
    # await send_data("deev")
    await asyncio.gather(send_data("deev"), send_data("mario"))

if __name__ == "__main__": 
    asyncio.run(main())
##asyncio.run() runs the main program