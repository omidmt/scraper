FROM python:3.8

ADD ps5 /app/ps5
ADD scraper /app/scraper
COPY requirements.txt run.sh /app/

WORKDIR /app

RUN pip3 --disable-pip-version-check --no-cache-dir install -r requirements.txt

CMD ["/bin/sh", "-c", "./run.sh"]