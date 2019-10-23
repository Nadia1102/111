async function fetch_json(request) {
    return await (await fetch(request)).json();
}

async function load_db_names() {
    const response = await fetch_json('api/databases');
    console.log(response);
    for(db_name of response){
        $("#main").append(db_name);
    }
}

async function load_table_names(db_name) {
    const response = await fetch_json(`api/databases/${db_name}`);
    console.log(response.json());
}