# -*- coding: utf-8 -*-

# this still needs to be implemented, this should take the O_items that are 
# created by our spider and put ship them off to the postgresql server

# need to find a way to log inlinks! during the storing of our items!


class O_SpiderPipeline(object):

	# here we need to creae a new instance of a pipeline, this will have the database info that we need to log 
	#info to our Postgresql 
	def __init__(self,database_info):
		# here we need to assign the revelvant variables self.assignment
		pass

    def from_crawler(cls,crawler):
    	return cls( # this needs to initialize a pipeline using the __init__ method above and pass all the relant
    		# info from our spider
    		)
    def open_spider():
    	pass

    def close_spider():
    	pass # this should save what we have in our queue at this point?

    def process_item(self, item, spider):
        return item["url"]
        # here is where all of the real work gets done