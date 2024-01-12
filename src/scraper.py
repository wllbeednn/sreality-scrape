import json
import math

import scrapy


class FlatsScraper(scrapy.Spider):
    name = 'sreality-flats-scraper'
    allowed_domains = ["sreality.cz"]

    page = 1
    per_page = 20
    estates_number = 20
    max_pages = math.ceil(estates_number / per_page)

    api_endpoint = 'https://www.sreality.cz/api/cs/v2/estates'
    start_urls = [
        f'{api_endpoint}?category_main_cb=1&category_type_cb=1&page={page}&per_page={per_page}'
    ]

    def parse(self, response, kwargs=None):
        data = json.loads(response.text)
        estates = data['_embedded']['estates']
        for estate in estates:
            title = estate['name']
            images = [image['href'] for image in estate['_links']['images']]
            print(title, images[0])
        if self.page < self.max_pages:
            self.page += 1
            url = f'{self.api_endpoint}?category_main_cb=1&category_type_cb=1&page={self.page}&per_page={self.per_page}'
            yield scrapy.Request(url=url, callback=self.parse)
