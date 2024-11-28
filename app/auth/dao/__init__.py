from .delivery_cost_dao import DeliveryCostDAO
from .delivery_dao import DeliveryDAO
from .price_dao import PriceDAO
from .product_category_dao import ProductCategoryDAO
from .product_dao import ProductDAO
from .product_details_dao import ProductDetailsDAO
from .product_expiration_dao import ProductExpirationDAO
from .store_dao import StoreDAO
from .store_supply_dao import StoreSupplyDAO
from .supplier_dao import SupplierDAO
from .urgency_type_dao import UrgencyTypeDAO

delivery_cost_dao = DeliveryCostDAO()
delivery_dao = DeliveryDAO()
price_dao = PriceDAO()
product_category_dao = ProductCategoryDAO()
product_dao = ProductDAO()
product_details_dao = ProductDetailsDAO()
product_expiration_dao = ProductExpirationDAO()
store_dao = StoreDAO()
store_supply_dao = StoreSupplyDAO()
supplier_dao = SupplierDAO()
urgency_type_dao = UrgencyTypeDAO()