"""User Configuration Manager

Small in-memory CRUD helper for managing user settings as key/value pairs.
Keys are always normalized to lowercase; string values are normalized to
lowercase as well.
"""

from typing import Any


def add_setting(settings: dict, add: tuple) -> str:
    """Add a new setting.

    Args:
        settings: The settings dictionary to modify.
        add: A (key, value) pair to add.

    Returns:
        A message describing the result.
    """
    key = add[0].lower()
    value = add[1].lower() if isinstance(add[1], str) else add[1]

    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."

    settings[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"


def update_setting(settings: dict, update: tuple) -> str:
    """Update an existing setting.

    Args:
        settings: The settings dictionary to modify.
        update: A (key, value) pair with the new value.

    Returns:
        A message describing the result.
    """
    key = update[0].lower()
    value = update[1].lower() if isinstance(update[1], str) else update[1]

    if key in settings:
        settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"

    return f"Setting '{key}' does not exist! Cannot update a non-existing setting."


def delete_setting(settings: dict, key_del: str) -> str:
    """Delete a setting.

    Args:
        settings: The settings dictionary to modify.
        key_del: The key to delete.

    Returns:
        A message describing the result.
    """
    key = key_del.lower()

    if key in settings:
        del settings[key]
        return f"Setting '{key}' deleted successfully!"

    return "Setting not found!"


def view_settings(settings: dict) -> str:
    """Return a human-readable listing of all current settings."""
    if not settings:
        return "No settings available."

    lines = "".join(f"{key.capitalize()}: {value}\n" for key, value in settings.items())
    return f"Current User Settings:\n{lines}"


if __name__ == "__main__":
    # Small demo showing the functions in action.
    demo_settings: dict[str, Any] = {}
    print(add_setting(demo_settings, ("theme", "dark")))
    print(update_setting(demo_settings, ("theme", "light")))
    print(view_settings(demo_settings))
    print(delete_setting(demo_settings, "theme"))
