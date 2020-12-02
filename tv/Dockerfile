FROM python:3-alpine
RUN apk add rrdtool
RUN apk add --virtual .build-dependencies \ 
            --no-cache \
            python3-dev \
            build-base \
            linux-headers \
            pcre-dev

RUN apk add --no-cache pcre
WORKDIR /tv
COPY . /tv
RUN pip install -r /tv/requirements.txt
RUN pip install uwsgi
RUN apk del .build-dependencies && rm -rf /var/cache/apk/*
EXPOSE 5002
CMD ["uwsgi", "--ini", "/tv/wsgi.ini"]