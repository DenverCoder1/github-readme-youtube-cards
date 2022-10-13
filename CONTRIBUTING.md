## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request if you have a way to improve this project.

Make sure your request is meaningful and you have tested the app locally before submitting a pull request.

### Installing dependencies

```bash
# Dependencies for running the Flask server
poetry install
# Dependencies for testing and development
poetry install --with dev
# Dependencies for running the action script
pip install feedparser
```

### Running the Flask server

```bash
gunicorn api.index:app
```

### Running the action Python part of the workflow locally

```bash
python action.py --channel=UCipSxT7a3rn81vGLw9lqRkg --comment-tag-name="EXAMPLE-YOUTUBE-CARDS"
```

Any additional arguments can be passed to the script. Run `python action.py -h` to see the full list of arguments.

### Running tests

```bash
tox
```