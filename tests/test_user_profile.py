import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
APP_FOLDER = PROJECT_ROOT / "app"

sys.path.insert(0, str(APP_FOLDER))

from user_profile import create_profile, get_profile_summary


def test_create_profile():
    profile = create_profile(
        name="Test User",
        age_group="Adult",
        user_type="Woman",
        education_level="College/University",
        interests=["Python", "Mathematics"],
        learning_goal="Improve programming skills"
    )

    assert profile["name"] == "Test User"
    assert profile["age_group"] == "Adult"
    assert profile["user_type"] == "Woman"
    assert profile["education_level"] == "College/University"
    assert profile["interests"] == ["Python", "Mathematics"]
    assert profile["learning_goal"] == "Improve programming skills"


def test_profile_contains_all_required_fields():
    profile = create_profile(
        name="Test User",
        age_group="Adult",
        user_type="Woman",
        education_level="College/University",
        interests=["Python"],
        learning_goal="Learn programming"
    )

    required_fields = [
        "name",
        "age_group",
        "user_type",
        "education_level",
        "interests",
        "learning_goal"
    ]

    for field in required_fields:
        assert field in profile


def test_get_profile_summary():
    profile = create_profile(
        name="Test User",
        age_group="Adult",
        user_type="Woman",
        education_level="College/University",
        interests=["Python", "English"],
        learning_goal="Improve my skills"
    )

    summary = get_profile_summary(profile)

    assert "Test User" in summary
    assert "Adult" in summary
    assert "Woman" in summary
    assert "College/University" in summary
    assert "Python, English" in summary
    assert "Improve my skills" in summary