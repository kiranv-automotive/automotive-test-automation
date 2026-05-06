# Automotive Test Automation Framework

Python-based test automation tools for automotive validation —
CAN bus, UDS diagnostics, and ECU test log analysis.

## Tools used
- Python 3.12
- pytest
- python-can
- cantools

## Scripts
| Script | Description |
|--------|-------------|
| `test_log_analyzer.py` | Parses CSV test logs, prints PASS/FAIL summary |

## Domain coverage
eCall, bCall, UDS diagnostics, CAN signal validation,
RES/RVI/RCC, Android Auto, VDC, Telematics

## How to run
```bash
python test_log_analyzer.py
```

## Author
Kiran V — Automotive Test Automation Engineer  
7+ years | Visteon | TCS | JLR | Mitsubishi Motors