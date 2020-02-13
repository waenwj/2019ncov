# -*- coding: utf-8 -*-
import json
from datetime import datetime, timedelta

import scrapy

from novel_coronavirus.items import NovelCoronaVirusItem, ProductLoader


class CoronaVirusSpider(scrapy.Spider):
    name = "coronavirus"
    allowed_domains = ["ncportal.esrichina.com.cn"]

    def start_requests(self):
        base = datetime.today()
        date_list = [base - timedelta(days=x) for x in range(15)]
        start_urls = []
        for row in date_list:
            dt_string = row.strftime("%Y%m%d")
            start_urls.append(
                f"https://ncportal.esrichina.com.cn/JKZX/yq_{dt_string}.json"
            )
        for url in start_urls:
            self.logger.info(url)
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        data = json.loads(response.text)
        for row in data.get("features", []):
            yield self.parse_data(row["properties"], response.url)

    def parse_data(self, data, crawl_url):
        item = ProductLoader(item=NovelCoronaVirusItem())
        item.add_value("name", data["name"])
        item.add_value("province", data["省份"])
        item.add_value("add_suspect", data["新增疑似"])
        item.add_value("cumulative_suspect", data["累计疑似"])
        item.add_value("new_diagnosis", data["新增确诊"])
        item.add_value("cumulative_diagnosis", data["累计确诊"])
        item.add_value("added_death", data["新增死亡"])
        item.add_value("cumulative_death", data["累计死亡"])
        item.add_value("published_at", crawl_url)
        return item.load_item()
