"""Small Binance market-data client built on ccxt.

Read-only: it fetches public market data and, when keys are present, the
account balance. It never places orders.
"""
import os

import ccxt
import pandas as pd
from dotenv import load_dotenv

load_dotenv()


def public_client() -> ccxt.binance:
    return ccxt.binance({"enableRateLimit": True})


def private_client() -> ccxt.binance:
    key = os.getenv("BINANCE_API_KEY")
    secret = os.getenv("BINANCE_API_SECRET")
    if not key or not secret:
        raise RuntimeError("Set BINANCE_API_KEY and BINANCE_API_SECRET in .env")
    return ccxt.binance({"apiKey": key, "secret": secret, "enableRateLimit": True})


def fetch_ohlcv(symbol: str = "BTC/USDT", timeframe: str = "1h", limit: int = 200) -> pd.DataFrame:
    rows = public_client().fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)
    frame = pd.DataFrame(rows, columns=["timestamp", "open", "high", "low", "close", "volume"])
    frame["timestamp"] = pd.to_datetime(frame["timestamp"], unit="ms")
    return frame


def fetch_balance() -> dict:
    return private_client().fetch_balance()


def summarize(frame: pd.DataFrame) -> dict:
    return {
        "rows": len(frame),
        "first_close": float(frame["close"].iloc[0]),
        "last_close": float(frame["close"].iloc[-1]),
        "change_pct": float((frame["close"].iloc[-1] / frame["close"].iloc[0] - 1) * 100),
        "high": float(frame["high"].max()),
        "low": float(frame["low"].min()),
    }
