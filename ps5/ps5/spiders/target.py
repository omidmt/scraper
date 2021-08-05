"""tareget crawler"""

import scrapy
from scraper import notification


class TargetSpider(scrapy.Spider):
  name = "target"
  urls = [
      # 'https://www.target.com.au/p/playstation-reg-5-dualsense-controller/64226194',
      'https://www.target.com.au/p/playstation-reg-5-console/64226187'
  ]

  def start_requests(self):
    for url in self.urls:
      yield scrapy.Request(url=url,
                           meta={'dont_redirect': True},
                           callback=self.parse)

  def parse(self, response):
    in_stock = False
    page = response.url.split("/")[4]

    available = response.css('meta[itemprop="price"]').get()
    if available:
      in_stock = True
    notification.update_status(
        self.name, in_stock, page, response)
