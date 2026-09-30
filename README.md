# UtilityBillingSystem

A Python command-line utility billing application that uses:

- **Object-Oriented Programming (OOP)** for bill types
- **SQLite (`sqlite3`)** for invoice storage

All details below are verified from repository files, primarily `billing_engine.py`.

## Repository Contents

- `/home/runner/work/UtilityBillingSystem/UtilityBillingSystem/billing_engine.py` – main CLI application
- `/home/runner/work/UtilityBillingSystem/UtilityBillingSystem/billing_system.db` – SQLite database file used by the app
- `/home/runner/work/UtilityBillingSystem/UtilityBillingSystem/invoices_log.txt` – text file present in repo (not used by current runtime code)

## How It Works (Python + OOP)

`billing_engine.py` defines three classes:

1. `UtilityBill`
   - Base class
   - Validates `units_consumed >= 0`
   - Rate is `25` per unit
   - `calculate_bill()` = `units_consumed * 25`

2. `CommercialBill(UtilityBill)`
   - Inherits from `UtilityBill`
   - Overrides `calculate_bill()` to add **20%** on top of standard amount

3. `SmartMeterBill(UtilityBill)`
   - Inherits from `UtilityBill`
   - Validates `solar_exported >= 0`
   - Net units = `units_consumed - solar_exported`
   - If net units are negative, they are clamped to `0`
   - Bill = `net_units * 25`

## SQLite Storage Details

On startup, the app runs `init_db()` and ensures this table exists:

- `invoices`
  - `id INTEGER PRIMARY KEY AUTOINCREMENT`
  - `bill_type TEXT`
  - `consumer_name TEXT`
  - `units_consumed INTEGER`
  - `solar_exported INTEGER`
  - `total_bill REAL`

When a bill is generated, it is inserted into `invoices` using parameterized SQL placeholders (`VALUES (?, ?, ?, ?, ?)`).

## CLI Behavior

Run loop (`main_menu`) shows these options:

1. Generate Standard Home Bill
2. Generate Commercial Shop Bill
3. Generate Smart/Solar Grid Bill
4. View All Saved Invoices (reads from SQLite)
5. Exit System

Input handling:

- Converts numeric inputs with `int(...)`
- Catches `ValueError` and prints an input error message
- Rejects invalid menu choices outside `1-5`

## Setup and Run

From repository root:

```bash
python billing_engine.py
```

Notes:

- The script uses Python's standard-library `sqlite3`; no external dependency file is present.
- If `billing_system.db` does not exist, SQLite will create it when the script runs.

## Testing Status

- No automated test suite or test files are present in this repository.
- No lint/build/test configuration files (such as `pyproject.toml`, `requirements.txt`, or `setup.py`) are present.

## Verified vs Unverified

### Verified

- OOP class structure and billing logic (`billing_engine.py`)
- SQLite table creation and insert/read workflow (`billing_engine.py`)
- Interactive CLI menu and input flow (`billing_engine.py`)

### Unverified / Not Present in Repository

- Deployment/infrastructure setup
- API/server endpoints
- Container configuration
- CI workflows
- Screenshots or UI assets
