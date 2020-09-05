FROM python:3.7-alpine
MAINTAINER Ampas Developer ID ~ @faisnasrullah

ENV PYTHONUNBEFFERD 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D ampasdev
USER ampasdev