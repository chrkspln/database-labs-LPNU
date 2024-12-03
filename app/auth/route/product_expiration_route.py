from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import product_expiration_controller
from ..model.insert_record import insert_record
from ..model.product_expiration_model import ProductExpiration

product_expiration_bp = Blueprint('product_expiration', __name__, url_prefix='/product_expiration')


@product_expiration_bp.route('', methods=['GET'])
def get_all_product_expirations() -> Response:
    return make_response(jsonify(product_expiration_controller.find_all()), HTTPStatus.OK)


@product_expiration_bp.route('', methods=['POST'])
def create_product_expiration() -> Response:
    content = request.get_json()
    product_expiration = ProductExpiration.create_from_dto(content)
    product_expiration_controller.create(product_expiration)
    return make_response(jsonify(product_expiration.put_into_dto()), HTTPStatus.CREATED)


@product_expiration_bp.route('/<int:product_expiration_id>', methods=['GET'])
def get_product_expiration(product_expiration_id: int) -> Response:
    return make_response(jsonify(product_expiration_controller.find_by_id(product_expiration_id)), HTTPStatus.OK)


@product_expiration_bp.route('/<int:product_expiration_id>', methods=['PUT'])
def update_product_expiration(product_expiration_id: int) -> Response:
    content = request.get_json()
    product_expiration = ProductExpiration.create_from_dto(content)
    product_expiration_controller.update(product_expiration_id, product_expiration)
    return make_response("product_expiration updated", HTTPStatus.OK)


@product_expiration_bp.route('/<int:product_expiration_id>', methods=['PATCH'])
def patch_product_expiration(product_expiration_id: int) -> Response:
    content = request.get_json()
    product_expiration_controller.patch(product_expiration_id, content)
    return make_response("product_expiration updated", HTTPStatus.OK)


@product_expiration_bp.route('/<int:product_expiration_id>', methods=['DELETE'])
def delete_product_expiration(product_expiration_id: int) -> Response:
    product_expiration_controller.delete(product_expiration_id)
    return make_response("product_expiration deleted", HTTPStatus.OK)

@product_expiration_bp.route('/parametrized', methods=['POST'])
def insert_product_expiration_record() -> Response:
    return insert_record(ProductExpiration, request.get_json())
