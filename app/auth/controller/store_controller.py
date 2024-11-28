from .general_controller import GeneralController
from ..service import store_service


class StoreController(GeneralController):
    _service = store_service