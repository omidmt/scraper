"""bigW crawler"""

import scrapy
from scraper import notification


_box_rules = [
  '!.tg .tg-tw1s',
  '!.tg .tg-tw2s',
  '!.tg .tg-tw3s',
  '!.tg .tg-tw4s',
  '!.tg .tg-tw5s',
  '!.tg .tg-tw6s',
  '!.tg .tg-tw7s',
  '.tg .tg-tx8s',
  '!.tg .tg-tx9s'
]

class PS5StockSpider(scrapy.Spider):
  name = "ps5stock"
  urls = [
      'https://ps5stock.com.au/',
  ]

  def start_requests(self):
    for url in self.urls:
      yield scrapy.Request(url=url, callback=self.parse)

  def parse(self, response):
    in_stock = False
    page = 'any'

    response_content = str(response.body)
    if not all(rule in response_content for rule in _box_rules):
      in_stock = True

    notification.update_status(
        self.name, in_stock, page, response)
