import requests
import json

from scrapy.exceptions import DropItem


class JsonWriterPipeline(object):
    def open_spider(self, spider):
        self.file = open("items.jl", "w")

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item


class CheckCrawlSourcePipeline(object):
    def process_item(self, item, spider):
        if spider.name in ["peopleapp"]:
            if item["crawlSource"] not in ["央视新闻客户端", "新华网", "人民网"]:
                raise DropItem(f"{item['crawlSource']} source not in crawl list ")
        return item


class DuplicatesPipeline(object):
    def process_item(self, item, spider):
        if spider.name in ["peopleapp"]:
            webpageCode = item.get("webpageCode")
            res = requests.head(f"http://127.0.0.1:8000/api/news/{webpageCode}/")
            if res.status_code == 200:
                raise DropItem("Duplicate item found: %s" % item)
        return item


class PostPipeline(object):
    def process_item(self, item, spider):
        if spider.name == "coronavirus":
            req = requests.post(
                "http://127.0.0.1:8000/api/epidemic/", json=dict(item)
            )
            if req.status_code == 201:
                spider.logger.info("post ok")
            else:
                spider.logger.error(req.text)

        elif spider.name == "peopleapp":
            req = requests.post(
                "http://127.0.0.1:8000/api/news/", json=dict(item)
            )
            if req.status_code == 201:
                spider.logger.info("post ok")
            else:
                spider.logger.error(req.text)
        return item
