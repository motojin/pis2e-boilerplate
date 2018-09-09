(function(ext) {		            
    // initially set status to yellow
    var extStatus = 1;
    
    // Cleanup function when the extension is unloaded
    ext._shutdown = function() {};

    // Status reporting code
    // Use this to report missing hardware, plugin or unsupported browser
    ext._getStatus = function() {
        return {status: extStatus, msg: 'Ready'};
    };

    // added function to support the Start The Program block
    ext.changeStatusGreen = function() {
        extStatus = 2;
    };

    // Block and block menu descriptions
    var descriptor = {
        blocks: [
	    // Block type, Block name, Function name
	    [" ", "Start The Scratch2 Extension", "changeStatusGreen"]
        ]
    };

    // Register the extension
    ScratchExtensions.register('pis2e by motojin', descriptor, ext);
})({});
