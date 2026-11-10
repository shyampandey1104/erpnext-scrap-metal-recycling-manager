"""Scrap Metal Weighbridge Tare/Gross Weighment & Chemical Purity Deduction Engine."""

from typing import Dict, Any, List, Optional
from pydantic import BaseModel, Field


class WeighbridgeSlip(BaseModel):
    ticket_no: str
    truck_number: str
    supplier_vendor: str
    scrap_grade: str  # Heavy Melting Steel (HMS 1/2), Shredded Steel, Copper Berry, Aluminum Cast
    gross_weight_kg: float
    tare_weight_kg: float
    moisture_rust_deduction_pct: float = 2.0  # standard deduction for non-metallic impurities
    base_rate_per_ton: float


class ScrapSettlementReceipt(BaseModel):
    ticket_no: str
    supplier_vendor: str
    net_weight_kg: float
    deduction_weight_kg: float
    payable_weight_metric_tons: float
    rate_per_ton: float
    total_payable_amount: float
    melt_yield_efficiency_pct: float


class ScrapRecyclingEngine:
    """Manages yard weighbridge ticketing, purity deductions, and furnace smelting yield."""

    STANDARD_MELT_YIELDS = {
        "Heavy Melting Steel (HMS 1/2)": 88.0,  # 88% recoverable molten steel
        "Shredded Steel": 92.0,
        "Copper Berry": 98.5,
        "Aluminum Cast": 84.0,
        "Brass Honey": 90.0
    }

    def process_weighment_settlement(self, slip: WeighbridgeSlip) -> ScrapSettlementReceipt:
        if slip.gross_weight_kg <= slip.tare_weight_kg:
            raise ValueError("Gross weight must be greater than tare weight.")

        net_weight_kg = slip.gross_weight_kg - slip.tare_weight_kg
        deduction_kg = net_weight_kg * (slip.moisture_rust_deduction_pct / 100.0)
        payable_weight_kg = net_weight_kg - deduction_kg

        # Convert to metric tons (1 MT = 1000 kg)
        payable_tons = round(payable_weight_kg / 1000.0, 3)
        total_payout = round(payable_tons * slip.base_rate_per_ton, 2)

        yield_pct = self.STANDARD_MELT_YIELDS.get(slip.scrap_grade, 85.0)

        return ScrapSettlementReceipt(
            ticket_no=slip.ticket_no,
            supplier_vendor=slip.supplier_vendor,
            net_weight_kg=round(net_weight_kg, 1),
            deduction_weight_kg=round(deduction_kg, 1),
            payable_weight_metric_tons=payable_tons,
            rate_per_ton=slip.base_rate_per_ton,
            total_payable_amount=total_payout,
            melt_yield_efficiency_pct=yield_pct
        )
