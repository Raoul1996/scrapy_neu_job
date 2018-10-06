# -*-coding:utf-8-*-
import scrapy
import logging


class ListSpider(scrapy.Spider):
    name = 'list'

    # start_urls = ['http://lab.scrapyd.cn/']
    def start_requests(self):
        url = 'http://lab.scrapyd.cn/'
        tag = getattr(self, 'tag', None)
        if tag is not None:
            url = url + 'tag/' + tag
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        quotes = response.css('div.quote')
        for quote in quotes:
            text = quote.css('.text::text').extract_first()
            author = quote.css('.author::text').extract_first()
            tags = quote.css('.tags .tag::text').extract()
            tags = ','.join(tags)
            filename = '%s-quotes.txt' % author
            with open(filename, 'a+') as f:
                f.write(text.encode('utf-8'))
                f.write('\n')
                f.write('tag: ' + tags.encode('utf-8'))
                f.write('\n\n')
                f.close()
        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            yield scrapy.Request(next_page, callback=self.parse)
