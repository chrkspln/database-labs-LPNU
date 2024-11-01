from .general_service import GeneralService
from ..dao import urgency_type_dao


class UrgencyTypeService(GeneralService):
    _dao = urgency_type_dao