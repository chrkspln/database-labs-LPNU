from .general_dao import GeneralDAO
from ..model.product_category_model import ProductCategory


class ProductCategoryDAO(GeneralDAO):
    _domain_type = ProductCategory