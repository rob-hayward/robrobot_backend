# Use the slim version of the Python 3.9 image as the base image
FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /app

# Install curl
RUN apt-get update && apt-get install -y curl

# Copy requirements.txt to the working directory
COPY requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the working directory
COPY . .

# Set the DJANGO_SETTINGS_MODULE environment variable
ENV DJANGO_SETTINGS_MODULE=robrobot_backend.production

# Expose the port on which the Django app will run
EXPOSE 8000

# Run the Django production server
CMD ["gunicorn", "robrobot_backend.wsgi:application", "--bind", "0.0.0.0:8000"]
