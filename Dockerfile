FROM python:3.6.13

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

ENV TZ Asia/Tokyo

ENV CONDUIT_SECRET 'something-really-secret'
ENV FLASK_APP '/app/autoapp.py'
ENV FLASK_DEBUG 1

RUN apt-get update
RUN apt-get install -y vim && \
  apt-get install -y curl

# Make working directory.
RUN mkdir /app
WORKDIR /app
RUN mkdir requirements

COPY ./requirements.txt /app
COPY ./requirements /app/requirements

# Install python packages.
RUN pip install -r requirements.txt
