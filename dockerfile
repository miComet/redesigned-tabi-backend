FROM python:3.9.10-bullseye
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y apt-utils && \
    apt-get install -y tmux git vim

RUN pip3 install --upgrade pip setuptools

ADD requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

ENV LANG C.UTF-8
ENV LC_ALL=C.UTF-8

WORKDIR /project

CMD uvicorn --host='0.0.0.0' main:app
