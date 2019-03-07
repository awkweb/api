#!/bin/bash

# apply database migrations
python manage.py migrate

uwsgi --ini uwsgi.ini
