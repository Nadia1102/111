from DatabaseManager.column import Column, ColumnType
from DatabaseManager.schema import Schema
from DatabaseManager.table import Table, Row
from DatabaseManager.json_encoder import RestEncoder, Generic
from DatabaseManager.utils import *

import json
import pickle
import jsonpickle
import dill
import unittest

class TestEncoder(unittest.TestCase):

    def setUp(self):
        self._rest_encoder = RestEncoder()

    def test_column(self):
        c = Column(ColumnType.REAL, 5)
        sj = json.dumps(c, cls=RestEncoder)
        self.assertEqual(sj, '{"column_type": 2, "_column_data": [0.0, 0.0, 0.0, 0.0, 0.0]}')

    def test_column_type(self):
        c = ColumnType.REAL
        self.assertEqual(json.dumps(c, cls=RestEncoder), '2')

    def test_schema(self):
        s = Schema([('id', 1), ('name', 4), ('weight', 2)])
        self.assertEqual(json.dumps(s, cls=RestEncoder), '[["id", 1], ["name", 4], ["weight", 2]]')

    def test_table(self):
        s = Schema([('id', 1), ('name', 4), ('weight', 2)])
        table = Table("Animals", s)

        table.add_row(Row(s, [1, "Mazya", 12]))
        table.add_row(Row(s, [2, "Iguana", 20]))
        table.add_row(Row(s, [3, "Uraeginthus granatina", 1023]))

        with open(get_filename('Animals', 'Weights'), 'w') as f:
            f.write(json.dumps(table, cls=RestEncoder))

    def test_schema2(self):
        s = Schema([('id', 1), ('name', 4), ('weight', 2)])
        self.assertEqual(json.dumps(s, cls=RestEncoder), '[["id", 1], ["name", 4], ["weight", 2]]')


    def test_load_table(self):
        with open(get_filename('Animals', 'Weights'), 'r') as f:
            t = json.loads(f.read())
            print(json.dumps(t, cls=RestEncoder))

    def get_test(selfs):


if __name__ == '__main__':
    unittest.main()