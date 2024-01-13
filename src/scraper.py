"""
Script to scrape data.
"""
import json
import math

import scrapy
import crud
from db.session import SessionLocal


class FlatsScraper(scrapy.Spider):
    """
    Scraper for flats on sreality.cz.
    """
    name = 'sreality-flats-scraper'
    allowed_domains = ["sreality.cz"]

    page = 1
    per_page = 20
    estates_number = 500
    max_pages = math.ceil(estates_number / per_page)

    api_endpoint = 'https://www.sreality.cz/api/cs/v2/estates'
    start_urls = [
        f'{api_endpoint}?category_main_cb=1&category_type_cb=1&page={page}&per_page={per_page}'
    ]

    def parse(self, response, kwargs=None):
        """
        Parse each response from start_urls and parse each next response yielded within this parsing.
        :param response: http response with data to scrape.
        """
        data = json.loads(response.text)
        estates = data['_embedded']['estates']
        db = SessionLocal()

        for estate in estates:
            title = estate['name']
            images = [image['href'] for image in estate['_links']['images']]
            crud.create(db=db, title=title, image_url=images[0])

        db.close()

        if self.page < self.max_pages:
            self.page += 1
            url = f'{self.api_endpoint}?category_main_cb=1&category_type_cb=1&page={self.page}&per_page={self.per_page}'
            yield scrapy.Request(url=url, callback=self.parse)
