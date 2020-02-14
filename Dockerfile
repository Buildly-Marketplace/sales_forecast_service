FROM python:3.7-slim

LABEL mantainer="hugoperlin"

ADD . /opt/app

ADD start.sh /

RUN chmod +x /start.sh

WORKDIR /opt/app

RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD ["/start.sh"] 