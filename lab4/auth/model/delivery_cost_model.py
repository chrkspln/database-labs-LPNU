from __future__ import annotations
from typing import Dict, Any
from lab4 import db


class DeliveryCost(db.Model):
    __tablename__ = 'delivery_costs'

    delivery_cost_id = db.Column(db.Integer, primary_key=True)
    urgency_type_id = db.Column(db.Integer, db.ForeignKey('urgency_types.urgency_type_id'), nullable=True)
    delivery_cost = db.Column(db.Numeric(10, 2), nullable=True)

    def __repr__(self) -> str:
        return (f"delivery_cost_id={self.delivery_cost_id}, "
                f"urgency_type_id={self.urgency_type_id}, "
                f"delivery_cost={self.delivery_cost})")

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'delivery_cost_id': self.delivery_cost_id,
            'urgency_type_id': self.urgency_type_id,
            'delivery_cost': self.delivery_cost
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> DeliveryCost:
        delivery_cost = DeliveryCost(
            urgency_type_id=dto_dict['urgency_type_id'],
            delivery_cost=dto_dict['delivery_cost']
        )
        return delivery_cost