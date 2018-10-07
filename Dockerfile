FROM python:2.7.15

MAINTAINER raoul1996

RUN apt-get clean

RUN apt-get update && \
    apt-get upgrade -y && \
    rm -rf /var/lib/apt/list/*
COPY requirements.txt /code/
COPY . /code/

RUN pip install -r /code/requirements.txt -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com
