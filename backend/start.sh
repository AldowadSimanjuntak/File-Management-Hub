#!/bin/sh

# Ensure data directory exists and has proper permissions
mkdir -p /app/data
chmod -R 777 /app/data

# Run migrations
echo "Running migrations..."
python manage.py makemigrations
python manage.py migrate

# Start server
echo "Starting server..."
gunicorn --bind 0.0.0.0:8000 core.wsgi:application 