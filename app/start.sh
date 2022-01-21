#!/bin/bash
# Run migrations
echo "Migrating the database before starting the server"
python manage.py makemigrations
python manage.py migrate
python manage.py importpostalcodesmx
# Start Gunicorn
echo "Starting Gunicorn."
exec gunicorn codigosPostalesMx.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 3