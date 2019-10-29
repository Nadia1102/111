import json
import os
from .schema import Schema
from .table import Table
from .utils import get_filename

def format_file_name(table_name):
    return table_name


class Database:

    def __init__(self, table_names):
        self._tables_map = {}
        for name in table_names:
            self._tables_map[name] = None

    def save_database_info(self):
        json.dump(self._tables_map.keys(), '.database-info')

    def create_table(self, table_name, schema):
        table = Table(table_name, schema)
        self._tables_map[table_name] = table
        self.save_database_info()

    def load_table(self, table_name):
        self._tables_map = Table.create_from_json(json.load(format_file_name(table_name)))

    def get_table(self, db_name, table_name):
        d = json.load(open(get_filename(db_name, table_name),'r'))
        s = Schema(d['_schema'])

        t = Table(d['_table_name'], s)
        t._column_dict = d['_column_dict']
        self._tables_map[table_name] = t

        return self._tables_map[table_name]

    def save_table(self, table_name):
        json.dump(self._tables_map[table_name].to_json(), format_file_name(table_name))
        self._tables_map[table_name] = None

    def delete_table(self, table_name):
        os.remove(format_file_name(table_name))
        self._tables_map.pop(table_name)
        self.save_database_info()