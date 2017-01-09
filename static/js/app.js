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
'use strict';

if (__private__ === undefined)
    var __private__ = new WeakMap();


class App {

    constructor( opt1 ) {
        
        // the local object contains all the private members used in this class             
        let m = {
            done: false
        };
        __private__.set( this, m );
        
        // Do some initialization of the member variables for the app
        if (opt1 !== undefined) {
            
            // Use it.
        }

        // Do some initialization of the member variables for the app
        this._getPlayerListFromServer();
            
        
        // Create controllers to manage model objects and link them to DOM
        // view elements
        
        // Define the Event handlers for the app
        
        // and go...
        this.run();
    }   

        
    run() {
      
        // update something
        // render something
    }
    	
    
    _resultFromData( data ) {

        let result = null; 
        switch (typeof data) {
            case 'string':
                result = $.parseJSON( data );
                break;
                
            case 'object':
                result = data;
                break;
            
            default:
                result = null; 
                break;
        }
        return result;
    }
        

    _getPlayerListFromServer() {
        	
    	// Post request for data to the server (assuming GAE server)
        let instr = $.param({'cmd':'get_player_data'});
        $.post( '/', instr )
            .then( ( data ) => {
                
                let result = this._resultFromData( data );
                if (result.returnCode === 0) {
    
                    // use the data inside result, each member will match the dictionary
                    // from the server
    
                } else if (result.returnCode === 99) {
    
                    // handle error returned by the server
                    window.location = '/';
                    return;        
                }
            });
    }
}

$(document).ready( function() {

    let app = new App();            

});