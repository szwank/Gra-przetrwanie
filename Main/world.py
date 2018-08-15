from graphics import *
from graphic_object_creator import GraphicObjectCreator


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

        self.window_handle = GraphWin(self.__WINDOW_NAME, self.__WIDTH, self.__HEIGHT)

        self.grafic_object_creator = GraphicObjectCreator(self.__HEIGHT)

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

            line = self.grafic_object_creator.create_line(Point(x, upper_y), Point(x, bottom_y))
            lines.append(line)
        return lines

    def __create_horizontal_lines(self):
        lines = []
        left_x = 0
        right_x = self.__BOARD_WIDTH_IN_FIELDS * self.__FIELD_SIZE
        for i in range(self.__BOARD_WIDTH_IN_FIELDS + 1):
            y = i * self.__FIELD_SIZE

            line = self.grafic_object_creator.create_line(Point(left_x, y), Point(right_x, y))
            lines.append(line)
        return lines

    def __display_graphic_objects(self, lines):
        for line in lines:
            self.display_object(line)

    def display_object(self, object):
        """Wyświetla obiekt Line"""
        object.draw(self.window_handle)

    def hide_object(self, object):
        object.undraw()

    def wait_to_press_key(self, key):
        """Czekaj aż zostanie wciśnięty klawisz 'key' """

        key_pressed = self.window_handle.checkKey()
        while key_pressed != key:
            key_pressed = self.window_handle.checkKey()

