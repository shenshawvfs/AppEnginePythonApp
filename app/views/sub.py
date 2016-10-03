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
            # check to see if this persona exists, limit the try except block to just
            # accessing the 
            #try:
                #playerPersona = Persona( key = self.currentPlayer.persona )
            #except ValueError:
            #    playerPersona = ""
            playerPersona = "Player" 
                
                
            tValues = {
                'player_name': self.currentPlayer.name,
                'persona_name': playerPersona
            }
            
        markup = self.render_template( '../templates/partials/sub.html', tValues )
        return markup
    

    
    

    