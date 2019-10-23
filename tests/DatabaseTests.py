from DatabaseManager.column import Column, ColumnType
from DatabaseManager.JsonEncoder import RestEncoder
import json
import unittest

class TestEncoder(unittest.TestCase):

    def setUp(self):
        self._rest_encoder = RestEncoder()

    def test_column(self):
        c = Column(ColumnType.REAL, 5)
        print(json.dumps(c, cls=RestEncoder))
        # self.assertEqual('foo'.upper(), 'FOO')

    def test_column_type(self):
        c = ColumnType.REAL

        print(c.value)

if __name__ == '__main__':
    unittest.main()