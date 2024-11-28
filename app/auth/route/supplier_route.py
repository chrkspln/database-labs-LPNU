from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import supplier_controller
from ..model.supplier_model import Supplier

supplier_bp = Blueprint('supplier', __name__, url_prefix='/supplier')


@supplier_bp.route('', methods=['GET'])
def get_all_suppliers() -> Response:
    return make_response(jsonify(supplier_controller.find_all()), HTTPStatus.OK)


@supplier_bp.route('', methods=['POST'])
def create_supplier() -> Response:
    content = request.get_json()
    supplier = Supplier.create_from_dto(content)
    supplier_controller.create(supplier)
    return make_response(jsonify(supplier.put_into_dto()), HTTPStatus.CREATED)


@supplier_bp.route('/<int:supplier_id>', methods=['GET'])
def get_supplier(supplier_id: int) -> Response:
    return make_response(jsonify(supplier_controller.find_by_id(supplier_id)), HTTPStatus.OK)


@supplier_bp.route('/<int:supplier_id>', methods=['PUT'])
def update_supplier(supplier_id: int) -> Response:
    content = request.get_json()
    supplier = Supplier.create_from_dto(content)
    supplier_controller.update(supplier_id, supplier)
    return make_response("Supplier updated", HTTPStatus.OK)


@supplier_bp.route('/<int:supplier_id>', methods=['PATCH'])
def patch_supplier(supplier_id: int) -> Response:
    content = request.get_json()
    supplier_controller.patch(supplier_id, content)
    return make_response("Supplier updated", HTTPStatus.OK)


@supplier_bp.route('/<int:supplier_id>', methods=['DELETE'])
def delete_supplier(supplier_id: int) -> Response:
    supplier_controller.delete(supplier_id)
    return make_response("Supplier deleted", HTTPStatus.OK)
