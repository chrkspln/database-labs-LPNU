from .general_dao import GeneralDAO
from ..model.product_model import Product


class ProductDAO(GeneralDAO):
    _domain_type = Product