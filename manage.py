#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""

import os
import pathlib
import sys

from dotenv import load_dotenv


def main():
    """Run administrative tasks."""
    DOT_ENV_PATH = pathlib.Path() / ".env"
    if DOT_ENV_PATH.exists():
        load_dotenv(dotenv_path=str(DOT_ENV_PATH))
    else:
        print("No .env file found, please add a .env file.")
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "storefront.settings.dev")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
