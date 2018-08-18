from graphics import *
from graphic_object_creator import GraphicObjectCreator
import random

from animal import Animal


class World:
    __CONSOLE_WIDTH = 300
    __CONSOLE_HEIGHT = 300
    __FIELD_SIZE = 30
    __WINDOW_NAME = 'Świat'

    def __init__(self, width_of_the_board_in_the_fields, the_height_of_the_board_in_the_fields):
        self.__BOARD_WIDTH_IN_FIELDS = width_of_the_board_in_the_fields
        self.__BOARD_HEIGHT_IN_FIELDS = the_height_of_the_board_in_the_fields

        self.__WIDTH = width_of_the_board_in_the_fields * self.__FIELD_SIZE + self.__CONSOLE_WIDTH
        self.__HEIGHT = the_height_of_the_board_in_the_fields * self.__FIELD_SIZE

        self.__WINDOW_HANDLE = GraphWin(self.__WINDOW_NAME, self.__WIDTH, self.__HEIGHT)

        self.__grafic_object_creator = GraphicObjectCreator(self.__WINDOW_HANDLE)

        random.seed()

    def draw_world(self):
        pass

    def make_turn(self):
        pass

    def display_board(self):
        """Utwórz i wyświetl linie pól planszy
        """
        lines = self.__create_board_lines()
        self.__display_graphic_objects(lines)

    def __create_board_lines(self):
        horizontal_lines = self.__create_horizontal_lines()
        vertical_lines = self.__create_vertical_lines()
        return horizontal_lines + vertical_lines

    def __create_vertical_lines(self):
        lines = []
        upper_y = 0
        bottom_y = self.__BOARD_HEIGHT_IN_FIELDS * self.__FIELD_SIZE
        for i in range(self.__BOARD_WIDTH_IN_FIELDS + 1):
            x = i * self.__FIELD_SIZE

            line = self.__grafic_object_creator.create_line(Point(x, upper_y), Point(x, bottom_y))
            lines.append(line)
        return lines

    def __create_horizontal_lines(self):
        lines = []
        left_x = 0
        right_x = self.__BOARD_WIDTH_IN_FIELDS * self.__FIELD_SIZE
        for i in range(self.__BOARD_WIDTH_IN_FIELDS + 1):
            y = i * self.__FIELD_SIZE

            line = self.__grafic_object_creator.create_line(Point(left_x, y), Point(right_x, y))
            lines.append(line)
        return lines

    def __display_graphic_objects(self, lines):
        for line in lines:
            self.display_object(line)

    def display_object(self, object):
        """Wyświetla obiekt Line"""
        object.draw(self.__WINDOW_HANDLE)

    def hide_object(self, object):
        object.undraw()

    def wait_to_press_key(self, key):
        """Czekaj aż zostanie wciśnięty klawisz 'key' """

        key_pressed = self.__WINDOW_HANDLE.checkKey()
        while key_pressed != key:
            key_pressed = self.__WINDOW_HANDLE.checkKey()

    '''                                                            #testowanie
    def create_organism(self):
        """Metoda testowa, tworzy organizm"""

        x_position = random.randint(1, self.__BOARD_WIDTH_IN_FIELDS)
        y_position = random.randint(1, self.__BOARD_HEIGHT_IN_FIELDS)
        organism = Organism(self.__WINDOW_HANDLE, x_position, y_position)

        return organism
    '''

    def create_animal(self):
        """Metoda testowa, tworzy organizm"""

        x_position = random.randint(1, self.__BOARD_WIDTH_IN_FIELDS)
        y_position = random.randint(1, self.__BOARD_HEIGHT_IN_FIELDS)
        animal = Animal(self.__WINDOW_HANDLE, x_position, y_position)

        return animal
