import unittest
from basic_shape import BasicShape
from circle import Circle
from rectangle import Rectangle
from square import Square

class Test_Polymorphism(unittest.TestCase):
    def test_polymorphism(self):
        #Arrange
        circle1 = Circle(5, 0, 0)
        rectangle1 = Rectangle(5, 10, "Rectangle")
        square1 = Square(5, "Square")
        #Act & Assert
        self.assertEqual(circle1._name, "Circle")
        self.assertEqual(rectangle1._name, "Rectangle")
        self.assertEqual(square1._name, "Square")



