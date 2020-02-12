FROM python:3.7.5
MAINTAINER jiaxin<edison7500@gmail.com>
RUN apt -y update && apt -y install supervisor
RUN git clone -b master https://github.com/edison7500/2019ncov.git /opt/2019ncov
RUN pip install --upgrade pip -i https://pypi.douban.com/simple
RUN pip install -r /opt/2019ncov/requirements/base.txt -i https://pypi.douban.com/simple

WORKDIR /opt/2019ncov/novel_coronavirus

EXPOSE 6800

RUN mkdir -p /etc/scrapyd/
RUN ln -s  /opt/2019ncov/novel_coronavirus/conf/scrapyd.conf /etc/scrapyd/scrapyd.conf
RUN ln -s /opt/2019ncov/novel_coronavirus/conf/spider.conf /etc/supervisor/conf.d/spider.conf
CMD  ["/usr/bin/supervisord"]
