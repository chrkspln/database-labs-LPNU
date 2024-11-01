from __future__ import annotations
from typing import Dict, Any

from unicodedata import category

from lab4 import db


class Product(db.Model):
    __tablename__ = 'products'

    product_id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=True)
    category_id = db.Column(db.Integer, db.ForeignKey('product_categories.category_id'), nullable=True)

    delivery = db.relationship("Delivery", backref="product")
    store_supply = db.relationship("StoreSupply", backref="product")

    def __repr__(self) -> str:
        return (f"product_id={self.product_id}, "
                f"product_name={self.product_name}, "
                f"category_id={self.category_id})")

    def put_into_dto(self) -> Dict[str, Any]:
        deliveries = [delivery.put_into_dto() for delivery in self.delivery]
        supplies = [supply.put_into_dto() for supply in self.store_supply]
        return {
            'product_id': self.product_id,
            'product_name': self.product_name,
            'category_id': self.category_id,
            'deliveries': deliveries,
            'supplies': supplies
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Product:
        product = Product(
            product_name=dto_dict['product_name'],
            category_id=dto_dict['category_id']
        )
        return product