## Latency Arbitrage Signal Processing with NBBO

This repository contains a data processing pipeline designed to identify latency arbitrage opportunities in NBBO (National Best Bid and Offer) quote data across exchanges. The current implementation parses raw quote streams, applies market hours and action filters, reshapes bid/ask data, and detects cross-exchange mispricings under latency and transaction cost constraints.

### Next Steps
* Implemented: Arbitrage signal detection
* Coming up: PnL generation using these signals
* Trade simulation logic
* lippage modeling
* Realized vs. theoretical PnL comparison

### File Structure
```
latency_arb/
   │
   ├── code
   │    ├─ signal_processing.py     # Core signal detection logic
   │    ├─ signal_per_strke.py      # Understanding signal distribution 
   │    ├─ strat_execution.py       # Core execution logic
   │    ├─ backtesting.py           # Planned
   │    ├─ util.py                  # Utility funcs
   │    ├─ settings.py              # Settings
   ├── data-sample                  # Snapshot of data structure algoseek
```
