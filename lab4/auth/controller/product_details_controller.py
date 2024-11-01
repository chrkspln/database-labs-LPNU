from .general_controller import GeneralController
from ..service import product_details_service


class ProductDetailsController(GeneralController):
    _service = product_details_service