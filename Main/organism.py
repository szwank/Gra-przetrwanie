from graphics import *
from graphic_object_creator import GraphicObjectCreator


class Organism(object):
    _SIZE_ON_THE_BOARD = 30
    strength = 0
    initiative = 0
    position = [0, 0]
    world = 0


    def __init__(self, world_handle, x_position_in_fields, y_position_in_fields):
        self.__WORLD_HANDLE = world_handle
        self.__GRAPHIC_OBJECT_CREATOR = GraphicObjectCreator(self.__WORLD_HANDLE)

        x_center = (x_position_in_fields - 1) * self._SIZE_ON_THE_BOARD + self._SIZE_ON_THE_BOARD / 2
        y_center = (y_position_in_fields - 1) * self._SIZE_ON_THE_BOARD + self._SIZE_ON_THE_BOARD / 2

        self._representation = self.__GRAPHIC_OBJECT_CREATOR.create_rectangle(
                                Point(x_center, y_center), self._SIZE_ON_THE_BOARD, self._SIZE_ON_THE_BOARD)
        self._representation.setFill('black')  #kolor klasy organism

    def make_action(self):
        pass

    def collision(self):
        pass

    def __display(self, object):
        object.draw(self.__WORLD_HANDLE)

    def __hide(self, object):
        object.undraw()

    def draw(self):
        """Metoda rysuje i zwraca munkt środkowy w ktorym się znajduje(do debugowania)"""
        self.__display(self._representation)
        return self._representation.getCenter()  #usunąc po debugowaniu
