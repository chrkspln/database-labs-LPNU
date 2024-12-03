from __future__ import annotations
from typing import Dict, Any
from app import db
from sqlalchemy import event, select, func


class StoreFeedback(db.Model):
    __tablename__ = 'store_feedbacks'

    feedback_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    store_id = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Integer, nullable=False)

    def __repr__(self) -> str:
        return (f"feedback_id={self.feedback_id}, "
                f"store_id={self.store_id}, "
                f"rating={self.rating}, "
                )

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'feedback_id': self.feedback_id,
            'store_id': self.store_id,
            'rating': self.rating
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> StoreFeedback:
        feedback = StoreFeedback(
            store_id=dto_dict['store_id'],
            rating=dto_dict['rating']
        )
        return feedback

    @staticmethod
    def get_min_rating() -> float:
        return db.session.query(func.min(StoreFeedback.rating)).scalar()

    @staticmethod
    def get_max_rating() -> float:
        return db.session.query(func.max(StoreFeedback.rating)).scalar()

    @staticmethod
    def get_sum_rating() -> float:
        return db.session.query(func.sum(StoreFeedback.rating)).scalar()

    @staticmethod
    def get_avg_rating() -> float:
        return db.session.query(func.avg(StoreFeedback.rating)).scalar()

@event.listens_for(StoreFeedback, "before_insert")
def check_store_feedback(mapper, connection, target):
    store_feedback = db.Table('stores', db.metadata, autoload_with=db.engine)

    store_has_feedback = connection.execute(
        select(store_feedback.c.store_id).where(store_feedback.c.store_id == target.store_id)
    ).first()

    if store_has_feedback is None:
        raise ValueError(f"Store {target.store_id} does not exist")
    