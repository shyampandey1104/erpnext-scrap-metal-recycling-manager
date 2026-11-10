# ERPNext Scrap Metal Recycling & Smelting Manager ♻️🏗️

![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)
![ERPNext](https://img.shields.io/badge/ERPNext-v14%20%7C%20v15-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Build](https://img.shields.io/badge/Build-Passing-brightgreen.svg)

An industrial scrap metal procurement, weighbridge automation, and induction furnace smelting yield engine for **ERPNext Manufacturing**. Built for steel rolling mills, copper recycling foundries, and circular economy scrap processors.

---

## 🚀 Key Features

- **Automated Weighbridge Ticket Inwarding**: Computes net tare/gross weight from truck weighbridge slips.
- **Dynamic Quality & Dirt Deductions**: Automatically applies moisture, rust, mud, and non-metallic contamination deductions.
- **Recoverable Smelting Yield Engine**: Estimates furnace melt recovery output percentages for HMS 1/2, Shredded Steel, and Copper Berry.
- **Supplier Payment Clearing**: Direct integration with ERPNext `Purchase Invoice` and `Stock Entry`.

---

## 📦 Installation & Setup

```bash
git clone https://github.com/shyampandey1104/erpnext-scrap-metal-recycling-manager.git
cd erpnext-scrap-metal-recycling-manager
pip install -r requirements.txt
```

---

## 🛠️ Usage Example

```python
from scrap.engine import ScrapRecyclingEngine, WeighbridgeSlip

engine = ScrapRecyclingEngine()

slip = WeighbridgeSlip(
    ticket_no="WB-1021",
    truck_number="MH-12-Q-4001",
    supplier_vendor="Apex Ferrous Recyclers",
    scrap_grade="Heavy Melting Steel (HMS 1/2)",
    gross_weight_kg=32000.0,
    tare_weight_kg=14000.0,
    moisture_rust_deduction_pct=2.0,
    base_rate_per_ton=37500.0
)

receipt = engine.process_weighment_settlement(slip)
print(f"Net: {receipt.net_weight_kg} kg | Payable: ₹{receipt.total_payable_amount}")
```

---

## 🧪 Testing

```bash
pytest tests/
```

---

## 📄 License
MIT License. Created with ❤️ by [Shyam Pandey](https://github.com/shyampandey1104).
