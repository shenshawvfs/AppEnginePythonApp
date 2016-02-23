"""
VFS Demo App
Copyright (C) 2014 Kibble Games Inc. In cooperation with Vancouver Film School All Rights Reserved. 

"""
import logging


from app.models.user import User

from app.views.page_controller import PageController

    
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
                #playerPersona = Persona( key = self.currentPlayer.persona )
                playerPersona = "Player" 
                
            except ValueError:
                playerPersona = ""
                
            tValues = {
                'player_name': self.currentPlayer.name,
                'persona_name': playerPersona.name
            }
            
        markup = self.render_template( '../templates/partials/sub.html', tValues )
        return markup
    

    
    def do_add_user(self, params):
        
        # initialize the result, set the value to indicate an error
        result = { 'returnCode': -1 }
        
        # Get player data from self.request
        try: 
            pName = params['PlayerName']
            dName = params['PersonaName']
                        
            # Create and save the persona so it has a key
            # should really check for an existing persona here first
            newUser = User( name = dName )
            newUser.put()
            
            result['returnCode'] = 0
            result['playerName'] = pName
            result['driverName'] = dName
            
        except ValueError:
            logging.error( 'Attempt to save a Player/Driver failed' )
            
        self.send_json( result )         
        return self

    