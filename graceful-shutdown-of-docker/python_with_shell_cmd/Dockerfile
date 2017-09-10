FROM ubuntu:16.04

RUN apt-get update --fix-missing && apt-get install -y \
  git \
  python \
  python-pip \
  ntp \
  curl vim screen lsof

RUN mkdir -p /app

COPY ./app /app

CMD ["/app/start-app.sh"]
