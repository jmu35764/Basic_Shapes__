from basic_shape import BasicShape
from rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, s:float, n: str = "Square"):
        super().__init__(s, s, n)
        self._side = s
        self._name = n
        self._area = self.calc_area()

    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Side must be a number")
        if value <= 0:
            raise ValueError("Side must be a positive number")
        self._side = value
        self._area = self.calc_area()







