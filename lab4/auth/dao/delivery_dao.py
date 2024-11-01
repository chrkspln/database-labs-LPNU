from .general_dao import GeneralDAO
from ..model.delivery_model import Delivery

class DeliveryDAO(GeneralDAO):
    _domain_type = Delivery