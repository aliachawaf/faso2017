/*
Chart.js will want it's bar chart data to be formatted like this, so after we get our JSON result from Flex.io, we'll use Lodash to reformat it to match what Chart.js is expecting:
var barChartData = {
  labels: ["January", "February", "March", "April", "May", "June", "July"],
  datasets: [{
    label: 'Dataset 1',
    backgroundColor: color(window.chartColors.red).alpha(0.5).rgbString(),
    borderColor: window.chartColors.red,
    borderWidth: 1,
    data: [...]
  }, {
    label: 'Dataset 2',
    backgroundColor: color(window.chartColors.blue).alpha(0.5).rgbString(),
    borderColor: window.chartColors.blue,
    borderWidth: 1,
    data: [...]
  }]
}
*/

function getRandomColor() {
  var letters = '0123456789ABCDEF'.split('');
  var color = '#';
  for (var i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random() * 16)];
  }
  return color;
}

$.ajax({
  type: 'post',
  url: 'https://www.flex.io/api/v1/pipes/flexio-chart-js-csv-to-json/run?stream=0',
  beforeSend: function(xhr) {
    xhr.setRequestHeader('Authorization', 'Bearer nmgzsqppgwqbvkfhjdjd');
  },
  data: $('form').serialize(),
  dataType: "json",
  success: function(content) {
    // render the JSON result from from the Flex.io pipe
    $("#flexio-result-data").text(JSON.stringify(content, null, 2))

    var first_item = _.get(content, '[0]', {})

    var column_labels = _.map(_.omit(first_item, ['os']), function(val, key) {
      if (key != 'os')
        return key
    })

    // use Lodash to reformat the JSON for use with Chart.js
    var datasets = _.map(content, function(item) {
      // use the 'os' column as our label
      var item_label = _.get(item, 'os', 'Not Found')

      // create an array of number values from each item's JSON object
      var item_values = _.map(_.omit(item, ['os']), function(val) {
        return parseFloat(val)
      })

      return {
        label: item_label,
        data: item_values,
        backgroundColor: getRandomColor()
      }
    })

    var chart_data = {
      labels: column_labels,
      datasets: datasets
    }

    // render the JSON result after mapping the data with Lodash
    $("#chart-data").text(JSON.stringify(chart_data, null, 2))

    // render the chart using Chart.js
    var ctx = document.getElementById("canvas").getContext("2d");
    window.my_chart = new Chart(ctx, {
      type: 'bar',
      data: chart_data,
      options: {
        responsive: true,
        legend: {
          position: 'top'
        },
        title: {
          display: true,
          text: 'Use Flex.io to Create a Chart With Chart.js Directly From a CSV File'
        }
      }
    });
  }
});