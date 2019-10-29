from .database import Database
from .utils import get_filename
import jsonpickle


import json

class TinyDB:

    def __init__(self):
        self._databases = json.load(open('data/_info.json'))
        self._db_registry = {}

    def get_all(self):
        return self._databases

    def get(self, db_name):
        self._load_database(db_name)
        return self._db_registry[db_name]

    def create(self, db_name):
        self._databases.append(db_name)

    def delete(self, db_name):
        pass

    def _create_database_file(self, db_name):
        pass

    def _load_database(self, db_name):
        with open(get_filename(db_name)) as f:
            print(db_name)
            txt = f.read()
            print(txt)
            d = json.loads(txt)
            print(d["table_names"])
            db = Database(d["table_names"])
            print("> ", list(db._tables_map.keys()))
            self._db_registry[db_name] = db
            print(self._db_registry[db_name])

    def _save_database(self, db_name):
        with open(get_filename(db_name)) as f:
            db = self._db_registry[db_name]
            json_object = jsonpickle.encode(db)
            f.write(json_object)
            print("SAVE", db_name, db._tables_map.keys())