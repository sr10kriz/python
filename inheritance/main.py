# import Inheritance.square as Sq
# import Inheritance.triangle as Tq
from square import Square
from triangle import Triangle

shapeSquare = Square()
shapeSquare.set_value(10, 20)
shapeSquare.set_shapeColor("Purple")
print(shapeSquare.areaOfSquare(), shapeSquare.get_shapeColor())

shapeTriangle = Triangle()
shapeTriangle.set_value(10, 20)
shapeTriangle.set_shapeColor("Pink")
print(shapeTriangle.areaOfTriangle(), shapeTriangle.get_shapeColor())

# here what Im doing is i have created 2 parents 1 - Polygon, 2 - Shape
# now the child wants to get the functionalities of both parents, which means Square and Triangle
# (is a) rule - Square is a Polygon<=>Square is a Shape, Triangle is a Polygon<=>Triangle is a Shape
# Polygon, Shape - SuperClasses/ParentClasses
# Square, Triangle - DerivedClasses/ChildClasses
