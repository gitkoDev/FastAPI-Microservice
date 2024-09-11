FROM python:3.12

ENV PYTHONDONTWRITEBYCODE = 1
ENV PYTHONUUNBUFFERED = 1

WORKDIR /app

COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/
