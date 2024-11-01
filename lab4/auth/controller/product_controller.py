from .general_controller import GeneralController
from ..service import product_service


class ProductController(GeneralController):
    _service = product_service