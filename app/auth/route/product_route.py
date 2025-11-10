from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import product_controller
from ..model.insert_record import insert_record
from ..model.product_model import Product

product_bp = Blueprint('product', __name__, url_prefix='/product')


@product_bp.route('', methods=['GET'])
def get_all_products() -> Response:
    """
    Get all products
    ---
    tags:
      - Product
    responses:
      200:
        description: List of all products
        schema:
          type: array
          items:
            type: object
    """
    return make_response(jsonify(product_controller.find_all()), HTTPStatus.OK)


@product_bp.route('', methods=['POST'])
def create_product() -> Response:
    """
    Create a new product
    ---
    tags:
      - Product
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
            category_id:
              type: integer
            price_id:
              type: integer
    responses:
      201:
        description: Product created
        schema:
          type: object
      400:
        description: Invalid input
    """
    content = request.get_json()
    product = Product.create_from_dto(content)
    product_controller.create(product)
    return make_response(jsonify(product.put_into_dto()), HTTPStatus.CREATED)


@product_bp.route('/<int:product_id>', methods=['GET'])
def get_product(product_id: int) -> Response:
    """
    Get a product by ID
    ---
    tags:
      - Product
    parameters:
      - in: path
        name: product_id
        type: integer
        required: true
        description: ID of the product
    responses:
      200:
        description: Product object
        schema:
          type: object
      404:
        description: Product not found
    """
    return make_response(jsonify(product_controller.find_by_id(product_id)), HTTPStatus.OK)


@product_bp.route('/<int:product_id>', methods=['PUT'])
def update_product(product_id: int) -> Response:
    """
    Replace an existing product by ID
    ---
    tags:
      - Product
    consumes:
      - application/json
    parameters:
      - in: path
        name: product_id
        type: integer
        required: true
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
            category_id:
              type: integer
            price_id:
              type: integer
    responses:
      200:
        description: Product updated
      400:
        description: Invalid input
      404:
        description: Product not found
    """
    try:
        content = request.get_json()
        product = Product.create_from_dto(content)
        product_controller.update(product_id, product)
        return make_response("Product updated", HTTPStatus.OK)
    except Exception as e:
        return make_response(jsonify({"error": f"An error occurred: {str(e)}"}), HTTPStatus.INTERNAL_SERVER_ERROR)


@product_bp.route('/<int:product_id>', methods=['PATCH'])
def patch_product(product_id: int) -> Response:
    """
    Partially update a product by ID
    ---
    tags:
      - Product
    consumes:
      - application/json
    parameters:
      - in: path
        name: product_id
        type: integer
        required: true
      - in: body
        name: body
        required: true
        schema:
          type: object
          description: Fields to update
    responses:
      200:
        description: Product patched
      400:
        description: Invalid input
      404:
        description: Product not found
    """
    try:
        content = request.get_json()
        product_controller.patch(product_id, content)
        return make_response("Product updated", HTTPStatus.OK)
    except Exception as e:
        return make_response(jsonify({"error": f"An error occurred: {str(e)}"}), HTTPStatus.INTERNAL_SERVER_ERROR)


@product_bp.route('/<int:product_id>', methods=['DELETE'])
def delete_product(product_id: int) -> Response:
    """
    Delete a product by ID
    ---
    tags:
      - Product
    parameters:
      - in: path
        name: product_id
        type: integer
        required: true
    responses:
      200:
        description: Product deleted
      404:
        description: Product not found
      500:
        description: Internal server error
    """
    try:
        product_controller.delete(product_id)
        return make_response("Product deleted", HTTPStatus.OK)
    except Exception as e:
        return make_response(jsonify({"error": f"An error occurred: {str(e)}"}), HTTPStatus.INTERNAL_SERVER_ERROR)


@product_bp.route('/parametrized', methods=['POST'])
def insert_product_record() -> Response:
    """
    Insert a parametrized Product record
    ---
    tags:
      - Product
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          description: Arbitrary parameters for inserting a Product record
    responses:
      201:
        description: Record inserted
      400:
        description: Invalid parameters
    """
    return insert_record(Product, request.get_json())
