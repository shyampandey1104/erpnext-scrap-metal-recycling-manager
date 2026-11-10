import unittest
from scrap.engine import ScrapRecyclingEngine, WeighbridgeSlip


class TestScrapRecyclingEngine(unittest.TestCase):
    def setUp(self):
        self.engine = ScrapRecyclingEngine()

    def test_weighment_settlement(self):
        slip = WeighbridgeSlip(
            ticket_no="WB-2026-9011",
            truck_number="MH-04-GP-3312",
            supplier_vendor="Modern Metal Traders",
            scrap_grade="Heavy Melting Steel (HMS 1/2)",
            gross_weight_kg=28500.0,
            tare_weight_kg=12500.0,  # Net = 16,000 kg
            moisture_rust_deduction_pct=2.5,  # 400 kg deduction -> 15,600 kg = 15.6 Tons
            base_rate_per_ton=38000.0
        )
        receipt = self.engine.process_weighment_settlement(slip)
        self.assertEqual(receipt.net_weight_kg, 16000.0)
        self.assertEqual(receipt.deduction_weight_kg, 400.0)
        self.assertEqual(receipt.payable_weight_metric_tons, 15.6)
        self.assertEqual(receipt.total_payable_amount, 592800.0)
        self.assertEqual(receipt.melt_yield_efficiency_pct, 88.0)


if __name__ == "__main__":
    unittest.main()
