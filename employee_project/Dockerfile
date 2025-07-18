# Use official Python image
FROM python:3.10-slim

# Set work directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn

# Copy project code
COPY . .

# Collect static files (optional if needed)
RUN python manage.py collectstatic --noinput

# Run migrations automatically (optional but helpful)
CMD ["sh", "-c", "python manage.py migrate && gunicorn employee_project.wsgi:application --bind 0.0.0.0:8000"]
