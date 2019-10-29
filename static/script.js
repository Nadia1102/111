async function fetch_json(request) {
    return await (await fetch(request)).json();
}


async function CreateButton(name, click_function, delete_click_function) {
    console.log(name);
    var button_group = $('<div/>', {
        class: "btn-group",
        style: "margin:5px"
    });

    button_group.append($('<button/>', {
        type: "button",
        class: "btn btn-primary",
        text: name,
        click: function () {
            click_function()
        },
    }));

    button_group.append($('<button/>', {
        type: "button",
        class: "btn btn-primary dropdown-toggle dropdown-toggle-split",
        "data-toggle": "dropdown",
        "aria-haspopup": "true",
        "aria-expanded": false
    }));

    var dropdown_menu = $('<button/>', {
        class: "dropdown-menu"
    });

    dropdown_menu.append($('<a/>', {
        class: "dropdown-item",
        click: function () {
            delete_click_function()
        },
        text: "Delete"
    }));

    button_group.append(dropdown_menu);
    return button_group
}


async function load_db_names() {
    const response = await fetch_json('api/databases');
    $("#databases-list").empty();
    console.log(response);

    for (db_name of response) {
        button = await CreateButton(db_name,
            function (name) {
                return () => load_table_names(name)
            }(db_name),
            function (name) {
                return () => delete_database(name)
            }(db_name),
        );
        $("#databases-list").append(button);
    }
    // <button class="btn btn-outline-secondary" type="button">Create</button>
}

async function delete_database(db_name) {

}

async function load_table_names(db_name) {
    const response = await fetch_json(`api/databases/${db_name}`);
    console.log(db_name, response);

    $("#tables-list").empty();
    for (table_name of response) {
        button = await CreateButton(table_name,
            function (d, t) {
                return () => load_table(d, t)
            }(db_name, table_name),
            function (d, t) {
                return () => delete_table(d, t)
            }(db_name, table_name)
        );
        $("#tables-list").append(button);
    }
}

async function load_table(db_name, table_name) {
    const response = await fetch_json(`api/databases/${db_name}/tables/${table_name}`);

    $("#table-responsive").empty();

    $("#table-responsive").append($("<h2/>").text(response['_table_name']));

    var table = $("<table/>", {
        class: "table table-striped table-sm"
    });
    let thead = $("<thead\>");
    let tr = $("<tr\>");
    let _schema = response['_schema'];
    for (obj of _schema) {
        tr.append($("<th/>").text(obj[0]));
    }
    table.append(thead.append(tr));

    let tbody = $("<tbody\>");
    let dict = response['_column_dict'];
    console.log(dict);
    let table_len = Math.min.apply(Math, $.map(dict, function(value, key) { return value.length }));
    console.log(table_len);
    for (let i = 0; i < table_len; i++) {
        let tr = $("<tr/>");
        for (obj of _schema) {
            tr.append($("<td/>").text(response['_column_dict'][obj[0]][i]));
        }
        tbody.append(tr);
    }
    table.append(tbody);
    $("#table-responsive").append(table);
    console.log(response)
}

async function delete_table(db_name, table_name) {
    console.log("Delete", db_name, table_name);
}

