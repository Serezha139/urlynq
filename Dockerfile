# Use an official Python runtime as a base image
FROM python:3.11.7-slim

# Set the working directory in the docker container to /app
WORKDIR /app

# Copy the current directory contents into the docker container at /app
ADD . /app

RUN pip install --upgrade pip

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]