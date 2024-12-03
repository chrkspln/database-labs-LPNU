from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import delivery_cost_controller
from ..model.delivery_cost_model import DeliveryCost
from ..model.insert_record import insert_record

delivery_cost_bp = Blueprint('delivery_cost', __name__, url_prefix='/delivery_cost')


@delivery_cost_bp.route('', methods=['GET'])
def get_all_delivery_costs() -> Response:
    return make_response(jsonify(delivery_cost_controller.find_all()), HTTPStatus.OK)


@delivery_cost_bp.route('', methods=['POST'])
def create_delivery_cost() -> Response:
    content = request.get_json()
    delivery_cost = DeliveryCost.create_from_dto(content)
    delivery_cost_controller.create(delivery_cost)
    return make_response(jsonify(delivery_cost.put_into_dto()), HTTPStatus.CREATED)


@delivery_cost_bp.route('/<int:delivery_cost_id>', methods=['GET'])
def get_delivery_cost(delivery_cost_id: int) -> Response:
    return make_response(jsonify(delivery_cost_controller.find_by_id(delivery_cost_id)), HTTPStatus.OK)


@delivery_cost_bp.route('/<int:delivery_cost_id>', methods=['PUT'])
def update_delivery_cost(delivery_cost_id: int) -> Response:
    content = request.get_json()
    delivery_cost = DeliveryCost.create_from_dto(content)
    delivery_cost_controller.update(delivery_cost_id, delivery_cost)
    return make_response("Delivery Cost updated", HTTPStatus.OK)


@delivery_cost_bp.route('/<int:delivery_cost_id>', methods=['PATCH'])
def patch_delivery_cost(delivery_cost_id: int) -> Response:
    content = request.get_json()
    delivery_cost_controller.patch(delivery_cost_id, content)
    return make_response("Delivery Cost updated", HTTPStatus.OK)


@delivery_cost_bp.route('/<int:delivery_cost_id>', methods=['DELETE'])
def delete_delivery_cost(delivery_cost_id: int) -> Response:
    delivery_cost_controller.delete(delivery_cost_id)
    return make_response("Delivery Cost deleted", HTTPStatus.OK)

@delivery_cost_bp.route('/parametrized', methods=['POST'])
def insert_delivery_cost_record() -> Response:
    return insert_record(DeliveryCost, request.get_json())
