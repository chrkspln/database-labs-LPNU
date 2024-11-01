from .general_service import GeneralService
from ..dao import product_expiration_dao


class ProductExpirationService(GeneralService):
    _dao = product_expiration_dao