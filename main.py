"""Print a short market summary for a symbol from Binance."""
import sys

from binance_client import fetch_ohlcv, summarize


def main(argv: list[str]) -> int:
    symbol = argv[1] if len(argv) > 1 else "BTC/USDT"
    frame = fetch_ohlcv(symbol)
    stats = summarize(frame)
    print(f"{symbol} ({stats['rows']} candles)")
    print(f"  last close : {stats['last_close']:.2f}")
    print(f"  change     : {stats['change_pct']:+.2f}%")
    print(f"  high / low : {stats['high']:.2f} / {stats['low']:.2f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
