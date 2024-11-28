from __future__ import annotations
from typing import Dict, Any
from app import db


class Price(db.Model):
    __tablename__ = 'prices'

    price_id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.product_id'), nullable=True)
    store_id = db.Column(db.Integer, db.ForeignKey('stores.store_id'), nullable=True)
    price = db.Column(db.Numeric(10, 2), nullable=True)

    def __repr__(self) -> str:
        return (f"price_id={self.price_id}, "
                f"product_id={self.product_id}, "
                f"store_id={self.store_id}, "
                f"price={self.price})")

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'price_id': self.price_id,
            'product_id': self.product_id,
            'store_id': self.store_id,
            'price': self.price
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Price:
        price = Price(
            product_id=dto_dict['product_id'],
            store_id=dto_dict['store_id'],
            price=dto_dict['price']
        )
        return price