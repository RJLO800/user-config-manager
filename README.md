# User Configuration Manager
Simple Python library + CLI for managing user settings (create/read/update/delete). Designed as a learning project and portfolio piece.

Badges:
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg) ![Python package](https://img.shields.io/badge/python-3.10%2B-blue)
Demo

(Insert a short GIF or screenshot here showing the CLI or example UI)
Features

    Add / update / delete / list user settings
    Normalize keys/values (lowercase)
    Persist to JSON (optional YAML)
    CLI interface and importable library
    Unit tests (pytest)

Quick start

Install (local dev)
bash

# optional: create a virtual environment
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate     # Windows

pip install -r requirements.txt

Usage (library)
Python

from userconfig.manager import add_setting, get_settings

settings = {}
add_setting(settings, ("Theme", "Dark"))
print(get_settings(settings))  # {'theme': 'dark'}

Usage (CLI)
bash

# after development install or via entrypoint:
userconfig add "theme" "dark"
userconfig list

Config file example (config.json)
JSON

{
  "theme": "dark",
  "language": "en",
  "notifications": true
}

Tests

Run tests with pytest:
bash

pytest

Roadmap / Stretch goals

    YAML support
    Encrypted storage option
    REST API (FastAPI demo)
    More validation (pydantic)

Contributing

See CONTRIBUTING.md for how to run tests and submit PRs.
License

This project is licensed under the MIT License — see the LICENSE file for details.
