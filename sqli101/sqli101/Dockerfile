# For building
FROM python:3.8-buster as builder

WORKDIR /opt/app

COPY requirements.txt /opt/app
# for mysqlclient installation
RUN apt update \
    && apt install -y python3-dev default-libmysqlclient-dev build-essential
RUN pip3 install -r requirements.txt --no-cache-dir

# For executing
FROM python:3.8-slim-buster as runner

COPY --from=builder /usr/local/lib/python3.8/site-packages /usr/local/lib/python3.8/site-packages
COPY --from=builder /usr/local/bin/uwsgi /usr/local/bin/uwsgi

RUN apt update \
    && apt install -y libpq5 libxml2 \
    && apt install -y python3-dev default-libmysqlclient-dev build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY deploy/uwsgi.ini /opt/app/uwsgi.ini
COPY src /opt/app
COPY flag.txt /opt/app/flag.txt

RUN useradd -r -s /bin/false uwsgiusr
USER uwsgiusr

EXPOSE 8000
ENTRYPOINT ["uwsgi", "--ini", "/opt/app/uwsgi.ini"]
