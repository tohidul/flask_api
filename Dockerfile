FROM ubuntu:18.04

RUN apt-get update -y && apt-get install -y \
    python3 \
    python3-pip

WORKDIR /app

COPY requirements.txt /app/

RUN pip3 install -r requirements.txt

EXPOSE 5000

COPY ./ /app
ENTRYPOINT [ "python3", "main.py" ]