from graphics import *


class InitWindow:
    __WINDOW_NAME = 'Pobranie wymiarów planszy'
    __ENTER_KEY = 'Return'

    def __init__(self, wight=400, height=200):
        self.wight = wight
        self.height = height
        self.window_handle = GraphWin(self.__WINDOW_NAME, wight, height) #zainicjowanie okna

    def wait_to_press_key(self, key):
        """Czekaj aż zostanie wciśnięty klawisz 'key' """

        key_pressed = self.window_handle.checkKey()
        while key_pressed != key:
            key_pressed = self.window_handle.checkKey()

    def get_input_massage(self, entry_position, font_size=5):
        """Pobierz wiadomość i potwierdz wiadomość
        okno do pobrania wiadomości zostanie wyświetlone w punkcie 'entry_position'(podany przez klase Point)
        """

        input_message = Entry(entry_position, font_size)
        input_message.draw(self.window_handle)

        self.wait_to_press_key(self.__ENTER_KEY)  # czekaj na potwierdzenie tekstu klawiszem Enter

        input_message.undraw()

        return input_message.getText()

    def display_message(self, message):
        """Pokarz wiadomość message klasy Text
        """

        message.draw(self.window_handle)

    def hide_message(self, message):
        """Ukryj wiadokość klasy Text
        """

        message.undraw()

    def get_wight(self):
        return self.wight

    def get_height(self):
        return self.height

    def ask_about_the_size_of_the_board
        """Tworzy okno w którym pyta użytkownika o wymiary głównej planszy
        """
