import psycopg2
from shoogle_spider.items import item


class Shoogle_pipeline(object):
  def __init__(self):
    self.connection = psycopg2.connect( "host='postsql', database='Shoogle', user='groupb', password='fwIgG3v6'")
    self.cursor = self.connection.cursor()
 
  def process_item(self, item, spider):
    # check item type to decide which table to insert
    try:
      if type(item) is USER1Item:
        self.cursor.execute("""INSERT INTO USER1 (UID, Username) VALUES(%s, %s)""", (item.get('UID'), item.get('Username'),))
       type(item) is USER2Item:
        self.cursor.execute("""INSERT INTO USER2 (Username, Pword) VALUES(%s, %s)""", (item.get('Username'), item.get('Pword'), ))
	   type(item) is SEARCHESItem:
	    self.cursor.execute("""INSERT INTO SEARCHES (Choseen_results, UID, Searched_terms, Cut_down_terms, Time_stamp) VALUES(%s, %s, %s, %s, %s)""", (item.get('Chosen_results'), item.get('UID'), item.get('Searched_terms'), item.get('Cut_down_terms'), item.get('Time_Stamp'), )))
       type(item) is CLIENTItem:
        self.cursor.execute("""INSERT INTO CLIENT (UID, Picture, IP) VALUES(%s, %s, %s)""", (item.get('UID'), item.get('Picture'), item.get('IP'), ))
	   type(item) is SEARCHABLEItem:
	    self.cursor.execute("""INSERT INTO SEARCHABLE (URL, PageRank, secure, Keywords) VALUES(%s, %s, %s, %s)""", (item.get('URL'), item.get('PageRank'), item.get('secure'), item.get('Keywords'), )))
  	   type(item) is ANALYTICSItem:
	    self.cursor.execute("""INSERT INTO ANALYTICS (Last_crawled, PageSize, URL, Times_visited, Searched, Image_count) VALUES(%s, %s, %s, %s, %s, %s)""", (item.get('Last_crawled'), item.get('PageSize'), item.get('Times_visited'), item.get('Searched'), item.get('Image_count'), )))
	   type(item) is CRAWL_LOGItem:
        self.cursor.execute("""INSERT INTO CRAWL_LOG (Username, Pword) VALUES(%s, %s)""", (item.get('Username'), item.get('Pword'), ))
	   type(item) is CRAWL_LIBItem:
        self.cursor.execute("""INSERT INTO CRAWL_LIB (Source, CID) VALUES(%s, %s)""", (item.get('Source'), item.get('CID'), ))
	   type(item) is CRAWLERSItem:
        self.cursor.execute("""INSERT INTO CRAWLERS (Pages_crawled, CID) VALUES(%s, %s)""", (item.get('Pages_crawled'), item.get('CID'), ))
	   type(item) is ENGINEItem:
        self.cursor.execute("""INSERT INTO ENGINE (Time_stamp, engine) VALUES(%s, %s)""", (item.get('Time_stamp'), item.get('Engine'), ))
	   type(item) is DOMAINItem:
        self.cursor.execute("""INSERT INTO DOMAIN (tag, body) VALUES(%s, %s)""", (item.get('Tag'), item.get('Body'), ))
	   type(item) is Full_PageItem:
        self.cursor.execute("""INSERT INTO Full_Page (URL, full_html) VALUES(%s, %s)""", (item.get('URL') item.get('full_html'), ))
	   type(item) is CREATE_LOG_LOOKUPItem:
        self.cursor.execute("""INSERT INTO CREATE_ITEM_LOOKUP (UID, URL) VALUES(%s, %s)""", (item.get('UID'), item.get('URL'), ))
	   type(item) is IN_TABLEItem:
        self.cursor.execute("""INSERT INTO IN_TABLE (Tag, Body, URL) VALUES(%s, %s, %s)""", (item.get('Tag'), item.get('Body'), item.get('URL'), ))
	   type(item) is BREAK_DOWNItem:
        self.cursor.execute("""INSERT INTO BREAK_DOWN (URL) VALUES(%s)""", (item.get('URL'), ))
	   type(item) is CONSUMEItem:
        self.cursor.execute("""INSERT INTO CONSUME (URL, CID) VALUES(%s, %s)""", (item.get('URL'), item.get('CID'), ))
	  self.connection.commit()
      self.cursor.fetchall()
 
    except psycopg2.DatabaseError, e:
      print "Error: %s" % e
    return item
