# -*- coding: utf-8 -*-
import scrapy
import json


class MinibizhiSpider(scrapy.Spider):
    name = 'minibizhi'
    allowed_domains = ['minibizhi.313515.com']
    start_urls = []
    page = 1

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.headers = {
            'deviceInfo': 'CH=1&Height=896&Lang=zh_CN&Model=iPhone%20XS%20Max%20China-exclusive%3CiPhone11%2C6%3E&Net'
                          '=unknown&PID=100&PixelRatio=3&SignatureStamp=1546858282272&Ver=5&Version=7.0.1&Width=414'
                          '&SignatureMD5=61351528ab225c486ae799cc1529c594'
        }

        fo = open("renwu-urls.txt", "r")

        while 1:
            line = fo.readline()
            self.start_urls.append(line.strip())

            if not line:
                break
            pass  # do something

        print(self.start_urls)
        fo.close()

    def start_requests(self):
        for url in self.start_urls:
            if url:
                yield scrapy.Request(
                    url=url,
                    headers=self.headers,
                    callback=self.parse_item
                )

    def parse_item(self, response):
        obj = json.loads(response.body_as_unicode().replace("'", '"'))
        # 打开一个文件
        fo = open("renwu-pictures.txt", "a+")

        for i in obj['Data']['DataList']:
            print(i['Image'] + '\n')
            fo.write(i['Image'] + '\n')

        fo.close()
