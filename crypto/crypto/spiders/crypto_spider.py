# -*- coding: utf-8 -*-
import scrapy
import datetime
import re

class CryptoSpider(scrapy.Spider):
    name = 'crypto'
    start_urls = ['https://coinmarketcap.com']
    currency_pattern = re.compile("^/currencies/[^/]+/$")
    visited = {}

    def parse(self, response):
        links = response.xpath('//a[@class="cmc-link"]/@href').extract()
        for link in links:
            if self.currency_pattern.match(link):
                # base url plus currency url
                absolute_url = self.start_urls[0] + link
                if absolute_url not in self.visited:
                    self.visited[absolute_url] = True
                    yield response.follow(absolute_url, self.goToHistory)

    def goToHistory(self, response):
        # we always need the 5th element
        li = response.xpath('//ul[@class="cmc-tabs__header"]/li')[4]
        startDate = "20190101"
        endDate = datetime.date.today().strftime("%Y%m%d")
        dateParam = "?start=" + startDate + "&end=" + endDate
        # only need first result
        linkHis = self.start_urls[0] + li.xpath('a/@href')[0].extract() + dateParam
        yield response.follow(linkHis, callback=self.getData)

    def getData(self, response):
        rows = response.xpath('//tbody/tr')
        for row in rows:
            items = row.xpath("td/div/text()")
            coin = {}
            coin['Name'] = response.xpath('//h1/text()').extract()
            coin['Date'] = items[0].extract()
            coin['Market_Cap'] = items[6].extract()
            yield coin
