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