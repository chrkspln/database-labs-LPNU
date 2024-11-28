from .general_controller import GeneralController
from ..service import delivery_cost_service


class DeliveryCostController(GeneralController):
    _service = delivery_cost_service