from .general_service import GeneralService
from ..dao import product_category_dao


class ProductCategoryService(GeneralService):
    _dao = product_category_dao