from graphics import *


class WindowInitializer:
    __WINDOW_NAME = 'Pobranie wymiarów planszy'
    __ENTER_KEY = 'Return'

    def __init__(self, width=400, height=200):
        self.width = width
        self.height = height
        self.window_handle = GraphWin(self.__WINDOW_NAME, width, height)  # zainicjowanie okna

    def close_window(self):
        """Zamknięcie okna"""

        self.window_handle.close()


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
        input_message.setText(0)
        input_message.draw(self.window_handle)

        self.wait_to_press_key(self.__ENTER_KEY)  # czekaj na potwierdzenie tekstu klawiszem Enter

        input_message.undraw()

        return input_message.getText()

    def display_message(self, message):
        """Pokarz wiadomość message klasy Text
        """

        message.draw(self.window_handle)

    def hide_message(self, message):
        """Ukryj wiadomość klasy Text
        """

        message.undraw()

    def get_widht(self):
        return self.width

    def get_height(self):
        return self.height

    def ask_about_number(self, ask_message):
        """Tworzy okno w którym pyta użytkownika o wymiary głównej planszy
        """

        display_message_point = Point(self.get_widht() / 2, self.get_height() / 2)
        message = Text(display_message_point, ask_message)
        self.display_message(message)
        input_message = self.get_input_massage(Point(display_message_point.getX() + len(message.getText()) * 4.5,
                                                     display_message_point.getY()))
        self.hide_message(message)

        while str.isdigit(input_message) is False:  # odpalenie pętli jeżeli string nie zawierał tylko cyfr

            message.setText('Wiadomość zawierała znaki nie będące cyframi!\nWciśnij Enter by kontynuować')
            self.display_message(message)
            self.wait_to_press_key('Return')


            message.setText(ask_message)
            input_message = self.get_input_massage(Point(display_message_point.getX() + len(message.getText()) * 4.5,
                                                         display_message_point.getY()))
            message.undraw()

        return (input_message)


