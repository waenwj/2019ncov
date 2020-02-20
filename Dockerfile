FROM python:3.7.5
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=ncov.settings.prod
COPY docker/conf/sources.list /etc/apt/sources.list
RUN apt-get -y update && apt-get -y install supervisor cron
RUN apt-get -y autoremove 
COPY docker/conf/gunicorn /etc/default/gunicorn
ADD docker/cron/spider /etc/cron.d/spider-cron
ADD . /opt/2019ncov
RUN pip install --upgrade pip -i https://pypi.douban.com/simple
RUN pip install -r /opt/2019ncov/requirements/prod.txt -i https://pypi.douban.com/simple
RUN crontab /etc/cron.d/spider-cron
WORKDIR /opt/2019ncov/ncov
RUN mv env.example .env
EXPOSE 8000
COPY docker/conf/supervisor.conf /etc/supervisor/conf.d/2019ncov.conf
CMD  ["/usr/bin/supervisord"]
