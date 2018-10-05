# -*-coding:utf-8-*-
import scrapy
import logging


class ItemSpider(scrapy.Spider):
    name = 'item'
    start_urls = ['http://lab.scrapyd.cn']

    def parse(self, response):
        quotes = response.css('div.quote')
        quote = quotes[0]

        text = quote.css('.text::text').extract_first()
        author = quote.css('.author::text').extract_first()
        tags = quote.css('.tags .tag::text').extract()
        tags = ','.join(tags)
        filename = '%s-quotes.txt' % author
        f = open(filename, 'a+')
        f.write(text.encode('utf-8'))
        f.write('\n')
        f.write('tag: ' + tags.encode('utf-8'))
        f.write('\n')
        f.close()
