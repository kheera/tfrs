#!/bin/bash

python manage.py makemigrations
python manage.py migrate

python manage.py syncdb --noinput

# create superuser
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'pass')" | python manage.py shell

# this method of loading data is depcrecated, but will do for now 
python manage.py loaddata tfrs/fixtures/initial_data.json

python manage.py runserver 0.0.0.0:9000

#exec $@
