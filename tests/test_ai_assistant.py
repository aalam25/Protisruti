import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
APP_FOLDER = PROJECT_ROOT / "app"

sys.path.insert(0, str(APP_FOLDER))

from ai_assistant import ask_ai


def test_photosynthesis_question():
    response = ask_ai("What is photosynthesis?")

    assert response is not None
    assert "Photosynthesis" in response
    assert "Sunlight" in response
    assert "Water" in response
    assert "carbon dioxide" in response.lower()


def test_python_question():
    response = ask_ai("What is Python?")

    assert response is not None
    assert "Python" in response
    assert "programming language" in response


def test_computer_question():
    response = ask_ai("What is a computer?")

    assert response is not None
    assert "computer" in response.lower()
    assert "Input" in response
    assert "Processing" in response
    assert "Storage" in response
    assert "Output" in response


def test_mathematics_question():
    response = ask_ai("Tell me about mathematics.")

    assert response is not None
    assert "Mathematics" in response
    assert "Arithmetic" in response
    assert "Algebra" in response
    assert "Statistics" in response


def test_unknown_question():
    response = ask_ai("Tell me about history.")

    assert response is not None
    assert "Thank you for your question" in response
    assert "development version" in response
    
    
def test_ask_ai_with_empty_question_returns_message():
    response = ask_ai("")

    assert response == "Please enter a question so Protisruti can help you learn."
    
    
def test_ask_ai_with_whitespace_question_returns_message():
    response = ask_ai("   ")

    assert response == "Please enter a question so Protisruti can help you learn."
    
    
    
def test_ai_uses_profile_context():
    profile = {
        "name": "Test User",
        "age_group": "18-25",
        "user_type": "Student",
        "education_level": "University",
        "interests": [
            "Programming",
            "Artificial Intelligence"
        ],
        "learning_goal": "Learn Python for AI"
    }

    result = ask_ai(
        "What is Python?",
        profile
    )

    assert "Learn Python for AI" in result
    assert "Programming" in result
    assert "Artificial Intelligence" in result
    
    
def test_ai_provides_next_learning_topic():
    result = ask_ai("What is Python?")

    assert "What to Learn Next" in result
    assert "variables" in result.lower()