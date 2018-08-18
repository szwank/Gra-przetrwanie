from organism import Organism
from graphic_object_creator import GraphicObjectCreator
from graphics import *


class Animal(Organism):

    def __init__(self, world_handle, x_position_in_fields, y_position_in_fields):
        super(Animal, self).__init__(world_handle, x_position_in_fields, y_position_in_fields)

        self._representation.setFill('grey')  # kolor klasy organism

    def make_action(self):
        pass

    def collision(self):
        pass
