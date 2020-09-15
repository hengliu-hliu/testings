import urllib
import scrapy
import json

class QuotesSpider(scrapy.Spider):
    name = "test"
    start_urls = [
        'https://www.huntington.org/exhibitions'
    ]

    def parse(self, response):

        title = response.css('title::text').get()
        subtitle = response.css('.block-title::text').extract()
        all_events = response.css('.ex_summary_title::text').getall()

        #still working on
        temp = response.css('.active a::attr(href)').getall()

        yield {
                'Title': title,
                'subtitle': subtitle,
                'all_events': all_events,
                'Temp' : temp
            }


