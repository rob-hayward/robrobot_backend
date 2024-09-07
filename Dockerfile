FROM python:3.9-slim-buster

WORKDIR /app

RUN apt-get update && apt-get install -y curl

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Create directories for static and media files
RUN mkdir -p /app/staticfiles /app/media

COPY . .

# Set the DJANGO_SETTINGS_MODULE environment variable
ENV DJANGO_SETTINGS_MODULE=robrobot_backend.settings

# Collect static files
RUN python manage.py collectstatic --noinput

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=10s --retries=3 CMD curl -f http://localhost:8000/health/ || exit 1

CMD ["gunicorn", "robrobot_backend.wsgi:application", "--bind", "0.0.0.0:8000"]