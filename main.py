from flask import Flask, render_template
from DatabaseManager.tiny_db import TinyDB
from DatabaseManager.JsonEncoder import RestEncoder

import json

app = Flask(__name__)

db_manager = TinyDB()

def jsonify(obj):
    return json.dumps(obj, cls=RestEncoder)

@app.route("/")
def hello():
    return render_template('index.html')


@app.route("/api/databases", methods=['GET'])
def get_database_names():
    return jsonify(db_manager.get_all())


@app.route('/api/databases/<string:db_name>', methods=['GET'])
def get_databse(db_name):
    db = db_manager.get(db_name)
    return jsonify(db)


@app.route('/api/databases/<string:db_name>', methods=['POST'])
def create_database(db_name):
    message = db_manager.create(db_name)
    return jsonify(message)


@app.route('/api/databases/<string:db_name>', methods=['DELETE'])
def delete_database(db_name):
    message = db_manager.delete(db_name)
    return jsonify(message)


@app.route('/api/databases/<string:db_name>/tables', methods=['GET'])
def get_all_tables(db_name):
    db = db_manager.get_database(db_name)
    return jsonify(db.get_all_tables())


@app.route('/api/databases/<string:db_name>/tables/<string:table_name>', methods=['GET'])
def get_table(db_name, table_name):
    db = db_manager.get_database(db_name)
    table = db.get_table(table_name)
    return jsonify(table)


@app.route('/api/databases/<string:db_name>/tables/<string:table_name>', methods=['POST'])
def create_table(db_name, table_name):
    db = db_manager.get_database(db_name)
    message = db.create_table(table_name)
    return jsonify(message)


@app.route('/api/databases/<string:db_name>/tables/<string:table_name>', methods=['DELETE'])
def delete_table(db_name, table_name):
    db = db_manager.get_database(db_name)
    message = db.delete_table(table_name)
    return jsonify(message)


if __name__ == "__main__":
    app.run(debug=True)