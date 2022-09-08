# GitHub Readme YouTube Cards

Workflow for displaying recent YouTube videos as SVG cards in your readme

## Live Example

<!-- YOUTUBE-CARDS:START -->
<!-- YOUTUBE-CARDS:END -->

## Contributing

Installing dependencies:

```bash
# Dependencies for running the Flask server
poetry install --with web

# Dependencies for running the action script
poetry install --with action

# Dependencies for development
poetry install --with dev
```

Running the Flask server

```bash
gunicorn web.app:app
```

Running tests

```bash
tox
```