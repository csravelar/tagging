FROM python:3.8.7-slim-buster

COPY . /

RUN apt-get update && \
    pip install -r requirements.txt

ENTRYPOINT ["/entrypoint.sh"]
