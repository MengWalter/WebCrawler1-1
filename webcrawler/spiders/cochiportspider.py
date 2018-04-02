# -*- coding: utf-8 -*-
# @Time     : 2018/3/7 11:04
# @Author   : wenzhe

from scrapy import Request
from scrapy.spiders import Spider
from cochiport.items import CochiportItem
import scrapy

class cochiportspider(Spider):
	name = 'cochiportspider'
	start_urls = ['http://cochinport.gov.in/index.php?opt=shipsatport&cat=ev&tab=2']
	

	def parse(self,response):
		item = CochiportItem()
		#locate the shipsinport table
		shipsinport = response.xpath('//div[@id="TabbedPanels1"]/div[1]/div[@class="TabbedPanelsContent"]//table[@class="shipsinport"]')
		#locate the expected vessel table
		expectedvessel = shipsinport[2]
		#get data
		for shipsinfo in expectedvessel.xpath('./tr')[1:]:
			item['date'] = shipsinfo.xpath('.//td[1]/text()').extract()
		        item['ata'] = shipsinfo.xpath('.//td[2]/text()').extract()
			item['vessel'] = shipsinfo.xpath('.//td[3]/text()').extract()
            		item['cargo'] = shipsinfo.xpath('.//td[4]/text()').extract()
            		item['quantity'] = shipsinfo.xpath('.//td[5]/text()').extract()
            		item['ie'] = shipsinfo.xpath('.//td[6]/text()').extract()
            		item['agent'] = shipsinfo.xpath('.//td[7]/text()').extract()
			yield item
		
