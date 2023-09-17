from polygon import Polygon
from shape import Shape


class Triangle(Polygon, Shape):
    def areaOfTriangle(self):
        print("HIT TRIANGLE CHILD CLASS")
        print("My Color is ", self.get_shapeColor())
        return self.get_width() * self.get_height() * 1 / 2
