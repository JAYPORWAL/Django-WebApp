# Use official Python image from the Docker registry
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the entire Django project directory into the container
COPY . /app/

# Expose the port for the Django app (default is 8000)
EXPOSE 8000

# Run Django using the manage.py command when the container starts
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
