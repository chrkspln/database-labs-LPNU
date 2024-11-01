from .general_dao import GeneralDAO
from ..model.store_model import Store


class StoreDAO(GeneralDAO):
    _domain_type = Store