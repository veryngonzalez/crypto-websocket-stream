import asyncio
import json
import websockets

STREAM_URL = "wss://stream.binance.com:9443/ws/btcusdt@trade"

async def handle_trade(data):
    trade = json.loads(data)

    side = "BUY" if trade["m"] else "SELL"

    print(
        f"[{trade['E']}] "
        f"Price: {trade['p']} "
        f"Qty: {trade['q']} "
        f"Side: {side}"
    )

async def listen():
    while True:
        try:
            async with websockets.connect(STREAM_URL) as ws:
                print(f"Connected to {STREAM_URL}")

                async for message in ws:
                    await handle_trade(message)

        except websockets.ConnectionClosed as e:
            print(
                f"WebSocket closed "
                f"(code {e.code}): {e.reason}"
            )

        except asyncio.TimeoutError:
            print("Connection timed out")

        except Exception as e:
            print(f"Unexpected error: {e}")

        print("Reconnecting in 5 seconds...")
        await asyncio.sleep(5)

if __name__ == "__main__":
    asyncio.run(listen())
