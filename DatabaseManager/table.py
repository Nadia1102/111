from .column import Column, ColumnType
from .schema import Schema
import json

class Row:
    _data = []
    _schema = None

    def __init__(self, schema : Schema, data : list):
        self._schema = schema
        self._data = data

    @property
    def data(self):
        return self._data

    @property
    def schema(self):
        return self._schema

class Table:
    def __init__(self, table_name, schema : Schema):
        self._table_name = table_name
        self._schema = schema
        self._column_dict = {}

        for column_name, column_type in self._schema.schema_list:
            self._column_dict[column_name] = []

    @property
    def table_name(self):
        return self._table_name

    @property
    def schema(self):
        return self._schema

    def add_row(self, row : Row):
        if row.schema != self._schema:
            raise Exception('Incorrect schema')

        for (c_name, c_type), entry in zip(self._schema.schema_list, row.data):
            self._column_dict[c_name].append(entry)

    def delete_row(self, row_index):
        for column_name in self._schema.get_list():
            self._column_dict[column_name].remove(row_index)

    def get_column(self, column_name):
        if column_name in self._column_dict:
            return self._column_dict[column_name]
        raise "Column with name {} doesn't exist".format(column_name)

    def add_column(self, column_name: str, column: Column, position = None):
        if column_name in self._column_dict:
            raise "Column with name {} already exist".format(column_name)

        self._schema.insert(position, column_name)
        self._column_dict[column_name] = column

    def rename_column(self, old_column_name: str, new_column_name: str) -> None:
        if not old_column_name in self._column_dict:
            raise "Column with name {} doesn't exist".format(old_column_name)

        if new_column_name in self._column_dict:
            raise "Column with name {} doesn't exist".format(old_column_name)

        self._column_dict[new_column_name] = self._column_dict.pop(old_column_name)

    def delete_column(self, column_name: str) -> None:
        if not column_name in self._column_dict:
            raise "Column with name {} doesn't exist".format(column_name)

        self._column_dict.pop(column_name)

    def save_database(self):
        json.dump(self, self.table_name + '.table')

    @classmethod
    def from_json(cls, data):
        table = cls(data['_table_name'], data['_schema'])
        for key, value in data['_column_dict']:
            table._column_dict[key] = Column(value['_column_type'])
        students = list(map(Student.from_json, data["students"]))
        return cls(students)


    # def get_table_projection(self, row_indices = None, column_names = None):
    #     if row_indices is None:
    #         row_indices = list(range(self._column_size))
    #
    #     result_table = Table()
    #     for column_name in column_names:
    #         column = self.get_column(column_name)
    #         result_table.add_column(column_name, column.get_projection(row_indices))
    #     return result_table