FROM python:3.8-slim

ENV PYTHONUNBUFFERED 1

# Expose our application port
EXPOSE 8000
# Install system requirements
RUN apt-get update -qqy && apt-get upgrade -qqy && apt-get install -y postgresql-client-11

RUN mkdir app

COPY . /app

WORKDIR /app

RUN pip install --upgrade pip pipenv

RUN pipenv install --skip-lock --system
