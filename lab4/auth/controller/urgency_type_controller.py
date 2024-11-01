from .general_controller import GeneralController
from ..service import urgency_type_service


class UrgencyTypeController(GeneralController):
    _service = urgency_type_service