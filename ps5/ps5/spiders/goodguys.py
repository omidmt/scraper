"""goodguys crawler"""

import scrapy
from scraper import notification


class GoodGuysSpider(scrapy.Spider):
  name = "goodguys"
  urls = [
      'https://www.thegoodguys.com.au/gaming/gaming-consoles/playstation-5',
  ]

  def start_requests(self):
    for url in self.urls:
      yield scrapy.Request(url=url,
                           headers={
                               'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:86.0) Gecko/20100101 Firefox/86.0'},
                           callback=self.parse)

  def parse(self, response):
    in_stock = False
    page = response.url.split("/")[5]

    prd_num = len(response.css('input#partNumber').getall())
    if prd_num > 4:
      in_stock = True
    notification.update_status(
        self.name, in_stock, page, response)
