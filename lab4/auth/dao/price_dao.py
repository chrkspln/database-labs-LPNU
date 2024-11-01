from .general_dao import GeneralDAO
from ..model.price_model import Price


class PriceDAO(GeneralDAO):
    _domain_type = Price