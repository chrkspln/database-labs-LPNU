from .general_service import GeneralService
from ..dao import product_dao


class ProductService(GeneralService):
    _dao = product_dao