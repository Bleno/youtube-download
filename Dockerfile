FROM python

MAINTAINER Bleno <blenobok@gmail.com>

RUN apt-get update \
    && apt-get upgrade -y



RUN apt-get install libav-tools -y
RUN cd /srv/ && git clone https://github.com/Bleno/youtube-download.git \
    && cd youtube-download && pip install -r requirements.txt \
    && python setup.py install

EXPOSE 6543

CMD pserve /srv/youtube-download/production.ini