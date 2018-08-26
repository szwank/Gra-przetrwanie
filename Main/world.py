from graphics import *
from graphic_object_creator import GraphicObjectCreator
import random
from organism_creator import OrganismCreator

from animal import Animal


class World:
    _CONSOLE_WIDTH = 300
    _CONSOLE_HEIGHT = 300
    _FIELD_SIZE = 30
    _WINDOW_NAME = 'Świat'

    def __init__(self, width_of_the_board_in_the_fields, the_height_of_the_board_in_the_fields):

        random.seed()

        self.__BOARD_WIDTH_IN_FIELDS = width_of_the_board_in_the_fields
        self.__BOARD_HEIGHT_IN_FIELDS = the_height_of_the_board_in_the_fields

        self.__WIDTH = width_of_the_board_in_the_fields * self._FIELD_SIZE + self._CONSOLE_WIDTH
        self.__HEIGHT = the_height_of_the_board_in_the_fields * self._FIELD_SIZE

        self.__WINDOW_HANDLE = GraphWin(self._WINDOW_NAME, self.__WIDTH, self.__HEIGHT)

        self.__graphic_object_creator = GraphicObjectCreator(self.__HEIGHT)
       # self.__NUMBER_OF_LIVING_BEING = round(self.__BOARD_HEIGHT_IN_FIELDS * self.__BOARD_WIDTH_IN_FIELDS / 3)
        self.__NUMBER_OF_LIVING_BEING = 3


        self.__ORGANISM_CREATOR = OrganismCreator()

        self.__live_organisms = self._create_life()    #tworzy losowe rośliny i zwierzęta

    def draw_world(self):
        self._display_board()

        for live_being in self.__live_organisms:
            live_being.draw()

    def make_turn(self):
        """wykonuje akcje żywymi istotami"""

        for live_being in self.__live_organisms:    #wykonuje akcje wszystkimi żywymi istotami
            live_being.make_action()

    def _display_board(self):
        """Utwórz i wyświetl linie pól planszy
        """
        lines = self._create_board_lines()
        self._display_graphic_objects(lines)

    def _create_board_lines(self):
        horizontal_lines = self._create_horizontal_lines()
        vertical_lines = self._create_vertical_lines()
        return horizontal_lines + vertical_lines

    def _create_vertical_lines(self):
        lines = []
        upper_y = 0
        bottom_y = self.__BOARD_HEIGHT_IN_FIELDS * self._FIELD_SIZE
        for i in range(self.__BOARD_WIDTH_IN_FIELDS + 1):
            x = i * self._FIELD_SIZE

            line = self.__graphic_object_creator.create_line(Point(x, upper_y), Point(x, bottom_y))
            lines.append(line)
        return lines

    def _create_horizontal_lines(self):
        lines = []
        left_x = 0
        right_x = self.__BOARD_WIDTH_IN_FIELDS * self._FIELD_SIZE
        for i in range(self.__BOARD_WIDTH_IN_FIELDS + 1):
            y = i * self._FIELD_SIZE

            line = self.__graphic_object_creator.create_line(Point(left_x, y), Point(right_x, y))
            lines.append(line)
        return lines

    def _display_graphic_objects(self, lines):
        for line in lines:
            self.display_object(line)

    def display_object(self, object):
        """Wyświetla obiekt"""
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

    def _create_wolf(self):
        """Metoda testowa, tworzy organizm"""

        position = self.get_random_position()

        animal = self.__ORGANISM_CREATOR.create_the_organism('wolf', self, position[0], position[1])

        return animal

    def _create_plant(self):
        pass

    def _create_random_plant(self):
        pass

    def _create_random_animal(self):
        """Tworzy losowe zwierze"""

        which_animal_to_create = random.randint(1, 1)

        if which_animal_to_create is 1:
            return self._create_wolf()

    def _create_random_organism(self):
        """Tworzy losowo zwierze lub roślinę"""

        which_plant_to_create = random.randint(1, 1)

        if which_plant_to_create is 1:
            return self._create_random_animal()
        else:
            return self._create_random_plant()

    def _create_life(self):
        """Tworzy rośliny i zwierzęta"""
        live_beings = []

        for i in range(self.__NUMBER_OF_LIVING_BEING):
            live_beings.append(self._create_random_organism())

        return live_beings

    def get_board_height_in_fields(self):
        return self.__BOARD_HEIGHT_IN_FIELDS

    def get_board_width_in_fields(self):
        return self.__BOARD_WIDTH_IN_FIELDS

    def kill_organism(self, organism):
        """Usuwa organizm z listy organizmów"""

        self.__live_organisms.remove(organism)

    def get_height_of_window(self):
        return self.__WINDOW_HANDLE.getHeight()

    def get_window_handle(self):
        return self.__WINDOW_HANDLE

    def get_random_position(self):
        """Losuje pozycję i listę z wartościami"""
        x_position = random.randint(1, self.__BOARD_WIDTH_IN_FIELDS)
        y_position = random.randint(1, self.__BOARD_HEIGHT_IN_FIELDS)

        return [x_position, y_position]




