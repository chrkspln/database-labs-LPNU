from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import delivery_controller
from ..model.delivery_model import Delivery

delivery_bp = Blueprint('delivery', __name__, url_prefix='/delivery')


@delivery_bp.route('', methods=['GET'])
def get_all_deliveries() -> Response:
    return make_response(jsonify(delivery_controller.find_all()), HTTPStatus.OK)


@delivery_bp.route('', methods=['POST'])
def create_delivery() -> Response:
    content = request.get_json()
    delivery = Delivery.create_from_dto(content)
    delivery_controller.create(delivery)
    return make_response(jsonify(delivery.put_into_dto()), HTTPStatus.CREATED)


@delivery_bp.route('/<int:delivery_id>', methods=['GET'])
def get_delivery(delivery_id: int) -> Response:
    return make_response(jsonify(delivery_controller.find_by_id(delivery_id)), HTTPStatus.OK)


@delivery_bp.route('/<int:delivery_id>', methods=['PUT'])
def update_delivery(delivery_id: int) -> Response:
    content = request.get_json()
    assert content is not None
    delivery = Delivery.create_from_dto(content)
    delivery_controller.update(delivery_id, delivery)
    return make_response("Delivery updated", HTTPStatus.OK)


@delivery_bp.route('/<int:delivery_id>', methods=['PATCH'])
def patch_delivery(delivery_id: int) -> Response:
    content = request.get_json()
    delivery_controller.patch(delivery_id, content)
    return make_response("Delivery updated", HTTPStatus.OK)


@delivery_bp.route('/<int:delivery_id>', methods=['DELETE'])
def delete_delivery(delivery_id: int) -> Response:
    delivery_controller.delete(delivery_id)
    return make_response("Delivery deleted", HTTPStatus.OK)
