from __future__ import annotations
from typing import Dict, Any
from lab4 import db


class UrgencyType(db.Model):
    __tablename__ = 'urgency_types'

    urgency_type_id = db.Column(db.Integer, primary_key=True)
    urgency_description = db.Column(db.String(50), nullable=True)

    delivery = db.relationship("Delivery", backref="urgency_type")
    delivery_cost = db.relationship("DeliveryCost", backref="urgency_type")

    def __repr__(self) -> str:
        return (f"urgency_type_id={self.urgency_type_id}, "
                f"urgency_description={self.urgency_description})")

    def put_into_dto(self) -> Dict[str, Any]:
        deliveries = [delivery.put_into_dto() for delivery in self.delivery]
        costs = [cost.put_into_dto() for cost in self.delivery_cost]
        return {
            'urgency_type_id': self.urgency_type_id,
            'urgency_description': self.urgency_description,
            'deliveries': deliveries,
            'costs': costs
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> UrgencyType:
        urgency_type = UrgencyType(
            urgency_description=dto_dict['urgency_description']
        )
        return urgency_type