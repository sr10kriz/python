from polygon import Polygon
from shape import Shape


class Square(
    Polygon, Shape
):  # its multiple inheritance, 1- Square is a Polygon, 2- Square is a Shape
    def areaOfSquare(self):
        print("HIT SQUARE CHILD CLASS")
        print("My Color is ", self.get_shapeColor())
        return self.get_width() * self.get_height()
