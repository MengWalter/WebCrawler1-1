# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs

class CochiportPipeline(object):

    def __init__(self):  
	#store data in json
	self.file = codecs.open('cochiport_data_utf8.json', 'wb', encoding='utf-8')  
    
    	#process item  
    def process_item(self, item, spider):  
        line = json.dumps(dict(item),ensure_ascii=False) + '\n'  
        # print line  
        self.file.write(line)  
        return item  

    def close_spider(self,spider):
	self.file.close()
