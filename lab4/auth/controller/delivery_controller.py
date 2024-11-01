from .general_controller import GeneralController
from ..service import delivery_service


class DeliveryController(GeneralController):
    _service = delivery_service