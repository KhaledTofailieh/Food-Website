$(document).ready(function() {
	
	// Bar Chart
    var sales_data = document.getElementById("charts").getAttribute("sales_data");
    var sales_data = JSON.parse(sales_data);
    var rests_data = document.getElementById("charts").getAttribute("rests_data");
    var rests_data = JSON.parse(rests_data);

	var barChartData = {
		labels: sales_data["place"],
		datasets: [{
			label: 'Dataset 1',
			backgroundColor: 'rgba(0, 158, 251, 0.5)',
			borderColor: 'rgba(0, 158, 251, 1)',
			borderWidth: 1,
			data: sales_data['sales']
		}]
	};
//{
//			label: 'Dataset 2',
//			backgroundColor: 'rgba(255, 188, 53, 0.5)',
//			borderColor: 'rgba(255, 188, 53, 1)',
//			borderWidth: 1,
//			data: [28, 48, 40, 19, 86, 27, 90]
//		}

//	alert(sales_data)
//    console.log(sales_data)
	var ctx = document.getElementById('bargraph').getContext('2d');
	window.myBar = new Chart(ctx, {
		type: 'bar',
		data: barChartData,
		options: {
			responsive: true,
			legend: {
				display: false,
			}
		}
	});

	// Line Chart

	var lineChartData = {
		labels: rests_data["name"],
		datasets: [{
		label: "My Second dataset",
		backgroundColor: "rgba(255, 188, 53, 0.5)",
		fill: true,
		data: rests_data["orders"]
		}]
	};
	
	var linectx = document.getElementById('linegraph').getContext('2d');
	window.myLine = new Chart(linectx, {
		type: 'bar',
		data: lineChartData,
		options: {
			responsive: true,
			legend: {
				display: false,
			},
//			tooltips: {
//				mode: 'index',
//				intersect: false,
//			}
		}
	});
	
	// Bar Chart 2
	
    barChart();
    
    $(window).resize(function(){
        barChart();
    });
    
    function barChart(){
        $('.bar-chart').find('.item-progress').each(function(){
            var itemProgress = $(this),
            itemProgressWidth = $(this).parent().width() * ($(this).data('percent') / 100);
            itemProgress.css('width', itemProgressWidth);
        });
    };
});