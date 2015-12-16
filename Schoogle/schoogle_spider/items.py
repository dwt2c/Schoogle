# -*- coding: utf-8 -*-

# Define here the models for your scraped items

import scrapy

#This class is simply a data structure to be filled out by O_Spider during it's scraping run

class O_Item(scrapy.Item):
	""" An item that will hold the content scraped by O_Spider """
	#below we initialize all the fields that will be filled during scraping
	url = scrapy.Field() # string
 	title = scrapy.Field() #string
	links = scrapy.Field()	#string
	timestamp = scrapy.Field()	#string
	page_size = scrapy.Field()	#int
	full_html = scrapy.Field()	#string
	full_text = scrapy.Field()	#string
	secure = scrapy.Field()	#bool
	cid = scrapy.Field()
	domain = scrapy.Field()
	tab = scrapy.Field()

    
  
