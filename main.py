from flask import Flask, jsonify, render_template, flash, request, redirect, url_for
import DatabaseManager.database

from flask_restplus import Api, Resource, fields

import json

app = Flask(__name__)

class DatabaseManager:
    _databases = ['Animals', 'Friends']

    def get_database_names(self):
        return self._databases


db_manager = DatabaseManager()


@app.route("/")
def hello():
    return render_template('index.html')


@app.route("/api/databases", methods=['GET'])
def get_database_names():
    return jsonify(db_manager.get_database_names())


@app.route('/api/databases/<string:db_name>', methods=['GET'])
def get_databse(db_name):
    db = db_manager.get_database(db_name)
    return jsonify(db.get_table_names)


@app.route('/api/databases/<string:db_name>', methods=['POST'])
def create_database(db_name):
    message = db_manager.create_database(db_name)
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

# def detect_objects(image):
#     return image
#
# @app.route('/upload-image', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         print(request.files)
#         if 'image' not in request.files:
#             flash('No image part')
#             return redirect(request.url)
#
#         file = request.files['image']
#
#         if file.filename == '':
#             flash('No selected file')
#             return redirect(request.url)
#
#         if file and allowed_file(file.filename):
#             filename = secure_filename(file.filename)
#
#             file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#             file.save(file_path)
#
#             detector.detect_image(file_path)
#
#             return redirect(url_for('uploaded_file',
#                                     filename=filename))
#     return '''
#     <!doctype html>
#     <title>Upload new File</title>
#     <h1>Upload new File</h1>
#     <form method=post enctype=multipart/form-data>
#       <input type=file name=file>
#       <input type=submit value=Upload>
#     </form>
#     '''
#
# from flask import send_from_directory
#
# @app.route('/uploads/<filename>')
# def uploaded_file(filename):
#     return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
#
