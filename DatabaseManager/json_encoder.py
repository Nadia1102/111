from .schema import Schema
from .table import Table
from .database import Database
from .column import Column, ColumnType

import json


class RestEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Schema):
            return obj.schema_list

        if isinstance(obj, Table):
            return {"_table_name": obj._table_name,
                    "_schema": obj._schema,
                    "_column_dict": obj._column_dict}

        if isinstance(obj, Database):
            return list(obj._tables_map.keys())

        if isinstance(obj, ColumnType):
            return obj.name, obj.value

        if isinstance(obj, Column):
            return obj.__dict__

        return json.JSONEncoder.default(self, obj)
