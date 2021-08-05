"""jbhifi crawler"""

import scrapy
from scraper import notification


class JBSpider(scrapy.Spider):
    name = "jbhifi"
    urls = [
            'https://vtvkm5urpx-dsn.algolia.net/1/indexes/*/objects?x-algolia-agent=Algolia%20for%20JavaScript%20(4.6.0)%3B%20Browser',
    ]

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url,
                                 method="POST",
                                 body='{"requests":[{"indexName":"shopify_products","objectID":"487924"}]}',
                                 headers={
                                     'x-algolia-api-key': '',
                                     'x-algolia-application-id': '',
                                     'content-type': 'application/x-www-form-urlencoded',
                                     'Origin': 'https://www.jbhifi.com.au',
                                     'DNT': '1',
                                     'Referer': 'https://www.jbhifi.com.au/pages/playstation-5'
                                 },
                                 callback=self.parse)

    def parse(self, response):
        in_stock = False
        page = 'json'
        
        if '"availableNow":"Available Now"' in str(response.body):
          in_stock = True
        notification.update_status(
            self.name, in_stock, page, response)