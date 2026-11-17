# Binance Market Data (ccxt)

> A small read-only client for Binance public market data, plus a summary command.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

## Features

- Fetch OHLCV candles for any symbol.
- Summary of change, high and low.
- Optional account balance when API keys are set.
- Read-only: it never places orders.

## Tech Stack

| Layer | Technology |
|---|---|
| Exchange | ccxt (Binance) |
| Data | pandas |
| Config | python-dotenv |

## Quick Start

```bash
git clone https://github.com/dastonbek8747/daston_binance.git
cd daston_binance
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python main.py BTC/USDT
```

## Environment variables

Only needed for the private balance call.

| Variable | Meaning |
|---|---|
| `BINANCE_API_KEY` | Binance API key (read-only). |
| `BINANCE_API_SECRET` | Binance API secret. |

## Tests

```bash
pip install pytest
pytest -q
```

## Disclaimer

Educational project. Not financial advice. Use a read-only API key.

## License

MIT © 2026 Doston Sultonov.
