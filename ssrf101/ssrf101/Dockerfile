# For building
FROM python:3.8-buster as builder

WORKDIR /opt/app

COPY requirements.txt /opt/app
RUN pip3 install -r requirements.txt --no-cache-dir

# For executing
FROM python:3.8-slim-buster as runner

COPY --from=builder /usr/local/lib/python3.8/site-packages /usr/local/lib/python3.8/site-packages
COPY --from=builder /usr/local/bin/uwsgi /usr/local/bin/uwsgi

RUN apt update \
    && apt install -y libpq5 libxml2 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY deploy/uwsgi.ini /opt/app/uwsgi.ini
COPY src /opt/app
COPY this_is_secret.txt /this_is_secret.txt

RUN useradd -r -s /bin/false uwsgiusr
USER uwsgiusr

EXPOSE 8000
ENTRYPOINT ["uwsgi", "--ini", "/opt/app/uwsgi.ini"]
