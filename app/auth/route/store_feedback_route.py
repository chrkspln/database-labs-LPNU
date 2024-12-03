from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import store_feedback_controller
from ..model.store_feedback_model import StoreFeedback

store_feedback_bp = Blueprint('store_feedback', __name__, url_prefix='/store_feedback')


@store_feedback_bp.route('', methods=['GET'])
def get_all_store_feedbacks() -> Response:
    return make_response(jsonify(store_feedback_controller.find_all()), HTTPStatus.OK)


@store_feedback_bp.route('', methods=['POST'])
def create_store_feedback() -> Response:
    try:
        content = request.get_json()
        store_feedback = StoreFeedback.create_from_dto(content)
        store_feedback_controller.create(store_feedback)
        return make_response(jsonify(store_feedback.put_into_dto()), HTTPStatus.CREATED)
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), HTTPStatus.BAD_REQUEST)


@store_feedback_bp.route('/<int:store_feedback_id>', methods=['GET'])
def get_store_feedback(store_feedback_id: int) -> Response:
    return make_response(jsonify(store_feedback_controller.find_by_id(store_feedback_id)), HTTPStatus.OK)


@store_feedback_bp.route('/<int:store_feedback_id>', methods=['PUT'])
def update_store_feedback(store_feedback_id: int) -> Response:
    try:
        content = request.get_json()
        store_feedback = StoreFeedback.create_from_dto(content)
        store_feedback_controller.update(store_feedback_id, store_feedback)
        return make_response(jsonify({"message": "StoreFeedback updated"}, HTTPStatus.OK))
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), HTTPStatus.BAD_REQUEST)


@store_feedback_bp.route('/<int:store_feedback_id>', methods=['PATCH'])
def patch_store_feedback(store_feedback_id: int) -> Response:
    try:
        content = request.get_json()
        store_feedback_controller.patch(store_feedback_id, content)
        return make_response(jsonify({"message": "StoreFeedback updated"}, HTTPStatus.OK))
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), HTTPStatus.BAD_REQUEST)

@store_feedback_bp.route('/<int:store_feedback_id>', methods=['DELETE'])
def delete_store_feedback(store_feedback_id: int) -> Response:
    try:
        store_feedback_controller.delete(store_feedback_id)
        return make_response(jsonify({"message": "StoreFeedback deleted"}, HTTPStatus.OK))
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), HTTPStatus.BAD_REQUEST)

@store_feedback_bp.route('/statistics', methods=['POST'])
def get_store_feedback_statistics() -> Response:
    try:
        statistics = {
            "min": StoreFeedback.get_min_rating(),
            "max": StoreFeedback.get_max_rating(),
            "sum": StoreFeedback.get_sum_rating(),
            "avg": StoreFeedback.get_avg_rating()
        }
        return make_response(jsonify(statistics), HTTPStatus.OK)
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), HTTPStatus.BAD_REQUEST)
