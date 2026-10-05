from basic_shapes import BasicShape

class Circle(BasicShape):
    def __init__(self, _name, _area, r:float, x:float, y:float, n: str = "Circle"):
        super().__init__(_name, _area)
        self._radius = r
        self._x_center = x
        self._y_center = y
        self._name = n
        self._area = self.calc_area()


    def calc_area(self):
        self._area = 3.14 * (self._radius ** 2)
        return self._area

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value
        self._area = self.calc_area()

    @property
    def x_center(self):
        return self._x_center

    @x_center.setter
    def x_center(self, value):
        self._x_center = value

    @property
    def y_center(self):
        return self._y_center

    @y_center.setter
    def y_center(self, value):
        self._y_center = value


