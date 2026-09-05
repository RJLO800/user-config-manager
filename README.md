# User Configuration Manager

A small Python library for managing user settings (add / update / delete / view) as key-value pairs. Built as a practice project.

![License: MIT](https://img.shields.io/badge/License-MIT-green.svg) ![Python](https://img.shields.io/badge/python-3.10%2B-blue)

## Features

- Add, update, delete, and view settings stored in a dictionary
- Keys are normalized to lowercase; string values are normalized to lowercase
- Unit tests with pytest

## Usage

```python
from main import add_setting, update_setting, delete_setting, view_settings

settings = {}
add_setting(settings, ("theme", "dark"))
print(view_settings(settings))
# Current User Settings:
# Theme: dark
```

Run the built-in demo directly:

```bash
python main.py
```

## Tests

```bash
pip install -r requirements-dev.txt
pytest
```

## Roadmap

- Persist settings to a JSON file
- Command-line interface
- Input validation

## License

MIT — see [LICENSE](LICENSE).
