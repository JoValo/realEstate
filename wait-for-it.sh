#!/bin/bash
while ! nc -z postgres 5432; do sleep 3; done
python manage.py runserver 0.0.0.0:8000