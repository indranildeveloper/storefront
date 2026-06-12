FROM python:3.14

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update \
    && apt-get install python3-dev libpq-dev gcc -y

RUN pip install --upgrade pip
RUN pip install pipenv


COPY Pipfile Pipfile.lock /app/

RUN pipenv install --system --dev

COPY . /app/

RUN chmod +x /app/wait-for-it.sh \
    && chmod +x /app/docker-entrypoint.sh

EXPOSE 8000