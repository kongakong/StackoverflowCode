FROM debian:jessie
ADD app /app
RUN apt-get update --fix-missing
RUN apt-get install -y golang
RUN go build -o app/main.exe app/main.go
CMD ["/app/main.exe"] 

