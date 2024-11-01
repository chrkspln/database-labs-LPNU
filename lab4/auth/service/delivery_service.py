from .general_service import GeneralService
from ..dao import delivery_dao


class DeliveryService(GeneralService):
    _dao = delivery_dao