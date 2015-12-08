# -*- coding: utf-8 -*-

# this still needs to be implemented, this should take the O_items that are 
# created by our spider and put ship them off to the postgresql server

# need to find a way to log inlinks! during the storing of our items!
class O_SpiderPipeline(object):
    def process_item(self, item, spider):
        return item
