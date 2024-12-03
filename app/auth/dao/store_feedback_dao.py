from .general_dao import GeneralDAO
from ..model.store_feedback_model import StoreFeedback


class StoreFeedbackDAO(GeneralDAO):
    _domain_type = StoreFeedback