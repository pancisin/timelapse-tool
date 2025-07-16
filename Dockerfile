FROM python:latest
LABEL authors="panci"

ENTRYPOINT ["top", "-b"]