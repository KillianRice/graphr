var plotData = []
var plotstyle = {
    margin : { t : 10, r : 0, b : 40 },
    legend : { x : 0, y : 1}
}
var totalHeight = 90;
var maxplots = 6;

var gettingData = null;

var allItems = [] // master list of items to get from the server
var plotItems = {} // the items to be plotted on each plot (denoted by its plotID)
var plotData = {} // the data for each of the items in allItems

var interval = 1 //minutes
var interval_ms = interval * 60 * 1000;

$( function(){
    

    var numPlots = 0;
    //Plotly.newPlot('plotNum1',data);
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
                    
                    /* if (plotData[allItems[i]]['y'].length > 0)
                    {
                        var newpoint = plotData[allItems[i]]['y'][last] + data[allItems[i]];
                        plotData[allItems[i]]['y'].push(newpoint);
                    } else {
                        plotData[allItems[i]]['y'].push( data[allItems[i]]);
                    } */
                }
                
                // loop over the plots and update them
                
                var now = Date.parse(data['x']);

                console.log(now - Date.parse(plotData[allItems[0]]['x'][0]))
                if ( interval_ms > now - Date.parse(plotData[allItems[0]]['x'][0])){
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
        }, 500);
    });

    $('button#stop').click( function(){
        clearInterval(gettingData);
    });

    $('button#clear').click( function(){
        clearInterval(gettingData);
        for (i=0; i<allItems.length; i++){
            plotData[allItems[i]]['x'] = [];
            plotData[allItems[i]]['y'] = [];
        }
        $('button#get_data').click()
    });

    $('#add_plot').click( function(){

        // Figure out what items belong to this plot
        var items = []
        var someChecked = false;
        $('.plot_item').each( function(){
            if($(this).is(":checked")) {
                //console.log($(this).attr('name'));
                items.push($(this).attr('name'));
                someChecked = true;
                $(this).prop('checked', false);
            }
        });

        if (someChecked){

            // check that the items are in the master list
            for (i=0; i<items.length; i++){
                console.log($.inArray(items[i],allItems))
                if ($.inArray(items[i],allItems) == -1){
                    allItems.push(items[i]);
                    plotData[items[i]] = {
                        x       : [],
                        y       : [],
                        name    : items[i]
                    };
                }
            }
            
            console.log(allItems)
            // create the plot
            numPlots++;
            var plotID = 'plotNum' + (numPlots);
            var plotdiv = '<div class="plot" id="' + plotID + '"></div>';
            plotItems[plotID] = items;

            if (numPlots == 1){
                $('div#plots').html(plotdiv)
            } else {
                $('div#plots').append(plotdiv)
            }
            
            var theData = []
            for (i=0; i<items.length; i++){
                theData.push(plotData[items[i]]);
            }
            Plotly.newPlot(plotID, theData, plotstyle);

            
            if (numPlots <= maxplots){
                $('div.plot').height(totalHeight / numPlots +'%');
                plotstyle['height'] = totalHeight / numPlots + '%';

                for (i=1; i<=numPlots; i++){
                    Plotly.relayout('plotNum'+i, plotstyle);
                }
            } else {
                //$('div.plot').height(totalHeight / maxplots + '%');
                //plotstyle['height'] = totalHeight / maxplots + '%';
                PLotly.relayout(plotID, plotstyle);
            }
        }
            
    });

    

 });







