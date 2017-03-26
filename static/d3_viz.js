"use strict";

$.get('/get_data.json', function(data) {
    console.log(data['response_data']);

    var div = d3.select('body').append('div')
        .attr('class', 'tooltip')
        .style('opacity', 0)

    var svg = d3.select("svg");

    var x_all_coord = [];
    var x_all_data = [];

    var y_all_coord = [];
    var y_all_data = [];
    
    var r_all_coord = [];
    var r_all_data = [];

    var names =[];

    setTimeout(function() {
        console.log(data['columns'])
        var state_data = data['response_data']
        var x_axis = data['columns']['x_axis']
        var y_axis = data['columns']['y_axis']
        var bubble = data['columns']['bubble']

        for (var i = 0; i < 50; i++) {
            // console.log('Beginning new iteration of loop.')
            x_all_data.push(state_data[i][x_axis])
            y_all_data.push(state_data[i][y_axis])
            r_all_data.push(state_data[i][bubble])
            names.push(state_data[i]['state_name'])
        } 

        var x_max = Math.max(...x_all_data);
        var x_min = Math.min(...x_all_data);

        var y_max = Math.max(...y_all_data);
        var y_min = Math.min(...y_all_data);

        var r_max = Math.max(...r_all_data);
        var r_min = Math.min(...r_all_data);

        for (i = 0; i < 50; i++) {
            x_all_coord.push((state_data[i][x_axis] - x_min) / x_max * 1000) 
            y_all_coord.push(500 - ((state_data[i][y_axis] - y_min) / y_max * 1000))
            r_all_coord.push((state_data[i][bubble] - r_min) / r_max * 100)
        }


        var circle = svg.selectAll("circle")
                        .data(r_all_coord)
                        .enter().append("circle")
                            .attr("cx", function(d, i) { return x_all_coord[i]; })
                            .attr("cy", function(d, i) { return y_all_coord[i]; })
                            .attr("r", function(d) { return d; })
                            // .style("fill", "gray");
                            .style("fill", function(d) {
                                if (d < 10) { return "#1A3507"; }
                                else if (d < 20) { return "#48841E"; }
                                else if (d < 30) { return "#6ED129"; }
                                else { return "#A8F970"; } 
                            })
                            .on('mouseover', function(d, i){ 
                                console.log(div);
                                div.transition().style('opacity', 1.0);
                                div.html("<strong>" + names[i] + "</strong> " + d)
                                    .style('left', d3.event.pageX + "px")
                                    .style('top', d3.event.pageY + "px");
                            }) 
                            .on('mouseout', function(d, i) {
                                div.transition().style('opacity', 0)
                            });

        var text = svg.selectAll('text')
                        .data(names)
                        .enter().append('text')
                            .attr('x', function(d, i) { return x_all_coord[i]; })
                            .attr('y', function(d, i) { return y_all_coord[i]; })
                            .text( function(d, i) { return names[i]; })
                                .attr('font-size', '12px')
                                .attr('font-family', 'sans-serif')
                                .attr('text-anchor', 'middle');


        circle.style("opacity", 0.5);

    }, 1000);
    
});

