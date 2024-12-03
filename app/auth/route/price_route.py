from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import price_controller
from ..model.insert_record import insert_record
from ..model.price_model import Price

price_bp = Blueprint('price', __name__, url_prefix='/price')


@price_bp.route('', methods=['GET'])
def get_all_prices() -> Response:
    return make_response(jsonify(price_controller.find_all()), HTTPStatus.OK)


@price_bp.route('', methods=['POST'])
def create_price() -> Response:
    content = request.get_json()
    price = Price.create_from_dto(content)
    price_controller.create(price)
    return make_response(jsonify(price.put_into_dto()), HTTPStatus.CREATED)


@price_bp.route('/<int:price_id>', methods=['GET'])
def get_price(price_id: int) -> Response:
    return make_response(jsonify(price_controller.find_by_id(price_id)), HTTPStatus.OK)


@price_bp.route('/<int:price_id>', methods=['PUT'])
def update_price(price_id: int) -> Response:
    content = request.get_json()
    price = Price.create_from_dto(content)
    price_controller.update(price_id, price)
    return make_response("Price updated", HTTPStatus.OK)


@price_bp.route('/<int:price_id>', methods=['PATCH'])
def patch_price(price_id: int) -> Response:
    content = request.get_json()
    price_controller.patch(price_id, content)
    return make_response("Price updated", HTTPStatus.OK)


@price_bp.route('/<int:price_id>', methods=['DELETE'])
def delete_price(price_id: int) -> Response:
    price_controller.delete(price_id)
    return make_response("Price deleted", HTTPStatus.OK)

@price_bp.route('/parametrized', methods=['POST'])
def insert_price_record() -> Response:
    return insert_record(Price, request.get_json())
