from __future__ import annotations
from typing import Dict, Any
from lab4 import db


class Delivery(db.Model):
    __tablename__ = 'deliveries'

    delivery_id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.product_id'))
    store_id = db.Column(db.Integer, db.ForeignKey('stores.store_id'), nullable=True)
    delivery_date = db.Column(db.Date, nullable=True)
    quantity = db.Column(db.Integer, nullable=True)
    urgency_type_id = db.Column(db.Integer, db.ForeignKey('urgency_types.urgency_type_id'), nullable=True)

    def __repr__(self) -> str:
        return (f"delivery_id={self.delivery_id}, "
                f"product_id={self.product_id}, "
                f"store_id={self.store_id}, "
                f"delivery_date={self.delivery_date}, "
                f"quantity={self.quantity}, "
                f"urgency_type_id={self.urgency_type_id})")

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'delivery_id': self.delivery_id,
            'product_id': self.product_id,
            'store_id': self.store_id,
            'delivery_date': self.delivery_date,
            'quantity': self.quantity,
            'urgency_type_id': self.urgency_type_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Delivery:
        delivery = Delivery(
            product_id=dto_dict['product_id'],
            store_id=dto_dict['store_id'],
            delivery_date=dto_dict['delivery_date'],
            quantity=dto_dict['quantity'],
            urgency_type_id=dto_dict['urgency_type_id']
        )
        return delivery