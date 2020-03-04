FROM python:3
LABEL maintainer="jovalo"
LABEL project="realState"

#Set 1 to receiving timely log messages
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .
