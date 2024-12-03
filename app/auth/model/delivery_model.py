from __future__ import annotations
from typing import Dict, Any

from sqlalchemy import select

from app import db
from .urgency_type_model import UrgencyType
from .store_model import Store


class Delivery(db.Model):
    __tablename__ = 'deliveries'

    delivery_id = db.Column(db.Integer, primary_key=True)
    store_id = db.Column(db.Integer, db.ForeignKey('stores.store_id'))
    urgency_type_id = db.Column(db.Integer, db.ForeignKey('urgency_types.urgency_type_id'))
    delivery_date = db.Column(db.Date, nullable=True)
    quantity = db.Column(db.Integer, nullable=True)

    def __repr__(self) -> str:
        return (f"delivery_id={self.delivery_id}, "
                f"store_id={self.store_id}, "
                f"delivery_date={self.delivery_date}, "
                f"quantity={self.quantity}, "
                f"urgency_type_id={self.urgency_type_id})")

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'delivery_id': self.delivery_id,
            'store_id': self.store_id,
            'delivery_date': self.delivery_date,
            'quantity': self.quantity,
            'urgency_type_id': self.urgency_type_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Delivery:
        delivery = Delivery(
            store_id=dto_dict['store_id'],
            delivery_date=dto_dict['delivery_date'],
            quantity=dto_dict['quantity'],
            urgency_type_id=dto_dict['urgency_type_id']
        )
        return delivery

    @staticmethod
    def add_link(store_name: str, urgency_type_name: str) -> Delivery:
        store = Store.query.filter_by(store_name=store_name).first()
        urgency_type = UrgencyType.query.filter_by(urgency_description=urgency_type_name).first()
        if store is None:
            raise ValueError(f"Store {store_name} not found")
        if urgency_type is None:
            raise ValueError(f"Urgency type {urgency_type_name} not found")

        delivery = Delivery(store_id=store.store_id, urgency_type_id=urgency_type.urgency_type_id)
        db.session.add(delivery)
        db.session.commit()
        return delivery