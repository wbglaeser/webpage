var svg = d3.select("#visualisation-1"),
    margin = {top: 10, right: 10, bottom: 10, left: 40},
    width = +svg.attr("width") - margin.left - margin.right,
    height = +svg.attr("height") - margin.top - margin.bottom;

var x = d3.scaleBand().rangeRound([0, width]).padding(0.1),
    y = d3.scaleLinear().rangeRound([height, 0]);

var g = svg.append("g")
.attr("transform", "translate(" + margin.left + "," + margin.top + ")");


d3.json("data.json", function(data) {

    console.log(data)

    x.domain(data.map(function(d) { return d.x_data; }));
    y.domain([0, d3.max(data, function(d) { return d.y_data; })]);

    g.append("g")
      .attr("class", "axis axis--x")
      .attr("transform", "translate(0," + height + ")")
      .call(d3.axisBottom(x));

    g.append("g")
      .attr("class", "axis axis--y")
      .call(d3.axisLeft(y).ticks(10, "%"))
        .append("text")
        .attr("transform", "rotate(-90)")
        .attr("y", 6)
        .attr("dy", "0.71em")
        .attr("text-anchor", "end")
        .text("Frequency");

    g.selectAll(".bar")
      .data(data)
      .enter().append("rect")
        .attr("class", "bar")
        .attr("x", function(d) { return x(d.x_data); })
        .attr("y", function(d) { return y(d.y_data); })
        .attr("width", x.bandwidth())
        .attr("height", function(d) { return height - y(d.y_data); });
});


