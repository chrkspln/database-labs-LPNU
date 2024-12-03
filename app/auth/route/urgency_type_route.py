from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import urgency_type_controller
from ..model.insert_record import insert_record
from ..model.urgency_type_model import UrgencyType

urgency_type_bp = Blueprint('urgency_type', __name__, url_prefix='/urgency_type')


@urgency_type_bp.route('', methods=['GET'])
def get_all_urgency_types() -> Response:
    return make_response(jsonify(urgency_type_controller.find_all()), HTTPStatus.OK)


@urgency_type_bp.route('', methods=['POST'])
def create_urgency_type() -> Response:
    content = request.get_json()
    urgency_type = UrgencyType.create_from_dto(content)
    urgency_type_controller.create(urgency_type)
    return make_response(jsonify(urgency_type.put_into_dto()), HTTPStatus.CREATED)


@urgency_type_bp.route('/<int:urgency_type_id>', methods=['GET'])
def get_urgency_type(urgency_type_id: int) -> Response:
    return make_response(jsonify(urgency_type_controller.find_by_id(urgency_type_id)), HTTPStatus.OK)


@urgency_type_bp.route('/<int:urgency_type_id>', methods=['PUT'])
def update_urgency_type(urgency_type_id: int) -> Response:
    content = request.get_json()
    urgency_type = UrgencyType.create_from_dto(content)
    urgency_type_controller.update(urgency_type_id, urgency_type)
    return make_response("Urgency Type updated", HTTPStatus.OK)


@urgency_type_bp.route('/<int:urgency_type_id>', methods=['PATCH'])
def patch_urgency_type(urgency_type_id: int) -> Response:
    content = request.get_json()
    urgency_type_controller.patch(urgency_type_id, content)
    return make_response("Urgency Type updated", HTTPStatus.OK)


@urgency_type_bp.route('/<int:urgency_type_id>', methods=['DELETE'])
def delete_urgency_type(urgency_type_id: int) -> Response:
    urgency_type_controller.delete(urgency_type_id)
    return make_response("Urgency Type deleted", HTTPStatus.OK)

@urgency_type_bp.route('/parametrized', methods=['POST'])
def insert_urgency_type_record() -> Response:
    return insert_record(UrgencyType, request.get_json())
