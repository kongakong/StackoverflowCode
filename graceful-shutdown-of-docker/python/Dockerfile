FROM debian:jessie
ADD app /app
RUN apt-get update --fix-missing
RUN apt-get install -y python
CMD ["python", "/app/main.py"] 

