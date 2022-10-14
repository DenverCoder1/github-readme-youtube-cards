## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request if you have a way to improve this project.

Make sure your request is meaningful and you have tested the app locally before submitting a pull request.

### Installing dependencies

```bash
# Dependencies for running the Flask server
pip install -r requirements.txt
# Dependencies for testing and development
pip install -r requirements-dev.txt
# Dependencies for running the action script
pip install -r requirements-action.txt
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

## Contributing translations

You can contribute to GitHub Readme YouTube Cards by adding translations in the `api/locale` folder.

To add translations for a new language:

- Copy the contents of `api/locale/en.yml` file to `api/locale/<IDENTIFIER>.yml`, where IDENTIFIER is shorthand for the language you are adding translations for.
- Change the top most yaml key `en:` to `<IDENTIFIER>:`.
- Add translations for the strings provided below in the file. Only alter the text enclosed in quotes.
- To test, run the project locally and add `&lang=IDENTIFIER` to a card URL to test if translation works as expected.
