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
(function() {
    
class NameSpace {
    constructor() {
        this.data = new WeakMap();
    }

    members( key, value = undefined ) {
        if (value != undefined) {
            this.data.set( key, value );
        }
        return this.data.get( key );
    }

    static resultFromData( data ) {

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
}

if (app === undefined) {
    var app = {
       'private': new NameSpace(),
       resultFromData: NameSpace.resultFromData
    }
}


class App {

    constructor() {
        
        // the local object contains all the private members used in this class             
        let m = app.private.members( this, {
            playerList: [],
            done:       false
        });
        
        // Do some initialization of the member variables for the app
        this.populatePlayerList();            
        
        // Create controllers to manage model objects and link them to DOM
        // view elements
        
        // Define the Event handlers for the app
        
    }   
        
    run() {
      
        // update something
        // render something
    }
    
    populatePlayerList() {
        let m = app.private.members( this );
        
    	// Post request for data to the server (assuming GAE server)
        let instr = $.param({'cmd':'get_player_data'});
        $.post( '/', instr )
            .then( ( data ) => {
                
                let result = app.resultFromData( data );
                if (result.returnCode === 0) {
    
                    // use the data inside result, each member will match the dictionary
                    // from the server
                    m.playerList = result.players;
    
                } else if (result.returnCode === 99) {
    
                    // handle error returned by the server
                    window.location = '/';
                    return;        
                }
            });
    }
    
    resultFromData( data ) {

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
}

$(document).ready( function() {

    let app = new App();            
});


})();
