from basic_shape import BasicShape

class Rectangle(BasicShape):
    def __init__(self, l:int, w:int, n: str = "Rectangle"):
        super().__init__(n)
        self._length = l
        self._width = w
        self._name = n
        self._area = self.calc_area()

    def calc_area(self):
        self._area = self._length * self._width
        return self._area

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        if not isinstance(value, int):
            raise TypeError("Length must be a number")
        if value <= 0:
            raise ValueError("Length must be a positive number")
        self._length = value
        self._area = self.calc_area()

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("Width must be a number")
        if value <= 0:
            raise ValueError("Width must be a positive number")
        self._width = value
        self._area = self.calc_area()


