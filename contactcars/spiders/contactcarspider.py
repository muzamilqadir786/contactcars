# -*- coding: utf-8 -*-
import csv
import scrapy
from scrapy.selector import Selector
from scrapy.http import Request
from contactcars.items import ContactcarsItem
from selenium import webdriver
from lxml.html import fromstring

mf = open('level2_links.csv','rb')
reader = csv.reader(mf)
class ContactcarspiderSpider(scrapy.Spider):
    name = "contactcarspider"
    allowed_domains = ["contactcars.com"]
    base_url = 'http://contactcars.com'
    # start_urls = (
    #     # http://www.contactcars.com/newcars/makes',
   	# 	'http://www.contactcars.com/newcars/modelengines/516?year=2014',
    # )
    start_urls = ('http://contactcars.com'+row[1] for row in reader)
    
    # def __init__(self):
    # 	self.driver = webdriver.Firefox()

    def parse(self, response):
    	print "here"
    	item = ContactcarsItem()
    	hxs = Selector(response)
    	# with open('checkout.html','wb') as cf:
    	# 	cf.write(response.body)
    	
    	# for row in reader:
    	# 	print row[1]

    	make = hxs.xpath('//text[@itemprop="name"]/text()').extract()
    	if make:
    		item['make'] = make[1].encode('utf-8')
    		print make

    	model = hxs.xpath('//span[@class="tit_2 right"][1]//text()').extract()
    	if model:
    		item['model'] = model
		year = hxs.xpath('//span[@class="tit_2 right"][2]//text()').extract()
		if year:
			item['year'] = year

    	price_table = hxs.xpath('//table[1]/tbody')
    	print price_table
    	for row in price_table:
			description = row.xpath('./tr/td[1]/a/@href').extract()
			if description:
				item['description_link'] = description#[0].encode('utf-8')
				# print description

			price = row.xpath('./tr/td[2]/span//text()').extract()
			if price:
				item['price'] = price#[0].encode('utf-8')
				print price

			print item
			yield item
			
		


 #    def parse(self, response):
 #        """
 #        Getting all newcars links from start_url
 #        """
 #        print "here in 1st level"
 #        hxs = Selector(response)
 #        newcar_links = hxs.xpath('//li/a[contains(@href,"NewCars")]/@href').extract()
 #        print newcar_links

 #        driver = self.driver
 #        for newcar_link in newcar_links:
 #        	link = self.base_url+newcar_link.lower()
 #        	driver.get(link)
 #        	html = driver.page_source
 #        	#Level 2 pages links
 #        	hxs = fromstring(html)
 #        	model_engines = hxs.xpath('//li/a[contains(@href,"NewCars/ModelEngines")]/@href')
 #        	for model_engine in model_engines:
	# 			item = ContactcarsItem()
	# 			item['links'] = model_engine
	# 			yield item
	# 			# yield Request(self.base_url+model_engine,self.parse_detail,dont_filter=True)

 #        	# print link
 #        	# print "hello world"
 #        	# yield Request(link,self.parse_newcar,dont_filter=True)
 #        	# yield Request('http://www.google.com',self.parse_newcar,dont_filter=True)


 #   	def parse_newcar(self, response):
 #   		"""
 #   		Getting second level links
 #   		"""
 #   		print "here in 2nd level"
 #   		hxs = Selector(response)
 #   		# make = hxs.xpath('//text[@itemprop="name"][2]/text()').extract()
 #   		model_engines = hxs.xpath('//li/a[contains(@href,"NewCars/ModelEngines")]/@href').extract()
 #   		# print model_engines
	# 	for model_engine in model_engines:
	# 		yield Request(self.base_url+model_engine,self.parse_detail,dont_filter=True)

	# def parse_detail(self, response):
	# 	print "here in 3rd level"
	# 	hxs = Selector(response)		
	# 	item = ContactcarsItem()
	# 	make = hxs.xpath('//text[@itemprop="name"][2]/text()').extract()
	# 	if make:
	# 		item['make'] = make

	# 	model = hxs.xpath('//span[@class="tit_2 right"][1]//text()').extract()
	# 	if model:
	# 		item['model'] = model

	# 	year = hxs.xpath('//span[@class="tit_2 right"][2]//text()').extract()
	# 	if year:
	# 		item['year'] = year
			
	# 	price_table = hxs.xpath('//table[1]/tbody')
	# 	for row in price_table:
	# 		description = row.xpath('./tr[1]/td/a/@href').extract()
	# 		if description:
	# 			item['description'] = description

	# 		price = row.xpath('./tr[2]/td/span//text()').extract()
	# 		if price:
	# 			item['price'] = price

	# 		print item
	# 		yield item







