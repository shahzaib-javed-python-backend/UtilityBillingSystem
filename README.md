# ⚡ Enterprise-Grade Utility Billing System

A high-performance Python CLI backend application engineered with Object-Oriented Programming (OOP) principles and structured SQLite data storage. This application automates multiple tiers of billing matrix algorithms including residential, commercial taxation grids, and solar grid net-metering protocols.

## 🛠️ Key Architectural Patterns & Features

*   **Object-Oriented Programming (OOP):** Deep implementations of structural abstraction, robust Class Inheritance, and execution of Method Overriding to process distinct billing structures.
*   **Dynamic super() Integration:** Used to forward parameters securely from derived subclasses to the foundational base initialization blocks without data dilution.
*   **Relational Database Engine:** Replaced linear flat file architecture with structured **SQLite3** relational pipelines to track rows and maintain permanent data logs.
*   **Algorithmic Net-Metering:** Embedded complex mathematical boundaries to handle threshold constraints (e.g., ensuring bills terminate smoothly at Rs. 0 when solar generation exceeds net household load).
*   **Input Guard & Exception Interception:** Configured explicit `try-except` execution layers to catch illegal biometric inputs or negative data footprints before database runtime operations.

## 🗂️ Relational Database Schema Mapping

```text
📁 UtilityBillingSystem/
 ├── 📄 billing_engine.py       # core python application runtime engine
 └── 📄 billing_system.db       # dynamic sqlite relational database schema
```

### SQL Relational Matrix Schema:
*   `id` (INTEGER, Primary Key)
*   `bill_type` (TEXT)
*   `consumer_name` (TEXT)
*   `units_consumed` (INTEGER)
*   `solar_exported` (INTEGER)
*   `total_bill` (REAL)

## 🚀 Deployment & Local Execution Instructions

1. Clone or download this project directory onto your environment.
2. Initialize the backend binary pipeline via terminal execution:
   ```bash
   python billing_engine.py
   ```
3. Engage with the interactive numeric data portal to calculate residential loads, track peak-hour commercial tariffs, or review historical relational SQL arrays directly from the interface.
