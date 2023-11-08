FROM --platform=linux/amd64 python:3.11.6-alpine3.18
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT [ "python" ]
CMD ["./app/echo_server.py" ]