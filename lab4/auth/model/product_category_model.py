from __future__ import annotations
from typing import Dict, Any
from lab4 import db


class ProductCategory(db.Model):
    __tablename__ = 'product_categories'

    category_id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(30), nullable=True)

    product = db.relationship("Product", backref="category")
    product_details = db.relationship("ProductDetails", backref="category")


    def __repr__(self) -> str:
        return (f"category_id={self.category_id}, "
                f"category_name={self.category_name})")

    def put_into_dto(self) -> Dict[str, Any]:
        products = [product.put_into_dto() for product in self.product]
        product_details = [product_detail.put_into_dto() for product_detail in self.product_details]
        return {
            'category_id': self.category_id,
            'category_name': self.category_name,
            'products': products,
            'product_details': product_details
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> ProductCategory:
        product_category = ProductCategory(
            category_name=dto_dict['category_name']
        )
        return product_category