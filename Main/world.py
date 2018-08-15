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

        self.window_handle = GraphWin(self.__WINDOW_NAME, self.__WIDTH, self.__HEIGHT )

        self.grafic_object_creator = GraphicObjectCreator(self.__HEIGHT)



    def draw_world(self):
        pass

    def make_turn(self):
        pass

    def draw_and_display_board(self):
        """Utwurz i wyświetl linie pól planszy
        """


        for i in range(self.__BOARD_WIDTH_IN_FIELDS + 1):

            left_x = 0
            right_x = self.__BOARD_WIDTH_IN_FIELDS * self.__FIELD_SIZE
            y = i * self.__FIELD_SIZE

            linia = self.grafic_object_creator.create_line(Point(left_x, y), Point(right_x, y))
            self.display_object(linia)

        for i in range(self.__BOARD_WIDTH_IN_FIELDS + 1):

            upper_y = 0
            bottom_y = self.__BOARD_HEIGHT_IN_FIELDS * self.__FIELD_SIZE
            x = i * self.__FIELD_SIZE

            linia = self.grafic_object_creator.create_line(Point(x, upper_y), Point(x, bottom_y))
            self.display_object(linia)


    def display_object(self,object):
        """Wyświetla obiekt Line"""
        object.draw(self.window_handle)

    def hide_object(self,object):
        object.undraw()

    def wait_to_press_key(self, key):
        """Czekaj aż zostanie wciśnięty klawisz 'key' """

        key_pressed = self.window_handle.checkKey()
        while key_pressed != key:
            key_pressed = self.window_handle.checkKey()





