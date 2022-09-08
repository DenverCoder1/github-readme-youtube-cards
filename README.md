# GitHub Readme YouTube Cards

Workflow for displaying recent YouTube videos as SVG cards in your readme

## Live Example

<!-- BEGIN YOUTUBE-CARDS -->
<!-- END YOUTUBE-CARDS -->

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