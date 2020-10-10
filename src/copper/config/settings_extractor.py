import os

from yaml import safe_load

SETTINGS_PATH = f"{os.getcwd()}/settings.yml"


def settings_parser():
    """Parser of settings file.

      Raises:
      -------
      FileNotFoundError
          Settings file not found.

      Returns:
      -------
      parsed_file
          A dictionary containing the keys of settings file
    """
    parsed_file = {}
    try:
        with open(SETTINGS_PATH, "r") as settings:
            parsed_file = safe_load(settings)
        return parsed_file
    except FileNotFoundError:
        print("settings.yml not found!")
