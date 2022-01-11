# -*- coding: utf-8 -*-
import scrapy
from qoutescrape.items import QoutescrapeItem

class SpidernameSpider(scrapy.Spider):
    name = 'spidername'
    allowed_domains = ['quotes.toscrape.com/']
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        # for quote in response.css('div.quote'):
        #     yield {
        #         'text': quote.css('span.text::text').get(),
        #         'author': quote.css('small.author::text').get(),
        #         'tags': quote.css('div.tags a.tag::text').getall(),
        #     }

        for quote in response.css('div.quote'):
            item_content = quote.css('span.text::text').extract_first()
            item_author = quote.css('small.author::text').extract_first()
            quoteItem = QoutescrapeItem(content= item_content,author=item_author)
            yield quoteItem