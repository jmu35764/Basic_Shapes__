from basic_shape import BasicShape
from circle import Circle
from rectangle import Rectangle
from square import Square

circle1 = Circle(5, 0, 0)
circle2 = Circle(7, 0, 0)

rectangle1 = Rectangle(5, 10)
rectangle2 = Rectangle(7, 14)

square1 = Square(5)

print("--- Polymorphism check ---")
print(f"Circle 1 Area: {circle1._area}")
print(f"Circle 2 Area: {circle2._area}")
print(f"Rectangle 1 Area: {rectangle1._area}")
print(f"Rectangle 2 Area: {rectangle2._area}")
print(f"Square 1 Area: {square1._area}")


#print(circle1._area)
