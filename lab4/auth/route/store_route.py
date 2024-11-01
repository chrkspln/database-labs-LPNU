from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import store_controller
from ..model.store_model import Store

store_bp = Blueprint('store', __name__, url_prefix='/store')


@store_bp.route('', methods=['GET'])
def get_all_stores() -> Response:
    return make_response(jsonify(store_controller.find_all()), HTTPStatus.OK)


@store_bp.route('', methods=['POST'])
def create_store() -> Response:
    content = request.get_json()
    store = Store.create_from_dto(content)
    store_controller.create(store)
    return make_response(jsonify(store.put_into_dto()), HTTPStatus.CREATED)


@store_bp.route('/<int:store_id>', methods=['GET'])
def get_store(store_id: int) -> Response:
    return make_response(jsonify(store_controller.find_by_id(store_id)), HTTPStatus.OK)


@store_bp.route('/<int:store_id>', methods=['PUT'])
def update_store(store_id: int) -> Response:
    content = request.get_json()
    store = Store.create_from_dto(content)
    store_controller.update(store_id, store)
    return make_response("Store updated", HTTPStatus.OK)


@store_bp.route('/<int:store_id>', methods=['PATCH'])
def patch_store(store_id: int) -> Response:
    content = request.get_json()
    store_controller.patch(store_id, content)
    return make_response("Store updated", HTTPStatus.OK)


@store_bp.route('/<int:store_id>', methods=['DELETE'])
def delete_store(store_id: int) -> Response:
    store_controller.delete(store_id)
    return make_response("Store deleted", HTTPStatus.OK)
