from .general_controller import GeneralController
from ..service import supplier_service


class SupplierController(GeneralController):
    _service = supplier_service