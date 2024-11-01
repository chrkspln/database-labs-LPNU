from .general_service import GeneralService
from ..dao import product_details_dao


class ProductDetailsService(GeneralService):
    _dao = product_details_dao