import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
APP_FOLDER = PROJECT_ROOT / "app"

sys.path.insert(0, str(APP_FOLDER))

from study_planner import create_study_plan


def test_create_study_plan_returns_plan():
    plan = create_study_plan(
        learning_goal="Python",
        skill_level="Beginner",
        study_time="1 hour",
        duration=4
    )

    assert plan is not None
    assert len(plan) > 0


def test_study_plan_contains_basic_information():
    plan = create_study_plan(
        learning_goal="Python",
        skill_level="Beginner",
        study_time="1 hour",
        duration=4
    )

    assert "Python" in plan
    assert "Beginner" in plan
    assert "1 hour" in plan
    assert "4 weeks" in plan


def test_study_plan_contains_correct_number_of_weeks():
    plan = create_study_plan(
        learning_goal="Mathematics",
        skill_level="Intermediate",
        study_time="2 hours",
        duration=3
    )

    assert "### Week 1" in plan
    assert "### Week 2" in plan
    assert "### Week 3" in plan
    assert "### Week 4" not in plan


def test_study_plan_uses_profile_information():
    profile = {
        "learning_goal": "Build computer skills",
        "interests": ["Python", "Mathematics"]
    }

    plan = create_study_plan(
        learning_goal="Programming",
        skill_level="Beginner",
        study_time="1 hour",
        duration=2,
        profile=profile
    )

    assert "Build computer skills" in plan
    assert "Python, Mathematics" in plan