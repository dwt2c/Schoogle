import psycopg2
#from shoogle.items import O_Item
#import sys
#sys.path.append("/Users/danielthornton/Schoogle/shoogle_spider/shoogle_spider/")
#import items
import upsert


class O_Pipeline(object):

  def __init__(self):
    #self.connection = psycopg2.connect( "host='postsql', database='Shoogle', user='groupb', password='fwIgG3v6'")
    self.connection = psycopg2.connect("dbname=SchoogleDB user=deek")
    self.cursor = self.connection.cursor()

  #def from_crawler(cls,crawler):

  def process_item(self, item, spider):

    #if item['id'] in self.ids_seen():
    # raise DropItem("Duplicate item found: %s" % item):
    #else:
    # self.ids_seen.
    try:
      upsert.searchable_Insert(self.cursor,item)
      #print item['full_text']
      self.connection.commit()
    except:
      self.connection.rollback()
    #self.connection.commit()
    #upsert.fullpage_Insert(self.cursor,item)
