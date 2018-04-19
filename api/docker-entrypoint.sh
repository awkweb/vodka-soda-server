#!/bin/bash

# apply database migrations
python manage.py migrate

# generate staticfiles files
python manage.py collectstatic --clear --noinput
python manage.py collectstatic --noinput

# start uwsgi
uwsgi --ini uwsgi.ini
