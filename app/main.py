"""
VFS Demo App
Copyright (C) 2014 Kibble Games Inc. In cooperation with Vancouver Film School All Rights Reserved. 

"""
import os
import sys
import logging
import webapp2

from google.appengine.ext.webapp import util
from google.appengine.ext.webapp import template

# Must set this env var *before* importing any part of Django.
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'


def log_exception(*args, **kwds):
    """Log the current exception.
    Invoked when a Django request raises an exception"""
    logging.exception("Exception in request:")


# Force sys.path to have our own directory first, so we can import from it.
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from views.home  import HomePage
from views.sub   import SubPage
from views.error import Error404Page


""" =====================================================================

App Main

This is the entry point for the application.   

app.yaml config file will specify this 'main' module variable 'app as the stat point for the application
main.app

Requests to the server are manged by the WSGIApplication object, created with a list of URLs that its aware
of and the coresponding Python classes that handle requests sent to those URLs 

"""
app = webapp2.WSGIApplication([ ('/', HomePage),
                                ('/sub', SubPage),
                                ('/(.*)', Error404Page)
                              ], debug=True)

    

