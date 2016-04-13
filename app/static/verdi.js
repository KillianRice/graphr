var plotData = []
var plotstyle = {
    margin : { t : 10, r : 0, b : 30 },
    legend : { x : 0.05, y : 0.95},
    showlegend : true,
    width : '85%',
}
var totalHeight = 90;
var maxplots = 6;

var gettingData = null;

// master list of items to get from the server
var allItems = ['Current (A)', 'Baseplate Temp (C)', 'Diode 1 Heatsink Temp (C)', 'Diode 2 Heatsink Temp (C)', 'Diode 1 Current (A)', 'Diode 2 Current (A)', 'Diode 1 Photocell Voltage (V)', 'Diode 2 Photocell Voltage (V)', 'Etalon Temp (C)', 'Vanadate Temp (C)', 'Diode 1 Temp (C)'
, 'Diode 2 Temp (C)', 'LBO Temp (C)'] 
var plotItems = {
                    // the items to be plotted on each plot (denoted by its plotID) 
                    plotNum1 : ['Current (A)', 'Diode 1 Current (A)', 'Diode 2 Current (A)'],
                    plotNum2 : ['Diode 1 Temp (C)', 'Diode 2 Temp (C)', 'Diode 1 Heatsink Temp (C)', 'Diode 2 Heatsink Temp (C)'],
                    plotNum3 : ['Diode 1 Photocell Voltage (V)', 'Diode 2 Photocell Voltage (V)'],
                    plotNum4 : ['Baseplate Temp (C)', 'Etalon Temp (C)', 'Vanadate Temp (C)'],
                    plotNum5 : ['LBO Temp (C)']
                } 
var numPlots = 5;
// initialize all of the plot data for each parameter
var plotData = {} 
for (i=0; i<allItems.length; i++){
    plotData[allItems[i]] = { x : [], y : [] , name : allItems[i]}
}


var interval = 1 //default interval in minutes
function getms(interval){
    return interval * 60 * 1000
}

var interval_ms = getms(interval)

var request_interval = 500 // time between requests in ms

$( function(){

    for (i=0; i<numPlots; i++){
        // define the html attributes of the plot
        var plotID = 'plotNum'+(i+1);
        var plotdiv = '<div class="plot" id="' + plotID + '"></div>';
        
        // add the html to the document appropriately
        if (i == 0){
            $('div#plots').html(plotdiv)
        } else {
            $('div#plots').append(plotdiv)
        }
        
        // get what data belongs to the plot
        var theData = []
        for (j=0; j<plotItems[plotID].length; j++){
            theData.push(plotData[plotItems[plotID][j]]);
        }

        // create the plot!
        Plotly.newPlot(plotID, theData, plotstyle);
    } 
    
    
    // resize the plots to fit the page
    if (numPlots <= maxplots){
        $('div.plot').height(totalHeight / numPlots +'%');
        plotstyle['height'] = totalHeight / numPlots + '%';

        for (i=1; i<=numPlots; i++){
            Plotly.relayout('plotNum'+i, plotstyle);
        }
    } else {
        //$('div.plot').height(totalHeight / maxplots + '%');
        //plotstyle['height'] = totalHeight / maxplots + '%';
        Plotly.relayout(plotID, plotstyle);
    }
    
    $('select#interval').change( function(){
        console.log('old value: ' +interval)
        var value = $(this).val();
        switch (value){
            case '1 min':
                interval = 1;
                break;
            case '5 min':
                interval = 5;
                break;
            case '10 min':
                interval = 10;
                break;
            case '30 min':
                interval = 30;
                break;
            case '60 min':
                interval = 60;
                break;
            case 'All time':
                interval = 0;
                break;
        }
        interval_ms = getms(interval);
        console.log('new value: '+interval)
    });

    $('select#update').change( function(){
        var value = $(this).val();
        switch(value){
            case '500 ms':
                request_interval = 500;
                break;
            case '1 second':
                request_interval = 1000;
                break;
            case '5 seconds':
                request_interval = 5000;
                break;
            case '10 seconds':
                request_interval = 10000;
                break;
        }
    });
    $('button#get_data').click( function(){
        gettingData = setInterval( function(){
            $.getJSON('/get_json',
            {
                n : numPlots,
                i : allItems
            })
            .done( function(data){
                //console.log(data);

                // Extract the new data from the server's response
                for (i=0; i<allItems.length; i++){
                    var last = plotData[allItems[i]]['x'].length - 1;
                    plotData[allItems[i]]['x'].push( data['x'] );
                    plotData[allItems[i]]['y'].push( data[allItems[i]] );
                }
                
                // loop over the plots and update them
                
                var now = Date.parse(data['x']);

                console.log(now - Date.parse(plotData[allItems[0]]['x'][0]))
                if ( interval_ms > now - Date.parse(plotData[allItems[0]]['x'][0]) || interval_ms == 0){
                    var before = Date.parse(plotData[allItems[0]][0]);
                } else {
                    var before = now - interval_ms;
                }

                nowStr = now.toString()
                beforeStr = before.toString()
                
                plotstyle['xaxis'] = {range : [beforeStr, nowStr]}
                for (i=0; i<numPlots; i++) {
                    plotID = 'plotNum'+(i+1);
                    Plotly.redraw(plotID, plotstyle);
                }
                 
            });
        }, request_interval);
    });

    $('button#stop').click( function(){
        // stops sending data requests to the server
        clearInterval(gettingData);
    });

    $('button#clear').click( function(){
        // stops sending requests
        clearInterval(gettingData);
        
        // sets all data to nothing
        for (i=0; i<allItems.length; i++){
            plotData[allItems[i]]['x'] = [];
            plotData[allItems[i]]['y'] = [];
        }

        // resumes data collection
        $('button#get_data').click()
    });

 });







