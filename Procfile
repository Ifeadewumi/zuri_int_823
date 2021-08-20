web: gunicorn resume.wsgi:myapp --log-file - --log-level debug
python manage.py collectstatic --noinput
manage.py migrate