
var diameter = 300;
var color = d3.scaleOrdinal(d3.schemeCategory20);

var svg_1 = d3.select("#visualisation-2").append("svg")
            .attr("width", 500)
            .attr("height", 300)
            .attr("class", "bubble");

d3.json("data_3.json", function(error, dataset) {
    if(error) throw error;

    console.log(dataset)

        var bubble = d3.pack()
            .size([diameter, diameter])
            .padding(1.5);

        var nodes = d3.hierarchy(dataset)
            .sum(function(d) { return d.Count; });

        var node = svg_1.selectAll(".node")
            .data(bubble(nodes).descendants())
            .enter()
            .filter(function(d){
                return  !d.children
            })
            .append("g")
            .attr("class", "node")
            .attr("transform", function(d) {
                return "translate(" + d.x + "," + d.y + ")";
            });

        node.append("title")
            .text(function(d) {
                return d.Name + ": " + d.Count;
            });

        node.append("circle")
            .attr("r", function(d) {
                return d.r;
            })
            .style("fill", function(d,i) {
                return color(i);
            });

        node.append("text")
            .attr("dy", ".2em")
            .style("text-anchor", "middle")
            .text(function(d) {
                return d.data.Name.substring(0, d.r / 3);
            })
            .attr("font-family", "sans-serif")
            .attr("font-size", function(d){
                return d.r/5;
            })
            .attr("fill", "white");

        node.append("text")
            .attr("dy", "1.3em")
            .style("text-anchor", "middle")
            .text(function(d) {
                return d.data.Count;
            })
            .attr("font-family",  "Gill Sans", "Gill Sans MT")
            .attr("font-size", function(d){
                return d.r/5;
            })
            .attr("fill", "white");

        d3.select(self.frameElement)
            .style("height", diameter + "px");
});