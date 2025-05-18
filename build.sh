#!/usr/bin/env bash
# exit on error
set -o errexit

python manage.py collectstatic --noinput
python manage.py migrate

gunicorn mocha.wsgi:application --bind 0.0.0.0:8000 --workers 3
