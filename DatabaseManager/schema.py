import json

class Schema:

    def __init__(self, schema_list):
        self.schema_list = schema_list

    @property
    def get_list(self):
        return self.schema_list

    def insert(self, column_name, column_type, position = None):
        if position is None:
            position = len(self.schema_list)
        self.schema_list.insert(position, (column_name, column_type))

    def get_projection(self, expected_names):
        schema_projection = []
        for expected_name in expected_names:
            for item in self.schema_list:
                if expected_name == item[0]:
                    schema_projection.append(item)

    def to_json(self):
        return json.dumps(self.schema_list)
