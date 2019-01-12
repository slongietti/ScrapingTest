# -*- coding: utf-8 -*-
import scrapy

class BovadaSpider(scrapy.Spider):
    name = 'bovada'

    def start_requests(self):
        #array of Urls to start crawling from
        start_urls = [
            #'https://www.bovada.lv/sports/',
            #'https://www.bovada.lv/sports/football',
            'https://www.bovada.lv/sports/basketball'
        ]

        browserHeaders = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0'}
        #loop through urls and make requests to callback to parse function
        for url in start_urls:
                yield scrapy.Request(url=url, callback=self.parse,method='GET',headers=browserHeaders)

    #parse function for the scrapy requests to callback to
    def parse(self, response):
        if response is None:
            print 'No Response'
        else:
            print 'Response Found'

        print(response.text)
        for game in response.xpath('//sp-happening-now'):
            print 'Here'
            yield {
                'date': game.xpath('.//sp-score-coupon[@class="period hidden-xs"]/text()').extract_first(),
                #'teamOne': game.xpath('./span[@class="text"]/text()').extract_first(),
                #'teamTwo': quote.xpath('.//small[@class="author"]/text()').extract_first(),
                #'tags': quote.xpath('.//div[@class="tags"]/a[@class="tag"]/text()').extract()
            }

        #next_page_url = response.xpath('//li[@class="next"]/a/@href').extract_first()
        #if next_page_url is not None:
        #    yield scrapy.Request(response.urljoin(next_page_url))


