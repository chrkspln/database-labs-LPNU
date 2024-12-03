from flask import Flask
from .error_handler import err_handler_bp

def register_routes(app: Flask) -> None:
    app.register_blueprint(err_handler_bp)
    from .delivery_cost_route import delivery_cost_bp
    from .delivery_route import delivery_bp
    from .price_route import price_bp
    from .product_category_route import product_category_bp
    from .product_details_route import product_details_bp
    from .product_expiration_route import product_expiration_bp
    from .product_route import product_bp
    from .store_route import store_bp
    from .store_supply_route import store_supply_bp
    from .supplier_route import supplier_bp
    from .urgency_type_route import urgency_type_bp
    from .store_feedback_route import store_feedback_bp


    app.register_blueprint(delivery_cost_bp)
    app.register_blueprint(delivery_bp)
    app.register_blueprint(price_bp)
    app.register_blueprint(product_category_bp)
    app.register_blueprint(product_details_bp)
    app.register_blueprint(product_expiration_bp)
    app.register_blueprint(product_bp)
    app.register_blueprint(store_bp)
    app.register_blueprint(store_supply_bp)
    app.register_blueprint(supplier_bp)
    app.register_blueprint(urgency_type_bp)
    app.register_blueprint(store_feedback_bp)