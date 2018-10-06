# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JobItem(scrapy.Item):
    company_name = scrapy.Field()
    company_link = scrapy.Field()
    briefing_city = scrapy.Field()
    school = scrapy.Field()
    room = scrapy.Field()
    time = scrapy.Field()
    pass


class CompanyItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    quality = scrapy.Field()
    industry = scrapy.Field()
    size = scrapy.Field()
    time = scrapy.Field()
    school = scrapy.Field()
    city = scrapy.Field()
    room = scrapy.Field()
    email = scrapy.Field()
    phone = scrapy.Field()
    has_pos_list = scrapy.Field()
    pos_list = scrapy.Field()
    # 消息来源
    info_from = scrapy.Field()
    addon_table = scrapy.Field()
    # 来自表格中的链接
    sub_link = scrapy.Field()
