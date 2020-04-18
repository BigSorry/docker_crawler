from scrapy.crawler import CrawlerProcess
from spiders.crypto_spider import *
import pandas as pd

ubunut_path = '/home/lex/PycharmProjects/crypto/crypto/crawlUpdate.csv'
windows_path = '/C:/Users/lexme/PycharmProjects/docker_crawler/crypto/crypto/crawlUpdate.csv'
process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
    'FEED_FORMAT': 'csv',
    'FEED_URI': windows_path
})

checkDate = "01 Jan, 2019"
process.crawl(CryptoSpider, term=checkDate)
process.start()

data = pd.read_csv(windows_path[1:])
names = data["Name"].unique()
print(len(names))
