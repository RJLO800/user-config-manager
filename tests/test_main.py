"""Unit tests for main.py"""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from main import add_setting, delete_setting, update_setting, view_settings


@pytest.fixture
def settings():
    return {}


def test_add_setting_new_key(settings):
    result = add_setting(settings, ("Theme", "Dark"))
    assert settings == {"theme": "dark"}
    assert "added" in result


def test_add_setting_existing_key(settings):
    add_setting(settings, ("theme", "dark"))
    result = add_setting(settings, ("theme", "light"))
    assert settings == {"theme": "dark"}
    assert "already exists" in result


def test_update_setting_existing_key(settings):
    add_setting(settings, ("theme", "dark"))
    result = update_setting(settings, ("theme", "light"))
    assert settings == {"theme": "light"}
    assert "updated" in result


def test_update_setting_missing_key(settings):
    result = update_setting(settings, ("theme", "light"))
    assert settings == {}
    assert "does not exist" in result


def test_delete_setting_existing_key(settings):
    add_setting(settings, ("theme", "dark"))
    result = delete_setting(settings, "theme")
    assert settings == {}
    assert "deleted" in result


def test_delete_setting_missing_key(settings):
    result = delete_setting(settings, "theme")
    assert "not found" in result.lower()


def test_view_settings_empty(settings):
    assert view_settings(settings) == "No settings available."


def test_view_settings_with_data(settings):
    add_setting(settings, ("theme", "dark"))
    result = view_settings(settings)
    assert "Theme: dark" in result
