from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import store_supply_controller
from ..model.insert_record import insert_record
from ..model.store_supply_model import StoreSupply

store_supply_bp = Blueprint('store_supply', __name__, url_prefix='/store_supply')


@store_supply_bp.route('', methods=['GET'])
def get_all_store_supplys() -> Response:
    return make_response(jsonify(store_supply_controller.find_all()), HTTPStatus.OK)


@store_supply_bp.route('', methods=['POST'])
def create_store_supply() -> Response:
    content = request.get_json()
    store_supply = StoreSupply.create_from_dto(content)
    store_supply_controller.create(store_supply)
    return make_response(jsonify(store_supply.put_into_dto()), HTTPStatus.CREATED)


@store_supply_bp.route('/<int:store_supply_id>', methods=['GET'])
def get_store_supply(store_supply_id: int) -> Response:
    return make_response(jsonify(store_supply_controller.find_by_id(store_supply_id)), HTTPStatus.OK)


@store_supply_bp.route('/<int:store_supply_id>', methods=['PUT'])
def update_store_supply(store_supply_id: int) -> Response:
    content = request.get_json()
    store_supply = StoreSupply.create_from_dto(content)
    store_supply_controller.update(store_supply_id, store_supply)
    return make_response("StoreSupply updated", HTTPStatus.OK)


@store_supply_bp.route('/<int:store_supply_id>', methods=['PATCH'])
def patch_store_supply(store_supply_id: int) -> Response:
    content = request.get_json()
    store_supply_controller.patch(store_supply_id, content)
    return make_response("StoreSupply updated", HTTPStatus.OK)


@store_supply_bp.route('/<int:store_supply_id>', methods=['DELETE'])
def delete_store_supply(store_supply_id: int) -> Response:
    store_supply_controller.delete(store_supply_id)
    return make_response("StoreSupply deleted", HTTPStatus.OK)

@store_supply_bp.route('/parametrized', methods=['POST'])
def insert_store_supply_record() -> Response:
    return insert_record(StoreSupply, request.get_json())
