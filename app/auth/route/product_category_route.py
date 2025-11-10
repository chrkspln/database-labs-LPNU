from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import product_category_controller
from ..model.insert_record import insert_record
from ..model.product_category_model import ProductCategory

product_category_bp = Blueprint('product_category', __name__, url_prefix='/product_category')


@product_category_bp.route('', methods=['GET'])
def get_all_product_categories() -> Response:
    """
    Get all product categories
    ---
    tags:
      - Product Category
    responses:
      200:
        description: List of all product categories
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
              name:
                type: string
    """
    return make_response(jsonify(product_category_controller.find_all()), HTTPStatus.OK)


@product_category_bp.route('', methods=['POST'])
def create_product_category() -> Response:
    """
    Create a new product category
    ---
    tags:
      - Product Category
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
    responses:
      201:
        description: Product category created
        schema:
          type: object
          properties:
            id:
              type: integer
            name:
              type: string
      400:
        description: Invalid input
    """
    content = request.get_json()
    product_category = ProductCategory.create_from_dto(content)
    product_category_controller.create(product_category)
    return make_response(jsonify(product_category.put_into_dto()), HTTPStatus.CREATED)


@product_category_bp.route('/<int:category_id>', methods=['GET'])
def get_product_category(category_id: int) -> Response:
    """
    Get a product category by ID
    ---
    tags:
      - Product Category
    parameters:
      - in: path
        name: category_id
        type: integer
        required: true
        description: ID of the product category
    responses:
      200:
        description: Product category object
        schema:
          type: object
          properties:
            id:
              type: integer
            name:
              type: string
      404:
        description: Product category not found
    """
    return make_response(jsonify(product_category_controller.find_by_id(category_id)), HTTPStatus.OK)


@product_category_bp.route('/<int:category_id>', methods=['PUT'])
def update_product_category(category_id: int) -> Response:
    """
    Replace an existing product category by ID
    ---
    tags:
      - Product Category
    consumes:
      - application/json
    parameters:
      - in: path
        name: category_id
        type: integer
        required: true
        description: ID of the product category to replace
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
    responses:
      200:
        description: Product category updated
      400:
        description: Invalid input
      404:
        description: Product category not found
    """
    content = request.get_json()
    product_category = ProductCategory.create_from_dto(content)
    product_category_controller.update(category_id, product_category)
    return make_response("Product Category updated", HTTPStatus.OK)


@product_category_bp.route('/<int:category_id>', methods=['PATCH'])
def patch_product_category(category_id: int) -> Response:
    """
    Partially update fields of a product category by ID
    ---
    tags:
      - Product Category
    consumes:
      - application/json
    parameters:
      - in: path
        name: category_id
        type: integer
        required: true
        description: ID of the product category to patch
      - in: body
        name: body
        required: true
        schema:
          type: object
          description: Fields to update (partial)
          properties:
            name:
              type: string
    responses:
      200:
        description: Product category patched
      400:
        description: Invalid input
      404:
        description: Product category not found
    """
    content = request.get_json()
    product_category_controller.patch(category_id, content)
    return make_response("Product Category updated", HTTPStatus.OK)


@product_category_bp.route('/<int:category_id>', methods=['DELETE'])
def delete_product_category(category_id: int) -> Response:
    """
    Delete a product category by ID
    ---
    tags:
      - Product Category
    parameters:
      - in: path
        name: category_id
        type: integer
        required: true
        description: ID of the product category to delete
    responses:
      200:
        description: Product Category deleted
      404:
        description: Product category not found
    """
    product_category_controller.delete(category_id)
    return make_response("Product Category deleted", HTTPStatus.OK)


@product_category_bp.route('/parametrized', methods=['POST'])
def insert_product_category_record() -> Response:
    """
    Insert a parametrized product category record
    ---
    tags:
      - Product Category
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          description: Arbitrary parameters for inserting a ProductCategory record
    responses:
      201:
        description: Record inserted
      400:
        description: Invalid parameters
    """
    return insert_record(ProductCategory, request.get_json())


@product_category_bp.route('/dynamic', methods=['POST'])
def create_dynamic_tables():
    """
    Create dynamic tables for ProductCategory
    ---
    tags:
      - Product Category
    responses:
      201:
        description: Dynamic tables created successfully
      500:
        description: Error creating dynamic tables
    """
    try:
        ProductCategory.create_dynamic_tables()
        return make_response(jsonify({"message": "Dynamic tables created successfully"}), HTTPStatus.CREATED)
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR)