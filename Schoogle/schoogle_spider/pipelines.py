import psycopg2
from shoogle import items
#import sys
#sys.path.append("/Users/danielthornton/Schoogle/shoogle_spider/shoogle_spider/")
#import items
import upsert


class O_Pipeline(object):
  
	def __init__(self):
		#self.connection = psycopg2.connect( "host='postsql', database='Shoogle', user='groupb', password='fwIgG3v6'")
		self.connection = psycopg2.connect ("database=exampleDB,user=danielthornton")
		self.cursor = self.connection.cursor()

	#def from_crawler(cls,crawler):

	def process_item(self, item, spider):
		#if item['id'] in self.ids_seen():
		#	raise DropItem("Duplicate item found: %s" % item):
		#else:
		#	self.ids_seen.
		upsert.searchable_Insert(self.cursor,item)
		upsert.fullpage_Insert(self.cursor,item)
		connection.commit()
		return item;



	  