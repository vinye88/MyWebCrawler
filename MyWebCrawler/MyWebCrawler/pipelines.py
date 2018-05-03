# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MywebcrawlerPipeline(object):
    def process_item(self, item, spider):
        if spider.name == 'SpiderSteam':
            for key in item.keys():
                for idx, i in enumerate(item[key]):
                    item[key][idx] = i.strip().replace('<br>',' - ')
                item[key] = [x for x in item[key] if x != '']
        return item
