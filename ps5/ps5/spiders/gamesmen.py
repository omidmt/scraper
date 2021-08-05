"""gamesmen crawler"""

import scrapy
from scraper import notification


class GamesmenSpider(scrapy.Spider):
  name = "gamesmen"
  urls = [
      'https://www.gamesmen.com.au/video-games/ps5/console-deals',
  ]

  def start_requests(self):
    for url in self.urls:
      yield scrapy.Request(url=url, callback=self.parse)

  def parse(self, response):
    in_stock = False
    page = response.url.split("/")[4]

    if 'There are no products matching the selection' not in str(response.body):
      in_stock = True
    notification.update_status(
        self.name, in_stock, page, response)
