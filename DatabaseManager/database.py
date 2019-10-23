import json
import os
from .table import Table

def format_file_name(table_name):
    return table_name


class Database:
    _database_name = ""
    _tables_map = {}

    def __init__(self):
        self.load_database_info()

    def load_database_info(self):
        table_names = json.load('.database-info')
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

    def get_table(self, table_name):
        return self._tables_map[table_name]

    def save_table(self, table_name):
        json.dump(self._tables_map[table_name].to_json(), format_file_name(table_name))
        self._tables_map[table_name] = None

    def delete_table(self, table_name):
        os.remove(format_file_name(table_name))
        self._tables_map.pop(table_name)
        self.save_database_info()