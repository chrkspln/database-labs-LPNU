from .general_dao import GeneralDAO
from ..model.urgency_type_model import UrgencyType


class UrgencyTypeDAO(GeneralDAO):
    _domain_type = UrgencyType