#!/usr/bin/env python
import os
import sys

def main():
    """
    Main entry point for Django's command-line utility.
    Sets up environment and runs the Django management command.
    """
    # Set default settings module
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_web_app.settings')

    try:
        # Import Django's command-line utility
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Helpful error message for missing Django installation
        raise ImportError(
            "Couldn't import Django. Make sure it's installed and "
            "available on your PYTHONPATH. "
            "Did you forget to activate your virtual environment?"
        ) from exc

    # Execute the command (e.g. runserver, migrate, etc.)
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
