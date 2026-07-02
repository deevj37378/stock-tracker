import yfinance as yf
import asyncio
import time

def fetch_price(symbol):
    price = yf.Ticker(symbol).fast_info['last_price']
    return f"{symbol}: ₹{price:.2f}"

async def main():
    symbols = ["RELIANCE.NS", "ADANIPORTS.NS", "COFORGE.NS", "ITC.NS", "ADANIENSOL.NS"]
    
    # Async concurrent fetch
    start = time.time()
    results = await asyncio.gather(
        *[asyncio.to_thread(fetch_price, symbol) for symbol in symbols]
    )
    async_time = time.time() - start
    
    print("\n--- Current Stock Prices ---")
    for result in results:
        print(result)
    print(f"\nAsync time: {async_time:.2f}s")

    # Sync fetch for comparison
    start = time.time()
    for symbol in symbols:
        fetch_price(symbol)
    sync_time = time.time() - start
    
    print(f"Sync time: {sync_time:.2f}s")
    print(f"\nAsync was {sync_time/async_time:.1f}x faster")

if __name__ == "__main__":
    asyncio.run(main())