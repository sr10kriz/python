class Shape:
    __shapeColor = None

    def set_shapeColor(self, color):
        print("HIT SHAPE PARENT CLASS")
        self.__shapeColor = color

    def get_shapeColor(self):
        return self.__shapeColor
