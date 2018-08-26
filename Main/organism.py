from graphics import *
from graphic_object_creator import GraphicObjectCreator


#  import random


class Organism(object):
    _SIZE_ON_THE_BOARD = 30
    _strength = 0
    _initiative = 0

    def __init__(self, world_handle, height_position_in_fields, width_position_in_fields):
        self._WORLD_HANDLE = world_handle

        self.__GRAPHIC_OBJECT_CREATOR = GraphicObjectCreator(
            self._WORLD_HANDLE.get_height_of_window())  # stworzenie fabryki obiektów

        self._BOARD_WIDTH_IN_FIELDS = self._WORLD_HANDLE.get_board_width_in_fields()
        self._BOARD_HEIGHT_IN_FIELDS = self._WORLD_HANDLE.get_board_height_in_fields()

        self._representation = self._create_organism_on_set_position(height_position_in_fields, width_position_in_fields)

        self._representation.setFill('black')  # ustawienie koloru klasy organizm

    def make_action(self):
        pass

    def collision(self, the_organism_with_witch_the_collision_occurred):
        """Mechaniz kolizij. Sprawdz czy 2 organizmy są takie same jeżeli są to zrob 3 taki sam obok, jeżeli nie są- walczą"""

        if self.check_if_the_organism_is_the_same_type_as_host(the_organism_with_witch_the_collision_occurred) is True:
            pass  # make child
        else:
            self.fight_with_enemy(the_organism_with_witch_the_collision_occurred)

    def __display(self):
        self._representation.draw(self._WORLD_HANDLE.get_window_handle())

    def __hide(self):
        self._representation.undraw()

    def draw(self):
        """Metoda rysuje i zwraca munkt środkowy w ktorym się znajduje(do debugowania)"""
        self.__display()
        return self._representation.getCenter()  # usunąc po debugowaniu

    def _create_organism_on_set_position(self, x_position_in_fields, y_position_in_fields):
        """Tworzy i zwraca organizm na zadanej pozycij"""

        self._x_position_in_fields = x_position_in_fields  # przypisane pozycij do organizmu
        self._y_position_in_fields = y_position_in_fields

        x_center = (self._x_position_in_fields - 1) * self._SIZE_ON_THE_BOARD + self._SIZE_ON_THE_BOARD / 2  # wyznaczenie centrum prostokąta
        y_center = (self._y_position_in_fields - 1) * self._SIZE_ON_THE_BOARD + self._SIZE_ON_THE_BOARD / 2

        return self.__GRAPHIC_OBJECT_CREATOR.create_rectangle(
            Point(x_center, y_center), self._SIZE_ON_THE_BOARD, self._SIZE_ON_THE_BOARD)  #  argumenty(punkt środkowy, wysokość, szerokość)

    def check_if_the_organism_is_the_same_type_as_host(self, organism):

        if __eq__(self.__class__, organism):
            return True
        else:
            return False

    def get_strength(self):
        return self._strength

    def fight_with_enemy(self, enemy):

        if self.check_if_host_is_stronger(enemy) is True:
            enemy.kill()
        else:
            self.kill()

    def check_if_host_is_stronger(self, enemy):

        if self.get_strength() >= enemy.get_strength:
            return True
        else:
            return False

    def kill(self):
        """Usuń organizm z listy organizmów i ukryj go"""

        self.__hide()
        self._WORLD_HANDLE.kill_organism(self)

    def make_child(self):
        """zrob kopje organizmu"""
