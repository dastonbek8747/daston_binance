"""Tests that do not touch the network."""
import pandas as pd

from binance_client import summarize


def test_summarize_computes_change():
    frame = pd.DataFrame({
        "timestamp": pd.to_datetime(["2026-01-01", "2026-01-02"]),
        "open": [100.0, 105.0],
        "high": [110.0, 120.0],
        "low": [90.0, 100.0],
        "close": [100.0, 110.0],
        "volume": [1.0, 2.0],
    })
    stats = summarize(frame)
    assert stats["rows"] == 2
    assert stats["last_close"] == 110.0
    assert round(stats["change_pct"], 2) == 10.0
    assert stats["high"] == 120.0
    assert stats["low"] == 90.0
