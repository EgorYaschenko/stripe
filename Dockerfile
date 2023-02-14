FROM python:3
ENV PYTHONUNBUFFERED 1
WORKDIR /app
ADD ./app
RUN pip install -r requirements.txt

Docker Compose version v2.15.1