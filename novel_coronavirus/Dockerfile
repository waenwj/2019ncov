FROM python:3.7.5
MAINTAINER jiaxin<edison7500@gmail.com>
RUN apt -y update && apt -y install supervisor
RUN cd /opt
RUN git clone -b master https://github.com/edison7500/2019ncov.git

RUN cd /opt/2019ncov/novel_coronavirus
RUN pip install --upgrade pip -i https://pypi.douban.com/simple
RUN pip install -r ../requirements/base.txt -i https://pypi.douban.com/simple

WORKDIR /opt/2019ncov/novel_coronavirus

EXPOSE 6800
