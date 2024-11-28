from .general_dao import GeneralDAO
from ..model.product_expiration_model import ProductExpiration


class ProductExpirationDAO(GeneralDAO):
    _domain_type = ProductExpiration