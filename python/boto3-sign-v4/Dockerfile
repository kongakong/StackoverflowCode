FROM ubuntu:18.04

RUN apt-get update --fix-missing
RUN apt-get install -y vim python python-pip

RUN mkdir scripts
COPY scripts/requirements.txt scripts
RUN pip install -r scripts/requirements.txt 

ADD scripts /scripts

