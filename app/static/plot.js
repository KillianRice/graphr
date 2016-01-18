var plotData = []
var plotstyle = {
    margin : { t : 10, r : 0, b : 40 }
}
var totalHeight = 90;
var maxplots = 6;

var gettingData = null;

$( function(){
    
    var numPlots = 0;
    //Plotly.newPlot('plotNum1',data);
    $('button#get_data').click( function(){

            gettingData = setInterval( function(){

                while (plotData.length < numPlots) {
                    plotData.push( { x:[], y:[] });
                }

                $.getJSON('/get_json',
                    { n : numPlots })
                    .done( function(data){
                        var last = 0;
                        for (i=0; i<numPlots; i++){
                            last = plotData[i]['y'].length-1;
                            plotData[i]['x'].push(data['x']);
                            if (last < 0){
                                plotData[i]['y'].push(data['y'][i]);
                            } else {
                                var newpoint = plotData[i]['y'][last] + data['y'][i];
                                plotData[i]['y'].push(newpoint);
                            }
                            Plotly.redraw('plotNum'+(i+1), plotstyle);
                        }
                    });

                //Plotly.redraw('plotNum1');
            
            } , 100);
        
        });

    $('button#add_plot').click( function(){

        numPlots++;
        var plotID = 'plotNum' + (numPlots);
        var plotdiv = '<div class="plot" id="' + plotID + '"></div>';

        if (numPlots == 1){
            $('div#plots').html(plotdiv)
        } else {
            $('div#plots').append(plotdiv)
        }
        
        if (plotData.length < numPlots){
            plotData.push( { x : [], y : [] } );
        }
        Plotly.newPlot(plotID, [plotData[numPlots-1]], plotstyle);

        
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

        $('button#stop').click( function(){
            clearInterval(gettingData);
        });

        $('button#clear').click( function(){
            clearInterval(gettingData);
            for (i=0; i<numPlots; i++){
                plotData[i]['x'] = [];
                plotData[i]['y'] = [];
            }
            $('button#get_data').click()
        });
    });
 });







