"""
VFS Demo App
Copyright (C) 2014 Kibble Games Inc. In cooperation with Vancouver Film School All Rights Reserved. 

"""
import os
import sys
import logging
import webapp2

import json

from google.appengine.ext.webapp import util
from google.appengine.ext.webapp import template


"""
PageController manages JSON translation and message dispatch command handling

All pages with require AJAX handling should subclass this Class

"""
class PageController( webapp2.RequestHandler ):
    
    CORSAccessAllowed = False

    """
    @function post
    
    This is the core of responding to AJAX requests.
    The request is expecting a 'cmd' parameter identifying a command to process (other parameters are considered 
    application specific
    
    If the command is valid (i.e the child class had a defined function 'do_<cmd>' then a function pointer
    is generated pointing to the 'do_<cmd>' and its executed.
    
    The executed command can call either 
    
    """
    def post(self):
        """ 
        Process the passed instruction and respond

        """        
        # Look for the command argument
        if self.request.params['cmd'] == '':
            # missing argument(s)
            logging.warning('PageController.post() missing command argument.')
            self.send_json_response( {'returnCode': 10} )
            return
        
        cmd = self.request.params['cmd']
        logging.debug('PageController: command['+cmd+'] called.')
        
        # process the command
        command_handler_name = 'do_' + cmd
        if hasattr(self, command_handler_name):
            command_handler = getattr(self, command_handler_name)
            command_handler( cmd )
        else:
            self.error(cmd, 11) 

        
        return


    """
    Helper methods to render templates to either strings or directly back to the calling client
     
    """
    def render_template(self, htmlTemplate, tValues):
        
        path = os.path.join( os.path.dirname(__file__), htmlTemplate )
        markup = template.render( path, tValues )
        return markup

        
    def render_json(self, data):
        
        jsonMarkup = json.dumps( data )
        return jsonMarkup
     

    def send_template(self, htmlTemplate, tValues ):
        
        if (self.CORSAccessAllowed):
            self.response.headers.add_header("Access-Control-Allow-Origin", "*")
            
        self.response.write( self.render_template( htmlTemplate, tValues ) )
        return


    def send_json( self, data ):
        
        if (self.CORSAccessAllowed):
            self.response.headers.add_header("Access-Control-Allow-Origin", "*")
            
        self.response.headers['Content-Type'] = 'application/json'
        self.response.write( self.render_json( data ) )
        return
    
    
    def send(self, data, asJSON):
        if (self.CORSAccessAllowed):
            self.response.headers.add_header("Access-Control-Allow-Origin", "*")
                   
        # assumes  data is a rendered template                   
        responseData = data 
        
        # if its a dictionary, reformat as JSON data
        if (asJSON == True):
            self.response.headers['Content-Type'] = 'application/json'
            responseData = self.render_json( data )
                    
        self.response.write( responseData )    
        return 


    def options(self):
        
        if (self.CORSAccessAllowed):
            self.response.headers['Access-Control-Allow-Origin'] = '*'
            self.response.headers['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept'
            self.response.headers['Access-Control-Allow-Methods'] = 'POST, GET, PUT, DELETE'
            
        return self










