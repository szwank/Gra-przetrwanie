from graphics import *


class GraphicObjectCreator:

    def __init__(self, height):
        self.__Height = height

    def __del__(self):
        pass

    def create_line(self, point1, point2):
        """Stworzenie obiektu Line w kartezjańskim układzie współżędnym(oś y skierowana go góry)
        """

        return Line(Point(point1.getX(), self.__Height - point1.getY()),
                    Point(point2.getX(), self.__Height - point2.getY()))

    def create_rectangle(self, center_point, rectangle_width, rectangle_height):
        pass
