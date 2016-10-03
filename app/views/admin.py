"""
VFS Demo App
Copyright (C) 2014 Kibble Games Inc. In cooperation with Vancouver Film School All Rights Reserved. 

"""
import logging

from app.models.user import User

# this is the parent class of all pages that need to respond to AJAX messages
from app.views.page_controller import PageController 


"""
Admin Page handler

"""    
class AdminPage( PageController ):
    
    def get(self):
        self.send_template( '../templates/admin.html' )
        return
    