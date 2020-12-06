const qt = document.getElementById('quantityField')
var index = 0

var dados = [{
    color_name: "",
    hex_value: "",
}];

var position = [{
    x: -1,
    y: -1
}]



chart_config = {
    scales: {
        yAxes: [{
            ticks: {
                max: 10000,
                min: 0,
                stepSize: 1
            },
            stacked: false,
        }],
        xAxes: [{
            ticks: {
                max: 100,
                min: 0,
                stepSize: 1
            }
        }]
    },
    legend: false,
};


var ctx = document.getElementById('colorGraph').getContext('2d');
var colorChart = new Chart(ctx, {
    type: 'scatter',
    data: {
        datasets: [{
            label: 'Position',
            data: position,
            backgroundColor: 'rgb(255, 99, 132)',
            borderColor: 'rgb(255, 99, 132)',
        }]
    },
    options: chart_config,
});

function addData(datax) {
    var raw = JSON.parse(datax);
    var extra = JSON.parse(raw)


    dados.push(extra[0])
    position.push({
        x: extra[0]['x'],
        y: extra[0]['y']
    }
    )
    colorChart.update();
    index = index + 1
    console.log(dados[index]['color_name'])
    document.body.style.backgroundColor = dados[index]['hex_value'];
}

function callRequestData() {
    quantity = parseInt(qt.value)
    console.log(quantity)
    for (i = 0; i < quantity; i++) {
        setTimeout(requestToServer(), 100)

    }
}

function requestToServer() {

    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            addData(this.responseText);
        }
    };
    xhttp.open("GET", "/request_data", true);
    xhttp.send();

}


