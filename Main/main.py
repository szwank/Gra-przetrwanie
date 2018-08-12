from graphics import *
import time
from world import World


def wait_to_press_key(window, key):
    '''Czekaj aż zostanie wciśnięty klawisz 'key', w onie 'window' '''

    key_pressed = window.checkKey()
    while key_pressed != key:
        key_pressed = window.checkKey()


def get_input_massage(window, entry_position, font_size = 5):
    '''Pobierz wiadomość i potwierdz wiadomość
    okno do pobrania wiadomości zostanie wyświetlone w punkcie 'entry_position'(podany przez klase Point) '''

    input_message = Entry(entry_position, font_size)
    input_message.draw(input_window)

    wait_to_press_key(window, 'Return') #czekaj na potwierdzenie tekstu klawiszem Enter

    input_message.undraw()

    return input_message.getText()


def check_if_string_contains_only_number(string):
    '''Sprawdz czy podany string posiada tylko czyfry'''
    return str.isdigit(string)


'''win = GraphWin()
pt = Point(100, 50)
pt.draw(win)

cir = Circle(pt, 25)
cir.draw(win)

cir.setOutline('red')
cir.setFill('blue')

line = Line(pt, Point(150, 100))
line.draw(win)

time.sleep(5)

pt.x=50
print(line.getP1())

time.sleep(10)
'''
input_window = GraphWin("Pobranie wymiarów okna", 400,100) #stworzenie okna do podania wymiarów

display_message_point = Point(input_window.getWidth() / 2, input_window.getHeight() / 2)
message = Text(display_message_point, 'Podaj ilość pól szerokości gry:')
message.draw(input_window)
input_message = get_input_massage(input_window, Point(display_message_point.getX() + len(message.getText()) * 4.5,
                                              display_message_point.getY()))
message.undraw()


while check_if_string_contains_only_number(input_message) is False: #odpalenie pętli jeżeli string nie zawierał tylko cyfr

    message.setText('Wiadomość zawierała znaki nie będące cyframi! Wciśnij enter by kontynuować')
    wait_to_press_key(input_window, 'Return')

    message.draw(input_window)
    input = get_input_massage(input_window, Point(display_message_point.getX() + len(message.getText()) * 4.5,
                                                  display_message_point.getY()))
    message.undraw()


print(input)


# input_window.getMouse()
# input_max_x.close()

# window = World(1000,500)
# while 1:
#     window.window.update()
# window.window.getMouse()
# window.window.close()
print('kot')


