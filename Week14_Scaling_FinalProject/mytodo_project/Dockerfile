# Dockerfile
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Install system dependencies for PostgreSQL
RUN apt-get update && apt-get install -y gcc libpq-dev

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Run ASGI server (can switch to gunicorn + daphne for prod)
CMD ["daphne", "-b", "0.0.0.0", "-p", "8000", "mytodo_project.asgi:application"]
