import unittest
from basic_shape import BasicShape
from rectangle import Rectangle
from square import Square

class TestSquare(unittest.TestCase):
    def test_square_initialization(self):
        #Arrange
        square1 = Square(5, "Square")
        #Act & Assert
        self.assertEqual(square1._name, "Square")
        self.assertEqual(square1._side, 5)
        self.assertEqual(square1._area, 25.0)

    def test_sqaure_side_change(self):
        #Arrange
        square1 = Square(5, "Square")
        #Act
        self.assertAlmostEqual(square1._area, 25.0)

        square1.side = 10
        #Assert
        self.assertEqual(square1._side, 10)
        self.assertEqual(square1._area, 100.0)

    def test_zero_side(self):
        #Arrange
        square1 = Square(5, "Square")
        #Act & Assert
        with self.assertRaises(ValueError):
            square1.side = 0

    def test_negative_side(self):
        #Arrange
        square1 = Square(5, "Square")
        #Act & Assert
        with self.assertRaises(ValueError):
            square1.side = -5

    def test_nonnumeric_side(self):
        #Arrange
        square1 = Square(5, "Square")
        #Act & Assert
        with self.assertRaises(TypeError):
            square1.side = "five"




