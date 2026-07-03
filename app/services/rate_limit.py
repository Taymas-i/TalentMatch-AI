from datetime import date
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.models.user_limit import UserLimit
from app.core.exceptions import RateLimitError

DAILY_LIMIT = 10

def check_and_increment(db: Session, user_id: int) -> None:
    limit_row = (
        db.query(UserLimit)
        .filter(UserLimit.user_id == user_id)
        .with_for_update()
        .first()
    )

    if limit_row is None:
        try:
            limit_row = UserLimit(user_id=user_id, request_count=0, last_reset_date=date.today())
            db.add(limit_row)
            db.flush()
        except IntegrityError:
            db.rollback()
            limit_row = (
                db.query(UserLimit)
                .filter(UserLimit.user_id == user_id)
                .with_for_update()
                .first()
            )

    if limit_row.last_reset_date != date.today():
        limit_row.request_count = 0
        limit_row.last_reset_date = date.today()

    if limit_row.request_count >= DAILY_LIMIT:
        db.commit()
        raise RateLimitError(f"Daily limit of {DAILY_LIMIT} requests exceeded.")

    limit_row.request_count += 1
    db.commit()