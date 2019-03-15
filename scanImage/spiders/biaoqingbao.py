# -*- coding: utf-8 -*-
import scrapy
import json
dir_path = './sougoubqb/'

class BiaoqingbaoSpider(scrapy.Spider):
    name = 'biaoqingbao'
    allowed_domains = ['pic.sogou.com']
    start_urls = []
    page = 1

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.headers = {
            'deviceInfo': 'CH=1&Height=896&Lang=zh_CN&Model=iPhone%20XS%20Max%20China-exclusive%3CiPhone11%2C6%3E&Net'
                          '=unknown&PID=100&PixelRatio=3&SignatureStamp=1546858282272&Ver=5&Version=7.0.1&Width=414'
                          '&SignatureMD5=61351528ab225c486ae799cc1529c594'
        }
        for i in range(29, 5495):
            self.start_urls.append(
                'https://pic.sogou.com/pic/emo/groupDetail.jsp?id=' + str(i) + '&from=emo_classify_pic'
            )

    def start_requests(self):
        for url in self.start_urls:
            if url:
                yield scrapy.Request(
                    url=url,
                    headers=self.headers,
                    callback=self.parse_item
                )

    def parse_item(self, response):
        title = response.xpath("//*[contains(@class, 'info-name')]/text()").extract_first()
        urls = response.xpath('//ul[@id="groupEmojiListUl"]/li/a/img').xpath("@rsrc").extract()

        file_path = dir_path + title

        if title:
            fo = open(file_path, 'w+')
            for url in urls:
                fo.write(url + '\n')

            print(title + '')
