from .delivery_cost_service import DeliveryCostService
from .delivery_service import DeliveryService
from .price_service import PriceService
from .product_category_service import ProductCategoryService
from .product_details_service import ProductDetailsService
from .product_expiration_service import ProductExpirationService
from .product_service import ProductService
from .store_service import StoreService
from .store_supply_service import StoreSupplyService
from .supplier_service import SupplierService
from .urgency_type_service import UrgencyTypeService
from .store_feedback_service import StoreFeedbackService

delivery_cost_service = DeliveryCostService()
delivery_service = DeliveryService()
price_service = PriceService()
product_category_service = ProductCategoryService()
product_details_service = ProductDetailsService()
product_expiration_service = ProductExpirationService()
product_service = ProductService()
store_service = StoreService()
store_supply_service = StoreSupplyService()
supplier_service = SupplierService()
urgency_type_service = UrgencyTypeService()
store_feedback_service = StoreFeedbackService()