import unittest
from basic_shape import BasicShape
from rectangle import Rectangle

class TestSquare(unittest.TestCase):
    def test_square_initialization(self):
        #Arrange
        square1 = Square(5, "Square")
        #Act & Assert
        self.assertEqual(square1._name, "Square")
        self.assertEqual(square1._side, 5)
        self.assertAlmostEqual(square1._area, 25.0)




