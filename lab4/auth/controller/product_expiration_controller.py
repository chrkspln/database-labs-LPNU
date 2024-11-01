from .general_controller import GeneralController
from ..service import product_expiration_service


class ProductExpirationController(GeneralController):
    _service = product_expiration_service