# Just to ensure the linux distro makes no difference
# FROM debian:jessie
FROM ubuntu:16.04
ADD app /app
RUN apt-get update --fix-missing
RUN apt-get install -y python
CMD ["python", "/app/main.py"] 

