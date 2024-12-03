from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import delivery_controller
from ..model.delivery_model import Delivery
from ..model.insert_record import insert_record

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
    try:
        delivery_controller.delete(delivery_id)
        return make_response("Delivery deleted", HTTPStatus.OK)
    except Exception as e:
        return make_response(jsonify({"error": f"An error occurred: {str(e)}"}), HTTPStatus.INTERNAL_SERVER_ERROR)

@delivery_bp.route('/parametrized', methods=['POST'])
def insert_delivery_record() -> Response:
    return insert_record(Delivery, request.get_json())

@delivery_bp.route('/new_link', methods=['POST'])
def add_link() -> Response:
    content = request.get_json()
    store_name = content['store_name']
    urgency_type_name = content['urgency_type_name']
    try:
        new_link = Delivery.add_link(store_name, urgency_type_name)
        return make_response(jsonify(new_link.put_into_dto()), HTTPStatus.CREATED)
    except ValueError as e:
        return make_response(str(e), HTTPStatus.BAD_REQUEST)
