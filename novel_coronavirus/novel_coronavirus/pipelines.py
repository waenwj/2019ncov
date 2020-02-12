import requests
import json


class JsonWriterPipeline(object):
    def open_spider(self, spider):
        self.file = open("items.jl", "w")

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item


class PostPipeline(object):
    def process_item(self, item, spider):
        req = requests.post(
            "http://127.0.0.1:8000/api/epidemic/", json=dict(item)
        )
        if req.status_code == 201:
            spider.logger.info("post ok")
        else:
            spider.logger.error(req.text)

        return item
