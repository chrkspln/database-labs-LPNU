from .general_controller import GeneralController
from ..service import store_feedback_service


class StoreFeedbackController(GeneralController):
    _service = store_feedback_service