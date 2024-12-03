from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import product_category_controller
from ..model.insert_record import insert_record
from ..model.product_category_model import ProductCategory

product_category_bp = Blueprint('product_category', __name__, url_prefix='/product_category')


@product_category_bp.route('', methods=['GET'])
def get_all_product_categories() -> Response:
    return make_response(jsonify(product_category_controller.find_all()), HTTPStatus.OK)


@product_category_bp.route('', methods=['POST'])
def create_product_category() -> Response:
    content = request.get_json()
    product_category = ProductCategory.create_from_dto(content)
    product_category_controller.create(product_category)
    return make_response(jsonify(product_category.put_into_dto()), HTTPStatus.CREATED)


@product_category_bp.route('/<int:category_id>', methods=['GET'])
def get_product_category(category_id: int) -> Response:
    return make_response(jsonify(product_category_controller.find_by_id(category_id)), HTTPStatus.OK)


@product_category_bp.route('/<int:category_id>', methods=['PUT'])
def update_product_category(category_id: int) -> Response:
    content = request.get_json()
    product_category = ProductCategory.create_from_dto(content)
    product_category_controller.update(category_id, product_category)
    return make_response("Product Category updated", HTTPStatus.OK)


@product_category_bp.route('/<int:category_id>', methods=['PATCH'])
def patch_product_category(category_id: int) -> Response:
    content = request.get_json()
    product_category_controller.patch(category_id, content)
    return make_response("Product Category updated", HTTPStatus.OK)


@product_category_bp.route('/<int:category_id>', methods=['DELETE'])
def delete_product_category(category_id: int) -> Response:
    product_category_controller.delete(category_id)
    return make_response("Product Category deleted", HTTPStatus.OK)

@product_category_bp.route('/parametrized', methods=['POST'])
def insert_product_category_record() -> Response:
    return insert_record(ProductCategory, request.get_json())

@product_category_bp.route('/dynamic', methods=['POST'])
def create_dynamic_tables():
    try:
        ProductCategory.create_dynamic_tables()
        return make_response(jsonify({"message": "Dynamic tables created successfully"}), HTTPStatus.CREATED)
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR)