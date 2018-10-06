# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json


class JobPipeline(object):
    # def __init__(self):
    #     self.file = self.file = open('job.json', 'wb')

    def process_item(self, item, spider):
        # content = json.dumps(dict(item), ensure_ascii=False) + "\n"  # 因为scrapy默认是ascii码的编码，中文要变成unicode编码
        # self.file.write(content.encode('utf-8'))
        return item

    # def open_spider(self, spider):
    #     pass
    #
    # def close_spider(self, spider):
    #     self.file.close()
