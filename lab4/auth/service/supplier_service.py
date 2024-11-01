from .general_service import GeneralService
from ..dao import supplier_dao


class SupplierService(GeneralService):
    _dao = supplier_dao