FROM python:3.7.5
MAINTAINER jiaxin<edison7500@gmail.com>
RUN apt -y update && apt -y install supervisor
ADD requirements /tmp/
RUN pip install -r /tmp/prod.txt -i https://pypi.douban.com/simple


ADD . /opt/shangguanspider/
WORKDIR /opt/shangguanspider/
EXPOSE 6800

RUN mkdir /etc/scrapyd/
COPY services/scrapyd.conf /etc/scrapyd/scrapyd.conf
COPY services/spider.conf /etc/supervisor/conf.d/
CMD  ["/usr/bin/supervisord"]
