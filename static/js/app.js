/**
 * App Singleton MAIN 
 * 
 * @copyright: (C) 2014 Kibble Games Inc in cooperation with Vancouver Film School. All Rights Reserved. 
 * @author: Scott Henshaw {@link mailto:shenshaw@vfs.com} 
 * @version: 1.1.0 
 * 
 * @summary: Framework Singleton Class to contain a web app
 * 
 *  This program is free software: you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation, either version 3 of the License, or
 *  (at your option) any later version.
 *   
 *  This program is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *  
 *  You should have received a copy of the GNU General Public License
 *  along with this program.  If not, see <http://www.gnu.org/licenses/>.
 * 
 */
var app = (function() {

    function AppConstructor( opt1 ) {
        
        var local = {
            // the local object contains all the private members used in this class             
            done: false
        };
        
        // this aka self contains all the public members and methods we wish to expose
        var self = this;
        
        
        self.init = function( option ) {        
            // Do some initialization of the member variables for the app
            if (option !== undefined) {
                
                // Use it.
            }

            // Do some initialization of the member variables for the app
            local.getPlayerListFromServer();
            
            
            // Create controllers to manage model objects and link them to DOM
            // view elements
            
            // Define the Event handlers for the app
        };   
	
        self.run = function() {
          
            // update something
            // render something
        };
    	
        local.getPlayerListFromServer = function() {
        	
        	// Post request for data to the server (assuming GAE server)
            $.post( '/', {'cmd':'get_player_data'})
                .then( function( data ) {
            	
                    // Data is returned as a native object already from GAE
                    var obj = data;
                    if (obj.returnCode === 0) {
        
                        // screen element update( obj.playerJSON );
                        // render();
        
                    } else if (obj.returnCode === 99) {
        
                        window.location = '/';
                        return;        
                    }
                });
        };
    };
	// Define the set of private methods that you want to make public and return them
	return new AppConstructor();
	
})();  // Run the unnamed function and assign the results to app for use.
        
        
$(document).ready( function() {

    app.init();            
    app.run();

});