class CharInvl:
    @staticmethod
    def is_char(c):
        return isinstance(c, str) and len(c) == 1

    def __init__(self, _min = 'a', _max = 'z'):
        if not self.is_char(_min) or not self.is_char(_max):
            raise ValueError("Char type required")

        if(_min > _max):
            raise Exception("max must be bigger than min")

        self._min = _min
        self._max = _max

class RealInvl:
    def __init__(self, _min = 0.0, _max = 0.0):
        if not isinstance(_min, float) or not isinstance(_max, float):
            raise ValueError("Float type required")

        if(_min > _max):
            raise Exception("min is bigger than max")

        self._min = _min
        self._max = _max

class Picture:
    pass


