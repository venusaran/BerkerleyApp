FROM python:3.6

ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /berkeley_app

# Set the working directory to /music_service
WORKDIR /berkeley_app

# Copy the current directory contents into the container at /music_service
ADD . /berkeley_app/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt