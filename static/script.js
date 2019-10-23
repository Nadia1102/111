/* globals Chart:false, feather:false */

(function () {
  'use strict'

  feather.replace()

  // Graphs
  var ctx = document.getElementById('myChart')
  // eslint-disable-next-line no-unused-vars
  var myChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: [
        'Sunday',
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday'
      ],
      datasets: [{
        data: [
          15339,
          21345,
          18483,
          24003,
          23489,
          24092,
          12034
        ],
        lineTension: 0,
        backgroundColor: 'transparent',
        borderColor: '#007bff',
        borderWidth: 4,
        pointBackgroundColor: '#007bff'
      }]
    },
    options: {
      scales: {
        yAxes: [{
          ticks: {
            beginAtZero: false
          }
        }]
      },
      legend: {
        display: false
      }
    }
  })
}())




async function fetch_json(request) {
    return await (await fetch(request)).json();
}

async function load_db_names() {
    const response = await fetch_json('api/databases');
    console.log(response);

    <div class="btn-group">
  <button type="button" class="btn btn-danger">Action</button>
  <button ">
    <span class="sr-only">Toggle Dropdown</span>
  </button>
  <div class="dropdown-menu">
    <a class="dropdown-item" href="#">Action</a>
    <a class="dropdown-item" href="#">Another action</a>
    <a class="dropdown-item" href="#">Something else here</a>
    <div class="dropdown-divider"></div>
    <a class="dropdown-item" href="#">Separated link</a>
  </div>
</div>


    for (db_name of response) {
        var button_group = $('<div/>', {
            class: "btn-group"
        });

        button_group.appendChild($('<button/>',{
            type:"button",
            class:"btn btn-danger",
            click: load_table_names(db_name)
        }));

        button_group.appendChild($('<button/>',{
            type:"button",
            class:"btn btn-danger dropdown-toggle dropdown-toggle-split",
            "data-toggle": "dropdown",
            "aria-haspopup": "true",
            "aria-expanded": false
        }));

        var dropdown_menu = $('<button/>',{
            class:"dropdown-menu"
        });
        dropdown_menu.appendChild($('<a/>', {
            class: "dropdown-item",
            onclick: console.log(db_name),
            text: "Edit"
        }));

        dropdown_menu.appendChild($('<a/>', {
            class: "dropdown-item",
            color: "#aa0000",
            onclick: console.log(db_name),
            text: "Delete"
        }));

        button_group.appendChild(dropdown_menu);
        var database_button = $('<div/>',
            {
                text: db_name,
                click: function () {
                    load_table_names(db_name)
                }
            });
        $("#main").append(button_group);
    }
}

async function load_table_names(db_name) {
    const response = await fetch_json(`api/databases/${db_name}`);
    console.log(response);
    for (table_name of response["table_names"]) {
        var table_button = $('<button/>',
            {
                text: table_name,
                click: function () {
                    load_table(table_name)
                }
            });
        $("#main").append(table_button);
    }
}