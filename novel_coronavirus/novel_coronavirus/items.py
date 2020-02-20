# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import re
from datetime import datetime
from urllib import parse

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose

date_pattern = re.compile(r"^/JKZX/yq_(\d{8}).json$", re.IGNORECASE)


def filter_date(value):
    o = parse.urlparse(value)
    m = date_pattern.match(o.path)
    if m:
        # print(m.group(1))
        dt_string = m.group(1)
        dt = datetime.strptime(dt_string, "%Y%m%d")
        return dt.strftime("%Y-%m-%d")
    return ""


# def process_dt(value):
#     _dt = pendulum.from_format(value, "YYYY-MM-DD HH:mm:ss", tz="Asia/Shanghai")
#     return _dt.convert(_dt)


class NovelCoronaVirusLoader(ItemLoader):
    default_output_processor = TakeFirst()
    published_at_in = MapCompose(filter_date)


class NovelCoronaVirusItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    province = scrapy.Field()
    add_suspect = scrapy.Field()
    cumulative_suspect = scrapy.Field()
    new_diagnosis = scrapy.Field()
    cumulative_diagnosis = scrapy.Field()
    added_death = scrapy.Field()
    cumulative_death = scrapy.Field()
    published_at = scrapy.Field()


class FlashNewsLoader(ItemLoader):
    default_output_processor = TakeFirst()
    # releaseTime_in = MapCompose(process_dt)


class FlashNewsItem(scrapy.Item):
    crawlSource = scrapy.Field()
    majorClassification = scrapy.Field()
    metaInfoName = scrapy.Field()
    releaseTime = scrapy.Field()
    title = scrapy.Field()
    summary = scrapy.Field()
    pictrueUrl = scrapy.Field()
    webpageCode = scrapy.Field()
    webpageUrl = scrapy.Field()
    reportSource = scrapy.Field()
