from enum import Enum
from .types import RealInvl, CharInvl, Picture

class ColumnType(Enum):
    INTEGER = 1
    REAL = 2
    CHAR = 3
    STRING = 4
    REALINVL = 5
    CHARINVL = 6
    DATE = 7
    PICTURE = 8

    @classmethod
    def default(cls):
        if cls == ColumnType.INTEGER:
            return 0
        elif cls == ColumnType.REAL:
            return 0.0
        elif cls == ColumnType.CHAR:
            return ''
        elif cls == ColumnType.STRING:
            return ''
        elif cls == ColumnType.REALINVL:
            return RealInvl()
        elif cls == ColumnType.CHARINVL:
            return CharInvl()
        elif cls == ColumnType.DATE:
            return Date()
        elif cls == Picture:
            return Picture()

class Column:
    def __init__(self, column_type: ColumnType, column_size = 0):
        self.column_type = column_type
        self._column_data = [column_type.default() for _ in range(column_size)]

    def append_zeros(self, column_type, count = 0):
        self._column_data.extend([column_type.default() for _ in range(count)])

    def append_values(self, values):
        for value in values:
            if not type(value) == self.column_type:
                raise 'Incorrect data type'
        self._column_data.extend(values)

