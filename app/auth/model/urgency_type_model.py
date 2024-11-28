from __future__ import annotations
from typing import Dict, Any
from app import db


class UrgencyType(db.Model):
    __tablename__ = 'urgency_types'

    urgency_type_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    urgency_description = db.Column(db.String(50), nullable=True)

    delivery_cost = db.relationship("DeliveryCost", backref="urgency_type")
    urgency_type_to_store = db.relationship("Store", secondary="deliveries", back_populates="store_has_urgency_type", lazy='dynamic')

    def __repr__(self) -> str:
        return (f"urgency_type_id={self.urgency_type_id}, "
                f"urgency_description={self.urgency_description})"
                )

    def put_into_dto(self) -> Dict[str, Any]:
        costs = [cost.put_into_dto() for cost in self.delivery_cost]
        return {
            'urgency_type_id': self.urgency_type_id,
            'urgency_description': self.urgency_description,
            'costs': costs
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> UrgencyType:
        urgency_type = UrgencyType(
            urgency_description=dto_dict['urgency_description']
        )
        return urgency_type