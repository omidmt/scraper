"""bigW crawler"""

import scrapy
from scraper import notification


class BigWSpider(scrapy.Spider):
  name = "bigw"
  urls = [
      'https://www.bigw.com.au/product/playstation-5-console/p/124625/',
  ]

  def start_requests(self):
    for url in self.urls:
      yield scrapy.Request(url=url, callback=self.parse)

  def parse(self, response):
    in_stock = False
    page = response.url.split("/")[4]

    available = response.css(
        'button.addToCartButtonNew.btn-orange::text').get()
    if available:
      in_stock = True
    notification.update_status(
        self.name, in_stock, page, response)
