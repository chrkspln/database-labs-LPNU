from __future__ import annotations
from typing import Dict, Any
from lab4 import db


class StoreSupply(db.Model):
    __tablename__ = 'store_supplies'

    supply_id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.product_id'), nullable=True)
    store_id = db.Column(db.Integer, db.ForeignKey('stores.store_id'), nullable=True)
    supplier_id = db.Column(db.Integer, db.ForeignKey('suppliers.supplier_id'), nullable=True)
    supply_date = db.Column(db.Date, nullable=True)

    def __repr__(self) -> str:
        return (f"supply_id={self.supply_id}, "
                f"product_id={self.product_id}, "
                f"store_id={self.store_id}, "
                f"supplier_id={self.supplier_id}, "
                f"supply_date={self.supply_date})")

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'supply_id': self.supply_id,
            'product_id': self.product_id,
            'store_id': self.store_id,
            'supplier_id': self.supplier_id,
            'supply_date': self.supply_date
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> StoreSupply:
        store_supply = StoreSupply(
            product_id=dto_dict['product_id'],
            store_id=dto_dict['store_id'],
            supplier_id=dto_dict['supplier_id'],
            supply_date=dto_dict['supply_date']
        )
        return store_supply