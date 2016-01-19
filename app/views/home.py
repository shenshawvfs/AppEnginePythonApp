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
class HomePage( PageController ):
        
    def get(self):       
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
        """ invalid command handler """ 
        logging.warning('MainPage.post() unrecognized command['+cmd+']')
        self.send_json( {'returnCode': return_code} )
        return
    
    
    def do_get_player_data(self, params):
        """
        Command handler for 'getPlayerData' command
        
        """
        result = { 'returnCode': 0 }
                
        result['playerList'] = self._get_player_list()
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
        