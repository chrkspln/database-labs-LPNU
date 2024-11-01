from .general_service import GeneralService
from ..dao import price_dao


class PriceService(GeneralService):
    _dao = price_dao