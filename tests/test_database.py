import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATABASE_FOLDER = PROJECT_ROOT / "database"

sys.path.insert(0, str(DATABASE_FOLDER))

from database import initialize_database, add_user, save_quiz_result, get_user_quiz_results


def test_database_initialization():
    initialize_database()


def test_add_user():
    initialize_database()

    user_id = add_user(
        "Test User",
        "Adult",
        "Woman",
        "College/University",
        "Learn programming"
    )

    assert user_id is not None
    assert user_id > 0


def test_save_and_get_quiz_result():
    initialize_database()

    user_id = add_user(
        "Quiz Test User",
        "Adult",
        "Woman",
        "College/University",
        "Improve Python skills"
    )

    save_quiz_result(
        user_id=user_id,
        subject="Python",
        topic="Functions",
        score=4,
        total_questions=5
    )

    results = get_user_quiz_results(user_id)

    assert len(results) > 0
    assert results[0][0] == "Python"
    assert results[0][1] == "Functions"
    assert results[0][2] == 4
    assert results[0][3] == 5