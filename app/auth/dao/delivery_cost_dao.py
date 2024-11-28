from .general_dao import GeneralDAO
from ..model.delivery_cost_model import DeliveryCost

class DeliveryCostDAO(GeneralDAO):
    _domain_type = DeliveryCost