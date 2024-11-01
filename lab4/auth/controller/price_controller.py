from .general_controller import GeneralController
from ..service import price_service


class PriceController(GeneralController):
    _service = price_service