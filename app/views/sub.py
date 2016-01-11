"""
VFS Demo App
Copyright (C) 2014 Kibble Games Inc. In cooperation with Vancouver Film School All Rights Reserved. 

"""
import logging


from m.models import Player
from m.models import Persona


from c.page import PageController

    
class SubPage( PageController ):
    
    currentPlayer = None    
    
    def get_markup(self):
                
        if self.currentPlayer is None:            
            tValues = { 
                'player_name': "Ash", 
                'persona_name': "Speed Racer"  
            }
        else:
            try:
                # check to see if this persona exists
                playerPersona = Persona( key = self.currentPlayer.persona ) 
                
            except ValueError:
                playerPersona = ""
                
            tValues = {
                'player_name': self.currentPlayer.name,
                'persona_name': playerPersona.name
            }
            
        markup = self.render_template( '../templates/sub.html', tValues )
        return markup
    

    
    def do_savePlayerData(self, cmd):
        
        # initialize the result, set the value to indicate an error
        result = { 'returnCode': -1 }
        
        # Get player data from self.request
        try: 
            pName = self.request.params['PlayerName']
            dName = self.request.params['PersonaName']
                        
            # Create and save the persona so it has a key
            # should really check for an existing persona here first
            newPersona = Persona( name = dName )
            newPersona.put()
            
            # use the player name and persona key to create the player.
            newPlayer = Player( name = pName )
            newPlayer.driver = newPersona.key                    
            newPlayer.put()
            
            result['returnCode'] = 0
            
        except ValueError:
            logging.error( 'Attempt to save a Player/Driver failed' )
            
        self.send_json_response( result )         
        return self

    