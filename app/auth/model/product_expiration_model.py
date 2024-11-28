from __future__ import annotations
from typing import Dict, Any
from app import db


class ProductExpiration(db.Model):
    __tablename__ = 'product_expiration'

    expiration_id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.product_id'), nullable=True)
    expiration_date = db.Column(db.Date, nullable=True)

    def __repr__(self) -> str:
        return (f"expiration_id={self.expiration_id}, "
                f"product_id={self.product_id}, "
                f"expiration_date={self.expiration_date})")

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'expiration_id': self.expiration_id,
            'product_id': self.product_id,
            'expiration_date': self.expiration_date
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> ProductExpiration:
        expiration = ProductExpiration(
            product_id=dto_dict['product_id'],
            expiration_date=dto_dict['expiration_date']
        )
        return expiration