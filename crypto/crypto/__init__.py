import scrapy
from scrapy.crawler import CrawlerProcess
from spiders.crypto_spider import *

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
    'FEED_FORMAT': 'csv',
    'FEED_URI': '/home/lex/PycharmProjects/crypto/crypto/crawlUpdate.csv'
})

checkDate =  "01 Jan, 2019"
process.crawl(CryptoSpider(scrapy.Spider), term=checkDate)
process.start()  # the script will block here until the crawling is finished