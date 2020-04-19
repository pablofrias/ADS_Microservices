FROM python:3.8.2-buster

RUN apt-get update && \
    apt-get install -y --no-install-recommends logrotate cron && \
    apt-get clean && \
    mkdir -p /usr/src/app && \
    mkdir -p /usr/src/app/logs && \
    mkdir -p /usr/src/app/data

WORKDIR /usr/src/app

ADD requirements.txt requirements.txt

RUN python3 -m pip install -r requirements.txt

ADD . /usr/src/app/

EXPOSE 5000

ENTRYPOINT ["python", "server.py"]
