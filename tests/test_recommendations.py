import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
APP_FOLDER = PROJECT_ROOT / "app"

sys.path.insert(0, str(APP_FOLDER))

from recommendations import generate_recommendations


def test_recommendations_use_learning_goal():
    profile = {
        "learning_goal": "Learn Python",
        "interests": []
    }

    recommendations = generate_recommendations(profile, [])

    assert len(recommendations) == 1
    assert "Learn Python" in recommendations[0]


def test_recommendations_use_interests():
    profile = {
        "learning_goal": "",
        "interests": ["Python", "Mathematics", "English", "Science"]
    }

    recommendations = generate_recommendations(profile, [])

    assert len(recommendations) == 3
    assert "Python" in recommendations[0]
    assert "Mathematics" in recommendations[1]
    assert "English" in recommendations[2]


def test_low_quiz_score_recommendation():
    profile = {
        "learning_goal": "",
        "interests": []
    }

    quiz_results = [
        ("Python", "Functions", 2, 5, 40)
    ]

    recommendations = generate_recommendations(
        profile,
        quiz_results
    )

    assert len(recommendations) == 1
    assert "40%" in recommendations[0]
    assert "Review this topic" in recommendations[0]


def test_medium_quiz_score_recommendation():
    profile = {
        "learning_goal": "",
        "interests": []
    }

    quiz_results = [
        ("Mathematics", "Basic Arithmetic", 3, 5, 60)
    ]

    recommendations = generate_recommendations(
        profile,
        quiz_results
    )

    assert len(recommendations) == 1
    assert "60%" not in recommendations[0]
    assert "making progress" in recommendations[0]


def test_high_quiz_score_recommendation():
    profile = {
        "learning_goal": "",
        "interests": []
    }

    quiz_results = [
        ("English", "Grammar", 5, 5, 100)
    ]

    recommendations = generate_recommendations(
        profile,
        quiz_results
    )

    assert len(recommendations) == 1
    assert "100%" in recommendations[0]
    assert "Excellent work" in recommendations[0]
    assert "advanced topic" in recommendations[0]


def test_default_recommendation():
    profile = {
        "learning_goal": "",
        "interests": []
    }

    recommendations = generate_recommendations(profile, [])

    assert len(recommendations) == 1
    assert "Start by choosing a subject" in recommendations[0]