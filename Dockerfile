FROM python:3.11.8-slim

WORKDIR /app

ADD djangogramm /app/

RUN apt-get update && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
RUN pip install -r requirements.txt --no-cache-dir

EXPOSE 8000

CMD gunicorn djangogramm.wsgi:application --bind 0.0.0.0:8000 --log-level info

#CMD sleep 5 \
#    && python manage.py migrate  \
#    && python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='root').exists() or User.objects.create_superuser('root', 'root@example.com', 'root')" \
#    && python manage.py create_fake_fill_db  \
#    && python manage.py collectstatic --no-input \
#    && gunicorn djangogramm.wsgi:application --bind 0.0.0.0:8000 --log-level info
