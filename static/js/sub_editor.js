 /*
  *  This singleton object controls the template code above
  */
    var subPanel = (function() {
    
        function SubPanelController() {

            var local = {};
            var self = this;
        
            self.init = function() {
                
                $("#sub-submit").on('submit', function( event ) {
                    event.preventDefault();                 
                    local.savePlayer();
                });
            }; 
        
            
            local.savePlayer = function() {
            
                // Post request for data to the server (python code)
                $('#status').html("");  // clear the result
                
                var instr = $("#sub-submit").serialize();
                $.post( '/', instr )
                    .then( function( data ) {
                        
                        // Data from AppEngine comes back as an object, 
                        // from PHP as a JSOn format string.
                        // This makes sure that whatever we get it gets 
                        // back to us eventually as an object.
                        var result = local.resultFromData( data );
                        
                        if (result.returnCode === 0) {
                
                            // screen element update( obj.playerJSON );
                            local.render( result );
                
                        } else if (result.returnCode === -1) {
                
                            window.location = '/';
                            return;
                        }
                    });
            };
        
            
            local.resultFromData = function( data ) {

                var result = null; 
                switch (typeof data) {
                    case 'string':
                        var result = $.parseJSON( data );
                        break;
                        
                    case 'object':
                        var result = data;
                        break;
                    
                    default:
                        var result = null; 
                        break;
                }
                return result;
            };
            
            
            local.render = function( data ) {
            
                $("input[name='PlayerName']").val( data.playerName );
                $("input[name='DriverName']").val( data.driverName );
                
                $('#status').html("User " + data.playerName + " logged in as " + data.driverName );
            };
        };
        return new SubPanelController();
        
    })().init();