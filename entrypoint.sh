#!/bin/bash


set -e

python manage.py makemigrations
python manage.py migrate


echo "
from django.contrib.auth import get_user_model
User = get_user_model()

email = '$DJANGO_SUPERUSER_EMAIL'
username = '$DJANGO_SUPERUSER_USERNAME'
first_name = '$DJANGO_SUPERUSER_FIRST_NAME'
last_name = '$DJANGO_SUPERUSER_LAST_NAME'
password = '$DJANGO_SUPERUSER_PASSWORD'

if not User.objects.filter(email=email).exists():
    User.objects.create_superuser(
        email=email,
        username=username,
        first_name=first_name,
        last_name=last_name,
        password=password
    )
" | python manage.py shell


python manage.py runserver 0.0.0.0:8000
