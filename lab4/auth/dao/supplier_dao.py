from .general_dao import GeneralDAO
from ..model.supplier_model import Supplier


class SupplierDAO(GeneralDAO):
    _domain_type = Supplier