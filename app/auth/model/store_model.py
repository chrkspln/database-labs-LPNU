from __future__ import annotations
from typing import Dict, Any
from app import db


class Store(db.Model):
    __tablename__ = 'stores'

    store_id = db.Column(db.Integer, primary_key=True)
    store_name = db.Column(db.String(100), nullable=True)
    store_address = db.Column(db.String(255), nullable=True)

    supply = db.relationship("StoreSupply", backref="store")
    price = db.relationship("Price", backref="store")
    store_has_urgency_type = db.relationship("UrgencyType", secondary="deliveries", back_populates="urgency_type_to_store", lazy='dynamic')

    def __repr__(self) -> str:
        return (f"store_id={self.store_id}, "
                f"store_name={self.store_name}, "
                f"store_address={self.store_address})")

    def put_into_dto(self) -> Dict[str, Any]:
        supplies = [supply.put_into_dto() for supply in self.supply]
        prices = [price.put_into_dto() for price in self.price]
        store_has_urgency_types = [urgency_type.put_into_dto() for urgency_type in self.store_has_urgency_type]
        return {
            'store_id': self.store_id,
            'store_name': self.store_name,
            'store_address': self.store_address,
            'supplies': supplies,
            'prices': prices,
            'store_has_urgency_types': store_has_urgency_types
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Store:
        store = Store(
            store_name=dto_dict['store_name'],
            store_address=dto_dict['store_address']
        )
        return store