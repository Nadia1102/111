from enum import IntEnum
from .types import RealInvl, CharInvl, Picture, Date

class ColumnType(IntEnum):
    INTEGER = 1
    REAL = 2
    CHAR = 3
    STRING = 4
    REALINVL = 5
    CHARINVL = 6
    DATE = 7
    PICTURE = 8

    def default(self):
        return [0, 0.0, '', '', RealInvl(), CharInvl(), Date(), Picture()][self.value-1]

class Column:
    def __init__(self, column_type: ColumnType, column_size = 0):
        self.column_type = column_type
        self._column_data = [column_type.default() for _ in range(column_size)]

    def append_zeros(self, column_type, count = 0):
        self._column_data.extend([column_type.default() for _ in range(count)])

    def append_values(self, values):
        self._column_data.extend(values)

