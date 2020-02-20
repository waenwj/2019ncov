# -*- coding: utf-8 -*-
import json
import scrapy
import requests


class TikrNewsSpider(scrapy.Spider):
    name = "tikrnews"
    allowed_domains = ["h5-api.tikrnews.com"]
    start_urls = [
        "https://h5-api.tikrnews.com/h5/province/epidemicdata/cityaccumulativecount"
    ]
    headers = {
        "accept": "application/json",
        "content-type": "application/json;charset=UTF-8",
        "origin": "https://h5.peopleapp.com",
    }
    data = {"province": ""}

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(
                url,
                body=json.dumps(self.data),
                headers=self.headers,
                method="POST",
                callback=self.parse,
            )

    def parse(self, response):
        data = json.loads(response.text)
        epidemicdata = data["data"]["records"]
        res = requests.post(
            "http://127.0.0.1:8000/api/peopleapp/epidemic/",
            json={"epidemics": epidemicdata},
        )
        if res.status_code == 201:
            self.logger.info("post ok")
        else:
            self.logger.error(res.json())
