from organism import Organism
from graphic_object_creator import GraphicObjectCreator
from graphics import *
import random


class Animal(Organism):

    def __init__(self, world_handle, x_position_in_fields, y_position_in_fields):
        super(Animal, self).__init__(world_handle, x_position_in_fields, y_position_in_fields)

        self._representation.setFill('grey')  # kolor klasy organism

    def make_action(self):
        self._move_in_random_direction()

    def collision(self):
        pass

    def _move_in_random_direction(self):
        """Losowo przesuwa zwierze i zwraca nową pozycję
        """
        direction = random.randint(1, 4)

        if direction is 1:
            self._move_animal_right()
        elif direction is 2:
            self._move_animal_left()
        elif direction is 3:
            self._move_animal_upward()
        else:
            self._move_animal_down()

        return direction

    def _move_animal_right(self):
        """Przesuwa zwierze w prawo"""
        self._representation.move(self._SIZE_ON_THE_BOARD, 0)

    def _move_animal_left(self):
        """Przesuwa zwierze w lewo"""
        self._representation.move( -self._SIZE_ON_THE_BOARD, 0)

    def _move_animal_upward(self):
        """Przesuwa zwierze do gury"""
        self._representation.move(0, -self._SIZE_ON_THE_BOARD)

    def _move_animal_down(self):
        """Przesuwa zwierze w duł"""
        self._representation.move(0, self._SIZE_ON_THE_BOARD)