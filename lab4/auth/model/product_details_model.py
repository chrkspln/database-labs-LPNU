from __future__ import annotations
from typing import Dict, Any
from lab4 import db


class ProductDetails(db.Model):
    __tablename__ = 'product_details'

    product_details_id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.product_id'), nullable=True)
    description = db.Column(db.Text, nullable=True)
    category_id = db.Column(db.Integer, db.ForeignKey('product_categories.category_id'), nullable=True)

    def __repr__(self) -> str:
        return (f"product_details_id={self.product_details_id}, "
                f"product_id={self.product_id}, "
                f"description={self.description}, "
                f"category_id={self.category_id})")

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'product_details_id': self.product_details_id,
            'product_id': self.product_id,
            'description': self.description,
            'category_id': self.category_id
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> ProductDetails:
        product_details = ProductDetails(
            product_id=dto_dict['product_id'],
            description=dto_dict['description'],
            category_id=dto_dict['category_id']
        )
        return product_details