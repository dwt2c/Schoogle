import psycopg2

def upsert(insert,update,item):
	pass


def searchable_Insert(cursor,item):
	cursor.execute("INSERT into searchable (title, URL, security, key_text)  values (%s,%s,%s,%s)", 
		(item['title'],item['url'],item['secure'],item['full_text']))


def searchable_Update(cursor,item):
	cursor.execute("UPDATE searchable SET (title,URL,security,key_text) = (%s,%s,%s,%s) WHERE URL = (%s)",
		(item['title'],item['url'],item['secure'],item['full_text'],url['title']))

def analytics_Insert(cursor,item):
	cursor.execute("INSERT into analytics (last_crawled, page_size, URL,image_count)  values (%s,%s,%s,%s)", 
		(item['timestamp'],item['page_size'],item['secure'],item['full_text']))

def analytics_Update(cursor,item):
	cursor.execute("UPDATE analytics SET (last_crawled, page_size, URL,image_count) = (%s,%s,%s,%s) WHERE URL = (%s)",
		(item['timestamp'],item['page_size'],item['secure'],item['full_text']))

def crawl_log_Insert(cursor,item):
	cursor.execute("INSERT into crawl_log (last_crawled,CID)  values (%s,%s)", 
		(item['timestamp'],item['CID']))

def crawl_log_Update(cursor,item):
	cursor.execute("UPDATE crawl_log SET (last_crawled,CID) = (%s,%s) WHERE URL = (%s)",
		(item['timestamp'],item['CID'],item['url']))

def crawlers_Update(cursor,item):
	cursor.execute("UPDATE crawlers SET (pages_crawled,CID) = (%s,%s) WHERE CID = (%s)",
		(item['timestamp'],item['CID'],item['CID']))

def fullpage_Insert(cursor,item):
	cursor.execute("INSERT into full_page (URL,HTML)  values (%s,%s)", 
		(item['url'],item['html']))

def fullpage_Update(cursor,item):
	cursor.execute("UPDATE full_page SET (URL,HTML) = (%s,%s) WHERE URL = (%s)",
		(item['url'],item['html'],item['url']))

def domain_Insert(cursor,item):
	cursor.execute("INSERT INTO domain (tag, body1) VALUES (%s, %s)",
		item['tag'],item['body'])


