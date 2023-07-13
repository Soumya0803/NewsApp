# Use the official Python base image
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy the Pipfile and Pipfile.lock to the container
COPY Pipfile Pipfile.lock /app/

# Install pipenv and project dependencies
RUN pip install pipenv && pipenv install --system --deploy

# Copy the Django project code to the container
COPY . /app/

# Expose the port the Django app will run on
EXPOSE 8000

# Set the working directory to the Django app folder
WORKDIR /app/newsaggregator

# Run Django development server
CMD bash -c "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"
