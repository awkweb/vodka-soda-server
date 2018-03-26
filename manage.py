#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
  settings = "server.settings.dev" if os.environ['DJ_DB_HOST'] == 'localhost' else "server.settings.prod"
  os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings)
  try:
    from django.core.management import execute_from_command_line
  except ImportError as exc:
    raise ImportError(
      "Couldn't import Django. Are you sure it's installed and "
      "available on your PYTHONPATH environment variable? Did you "
      "forget to activate a virtual environment?"
    ) from exc
  execute_from_command_line(sys.argv)
