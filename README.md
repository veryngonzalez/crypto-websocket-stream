# Crypto WebSocket Stream

Streams live BTCUSDT trades from Binance WebSocket and prints them in real time.

## Features
- Asynchronous WebSocket connection using `websockets`
- Auto-reconnect with explicit error handling
- Lightweight terminal-based trade stream output

## Usage
1. Install requirements: `pip install -r requirements.txt`
2. Run: `python ws_stream.py`
3. Watch live BTCUSDT trades in real time.

## Entry point
The script uses `if __name__ == "__main__"` to start the async event loop only when executed directly.

## Example Output
```

Connected to wss://stream.binance.com:9443/ws/btcusdt@trade
[1680000000123] Price: 27000.01 Qty: 0.005 Side: BUY
[1680000000456] Price: 27000.05 Qty: 0.120 Side: SELL

```


### Terminal screenshot
<!-- Add your own screenshot or GIF here -->
![WebSocket stream output](screenshots/ws_stream.png)

## Why this matters
- Demonstrates real-time data streaming
- Shows basic async programming with `asyncio`
- Demonstrates reconnect handling for unstable connections

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
