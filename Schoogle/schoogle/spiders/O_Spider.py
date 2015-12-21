from __future__ import absolute_import

from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy import Request
import sys
#sys.path.append("/Users/danielthornton/Desktop/schoogle/schoogle")
#from items import O_Item
#from schoogle.schoogle.items import O_Item
from schoogle.items import O_Item
from sys import getsizeof
from datetime import datetime
import time
import re

def reduce(text):
	return "".join([c for c in text if c in string.letters or c in (" ",)])
	#return re.sub('\s+',' ', re.sub(r'([^\s\w]|_)+', '', text))

#@params:
#@html_list: this is list of html in a "List"(aka vector), we replace all of those annoying
#	\t and \n's in clunkey html and return a string with the pages entire html contents,
# 	this object will later be used by postgreql for a full text search.
def prune(html_list):
	toreturn = []
	for i in html_list:
		t = i.encode('ascii','ignore')
		t = reduce(t)
		if t != '' or ' ':
			toreturn.append(t)
	return " ".join(toreturn)

class O_Spider(Spider):
	name = 'O_Spider'
	allowed_domains = ['owu.edu']
	start_urls = ['http://www.owu.edu']

	# @params
	# @response: this is a Scrapy.Response object containing much of the website information
	# 				attibutes of this object will be used to flesh out our O_Item object
	# @yield(1): this returns a single object each time next( this object ) is called
	# first parse yields all items
	# @yield(2): this is completed only after we have yielded an object from this webpage, it will 
	# recursively call parse on all links in a web page
	def parse(self,response):
		# here we use scrapy's request object to catch all invalid links when parsing our documnet
		try:
			for link in response.xpath('//@href').extract():
				try:
					req = Request(link,callback = self.parse)
				except ValueError:
					pass # might want to log these eventually
		except AttributeError:
			pass # log these eventually
		# fill up item with statistics
		current_item = O_Item()
		current_item['url'] = response.url
		try:
			current_item['title'] = response.xpath('//title/text()').extract()
			current_item['timestamp'] = datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
			current_item['page_size'] = getsizeof(response.body)
			current_item['full_html'] = response.body_as_unicode() # not sure if we really want this..
			current_item['full_text'] = " ".join(prune(response.xpath('//text()').extract()))
			current_item['secure'] = 'https' in str(response.request)
			current_item['links'] = response.xpath('//@href').extract()
			yield current_item
		except:
			pass



			# recursive page search is below, this must happen after the item is pipelined to postgresql
			# this is where we yield a requests object with parse as the callback and the real recursion kicks ins
		try:
			for link in response.xpath('//@href').extract():
				try:
					req = Request(link,callback = self.parse)
					yield req
				except ValueError:
					pass # might want to log these eventually
		except AttributeError:
				pass # log these eventually
			
