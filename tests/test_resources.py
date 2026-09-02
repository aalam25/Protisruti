import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
APP_FOLDER = PROJECT_ROOT / "app"

sys.path.insert(0, str(APP_FOLDER))

from resources import get_resources


def test_get_womens_education_resources():
    resources = get_resources("🌸 Women's Education")

    assert resources is not None
    assert len(resources) == 4


def test_resources_have_required_fields():
    resources = get_resources("📚 Children's Learning")

    for resource in resources:
        assert "title" in resource
        assert "description" in resource
        assert "type" in resource

        assert resource["title"]
        assert resource["description"]
        assert resource["type"]


def test_get_career_resources():
    resources = get_resources("💼 Skills & Career")

    assert len(resources) == 4
    assert resources[0]["title"] == "Computer Skills"


def test_get_unknown_category_returns_empty_list():
    resources = get_resources("Unknown Category")

    assert resources == []