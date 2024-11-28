from .general_service import GeneralService
from ..dao import store_supply_dao


class StoreSupplyService(GeneralService):
    _dao = store_supply_dao