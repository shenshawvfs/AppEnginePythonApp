"""
VFS Demo App
Copyright (C) 2014 Kibble Games Inc. In cooperation with Vancouver Film School All Rights Reserved. 

"""
import logging

from app.models.user import User

# this is the parent class of all pages that need to respond to AJAX messages
from app.views.page_controller import PageController 

from app.views.sub import SubPage


"""
Home Page handler

"""    
class IndexPage( PageController ):
        
    def get(self):   

        # use a sub page partial to render some HTML to use within this page. Optional.            
        panel = SubPage()
        markup = panel.get_markup()
        
        tValues = {
            'msg': "Scott is the Winner",
            'current_panel': markup
        }

        logging.debug( "rendering main page" )
        self.send_template( '../templates/index.html', tValues )        
        return
    
           
    def error(self, cmd, return_code):
        """ 
        invalid command handler 
        
        """ 
        logging.warning('MainPage.post() unrecognized command['+cmd+']')
        self.send_json( {'returnCode': return_code} )
        return
    
    
    def do_add_user(self, params):
        
        # initialize the result, set the value to indicate an error
        result = { 'returnCode': -1 }
        
        # Get player data from self.request
        pName = params['PlayerName']
        dName = params['PersonaName']
                        
        # Create and save the persona so it has a key
        # should really check for an existing persona here first
        newUser = User( name = dName )
            
        try:
            # try blocks should be limited just to calls that may fail 
            newUser.put()
            
        except ValueError:
            logging.error( 'Attempt to save a Player/Driver failed' )
            self.send_json( result )    
            
            
        result['returnCode'] = 0
        result['playerName'] = pName
        result['driverName'] = dName
            
        self.send_json( result )
        return
    

    def do_get_player_data(self, params):
        """
        Command handler for 'get_player_data' command
        
        """
        result = { 'returnCode': 0 }
                
        #result['playerList'] = self._get_player_list()
        self.send_json( result )
        return
    
    
    def _get_player_list( self ):
        """
        Returns player list from datastore
        
        """
        # get players
        query = User.query()        
        player_list = None # query.fetch( self.MAX_PLAYERS )                
        return player_list
        