from .general_service import GeneralService
from ..dao import store_dao


class StoreService(GeneralService):
    _dao = store_dao