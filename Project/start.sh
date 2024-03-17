#!/bin/sh

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser --noinput

python manage.py runserver 172.20.2.13:8000