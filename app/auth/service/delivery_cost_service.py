from .general_service import GeneralService
from ..dao import delivery_cost_dao


class DeliveryCostService(GeneralService):
    _dao = delivery_cost_dao