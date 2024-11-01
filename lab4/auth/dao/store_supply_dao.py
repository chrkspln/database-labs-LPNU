from .general_dao import GeneralDAO
from ..model.store_supply_model import StoreSupply


class StoreSupplyDAO(GeneralDAO):
    _domain_type = StoreSupply