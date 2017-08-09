FROM debian:jessie
ADD app /app
RUN apt-get update --fix-missing
RUN apt-get install -y golang
CMD ["go", "run", "/app/main.go"] # this is the exec syntax as opposed to `CMD /app`

