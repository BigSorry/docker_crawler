# -*- coding: utf-8 -*-
import scrapy
import datetime

class CryptoSpider(scrapy.Spider):
    name = 'crypto'
    start_urls = ['https://coinmarketcap.com/']

    def parse(self, response):
        links = response.xpath('//a[@class="currency-name-container link-secondary"]')
        for link in links:
            yield response.follow(link, self.goToHistory)

    def goToHistory(self, response):
        # we always need the 5th element
        li = response.xpath('//ul[@class="nav nav-tabs text-left"]/li')[4]
        startDate = self.term.strftime("%Y%m%d")
        endDate = datetime.date.today().strftime("%Y%m%d")
        dateParam = "?start=" + startDate + "&end=" + endDate
        # only need first result
        linkHis = li.xpath('a/@href')[0].extract() + dateParam
        yield response.follow(linkHis, callback=self.getData)

    def getData(self, response):
        rows = response.xpath('//tbody/tr')
        for row in rows:
            items = row.xpath("td/text()")
            coin = {}
            coin['Name'] = response.xpath('//h1[@class="details-panel-item--name"]/img/@alt').extract()
            coin['Date'] = items[0].extract()
            coin['Market_Cap'] = items[6].extract()
            yield coin
