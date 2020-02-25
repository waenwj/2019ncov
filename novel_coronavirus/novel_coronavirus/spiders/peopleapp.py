import json
import scrapy
from pprint import pprint

from novel_coronavirus.items import FlashNewsLoader, FlashNewsItem


class PeopleAPPSpider(scrapy.Spider):
    name = "peopleapp"
    allowed_domains = ["h5-api.tikrnews.com"]
    start_urls = ["https://h5-api.tikrnews.com/h5/province"]
    headers = {
        "accept": "application/json",
        "content-type": "application/json;charset=UTF-8",
        "origin": "https://h5.peopleapp.com"
    }

    def start_requests(self):
        data = {
            "type": "rapidReport",
            "lastTimestamp": None,
            "current": 1,
            "size": 10,
            "province": "",
            "city": ""
        }

        for url in self.start_urls:
            yield scrapy.Request(url, body=json.dumps(data),
                                 headers=self.headers,
                                 method="POST", callback=self.parse)

    def parse(self, response):
        # self.logger.info(response.text)
        _data = json.loads(response.text)
        # print(_data["data"]["records"])
        for row in _data["data"]["records"]:
            # pprint(row, indent=2)
            yield self.parse_data(data=row)

    def parse_data(self, data: dict):
        self.logger.debug(data)
        item = FlashNewsLoader(item=FlashNewsItem())
        item.add_value("crawlSource", data["crawlSource"])
        item.add_value("majorClassification", data["majorClassification"])
        item.add_value("metaInfoName", data["metaInfoName"])
        item.add_value("releaseTime", data["releaseTime"])
        item.add_value("summary", data.get("summary"))
        item.add_value("title", data["title"])
        item.add_value("pictrueUrl", data.get("pictrueUrl"))
        item.add_value("webpageCode", data["webpageCode"])
        item.add_value("webpageUrl", data.get("webpageUrl"))
        item.add_value("reportSource", data.get("reportSource"))
        # self.logger.info(item.load_item())
        return item.load_item()
