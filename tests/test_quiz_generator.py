import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
APP_FOLDER = PROJECT_ROOT / "app"

sys.path.insert(0, str(APP_FOLDER))

from quiz_generator import get_quiz


def test_get_quiz_returns_questions():
    quiz = get_quiz(
        subject="Python",
        topic="Functions",
        difficulty="Beginner",
        number_of_questions=3
    )

    assert quiz is not None
    assert len(quiz) == 3


def test_quiz_questions_have_required_fields():
    quiz = get_quiz(
        subject="Python",
        topic="Functions",
        difficulty="Beginner",
        number_of_questions=3
    )

    for question in quiz:
        assert "question" in question
        assert "options" in question
        assert "answer" in question
        assert "explanation" in question

        assert question["question"]
        assert len(question["options"]) == 4
        assert question["answer"] in question["options"]
        assert question["explanation"]


def test_get_quiz_respects_question_count():
    quiz = get_quiz(
        subject="Mathematics",
        topic="Basic Arithmetic",
        difficulty="Beginner",
        number_of_questions=2
    )

    assert len(quiz) == 2
    
    
def test_get_quiz_with_invalid_subject_returns_empty_list():
    quiz = get_quiz(
        subject="History",
        topic="World History",
        difficulty="Beginner",
        number_of_questions=3
    )

    assert quiz == []
    
    
def test_get_quiz_with_zero_questions_returns_empty_list():
    quiz = get_quiz(
        subject="Python",
        topic="Functions",
        difficulty="Beginner",
        number_of_questions=0
    )

    assert quiz == []