FROM python:3.11-slim

COPY . /
WORKDIR /

RUN apt-get clean \
        && apt-get -y update

RUN apt-get install -y --no-install-recommends \
        && apt-get -y install nginx \
        && apt-get -y install build-essential

RUN pip install -r requirements.txt --src /usr/local/src

COPY nginx.conf /etc/nginx
RUN chmod +x ./start.sh
CMD ["./start.sh"]





