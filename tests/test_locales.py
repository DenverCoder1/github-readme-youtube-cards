import os

import yaml
from babel import Locale, UnknownLocaleError


def test_locales_valid():
    """Test that all locales are valid"""

    # get the list of locales
    files = os.listdir(os.path.join("api", "locale"))

    # assert that all locales are valid yaml files
    assert all(file.endswith(".yml") for file in files)

    # assert that all locales contain valid yaml
    for file in files:
        with open(os.path.join("api", "locale", file), "r") as f:
            contents = f.readlines()
            locale = file.split(".")[0]
            assert contents[0].strip() == f"{locale}:"
            assert yaml.safe_load("".join(contents)) is not None

    # assert that all locales are valid babel locales
    locales = [file.split(".yml")[0] for file in files]
    for locale in locales:
        try:
            Locale.parse(locale)
        except UnknownLocaleError:
            assert False, f"{locale} is not a valid locale"
