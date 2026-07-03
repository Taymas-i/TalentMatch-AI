import threading
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from app.core.config import settings
import app.models  
from app.services.rate_limit import check_and_increment
from app.core.exceptions import RateLimitError

engine = create_engine(settings.database_url)
SessionLocal = sessionmaker(bind=engine)

TEST_USER_ID = 1
DAILY_LIMIT = 10
TOTAL_REQUESTS = 15


def test_concurrent_requests_respect_daily_limit():
    """
    When many requests arrive simultaneously, exactly DAILY_LIMIT should
    be allowed and the rest should be blocked — no race condition should
    let more than DAILY_LIMIT requests through.
    """
    # Clean slate before the test
    db = SessionLocal()
    db.execute(
        text(
            "DELETE FROM user_limits WHERE user_id = :uid"
        ),
        {"uid": TEST_USER_ID},
    )
    db.commit()
    db.close()

    results = {"allowed": 0, "blocked": 0}
    lock = threading.Lock()

    def make_request():
        db = SessionLocal()
        try:
            check_and_increment(db, TEST_USER_ID)
            with lock:
                results["allowed"] += 1
        except RateLimitError:
            with lock:
                results["blocked"] += 1
        finally:
            db.close()

    threads = [threading.Thread(target=make_request) for _ in range(TOTAL_REQUESTS)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    assert results["allowed"] == DAILY_LIMIT
    assert results["blocked"] == TOTAL_REQUESTS - DAILY_LIMIT