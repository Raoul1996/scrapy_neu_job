# -*- coding: utf-8 -*-
import scrapy
import re
from job.items import JobItem
from job.items import CompanyItem


class JobSpider(scrapy.Spider):
    name = 'job'
    allowed_domains = ['jobneu.jysd.com']
    base_url = 'http://jobneu.jysd.com'
    start_urls = ['http://jobneu.jysd.com/teachin/']
    # 会计，财务，出纳
    pattern = re.compile(u'会计|财务|出纳')

    def parse(self, response):
        job_list = response.css('.infoBox ul.infoList.teachinList')
        for job_info in job_list:
            item = JobItem()
            item['company_name'] = job_info.css('li.span1 a::text').extract_first().encode('utf-8')
            item['company_link'] = job_info.css('li.span1 a::attr(href)').extract_first()
            item['briefing_city'] = job_info.css('li.span2::text').extract_first()
            item['school'] = job_info.css('li.span5::text').extract_first()
            item['room'] = job_info.css('li.span4::text').extract_first()
            item['time'] = job_info.css('li.span5::text').extract()[1]

            # yield item
            company_detail = job_info.css('li.span1 a::attr(href)').extract_first()

            if company_detail is not None:
                # company_datail: /teachin/view/id/{company_page_id}
                yield response.follow(url=self.base_url + company_detail, callback=self.detail)

        next_page = response.css('div.ctl ul.page li.next a::attr(href)').extract_first()
        if next_page is not None:
            # next_page: /teachin/index?page={page_num}
            next_page = self.base_url + next_page
            yield scrapy.Request(next_page, callback=self.parse)

    def detail(self, response):
        """
        宣讲会详细信息
        :param response:
        :return:
        """
        item = CompanyItem()
        # common info
        item['title'] = response.css('.viewHead h1::text').extract_first()
        item['link'] = self.base_url + response.css('.viewHead a::attr(href)').extract_first()
        item['quality'] = response.css('ul.xInfo.xInfo-2 li span::text').extract()[0]
        item['industry'] = response.css('ul.xInfo.xInfo-2 li span::text').extract()[1]
        item['size'] = response.css('ul.xInfo.xInfo-2 li span::text').extract()[2]

        item['time'] = response.css('ul.cl.tInfo-2 li span::text').extract()[0]
        item['school'] = response.css('ul.cl.tInfo-2 li span::text').extract()[1]
        item['city'] = response.css('ul.cl.tInfo-2 li span::text').extract()[2]
        item['room'] = response.css('ul.cl.tInfo-2 li span::text').extract()[3]

        try:
            email = response.css('ul.cl.tInfo-2 li span::text').extract()[4]
            phone = response.css('ul.cl.tInfo-2 li span::text').extract()[5]
            item['email'] = email
            item['phone'] = phone
        except:
            pass

        has_pos_list = response.css('ul#vTab3.xInfo table').extract_first()

        if has_pos_list is not None:
            item['has_pos_list'] = 1
            pos_list = response.css('ul#vTab3.xInfo table tr')[1:]
            item['pos_list'] = []
            for pos in pos_list:
                pos_ok = re.search(self.pattern, unicode(pos.extract()))
                if pos_ok:
                    item['info_from'] = 3
                    item['pos_list'].append({
                        'id': pos.css('td::text').extract()[0],
                        'name': pos.css('td::text').extract()[1],
                        'subject': pos.css('td a::text').extract()[0],
                        'hc': pos.css('td::text').extract()[2]
                    })
                    item['sub_link'] = pos.css('td a::attr(href)').extract()[0],
        else:
            item['has_pos_list'] = 0
            item['pos_list'] = ''
            filename = 'no_pos_table_list.txt'
            with open(filename, 'a+') as f:
                f.write(response.url.encode('utf-8'))
                f.write('\n\n')
                f.close()

        v_tab1 = response.css('#vTab1')
        if re.search(self.pattern, unicode(v_tab1.extract_first())):
            item['info_from'] = 1
        if v_tab1.css('table'):
            item['addon_table'] = v_tab1.css('table').extract()
        v_tab2 = response.css('#vTab2')
        if re.search(self.pattern, unicode(v_tab2.extract_first())):
            item['info_from'] = 2
        yield item
