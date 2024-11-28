from __future__ import annotations
from typing import Dict, Any
from app import db


class Supplier(db.Model):
    __tablename__ = 'suppliers'

    supplier_id = db.Column(db.Integer, primary_key=True)
    supplier_name = db.Column(db.String(100), nullable=True)

    store_supply = db.relationship("StoreSupply", backref="supplier")

    def __repr__(self) -> str:
        return (f"supplier_id={self.supplier_id}, "
                f"supplier_name={self.supplier_name})")

    def put_into_dto(self) -> Dict[str, Any]:
        supplies = [supply.put_into_dto() for supply in self.store_supply]
        return {
            'supplier_id': self.supplier_id,
            'supplier_name': self.supplier_name,
            'supplies': supplies
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Supplier:
        supplier = Supplier(
            supplier_name=dto_dict['supplier_name']
        )
        return supplier