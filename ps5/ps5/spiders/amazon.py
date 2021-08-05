"""amazon crawler"""

import scrapy
from scraper import notification


class AmazonSpider(scrapy.Spider):
  name = "amazon"
  urls = [
      'https://www.amazon.com.au/PlayStation-5-Console/dp/B08HHV8945',
      # 'https://www.amazon.com.au/PlayStation-5-DualSense-Wireless-Controller/dp/B08H99BPJN'
  ]

  def start_requests(self):
    for url in self.urls:
      yield scrapy.Request(url=url,
                           headers={
                               'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:86.0) Gecko/20100101 Firefox/86.0',
                               },
                           callback=self.parse)

  def parse(self, response):
    in_stock = False
    page = response.url.split("/")[-3]

    available = response.css(
        'span.a-size-medium.a-color-success::text').get()
    if available and 'in stock' in available.lower():
      in_stock = True

    notification.update_status(
        self.name, in_stock, page, response)
