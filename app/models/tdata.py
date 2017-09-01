"""
VFS Demo App
Copyright (C) 2014-2017 Kibble Games Inc. In cooperation with Vancouver Film School All Rights Reserved. 

"""

from google.appengine.ext import ndb

# Once instance per game session collecting data
class TelemetryData( ndb.Model ):
    session = ndb.IntegerProperty( unique = True )
    time = ndb.TimeProperty( auto_now = True )
    x = ndb.FloatProperty()
    y = ndb.FloatProperty()
    action = ndb.IntegerProperty()
    
    
    
    
