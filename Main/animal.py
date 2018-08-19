from organism import Organism
from graphic_object_creator import GraphicObjectCreator
from graphics import *
import random


class Animal(Organism):

    def __init__(self, world_handle, board_height_in_fields, board_width_in_fields):
        super(Animal, self).__init__(world_handle, board_height_in_fields, board_width_in_fields)

        self._representation.setFill('grey')  # kolor klasy organism

    def make_action(self):
        self._move_in_random_direction()

    def collision(self):
        pass

    def _move_in_random_direction(self):
        """Losowo przesuwa zwierze i zwraca nową pozycję
        """
        #direction = random.randint(1, 4)
        direction = 4

        if direction is 1:

            print('Ruch w prawo został wykonany: ')
            print(self._move_animal_right())
        elif direction is 2:
            print('Ruch w lewo został wykonany: ')
            print(self._move_animal_left())
        elif direction is 3:
            print('Ruch do gury został wykonany: ')
            print(self._move_animal_upward())
        else:
            print('Ruch w dół został wykonany: ')
            print(self._move_animal_down())

        return direction

    def _move_animal_right(self):
        """Przesuwa zwierze w prawo, zwraca Prawde gdy uda się wykonać przesunięcie, i fałsz gdy nie można przesunąć
        zwierzęcia
        """

        if self._x_position_in_fields < self._BOARD_WIDTH_IN_FIELDS:
            self._representation.move(self._SIZE_ON_THE_BOARD, 0)
            self._x_position_in_fields += 1
            return True
        else:
            return False

    def _move_animal_left(self):
        """Przesuwa zwierze w lewo, zwraca Prawde gdy uda się wykonać przesunięcie, i fałsz gdy nie można przesunąć
        zwierzęcia
        """
        if self._x_position_in_fields > 1:
            self._representation.move( -self._SIZE_ON_THE_BOARD, 0)
            self._x_position_in_fields -= 1
            return True
        else:
            return False

    def _move_animal_upward(self):
        """Przesuwa zwierze do gury, zwraca Prawde gdy uda się wykonać przesunięcie, i fałsz gdy nie można przesunąć
        zwierzęcia
        """
        if self._y_position_in_fields < self._BOARD_HEIGHT_IN_FIELDS:
            self._representation.move(0, -self._SIZE_ON_THE_BOARD)
            self._y_position_in_fields += 1
            return True
        else:
            return False

    def _move_animal_down(self):
        """Przesuwa zwierze w dół, zwraca Prawde gdy uda się wykonać przesunięcie, i fałsz gdy nie można przesunąć
        zwierzęcia
        """
        if self._y_position_in_fields > 1:
            self._representation.move(0, self._SIZE_ON_THE_BOARD)
            self._y_position_in_fields -= 1
            return True
        else:
            return False