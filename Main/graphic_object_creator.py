from graphics import *
from math import floor

class GraphicObjectCreator:

    def __init__(self, window_height):
        self.__Height = window_height

    def __convert_y_coordinate(self, y):
        """przekształca podaną koortynate y do kartezjańskiego układu współżędnych
        """

        return self.__Height - y

    def create_line(self, point1, point2):
        """Stworzenie obiektu Line w kartezjańskim układzie współżędnym(oś y skierowana go góry)
        """

        return Line(Point(point1.getX(), self.__convert_y_coordinate(point1.getY())),
                    Point(point2.getX(), self.__convert_y_coordinate(point2.getY())))

    def create_rectangle(self, center_point, rectangle_width, rectangle_height):
        """Tworzy obiekt Rectangle w kartezjańskim układzie współżędnych. Punkt (0,0) jest w lewym dolnym rogu.
        Prostokąt jest tworzony na podstawie punktu środko0wego prostokąta i jego szerokości i wysokośći.
        """
        half_of_height = floor(rectangle_height / 2)
        half_of_width = floor(rectangle_width / 2)
        left_upper_point = Point(center_point.getX() - half_of_width, self.__convert_y_coordinate(center_point.getY()
                                                                                                  + half_of_height))
        right_bottom_point = Point(center_point.getX() + half_of_width, self.__convert_y_coordinate(center_point.getY()
                                                                                                    - half_of_height))
        return Rectangle(left_upper_point, right_bottom_point)
