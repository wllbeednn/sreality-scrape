import scrapy


class FlatsScraper(scrapy.Spider):
    name = 'sreality-flats-scraper'
    start_urls = ["https://www.sreality.cz/hledani/prodej/byty"]

    def parse(self, response, kwargs=None):
        self.logger.debug("=================STARTING CRAWLING=================")
        print(response.body)
        with open('output.html', 'w') as file:
            file.write(response.body.__str__())

        print(response.css("div.dir-property-list div.property"))

        for flat in response.css("div.dir-property-list div.property"):
            self.logger.debug("-------------------------------------------------")
            print(flat)
            self.logger.debug("-------------------------------------------------")
            break
        self.logger.debug("=================FINISHING CRAWLING=================")
        #     yield {
        #         "title": quote.xpath("span/small/text()").get(),
        #     }

        # next_page = response.css('li.next a::attr("href")').get()
        # if next_page is not None:
        #     yield response.follow(next_page, self.parse)
