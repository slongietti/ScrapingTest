# -*- coding: utf-8 -*-
import scrapy


class QuoteSpider(scrapy.Spider):
    #give name to spider so scrapy can find it to run command
    #scrapy crawl [SPIDERNAME]
    name = 'quotes'

    def start_requests(self):
        #array of Urls to start crawling from
        start_urls = [
            'http://quotes.toscrape.com/',
        ]

        #loop through urls and make requests to callback to parse function
        for url in start_urls:
                yield scrapy.Request(url=url, callback=self.parse)

    #parse function for the scrapy requests to callback to
    def parse(self, response):
        #loop through all the quotes on teh web page and create a object with text,author, and tags properties
        for quote in response.xpath('//div[@class="quote"]'):
            print 'Found Quotes'
            yield {
                'text': quote.xpath('.//span[@class="text"]/text()').extract_first(),
                'author': quote.xpath('.//small[@class="author"]/text()').extract_first(),
                'tags': quote.xpath('.//div[@class="tags"]/a[@class="tag"]/text()').extract()
            }

        #after looping through and capturing all quotes get the next page URL to crawl.
        next_page_url = response.xpath('//li[@class="next"]/a/@href').extract_first()

        #next url found, call scrapy Request which will recursively callback to this function
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))