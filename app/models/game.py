"""
VFS Demo App
Copyright (C) 2014 Kibble Games Inc. In cooperation with Vancouver Film School All Rights Reserved. 

"""

from google.appengine.ext import ndb


class GameCategories( ndb.Model ):
    id = ndb.IntegerProperty( required = True )
    game_id = ndb.IntegerProperty()  # maps a collection of 


class Game( ndb.Model ):
    id = ndb.IntegerProperty( required = True )
    title = ndb.StringProperty()

    categories = []

    def populate(self):
        qry = GameCategories.query().filter( self.id )
        for cat in qry.fetch():
            self.category[self.category.length] = cat