from .general_controller import GeneralController
from ..service import product_category_service


class ProductCategoryController(GeneralController):
    _service = product_category_service