"""sony crawler"""

import scrapy
from scraper import notification


class SonySpider(scrapy.Spider):
  name = "sony"
  urls = [
      'https://store.sony.com.au/playstation-5/PLAYSTATION5W.html',
      # 'https://store.sony.com.au/playstation-5-accessories/PS5MEDIAREMOTEW.html'
  ]

  def start_requests(self):
    for url in self.urls:
      yield scrapy.Request(url=url, callback=self.parse)

  def parse(self, response):
    in_stock = False
    page = response.url.split("/")[4]

    available = response.css('button#add-to-cart::attr("title")').get(
    ) == 'Add to Cart' and not response.css('button#add-to-cart::attr("disabled")')
    if available:
      in_stock = True
    notification.update_status(
        self.name, in_stock, page, response)
