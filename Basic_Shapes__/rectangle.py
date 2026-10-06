from basic_shape import BasicShape


class Rectangle(BasicShape):
    def __init__(self, l:int, w:int, n: str = "Circle"):
        #super().__init__(n)
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
        if not isinstance(value, (int, float)):
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
        if not isinstance(value, (int, float)):
            raise TypeError("Width must be a number")
        if value <= 0:
            raise ValueError("Width must be a positive number")
        self._width = value
        self._area = self.calc_area()

    @radius.setter
    def radius(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Radius must be a number")
        if value <= 0:
            raise ValueError("Radius must be a positive number")
        self._radius = value
        self._area = self.calc_area()


