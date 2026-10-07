from basic_shape import BasicShape
from circle import Circle
from rectangle import Rectangle
from square import Square

#CIRCLE OBJECTS
circle1 = Circle(5, 0, 0)
circle2 = Circle(7, 0, 0)

#RECTANGLE OBJECTS
rectangle1 = Rectangle(5, 10)
rectangle2 = Rectangle(7, 14)

#SQUARE OBJECT
square1 = Square(5)

#POLYMORPHISM CHECK
print("--- Polymorphism check ---")
print(f"Circle 1 Area: {circle1._area}")
print(f"Circle 2 Area: {circle2._area}")
print(f"Rectangle 1 Area: {rectangle1._area}")
print(f"Rectangle 2 Area: {rectangle2._area}")
print(f"Square 1 Area: {square1._area}")

#GETTER/SETTER CHECK
print("\n--- Getter/Setter check ---")

#CIRCLE GETTER/SETTER CHECK
print(f"Circle 1 Current Radius: {circle1.radius}, Area: {circle1.area}")

circle1.radius = 10

print(f"Circle 1 Doubled Radius: {circle1.radius}, Area : {circle1.area}")

#RECTANGLE GETTER/SETTER CHECK
print(f"\nRectangle 1 Current Dimensions: {rectangle1.length} x {rectangle1.width}, Area: {rectangle1.area}")

rectangle1.length = 10
rectangle1.width = 20

print(f"Rectangle 1 Doubled Dimensions: {rectangle1.length} x {rectangle1.width}, Area: {rectangle1.area}")

#SQUARE GETTER/SETTER CHECK
print(f"\nSquare 1 Current Side: {square1.side}, Area: {square1.area}")

square1.side = 10
print(f"Square 1 Doubled Side: {square1.side}, Area: {square1.area}")