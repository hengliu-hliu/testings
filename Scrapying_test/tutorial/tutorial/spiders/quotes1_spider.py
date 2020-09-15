import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes1"

    def start_requests(self):
        urls = [
            'https://www.metmuseum.org/art/art-at-home'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'title': quote.css('title::text').get(),

            }
