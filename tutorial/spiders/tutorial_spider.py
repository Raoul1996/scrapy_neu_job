import scrapy


class Tutorial(scrapy.Spider):
    name = "tutorial"
    start_urls = [
        'http://lab.scrapyd.cn/',
        'http://lab.scrapyd.cn/page/1/',
        'http://lab.scrapyd.cn/page/2/',
    ]

    def parse(self, response):
        """
        scrapy workflow:
        1. defined the request url
        2. download the page content.
        3. defined rules, and select the data what we need.
        """

        page = response.url.split('/')[-2]
        filename = 'tutorial-%s.html' % page

        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('save file: %s' % filename)
