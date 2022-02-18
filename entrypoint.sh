#!/usr/bin/env sh

python manage.py migrate --no-input
python manage.py collectstatic --no-input
#gunicorn -c config/gunicorn/dev.py
gunicorn scape.wsgi:application --bind 0.0.0.0:8000