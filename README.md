# Nifty Options Lab (learning only)

A small, offline Python project to learn how options work. It:

- calculates profit and loss for strategies such as an iron condor (`src/strategies.py`),
- estimates rough probabilities from a volatility number you type in (`src/probability.py`),
- checks position size and stop-loss rules (`src/risk.py`).

## What it does NOT do
- No broker connection. It never logs into Axis or any other broker.
- No orders. It never buys or sells anything.
- No recommendations. It doesn't pick trades or tell you what to do.

## Run the tests
```
python3 -m pip install pytest
python3 -m pytest tests -q
```

## Read first
- `docs/GITHUB_FOR_BEGINNERS.md`: how GitHub works, step by step.
- `docs/OPTIONS_GLOSSARY.md`: the words used in options trading.

## Before any real trade
Check your service rules, your broker's risk limits and margin, and use a stop loss on every position.
