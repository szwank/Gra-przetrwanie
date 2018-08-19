from graphics import *
from graphic_object_creator import GraphicObjectCreator
import random


class Organism(object):
    _SIZE_ON_THE_BOARD = 30
    _strength = 0
    _initiative = 0
    _name = 'None'

    def __init__(self, world_handle, board_height_in_fields, board_widthn_in_fields):
        self._WORLD_HANDLE = world_handle
        self.__GRAPHIC_OBJECT_CREATOR = GraphicObjectCreator(self._WORLD_HANDLE)  # stworzenie fabryki obiektów

        self._BOARD_WIDTH_IN_FIELDS = board_height_in_fields
        self._BOARD_HEIGHT_IN_FIELDS = board_widthn_in_fields

        random.seed()
        self._representation = self._create_organism_on_random_position()

        self._representation.setFill('black')  # ustawienie koloru klasy organizm

    def make_action(self):
        pass

    def collision(self, being):
        """"Wykonanie mechanizmu kolizij
        """
        if self._check_if_they_are_the_same_beings(being) is True:
            pass  # rozmnuz sie
        else:
            pass  # walcz

    def __display(self, object):
        object.draw(self._WORLD_HANDLE)

    def __hide(self, object):
        object.undraw()

    def draw(self):
        """Metoda rysuje i zwraca munkt środkowy w ktorym się znajduje(do debugowania)"""
        self.__display(self._representation)
        return self._representation.getCenter()  # usunąc po debugowaniu

    def _create_organism_on_random_position(self):
        """Tworzy i zwraca organizm na losowej pozycij"""
        self.x_position_in_fields = random.randint(1, self._BOARD_WIDTH_IN_FIELDS)
        self.y_position_in_fields = random.randint(1, self._BOARD_HEIGHT_IN_FIELDS)

        x_center = (self.x_position_in_fields - 1) * self._SIZE_ON_THE_BOARD + self._SIZE_ON_THE_BOARD / 2
        y_center = (self.y_position_in_fields - 1) * self._SIZE_ON_THE_BOARD + self._SIZE_ON_THE_BOARD / 2
        return self.__GRAPHIC_OBJECT_CREATOR.create_rectangle(
            Point(x_center, y_center), self._SIZE_ON_THE_BOARD, self._SIZE_ON_THE_BOARD)

    def get_name(self):
        return self._name

    def _check_if_they_are_the_same_beings(self, being):
        """"Sprawdza czy obiekty sá tymi samymi istotami na podstawie ich nazwy"""

        if self._name is being.getname():
            return True
        else:
            return False

    def _make_child(self):
        return child = Organism(self._WORLD_HANDLE, 1, 1)