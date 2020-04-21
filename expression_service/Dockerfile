FROM python:3.8.2-buster

RUN apt-get update && \
    apt-get install -y logrotate cron && \
    apt-get clean && \
    mkdir -p /usr/src/app

WORKDIR /usr/src/app

ADD . /usr/src/app

RUN python3 -m pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python", "server.py"]