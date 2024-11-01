from .general_controller import GeneralController
from ..service import store_supply_service


class StoreSupplyController(GeneralController):
    _service = store_supply_service