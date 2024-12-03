from __future__ import annotations

from datetime import datetime
from random import randint, choice
from typing import Dict, Any

from sqlalchemy import text

from app import db


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

    @staticmethod
    def create_dynamic_tables():
        category_names = db.session.query(ProductCategory.category_name).all()
        table_count = 0
        for name_tuple in category_names:
            if table_count >= 10:
                break
            category_name = name_tuple[0].replace(" ", "_")
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            table_name = f"{category_name}_{timestamp}"
            num_columns = randint(1, 9)
            columns_sql = []
            for i in range(1, num_columns + 1):
                col_name = f"col_{i}"
                col_type = choice(["VARCHAR(255)", "INT", "DECIMAL(10,2)", "DATE"])
                columns_sql.append(f"{col_name} {col_type}")
            columns_sql_str = ", ".join(columns_sql)
            create_table_sql = f"CREATE TABLE `{table_name}` (id INT AUTO_INCREMENT PRIMARY KEY, {columns_sql_str});"
            db.session.execute(text(create_table_sql))
            print(f"Created table: {table_name}")
            table_count += 1
        db.session.commit()