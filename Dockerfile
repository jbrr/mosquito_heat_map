FROM python:3.7.4

RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

COPY src/server /usr/src/app

ENV DATABASE_URL NOT_SET
ENV APP_SETTINGS NOT_SET
ENV FLASK_APP NOT_SET
ENV FLASK_ENV NOT_SET
ENV NODE_ENV NOT_SET
