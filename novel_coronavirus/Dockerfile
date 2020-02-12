FROM python:3.7.5
MAINTAINER jiaxin<edison7500@gmail.com>
RUN apt -y update && apt -y install supervisor
RUN cd /opt
RUN git clone -b master https://github.com/edison7500/2019ncov.git

WORKDIR /opt/2019ncov/novel_coronavirus
RUN pip install -r ../requirements/base.txt -i https://pypi.douban.com/simple


EXPOSE 6800
<!--COPY services/scrapyd.conf /etc/scrapyd/scrapyd.conf-->
<!--COPY services/spider.conf /etc/supervisor/conf.d/-->
<!--CMD  ["/usr/bin/supervisord"]-->
<!---->
