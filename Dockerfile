FROM python:3
LABEL maintainer="jovalo"
LABEL project="realState"

#Set 1 to receiving timely log messages
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y \
    netcat

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .
