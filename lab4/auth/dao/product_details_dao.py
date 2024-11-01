from .general_dao import GeneralDAO
from ..model.product_details_model import ProductDetails


class ProductDetailsDAO(GeneralDAO):
    _domain_type = ProductDetails