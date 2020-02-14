FROM python:3.7.5
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=ncov.settings.dev
COPY conf/sources.list /etc/apt/sources.list
COPY conf/gunicorn /etc/default/gunicorn
COPY cron/spider /etc/cron.d/spider-cron
RUN apt-get -y update && apt-get -y install supervisor cron
RUN git clone -b master https://github.com/edison7500/2019ncov.git /opt/2019ncov
RUN pip install --upgrade pip -i https://pypi.douban.com/simple
RUN pip install -r /opt/2019ncov/requirements/prod.txt -i https://pypi.douban.com/simple
WORKDIR /opt/2019ncov/ncov
RUN mv env.example .env
RUN python manage.py migrate 
EXPOSE 8000
COPY conf/supervisor.conf /etc/supervisor/conf.d/2019ncov.conf
CMD  ["/usr/bin/supervisord"]
