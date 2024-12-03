from .general_service import GeneralService
from ..dao import store_feedback_dao


class StoreFeedbackService(GeneralService):
    _dao = store_feedback_dao