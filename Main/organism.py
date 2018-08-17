from graphics import *
from graphic_object_creator import GraphicObjectCreator

class Organism:
    strength = 0
    initiative = 0
    position = [0, 0]
    world = 0
    __SIZE_ON_THE_BOARD = 30

    def __init__(self, world_handle, x_in_fields, y_in_fields):
        self.__WORLD_HANDLE = world_handle

        x_center = (x_in_fields - 1) * self.__SIZE_ON_THE_BOARD + self.__SIZE_ON_THE_BOARD / 2
        y_center = (y_in_fields - 1) * self.__SIZE_ON_THE_BOARD + self.__SIZE_ON_THE_BOARD / 2

        Left_upper_point = Point(x_center - self.__SIZE_ON_THE_BOARD / 2, y)

        self.__representation = Rectangle()                                                     #Dokończyć!!!!

    def make_action(self):
        pass

    def collision(self):
        pass

    def __display(self, object):
        object.draw(self.__WORLD_HANDLE)

    def __hide(self, object):
        object.undraw()

    def draw(self):
        self.__display(self.__position)
