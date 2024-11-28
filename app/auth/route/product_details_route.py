from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import product_details_controller
from ..model.product_details_model import ProductDetails

product_details_bp = Blueprint('product_details', __name__, url_prefix='/product_details')


@product_details_bp.route('', methods=['GET'])
def get_all_product_details() -> Response:
    return make_response(jsonify(product_details_controller.find_all()), HTTPStatus.OK)


@product_details_bp.route('', methods=['POST'])
def create_product_details() -> Response:
    content = request.get_json()
    product_details = ProductDetails.create_from_dto(content)
    product_details_controller.create(product_details)
    return make_response(jsonify(product_details.put_into_dto()), HTTPStatus.CREATED)


@product_details_bp.route('/<int:product_details_id>', methods=['GET'])
def get_product_details(product_details_id: int) -> Response:
    return make_response(jsonify(product_details_controller.find_by_id(product_details_id)), HTTPStatus.OK)


@product_details_bp.route('/<int:product_details_id>', methods=['PUT'])
def update_product_details(product_details_id: int) -> Response:
    content = request.get_json()
    product_details = ProductDetails.create_from_dto(content)
    product_details_controller.update(product_details_id, product_details)
    return make_response("Product details updated", HTTPStatus.OK)


@product_details_bp.route('/<int:product_details_id>', methods=['PATCH'])
def patch_product_details(product_details_id: int) -> Response:
    content = request.get_json()
    product_details_controller.patch(product_details_id, content)
    return make_response("Product details updated", HTTPStatus.OK)


@product_details_bp.route('/<int:product_details_id>', methods=['DELETE'])
def delete_product_details(product_details_id: int) -> Response:
    product_details_controller.delete(product_details_id)
    return make_response("Product details deleted", HTTPStatus.OK)
